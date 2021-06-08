# Set up

## Local broker (for $SYS topics)

1.  `pip install paho-mqtt`
2.   Follow this [instruction](https://www.emqx.io/downloads#broker) to install EMQ X local broker.
3.   Run `emqx start` in command line to start local broker.
4.  Make sure **hostname, port, username, password** are the correct settings. Comment these for other brokers in `controller.py` and `analyser.py`.
5.  Run `python controller.py`.
6.  Run `python analyser.py` to start analysing.

## Remote broker (for statistics)

1.  `pip install paho-mqtt`
2.  Make sure **hostname, port, username, password** are the correct settings. Comment these for other brokers in `controller.py` and `analyser.py`.
3.  Run `python controller.py`.
4.  Run `python analyser.py` to start analysing.

---

# Code design

-   Code files: `analyser.py`, `controller.py`
    -   `controller.py`: contains both **Controller** and **Publisher** clients. 

        Controller listens forever, it needs to be terminated by hand.

        Once Controller receives the requests from Analyser, it makes Publisher to sends counters for 120 seconds. After that, if Controller gets new requests, it will activate Publisher once again.

    -   `analyser.py`: contains the **Analyser** client. 

        It listens for a 2-minute period for each measurement, but it does not guarantee that it will receive counters for the full 2 minutes. Hence I calculate the period length using the first and last timestamp recorded in the (counter, time) tuples in list `stats`.

-   Since EMQ X Cloud broker does not allow \$SYS topics subscription, I can only collect the required statistics over cloud broker. Then I run the code again on EMQ X local broker to subscribe for \$SYS topics.

-   **$SYS topics** collected: 
    
    -   Bytes received
    -   Bytes sent
    -   Messages received
    -   Messages sent
    -   Messages dropped
    -   Messages delayed

---

# Technical details

-   Python 3.8.5
-   paho-mqtt 1.5.1
-   MQTT Explorer 0.4.0-beta1 (Lower versions do not support QoS level selection.)
-   ClientID is not restricted.
