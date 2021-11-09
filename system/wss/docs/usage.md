---
grand_parent: Harmony 3 PIC32MZW1 wireless system services package
parent: Web Socket Server System Service
title: Net System Service Usage
has_toc: true
nav_order: 2
---

# Web Socket Server System Service Usage
## Description
Web Socket Server System Service Library provides an application programming interface (API) for implementing a Web Socket Server functionalities. The user need not take care about the frame connection handshakes,the data frame formatting etc.   The WSS System Service uses the underlying Net system  Service APIs for achieving TCPIP network functionalities. 

### Command Line:
User can follow below commands of the NET System Service: 

1. sysnethelp 
    
    NET System Service help command which displays the supported CLI commands
    ![](./images/sysnethelp_cli.png)

2. sysnet open 
    
     Command for Reconfiguring an already open instance of Net System Service 
    ![](./images/sysnetopen_cli.png)

3. sysnet close 

    Command to close the instance of Net System Service 
    ![](./images/sysnetclose_cli.png)

4. sysnet send 

    Command to send message on the network connection established by the instance of Net System Service 
    ![](./images/sysnetsend_cli.png)

5. sysnet get info 
    
    Command for knowing the Current Information for all the Instances of Net System Service 
    ![](./images/sysnetgetinfo_cli.png)



