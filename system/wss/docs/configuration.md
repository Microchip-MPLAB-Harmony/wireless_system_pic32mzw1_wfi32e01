---
grand_parent: Harmony 3 PIC32MZW1 wireless system services package
parent: Web Socket Server Service
title: Web Socket Server System Service Configuration
has_toc: true
nav_order: 1
---

# Web Socket Server (WSS) System Service Configuration
The WSS System Service library should be configured through MHC. When user adds the WSS System Service into a project, all the required dependencies and components are added automatically into the the projects MHC configuration. The user can make changes according to the application requirement in the WSS System Service configuration menu.

The following figure shows the MHC configuration window for configuring the WSS System Service and a brief description of various configuration options.

1. Open the MHC 3
2. Drag the WSS Service Module into from the Available components into the Project Graph. This will trigger the auto activation of the dependent modules.Click on 'Yes' in the confirmation window popped up for component auto activation. 

    ![](./images/Activate_WSS.png)

3. Configure the various parameters

    ![](./images/ConfigWSS.png)

|Parameter     	                    | Description   	                                |
|---	                            |---	                                            |
|Port   	                        |port used by the WSS service. Default is 8000   	|
|Debug         	                    |Control debug prints. Disabled by default     	    |
|Secure Socket                      |Enable/Disable secure web socket. Make sure that you configure the required server certificate and keys in the underlying layers.|
|Application template Generation| Control the generation of an application template with all the available callbacks.|

   

![](./images/ConfWSS_PortDebugTLSAppTemplate.png)

5. Advanced Configuration with RX buffer size, maximum number of supported clients, client timeout and start at boot features.
   
| Parameter             | Description                                                                                                          |
|---                    |---                                                                                                                   |
|Max Rx buffer length   | Max length of the buffer used to receive and process messages. Default is 1400                                       |
|Max number of clients  | Max number of clients allowed to connect to teh WSS. Default is 2                                                    |
|Client timeout in ms   | Timeout after which the client is disconnected in case of no data transfer or ping after connection. Default is 30000|
|Start at boot          |Control when the WSS is enabled. Enabled at boot by default.                                                          |

  ![](./images/AdvancedConf_WSS.png)

6. FreeRTOS configuration enabled by default
   
|Parameter | Description |
|--- |--- |
|  RTOS Task Delay(ms)  | WSS RTOS task delay. Default is 1 ms   |
| RTOS Task Stack Size  | WSS RTOS task stack size. Default is 4096 |
| RTOS Task priority    | WSS RTOS task priority. Default is 1|
   

All of the required files are automatically genarted and added into the MPLAB X IDE project by the MHC when the code generation
completes successfully.
