---
grand_parent: Harmony 3 PIC32MZW1 wireless system services package
parent: MQTT Service
title: MQTT System Service Developer's Guide
has_toc: true
nav_order: 3
---

# MQTT System Service Developer's Guide
{: .no_toc }

### Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---
The purpose of this document is to explain the MQTT system service design to enable the developer to make changes in the service code as per his/ her requirements if the need be.

# Overview

MQTT system service Library provides an application programming interface (API) to manage MQTT Protocol functionalities. The MQTT system service uses the third party software Paho APIs for achieving these functionalities. It supports key features like client mode for MQTT connectivity, TLS for MQTT connection, Self-Healing, etc.

<p align="center">
<img src="./images/Stack.png" style="width:2.70833in;height:3.53125in" />
</p>

Though the application developer is free to use the third party software directly to manage the MQTT functionalities, the use of MQTT system service eases the work of the developer by reducing the state machine that the application needs to maintain while also reducing the amount of bookkeeping that otherwise is needed.

# Detailed Design

MQTT system service is a background service that runs in the context of the application task. The idea of the MQTT system service is to reduce the code size for the application and simplifying the state machine that the application may need to maintain by abstracting out the complexity in the system service. The system service achieves this by maintaining a state machine of its own and any bookkeeping that may be needed.

The MQTT system service supports only client mode. Also, the service supports secured connections for its MQTT connection with the server.

The MQTT system service also supports Self-Healing, or ‘Auto-Reconnect’. In case there is an interruption in the connection due to the underlying lower layer or when the peer disconnects, the service tries to reconnect again without making the application to bother about retriggering the connection.

## State Machine 

