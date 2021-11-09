---
grand_parent: Harmony 3 PIC32MZW1 wireless system services package
parent: Web Socket Server System Service
title: Web Socket System Service Developer's Guide
has_toc: true
nav_order: 1
---

# Web Socket Server System Service Developer's Guide
{: .no_toc }

### Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---
The purpose of this document is to explain the Web Socket Server system service design to enable the developer to make changes in the service code as per his/ her requirements if the need be.

# Overview

The WSS system service provides an application programming interface (API) to manage the Web Socket Server functionalities over TCP/IP Networking. The WSS system service uses the MPLAB Harmony NET system service to achieve the TCPIP functionalities. 

Key Features:
- Implements the WSS protocol as a service
- Supports multiple client connections simultaneously

<p align="center">
<img src="./images/AbstractionModel_WSS.png" />
</p>



# Detailed Design

WSS system service is a background service with which the application can interact using the APIs provided. The idea of the WSS system service is to reduce the code size for the application and simplifying the state machine that the application may need to maintain by abstracting out the complexity of the Web Socket Server in the system service. 

## State Machine 

The various states of the WSS system service are of the enum type [*SYS_WSS_STATE*](https://microchip-mplab-harmony.github.io/wireless_system_pic32mzw1_wfi32e01/system/wss/docs/interface.html#SYS_WSS_STATE). 

The WSS system service runs a finite state machine with the following states:

1.  *SYS_WSS_STATE_CLOSED*: Initial State of the WSS system service, at the initialization.
2.  *SYS_WSS_STATE_CLOSING*: An intermediate state which handles the processing of the client closing handshake .
3.  *SYS_WSS_STATE_CONNECTING*: An intermediate state which handles the processing of the client opening handshake.
4.  *SYS_WSS_STATE_CONNECTED*: The state which  handles all the data transmissions.

<p align="center">
<img src="./images/StateMachine.png"/>
</p>
## Number of Clients Supported

The maximum number of Clients supported by WSS system service currently is 8. The user can change the value via the MHC.By default the value is set to 2.

## Client time out

The user can configure a timeout value which will be considered as a maximum idle time for a client connection. The default timeout value is 30s. 

## External APIs

### [SYS_WSS_register_callback ()](https://microchip-mplab-harmony.github.io/wireless_system_pic32mzw1_wfi32e01/system/wss/docs/interface.html#SYS_WSS_register_callback.png)

Description: The API is used for registering the application callback function with the WSS service.

<p align="center">
<img src="./images/SYS_WSS_register_callback.png" style="width:6.84375in;height:6.91667in" />
</p>

### [SYS_WSS_CloseConnection ()](https://microchip-mplab-harmony.github.io/wireless_system_pic32mzw1_wfi32e01/system/wss/docs/interface.html#SYS_WSS_CloseConnection.png)

Description: This API is used to closes the Web Socket connection to the client indicated by the parameter clientIndex. This will initiate the closing handshake from the server.

<p align="center">
<img src="./images/SYS_WSS_CloseConnection.png" style="width:6.48958in;height:2.63542in" />
</p>


### [SYS_WSS_PingClient ()](https://microchip-mplab-harmony.github.io/wireless_system_pic32mzw1_wfi32e01/system/wss/docs/interface.html#SYS_WSS_PingClient.png)

Description: This API is used to send a ping message to the client indicated by the parameter clientIndex.


<p align="center">
<img src="./images/SYS_WSS_PingClient.png" style="width:6.48958in;height:4in" />
</p>

### [SYS_WSS_sendMessage ()](https://microchip-mplab-harmony.github.io/wireless_system_pic32mzw1_wfi32e01/system/wss/docs/interface.html#SYS_WSS_sendMessage.png)

Description: This API is used to send a message to the client indicated by the parameter clientIndex.

<p align="center">
<img src="./images/SYS_WSS_sendMessage.png" />
</p>


### [SYS_WSS_Initialize](https://microchip-mplab-harmony.github.io/wireless_system_pic32mzw1_wfi32e01/docs/system/wss/docs/interface.html#SYS_WSS_Initialize)()/ [SYS_WSS_Deinitialize()](https://microchip-mplab-harmony.github.io/wireless_system_pic32mzw1_wfi32e01/docs/system/wss/docs/interface.html#SYS_WSS_Deinitialize)

Description: These functions are used for initializing/ deinitializing the data structures of the WSS system service.


## Code location

The base code for the WSS system service can be found in the *wireless_system_pic32mzw1_wfi32e01\\system\\wss*

The same shall be copied to the following location after the code for the application is generated – *my_application\\firmware\\src\\config\\pic32mz_w1_curiosity\\system\\wss*

The code has 2 files:

1.  Header file: *sys_wss.h*

2.  Source file: *src/sys_wss.c*

> Since the above files could see modifications across releases, hence the users would need to take care of merging the changes they did in these files with the ones which were done in the new release by Microchip Team. For this the user needs to take care of this while generating the code via the MHC:
>
<p align="center">
<img src="./images/MhcMergeStrategy.png" style="width:6.5in;height:6.67639in" />
</p>

While generating the code the user should use the Merge Strategy as “USER_ALL”, and press “Generate”. In case there are changes done by user in any of the files, the MHC shall prompt the user about it:

<p align="center">
<img src="./images/MhcMergeWindow.png" style="width:6.5in;height:3.16528in" />
</p>

The user can merge his changes with the the latest changes done in the services using the above window.

# Reference

| S. No | Name                         | Link                                                                                                               |
|-------|------------------------------|--------------------------------------------------------------------------------------------------------------------|
| 1     | WSS system service Usage     | <https://microchip-mplab-harmony.github.io/wireless_system_pic32mzw1_wfi32e01/docs/system/wss/docs/usage.html>     |
| 2     | WSS system service Interface | <https://microchip-mplab-harmony.github.io/wireless_system_pic32mzw1_wfi32e01/docs/system/wss/docs/interface.html> |
