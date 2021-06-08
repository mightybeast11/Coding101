import paho.mqtt.client as mqtt
from time import time, time_ns
import statistics

def on_message(client, userdata, message):
    topic = str(message.topic)

    if "count" in topic:
        global stats
        stats.append((int(message.payload), time_ns() // 1_000_000)) # record (count, time in ms) tuples
    elif "bytes/received" in topic:
        global br
        br = int(message.payload)
    elif "bytes/sent" in topic:
        global bs
        bs = int(message.payload)
    elif "messages/received" in topic:
        global mr
        mr = int(message.payload)
    elif "messages/sent" in topic:
        global ms
        ms = int(message.payload)
    elif "messages/dropped" in topic:
        global pr
        mdr = int(message.payload)
    elif "messages/delayed" in topic:
        global ps
        mde = int(message.payload)

def analyse(stats, delay):
    length = len(stats)
    period = stats[-1][1] - stats[0][1] # in ms
    misorder_count = 0
    inter_message_gap = []

    print("-----Statistics-----")

    message_rate = length / (period // 1000) # in seconds
    print("Message rate:", message_rate, "mes/s")
    
    # print("Total received:", length, "(for loss rate calculation)")
    if delay == 0:
        print("Loss rate: not clear")
    else:
        loss_rate = (period // delay - length) / (period // delay)
        print("Loss rate:", loss_rate)

    i = 1
    while i < length:
        if stats[i][0] < stats[i-1][0]:
            misorder_count += 1
        if int(stats[i][0] - 1) == stats[i-1][0]:
            inter_message_gap.append(stats[i][1] - stats[i-1][1])
        i += 1

    misorder_rate = misorder_count / length
    print("Misorder rate:", misorder_rate)
    
    gap_mean = statistics.mean(inter_message_gap)
    gap_median = statistics.median(inter_message_gap)
    print("Gap mean:", gap_mean, "ms")
    print("Gap median:", gap_median, "ms")


if __name__ == '__main__':

    # emqx local broker
    broker = "localhost"
    port = 1883 
    username = ""
    password = ""

    # analysis preparation
    count = -1
    stats = []
    qos = [0, 1, 2]
    delay = [0, 10, 20, 50, 100, 500] # in ms
    # $SYS topic records
    br = -1
    bs = -1
    mr = -1
    ms = -1
    mdr = -1
    mde = -1

    # set up analyser client
    analyser = mqtt.Client(client_id="3310-analyser")
    analyser.username_pw_set(username, password)
    analyser.on_message = on_message
    analyser.connect(broker, port=port, keepalive=2500)

    # run analysis
    measurement_no = 0
    for q in qos:
        for d in delay:

            measurement_no += 1
            print("===== Measurement", measurement_no, "=====")
            print("QoS: Level", q)
            print("Delay:", d, "ms")

            # $SYS topics
            analyser.subscribe("$SYS/brokers/emqx@127.0.0.1/metrics/bytes/received", qos=q)
            analyser.subscribe("$SYS/brokers/emqx@127.0.0.1/metrics/bytes/sent", qos=q)
            analyser.subscribe("$SYS/brokers/emqx@127.0.0.1/metrics/messages/received", qos=q)
            analyser.subscribe("$SYS/brokers/emqx@127.0.0.1/metrics/messages/sent", qos=q)
            analyser.subscribe("$SYS/brokers/emqx@127.0.0.1/metrics/messages/dropped", qos=q)
            analyser.subscribe("$SYS/brokers/emqx@127.0.0.1/metrics/messages/delayed", qos=q)
            # collect stats
            analyser.publish("request/qos", payload=q, qos=q)
            analyser.publish("request/delay", payload=d, qos=q)
            analyser.subscribe("counter/" + str(q) + "/" + str(d), qos=q)

            # listen for 2 min
            analyser.loop_start()
            two_min = time() + 120
            while True:
                if time() > two_min:
                    analyser.loop_stop()
                    break

            analyse(stats, d) # analyse and print results
            stats.clear()
            
            # print all stats to observe pattern
            print("-----Broker Status-----")
            print("Bytes received:", br)
            print("Bytes sent:", bs)
            print("Messages received:", mr)
            print("Messages sent:", ms)
            print("Messages dropped:", mdr)
            print("Messages delayed:", mde)
            print("------------------------\n")

    # termination    
    analyser.disconnect()