The various states of the MQTT system service are of the enum type [*SYS_MQTT_STATUS*](https://microchip-mplab-harmony.github.io/wireless_system_pic32mzw1_wfi32e01/docs/system/mqtt/docs/interface.html#sys_mqtt_status). The application is expected to call [*SYS_MQTT_Task()*](https://microchip-mplab-harmony.github.io/wireless_system_pic32mzw1_wfi32e01/docs/system/mqtt/docs/interface.html#sys_mqtt_task)periodically from its own task context. This function ensures that the MQTT system service state machine receives sufficient execution cycles to process pending packets in the network stack.

### MQTT Client State Machine

The MQTT system service runs a finite state machine with the following states:

1.  *SYS_MQTT_STATUS_IDLE*: Initial State of the MQTT system service, at the initialization.

2.  *SYS_MQTT_STATUS_LOWER_LAYER_DOWN*:

    1.  State the MQTT system service enters after initialization.

    2.  In this state, the MQTT system service opens the TCP socket using NET system service without bothering if the lower layer is UP or DOWN. This offloads the application’s burden to poll the link before communicating over the network.

3.  *SYS_MQTT_STATUS_SOCK_CLIENT_CONNECTING*: In this state, the service opens a socket to connect to the MQTT server using NET system service, and waits for the connection to get established.

4.  *SYS_MQTT_STATUS_SOCK_CONNECTED*: TCP connection between the client the MQTT server established; client triggers MQTT ‘Connect’ to the server via the Paho APIs.

5.  *SYS_MQTT_STATUS_SOCK_OPEN_FAILED*: Opening the Socket failed. Failure is conveyed to the application via the [callback](https://microchip-mplab-harmony.github.io/wireless_system_pic32mzw1_wfi32e01/docs/system/mqtt/docs/interface.html#sys_mqtt_callback) registered with the service.

6.  *SYS_MQTT_STATUS_MQTT_CONNECTED*: Client connected to the MQTT server; Connection status is conveyed to the application via the registered callback. In this state, the service is waiting to receive data on topic(s).

7.  *SYS_MQTT_STATUS_MQTT_DISCONNECTING*: Client comes into this state whenever there is either of the following:

    1.  A failure to connect to the server (tcp or mqtt connection), or

    2.  Timeout occurs on not receiving expected response, or

    3.  Failure in case of publishing a message or subscribing to a topic. In this state, the client reinitializes the data w.r.t subscriptions topics.

8.  *SYS_MQTT_STATUS_MQTT_DISCONNECTED*: Client disconnected from the server. ‘Disconnection’ is conveyed to the application via the registered callback.

9.  *SYS_MQTT_STATUS_MQTT_CONN_FAILED*: Client failed to connect to MQTT server as Paho API failed or ‘CONACK’ message not received by the client after waiting for a specific time period.

10. *SYS_MQTT_STATUS_WAIT_FOR_MQTT_CONACK*: Client waits for the reply ‘CONACK’ from the MQTT server in response to his ‘CONNECT’ message, for SYS_MQTT_PERIOIDC_TIMEOUT seconds.

11. *SYS_MQTT_STATUS_WAIT_FOR_MQTT_SUBACK*: Client waits for the reply ‘SUBACK’ from the MQTT server in response to his ‘SUBSCRIBE’ message, for SYS_MQTT_PERIOIDC_TIMEOUT seconds.

12. *SYS_MQTT_STATUS_WAIT_FOR_MQTT_PUBACK*: Client waits for the reply ‘PUBACK’ from the MQTT server in response to his ‘PUBLISH’ message in case it was sent with Qos as 1 or 2, for SYS_MQTT_PERIOIDC_TIMEOUT seconds.

13. *SYS_MQTT_STATUS_WAIT_FOR_MQTT_UNSUBACK*: Client waits for the reply ‘UNSUBACK’ from the MQTT server in response to his ‘UNSUBSCRIBE’ message, for SYS_MQTT_PERIOIDC_TIMEOUT seconds.

<p align="center">
<img src="./images/StateMachine.png" style="width:6.5in;height:6.73958in" />
</p>

The above state machine has been implemented in the function *SYS_MQTT_Paho_Task().* The statme machine figure has been broken into two, so as to make it simpler to understand, and hence both the above state machine figures should be seen in conjection.

**In case the user wants to add or remove a state or modify the action to be done in an existing state (for instance, adding a timer for a time-bound result), one would need to modify the function *SYS_MQTT_Paho_Task()* along with the enum [SYS_MQTT_STATUS](https://microchip-mplab-harmony.github.io/wireless_system_pic32mzw1_wfi32e01/docs/system/mqtt/docs/interface.html#sys_mqtt_status)*.***

## Number of Subscription Topics Supported

The number of subscription topics supported by MQTT system service currently is 2. **The same can be increased by changing the value of the macro *SYS_MQTT_SUB_MAX_TOPICS. ***Also note, that the underlying third party software Paho supports 5 subscription topics, so if the developer needs to use more than 5 topics, he/ she will need to make changes in the Paho code (*MAX_MESSAGE_HANDLERS*) too.

## Timeperiod for ACK

The number of seconds the MQTT system service will wait for the ACK to come – CONACK, or SUBACK, or PUBACK, or UNSUBACK is currently 5 seconds. The developer can increase or decrease this time by modifying the value of SYS_MQTT_PERIOIDC_TIMEOUT.

## External APIs

### [SYS_MQTT_Connect ()](https://microchip-mplab-harmony.github.io/wireless_system_pic32mzw1_wfi32e01/docs/system/mqtt/docs/interface.html#sys_mqtt_connect)

Description: The API is used for connecting an MQTT client to the server. The user needs to register a callback function via this API. The registered callback lets the user know the operational status change or when data is received on the topic subscribed to. One of the advantages of this API is that the user can call this API without bothering about the operational state of the underlying layers, and the service shall take care of all the complexity in such cases.

<p align="center">
<img src="./images/SYS_MQTT_Connect.png" style="width:7.08056in;height:6.87387in" />
</p>

### [SYS_MQTT_Disconnect ()](https://microchip-mplab-harmony.github.io/wireless_system_pic32mzw1_wfi32e01/docs/system/mqtt/docs/interface.html#sys_mqtt_disconnect)

Description: The API is used for disconnecting the MQTT client from the server.

<p align="center">
<img src="./images/SYS_MQTT_Disconnect.png" style="width:6.49653in;height:2.15903in" />
</p>


### [SYS_MQTT_Publish ()](https://microchip-mplab-harmony.github.io/wireless_system_pic32mzw1_wfi32e01/docs/system/mqtt/docs/interface.html#sys_mqtt_publish)

Description: The API is used for publishing a message onto a topic.

<p align="center">
<img src="./images/SYS_MQTT_Publish.png" style="width:6.49583in;height:4.41458in" />
</p>

### [SYS_MQTT_Subscribe ()](https://microchip-mplab-harmony.github.io/wireless_system_pic32mzw1_wfi32e01/docs/system/mqtt/docs/interface.html#sys_mqtt_subscribe)

Description: The API is used for subscribing to a topic.

<p align="center">
<img src="./images/SYS_MQTT_Subscribe.png" style="width:6.49583in;height:4.27917in" />
</p>

### [SYS_MQTT_Unsubscribe ()](https://microchip-mplab-harmony.github.io/wireless_system_pic32mzw1_wfi32e01/docs/system/mqtt/docs/interface.html#sys_mqtt_unsubscribe)

Description: The API is used for unsubscribing from a topic.

<p align="center">
<img src="./images/SYS_MQTT_Unsubscribe.png" style="width:6.49583in;height:4.05417in" />
</p>

### Handling of the messages received for a Topic

<p align="center">
<img src="./images/ReceiveMsgOnTopic.png" style="width:6.49028in;height:3.03333in" />
</p>

### Handling of KeepAlive messages after the MQTT connection is UP

<p align="center">
<img src="./images/KeepAlive.png" style="width:6.49028in;height:7.70833in" />
</p>

### [SYS_MQTT_Task ()](https://microchip-mplab-harmony.github.io/wireless_system_pic32mzw1_wfi32e01/docs/system/mqtt/docs/interface.html#sys_mqtt_task)

Description: This API is used for smooth functioning of the state machine of the MQTT system service**.** The application needs to call this API periodically. Also, this API takes as parameter the handle returned when we connect to server via the SYS_MQTT_Connect() call.

### [SYS_MQTT_Initialize ()](https://microchip-mplab-harmony.github.io/wireless_system_pic32mzw1_wfi32e01/docs/system/mqtt/docs/interface.html#sys_mqtt_initialize)/ [SYS_MQTT_Deinitialize ()](https://microchip-mplab-harmony.github.io/wireless_system_pic32mzw1_wfi32e01/docs/system/mqtt/docs/interface.html#sys_mqtt_deinitialize)

Description: These functions are used for initializing/ deinitializing the data structures of the MQTT system service. The SYS_MQTT_Initialize() function is called from within the System Task. **Users can modify these functions in case they want to take some additional actions during the initialization of the service.**

## CLI Commands

The details of the cli commands supported by MQTT system service can be found [here](https://microchip-mplab-harmony.github.io/wireless_system_pic32mzw1_wfi32e01/docs/system/mqtt/docs/usage.html). The CLI commands are implemented using the function *SysMqtt_Command_Process()*. **The users can modify any of the commands – configuration or get as per their needs by modifying the above function.**

## Code location

The base code for the MQTT system service can be found in the *wireless_system_pic32mzw1_wfi32e01\\system\\mqtt*

The same shall be copied to the following location after the code for the application is generated – *my_application\\firmware\\src\\config\\pic32mz_w1_curiosity\\system\\mqtt*

The code has 4 files:

1.  Header file: *sys_mqtt.h* and *sys_paho_mqtt.h*

2.  Source file: *src/sys_mqtt.c* and *src/sys_paho_mqtt.c*

Since the above files could see modifications across releases, hence the users would need to take care of merging the changes they did in these files with the ones which were done in the new release by Microchip Team. For this the user needs to take care of this while generating the code via the MHC:

<p align="center">
<img src="./images/MhcMergeStrategy.png" style="width:6.5in;height:6.67639in" />
</p>

While generating the code the user should use the Merge Strategy as “USER_ALL”, and press “Generate”. In case there are changes done by user in any of the files, the MHC shall prompt the user about it:

<p align="center">
<img src="./images/MhcMergeWindow.png" style="width:6.5in;height:3.16528in" />
</p>

The user can merge his changes with the the latest changes done in the services using the above window.

# Reference

| S. No | Name                          | Link                                                                                                                |
|-------|-------------------------------|---------------------------------------------------------------------------------------------------------------------|
| 1     | MQTT system service Usage     | <https://microchip-mplab-harmony.github.io/wireless_system_pic32mzw1_wfi32e01/docs/system/mqtt/docs/usage.html>     |
| 2     | MQTT system service Interface | <https://microchip-mplab-harmony.github.io/wireless_system_pic32mzw1_wfi32e01/docs/system/mqtt/docs/interface.html> |
| 3     | NET system service Interface  | <https://microchip-mplab-harmony.github.io/wireless_system_pic32mzw1_wfi32e01/docs/system/net/docs/interface.html>  |
