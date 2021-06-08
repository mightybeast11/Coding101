import paho.mqtt.client as mqtt
from time import time, sleep

def on_message(client, userdata, message):
    topic = str(message.topic)

    if "qos" in topic:
        global qos
        qos = int(message.payload)
    if "delay" in topic:
        global delay
        delay = int(message.payload)

def on_publish(client, userdata, result):
    global total_sent
    total_sent += 1

def publish(publisher, qos, payload, delay):
    # publish counter forever until controller intercepts
    topic = "counter/" + str(qos) + "/" + str(delay)
    publisher.publish(topic=topic, payload=payload, qos=qos)


if __name__ == '__main__':

    # emqx local broker
    broker = "localhost"
    port = 1883 
    username = ""
    password = ""

    qos = -1
    delay = -1
    total_sent = 0

    # set up controller client
    controller = mqtt.Client(client_id="3310-controller")
    controller.username_pw_set(username, password)
    controller.connect(broker, port=port, keepalive=3000)
    controller.on_message = on_message
    controller.subscribe("request/qos")
    controller.subscribe("request/delay")
    
    # set up publisher client
    publisher = mqtt.Client(client_id="3310-publisher")
    publisher.username_pw_set(username, password)
    publisher.connect(broker, port=port, keepalive=3000)
    publisher.on_publish = on_publish

    # controller listens forever
    controller.loop_start()
    while True:
        if qos > -1 and delay > -1:
            # reset immediately, because controller is still listening,
            # new parameters can be received before current loop finishes
            q = qos 
            d = delay
            qos = -1
            delay = -1
            counter = -1
            total_sent = 0

            # publish for 2 min
            publisher.loop_start()
            publish_time = time() + 120
            while time() < publish_time:
                counter += 1
                publisher.publish("counter/" + str(q) + "/" + str(d), payload=counter, qos=q)
                sleep(d / 1000)
            publisher.loop_stop()
            print("Total sent:", total_sent) # for loss rate calculation
            
    controller.loop_stop()
    publisher.disconnect()
    controller.disconnect()
