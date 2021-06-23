var myVariable = `
{"0": {
    "doc": "App Debug System Service Configuration",
    "title": "App Debug System Service Configuration",
    "content": "The enabling/ disabling of App Debug System Service library should be done through the MHC. More on how any component can integrate this library into his own component can be found by going through some of the system services like the MQTT, NET, and Wifi System Service. Note that App Debug System Service component does not have any conifgurations to be done separately. All the configurations needs to come via the other components using it. ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/appdebug/docs/configuration.html",
    "relUrl": "/system/appdebug/docs/configuration.html"
  },"1": {
    "doc": "Wi-Fi System Service Configuration",
    "title": "Wi-Fi System Service Configuration",
    "content": "The Wi-Fi System Service library should be configured through MHC(MPLAB Harmony Configurator). The following figure shows the MHC configuration window for configuring the Wi-Fi System Service and a brief description of various configuration options. When user select the Wi-Fi System Service library, all the required dependencies are added automatically into the MHC configuration. In the Wi-Fi System Service library, user can select the operating device mode as station(STA) or access point(AP) and make a required changes in the selected mode. ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/wifi/docs/configuration.html",
    "relUrl": "/system/wifi/docs/configuration.html"
  },"2": {
    "doc": "Wi-Fi System Service Configuration",
    "title": "Configuration Options:",
    "content": " Using MHC menu,user can select required device mode as a station(STA) or access point(AP) . Device Mode: . Indicates the device operation mode(STA/AP). STA Mode: . SSID: Access Point (AP/Router) SSID to connect. Security type : Indicates the security being used by the AP with which device should connect – OPEN / WPA2 / WPAWPA2 (Mixed)/ WPA3. Password: Password to be used while connecting to the AP. This is mandatory if security mode is set to anything other than OPEN. It will be ignored if security mode is set to OPEN. Auto Connect: Indicate whether to auto connect to AP (enable) or wait for user input (disable). AP Mode: . SSID: Indicate AP mode SSID. Security: Indicate AP mode security: - OPEN - WPA2 - WPAWPA2(Mixed) - WPA3 Password: Indicate AP mode password(passphrase). SSID Visibility: Indicate AP mode SSID visibility. Channel: Indicate operating channel of AP mode. Advanced configuration: . Country code: Regulatory domain country code configuration: - GEN - General - USA - North America - EMEA - Europe - JPN - Japan Number of Clients: Indicates the maximum number of clients user can register. Enable Wi-Fi Provisioning service: Enables/Disables Wi-Fi Provisioning System Service functionality along with Wi-Fi System Service. Enable Debug Logs: Enables/Disables Wi-Fi and Wi-Fi Provisioning System Service flows and levels. Note: In case the user enables debug logs, user needs to manually add the 'App Debug Service' component from Wireless-&gt; System Service-&gt; App Debug Service. ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/wifi/docs/configuration.html#configuration-options",
    "relUrl": "/system/wifi/docs/configuration.html#configuration-options"
  },"3": {
    "doc": "Wi-Fi System Service Configuration",
    "title": "Enabling Wi-Fi System Service",
    "content": "All of the required files are automatically added into the MPLAB X IDE project by the MHC when the library is selected for use. ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/wifi/docs/configuration.html#enabling-wi-fi-system-service",
    "relUrl": "/system/wifi/docs/configuration.html#enabling-wi-fi-system-service"
  },"4": {
    "doc": "Net System Service Configuration",
    "title": "Net System Service Configuration",
    "content": "The NET System Service library should be configured through the MHC. When user selects the NET System Service library, all the required dependencies components are added automatically in the MHC configuration. In the NET System Service library, user can select the mode as Client or Server and make required changes for the selected mode. The following figure shows the MHC configuration window for configuring the NET System Service and a brief description of various configuration options. | Open the MHC 3 | Drag the Net Service Module into the Active components from the Available components . | Configure the various parameters . | Configure the Supported Interface - ‘WIFI_ONLY’ (Wifi Only), or ‘WIFI_ETHERNET’ (Wifi and Ethernet Both). On choosing WIFI_ETHERNET, the MHC will add EthMAC, MIIM, and LAM8740 Components. The User needs to attach the EthMAC to the NetConfig (in System Component Window) via the MAC parameter in Instance 1 like below: . | Debug - Enabled by default - has ‘CLI Commands’ and ‘Debug Logs’ as sub parameters . | Enable CLI Commands - This is enabled by default. This can be used by the user to give commands on the CLI to open/ close/ send message on a socket. | Enable Debug Logs in case more prints are required for debugging. By Default, the parameter value is ‘False’.Note: In case the user enables debug logs, user needs to manually add the ‘App Debug Service’ component from Wireless-&gt; System Service-&gt; App Debug Service. | . | User can configure 2 instances of a Net Socket. By default, only the first one is enabled. | Instance 0: . | Configure the Network Interface as Wifi or Ethernet. Note that Ethernet as an interface can only be chosen if the ‘Supported Intefaces’ parameter is WIFI_ETHERNET. | Configure the IP Protocol as either TCP or UDP . | Configure the Mode as either Client or Server . | Enable/ Disable “Auto Connect” as per your requirement. This parameter when enabled ensures that if the NET Connection disconnects, the service internally tries to reconnect. By Default, the parameter value is ‘True’. | Enable/ Disable “Enable TLS” in case the connection needs to be secured. This parameter is valid only in case of ‘Client’ mode. Please note that in case this parameter is Enabled, users need to configure the WolfSSL related configuration on their own. Also, this parameter is valid only for TCP Connections. By Default, the parameter value is ‘False’.Note: In case the TLS is enabled, the User needs to update the component ‘Presentation Layer’ with the CA Certificate format, location, name, and size. Other parameters can be updated as per the User’s requirements. | Configure the various parameters of Presentation Layer if TLS enabled | . | Server Port - 1-65535. This is a mandatory parameter. In case Mode is selected as Client, Server port should be set to the port number of the server with which the device will connect. In case mode is selected as Server, Server port should be set to the port number at which the server will start . | Host Name/ IP Address: Can be a Host Name or an IP Address. By Default, the parameter value is ‘192.168.1.1’. | . | Instance 1 - User can enable this to give a configuration for another socket. Also, once the user gives this config, SYS_NET_Open() API will return error if it is passed NULL as config since now more than one instance is defined in the MHC. | . All of the required files are automatically added into the MPLAB X IDE project by the MHC when the Net Service is selected for use. ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/net/docs/configuration.html",
    "relUrl": "/system/net/docs/configuration.html"
  },"5": {
    "doc": "MQTT System Service Configuration",
    "title": "MQTT System Service Configuration",
    "content": "The MQTT System Service library should be configured through the MHC. When user selects the MQTT System Service library, all the required dependencies components are added automatically in the MHC configuration. The following figure shows the MHC configuration window for configuring the MQTT System Service and a brief description of various configuration options. | Open the MHC 3 | Drag the MQTT Service Module into the Active components from the Available components | . | Configure the various parameters of Basic Configuration | . | Parameter Name | Default Value | Description | . | Broker Name |   | Name of the MQTT BrokerNote: User should ensure that the Broker is UP and running. In case the connection timesout often, the User can modify the value of SYS_MQTT_PERIOIDC_TIMEOUT as per his requirement. | . | Server Port |   | Port number of the MQTT Broker at which the MQTT Client should connect | . | Enable TLS | FALSE | If TRUE, the MQTT connection should use TLS while connecting to the broker. If FALSE, the MQTT connection should not use TLS.Note: In case the TLS is enabled, the User needs to update the component ‘Presentation Layer’ with the CA Certificate format, location, name, and size. Other parameters can be updated as per the User’s requirements. | . | Client Id |   | MQTT Client Id should be unique for the Broker. If left empty, the Id will be generated randomly | . | Network Interface |   | Network Interface - Wifi or Ethernet on which the MQTT Client should run. On choosing Ethernet, the MHC will add EthMAC, MIIM, and LAM8740 Components. The User needs to attach the EthMAC to the NetConfig (in System Component Window) via the MAC parameter in Instance 1 | . | Configure the various parameters of Presentation Layer if TLS enabled | . | Configure the various parameters of ‘Advanced Configuration’ of the MQTT Service | . | Parameter Name | Default Value | Description | . | Enable Auto Reconnect | TRUE | If TRUE, the MQTT Service will auto reconnect to the Broker if connection is broken. If FALSE, the customer application needs to take care of triggering the connection process again. | . | Enable Clean Session | TRUE | If TRUE, the MQTT Client shall tell the Broker that the session is clean, else it will let the Broker know that the Session is a continuation of the previous session | . | KeepAlive Interval | 60 sec | If no data flows over an open connection for a certain KeepAliveInterval then the client will generate a PINGREQ and expect to receive a PINGRESP from the broker. This message exchange confirms that the connection is open and working | . | Username/ Password | Disabled | In case the connection to Broker needs a Username and Password | . | Last Will and testament | Disabled | LWT Configuration has the following parameters – 1. Topic, 2. QoS, 3. Retain, and 4. Message This ‘Message’ will be sent on the ‘Topic’ whenever the Broker finds that there is an ungraceful disconnection with the Client. | . | Configure the remaining parameters | . | Parameter Name | Default Value | Description | . | Subscription Topic | Disabled | Subscription configuration has 2 Parameters – 1. Topic and 2. Qos. (0 (Atmost Once), 1 (Atleast Once), 2 (Exactly Once)) The User can configure these parameters to subscribe to a Topic to receive messages. | . | Publish to Topic | Disabled | Publishing a message to Topic has 3 Parameters – 1. Topic and 2. Qos ( 0 (Atmost Once), 1 (Atleast Once), 2 (Exactly Once)) 3. Retain: If the Broker should retain the message The User can configure these parameters to and use them along with the message to send it on a particular Topic. | . | Enable CLI Commands | Enabled | Enabling this flag compiles in the CLI commands related to Mqtt Service. The user can use these CLI commands to connect/ disconnect, subscribe/ unsusbscribe, publish messages onto a topic. | . | Enable Debug Logs | Disabled | Enabling this flag compiles in debug logs and user can enable them at runtime. The user can use the following CLI commands to enable/ disable levels and flows for the MQTT service: 1. sysmqtt debug level 2. sysmqtt debug flow Note: In case the user enables debug logs, user needs to manually add the 'App Debug Service' component from Wireless-&gt; System Service-&gt; App Debug Service. | . All of the required files are automatically added into the MPLAB X IDE project by the MHC when the MQTT Service is selected for use. ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/mqtt/docs/configuration.html",
    "relUrl": "/system/mqtt/docs/configuration.html"
  },"6": {
    "doc": "Wi-Fi provisioning System Service Configuration",
    "title": "Wi-Fi provisioning System Service Configuration",
    "content": "The Wi-Fi Provisioning System Service library should be configured through MHC(MPLAB Harmony Configurator). The following figure shows the MHC configuration window for configuring the Wi-Fi Provisioning System Service and a brief description of various configuration options. The Wi-Fi Provisioning System Service library MHC menu provide option to enable required Wi-Fi Provisioning methods base on user application requirements. User can select Command line , Socket mode and HTTP as shown in below diagram. ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/configuration.html",
    "relUrl": "/system/wifiprov/docs/configuration.html"
  },"7": {
    "doc": "Wi-Fi provisioning System Service Configuration",
    "title": "Configuration Options:",
    "content": ". | WiFi Configuration Stored at NVM Address(Program Flash memory): . | NVM Address for storing Wi-Fi Configuration. | User can change this configuration value with program flash memory page aligned address. | User has to make sure the NVM address(Program Flash memory) page is not overwritten by application code. | . | Save Configuration in the NVM(Program flash memory): . | Indicates the Wi-Fi configuration storing in the NVM. | This configuration is only valid when “Enable Wi-Fi Provisioning service” is enabled. | . | . Wi-Fi Provisioning Methods . | Command Line(CLI): . | Enable/Disable Wi-Fi Provision using command line. | . | HTTP pages: . | Enable/Disable Wi-Fi Provision using HTTP pages(webpage). | HTTP Socket Number: . | User configuration for HTTP Server Socket. | Defult port number is 80. | . | . | TCP socket: . | Enable/Disable Wi-Fi Provision using TCP Socket. | TCP Socket Number: . | User configuration for TCP Server Socket. | Defult port number is 6666. TCP Socket port number is used by Mobile Applicaiton and JSON. | . | . | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/configuration.html#configuration-options",
    "relUrl": "/system/wifiprov/docs/configuration.html#configuration-options"
  },"8": {
    "doc": "Wi-Fi provisioning System Service Interface",
    "title": "Wi-Fi Provisioning System Service Interface",
    "content": ". | Data Types and Constants Summary | Initialization functions Summary | Status functions Summary | Setup functions Summary | Data Types and Constants . | SYS_WIFIPROV_AUTH | SYS_WIFIPROV_CTRLMSG | SYS_WIFIPROV_MODE | SYS_WIFIPROV_STA_CONFIG | SYS_WIFIPROV_AP_CONFIG | SYS_WIFIPROV_CONFIG | SYS_WIFIPROV_STATUS | SYS_WIFIPROV_RESULT | SYS_WIFIPROV_CALLBACK | . | Initialization functions . | SYS_WIFIPROV_Initialize | SYS_WIFIPROV_Deinitialize | . | Status functions . | SYS_WIFIPROV_GetStatus | . | Setup functions . | SYS_WIFIPROV_Tasks | SYS_WIFIPROV_CtrlMsg | . | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/interface.html#wi-fi-provisioning-system-service-interface",
    "relUrl": "/system/wifiprov/docs/interface.html#wi-fi-provisioning-system-service-interface"
  },"9": {
    "doc": "Wi-Fi provisioning System Service Interface",
    "title": "Data Types and Constants Summary",
    "content": "| Name | Description | . | SYS_WIFIPROV_AUTH | Identifies the type of Authentication requested. | . | SYS_WIFIPROV_CTRLMSG | Identifies the control message for which the client has called | . | SYS_WIFIPROV_MODE | Identifies the Wi-Fi operating mode. | . | SYS_WIFIPROV_STA_CONFIG | Configuration of station parameters. | . | SYS_WIFIPROV_AP_CONFIG | Configuration of access point mode parameters. | . | SYS_WIFIPROV_CONFIG | Configuration of device configuration parameters. | . | SYS_WIFIPROV_STATUS | Result of a Wi-Fi Provisioning system service client interface get | . | SYS_WIFIPROV_RESULT | Result of a Wi-Fi Provisioning system service client interface operation. | . | SYS_WIFIPROV_CALLBACK | Pointer to a Wi-Fi Provisioning system service callback function. | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/interface.html#data-types-and-constants-summary",
    "relUrl": "/system/wifiprov/docs/interface.html#data-types-and-constants-summary"
  },"10": {
    "doc": "Wi-Fi provisioning System Service Interface",
    "title": "Initialization functions Summary",
    "content": "| Name | Description | . | SYS_WIFIPROV_Initialize | Initializes the System Wi-Fi Provisioning module. | . | SYS_WIFIPROV_Deinitialize | Deinitializes the module instance of the SYS WIFIPROV module | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/interface.html#initialization-functions-summary",
    "relUrl": "/system/wifiprov/docs/interface.html#initialization-functions-summary"
  },"11": {
    "doc": "Wi-Fi provisioning System Service Interface",
    "title": "Status functions Summary",
    "content": "| Name | Description | . | SYS_WIFIPROV_GetStatus | Returns System Wi-Fi Provisioning service status. | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/interface.html#status-functions-summary",
    "relUrl": "/system/wifiprov/docs/interface.html#status-functions-summary"
  },"12": {
    "doc": "Wi-Fi provisioning System Service Interface",
    "title": "Setup functions Summary",
    "content": "| Name | Description | . | SYS_WIFIPROV_Tasks | Maintains the Wi-Fi Provisioning System tasks and functionalities. | . | SYS_WIFIPROV_CtrlMsg | Request Wi-Fi Provisioning system service control request interface | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/interface.html#setup-functions-summary",
    "relUrl": "/system/wifiprov/docs/interface.html#setup-functions-summary"
  },"13": {
    "doc": "Wi-Fi provisioning System Service Interface",
    "title": "Data Types and Constants",
    "content": "SYS_WIFIPROV_AUTH . Summary . Identifies the type of Authentication requested. Description . Identifies the type of Authentication requested. Remarks . None. typedef enum { /* Requesting a Open Authentication types */ SYS_WIFIPROV_OPEN = 1, /* Requesting a WEP Authentication types */ SYS_WIFIPROV_WEP, /* Requesting a WPA/WPA2(Mixed) Authentication types */ SYS_WIFIPROV_WPAWPA2MIXED, /* Requesting a WPA2 Authentication types */ SYS_WIFIPROV_WPA2, /* Requesting a WPA2/WPA3(Mixed) Authentication types */ SYS_WIFIPROV_WPA2WPA3MIXED, /* Requesting a WPA3 Authentication types */ SYS_WIFIPROV_WPA3 } SYS_WIFIPROV_AUTH ; . SYS_WIFIPROV_CTRLMSG . Summary . Identifies the control message for which the client has called the SYS_WIFIPROV_CtrlMsg(). Description . Identifies the control message for which the client has called the SYS_WIFIPROV_CtrlMsg(). Remarks . The different control messages which can be invoked by the client. typedef enum { /* Requesting a Wi-Fi Configuration set(for connect) */ SYS_WIFIPROV_SETCONFIG = 0, /* Requesting a Wi-Fi configuration get */ SYS_WIFIPROV_GETCONFIG, /* Updating Wi-Fi Connect status for enabling Wi-Fi Provisioning service */ SYS_WIFIPROV_CONNECT, } SYS_WIFIPROV_CTRLMSG ; . SYS_WIFIPROV_MODE . Summary . Identifies the Wi-Fi operating mode. Description . Identifies the Wi-Fi operating mode. Remarks . Client need to manually reboot device after switching mode. For example changing operating mode from STA to AP or AP to STA. typedef enum { /* Requesting a operating mode as a station */ SYS_WIFIPROV_STA = 0, /* Requesting a operating mode as a access point. */ SYS_WIFIPROV_AP = 1 } SYS_WIFIPROV_MODE ; . SYS_WIFIPROV_STA_CONFIG . Summary . Configuration of station parameters. Description . Configuration of station parameters. Remarks . None. typedef struct { /* Wi-Fi station mode SSID */ uint8_t ssid[32]; /* Wi-Fi station mode passphrase */ uint8_t psk[64]; /* Wi-Fi station mode authentication type */ SYS_WIFIPROV_AUTH authType; /* Wi-Fi station mode channel number. values of channel: 0 - scan and connect to all the channels 1 to 13 - - scan and connect to specified channel */ uint8_t channel; /* Wi-Fi station mode auto connect flag. value 0- Don't connect to AP, wait for client request. value 1- Connect to AP */ bool autoConnect; } SYS_WIFIPROV_STA_CONFIG; . SYS_WIFIPROV_AP_CONFIG . Summary . Configuration of access point mode parameters. Description . Configuration of access point mode parameters. Remarks . None. typedef struct { /* Wi-Fi access point mode SSID */ uint8_t ssid[32]; /* Wi-Fi access point mode passphrase */ uint8_t psk[64]; /* Wi-Fi access point mode authentication type */ SYS_WIFIPROV_AUTH authType; /* Wi-Fi access point mode channel number values of channel: 1 to 13 - operating channel of access point */ uint8_t channel; /* Wi-Fi access point mode SSID visibility Value of ssidVisibility: 0 - Hidden SSID 1 - broadcast the SSID */ bool ssidVisibility; } SYS_WIFIPROV_AP_CONFIG; . SYS_WIFIPROV_CONFIG . Summary . Configuration of device configuration parameters. Description . Configuration of device configuration parameters. Remarks . None. typedef struct { /* Operating mode of device */ SYS_WIFIPROV_MODE mode; /* Flag to identify if configuration needs to be saved in NVM. 0 - Do not save configuration in NVM. 1 - Save configuration in NVM. */ uint8_t saveConfig; /* Country Code configuration */ uint8_t countryCode[5]; /* Wi-Fi station mode configuration */ SYS_WIFIPROV_STA_CONFIG staConfig; /* Wi-Fi access point mode configuration */ SYS_WIFIPROV_AP_CONFIG apConfig; }SYS_WIFIPROV_CONFIG; . SYS_WIFIPROV_STATUS . Summary . Result of a Wi-Fi Provisioning system service client interface get operation(SYS_WIFIPROV_GetStatus()). Description . Result of a Wi-Fi Provisioning system service client interface get operation(SYS_WIFIPROV_GetStatus()). Remarks . None. typedef enum { /* Wi-Fi Provisioning system service is in MPFS filesystem mount state */ SYS_WIFIPROV_STATUS_MPFS_MOUNT=1, /* Wi-Fi Provisioning system service is in NVM read state */ SYS_WIFIPROV_STATUS_NVM_READ, /* Wi-Fi Provisioning system service is in NVM read Wi-Fi Configuration checking state */ SYS_WIFIPROV_STATUS_CONFIG_CHECK, /* Wi-Fi Provisioning system service is in NVM erase state */ SYS_WIFIPROV_STATUS_NVM_ERASE, /* Wi-Fi Provisioning system service is in NVM write state */ SYS_WIFIPROV_STATUS_NVM_WRITE, /* Wi-Fi Provisioning system service is in wait for NVM write to complate state */ SYS_WIFIPROV_STATUS_WAITFORWRITE, /* Wi-Fi Provisioning system service is in client request state */ SYS_WIFIPROV_STATUS_WAITFORREQ, /*Wi-Fi Provisioning system service is in invalid state */ SYS_WIFIPROV_STATUS_NONE =255 } SYS_WIFIPROV_STATUS; . SYS_WIFIPROV_RESULT . Summary . Result of a Wi-Fi Provisioning system service client interface operation. Description . Identifies the result of Wi-Fi Provisioning service operations . Remarks . None. typedef enum{ /* Operation completed with success */ SYS_WIFIPROV_SUCCESS = 0, /* Operation failed. */ SYS_WIFIPROV_FAILURE, /* Operation request object is invalid */ SYS_WIFIPROV_OBJ_INVALID=255 }SYS_WIFIPROV_RESULT; . SYS_WIFIPROV_CALLBACK . Function . typedef void (*SYS_WIFIPROV_CALLBACK ) ( uint32_t event, void * data, void *cookie ) . Summary . Pointer to a Wi-Fi Provisioning system service callback function. Description . This data type defines a pointer to a Wi-Fi Provisioning service callback function. Callback functions can be registered by client at initializing. Precondition . None . Parameters . event - A event value, event can be any of SYS_WIFIPROV_CTRLMSG types. data - Wi-Fi Provisioning service Data. cookie - Client register cookie. Returns . None. Example . void WiFiProvServCallback (uint32_t event, void * data,void *cookie ) { switch(event) { case SYS_WIFIPROV_SETCONFIG: { SYS_WIFIPROV_CONFIG* wifiProvConfig = (SYS_WIFIPROV_CONFIG *) data; // Provisioning service updated data SYS_CONSOLE_PRINT(\\\"%s:%d Device mode=%d\\\\r\\\\n\\\",__func__,__LINE__,wifiProvConfig-&gt;mode); break; } case SYS_WIFIPROV_GETCONFIG: { SYS_WIFIPROV_CONFIG* wifiProvConfig = (SYS_WIFIPROV_CONFIG *) data; // client requested get Wi-Fi Configuration SYS_CONSOLE_PRINT(\\\"%s:%d Device mode=%d\\\\r\\\\n\\\",__func__,__LINE__,wifiProvConfig-&gt;mode); break; } } } . Remarks . None. typedef void (*SYS_WIFIPROV_CALLBACK )(uint32_t event, void * data,void *cookie ); . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/interface.html#data-types-and-constants",
    "relUrl": "/system/wifiprov/docs/interface.html#data-types-and-constants"
  },"14": {
    "doc": "Wi-Fi provisioning System Service Interface",
    "title": "Initialization functions",
    "content": "SYS_WIFIPROV_Initialize . Function . SYS_MODULE_OBJ SYS_WIFIPROV_Initialize ( SYS_WIFIPROV_CONFIG *config, SYS_WIFIPROV_CALLBACK callback, void *cookie ) . Summary . Initializes the System Wi-Fi Provisioning module. Description . Wi-Fi Provisioning service supports only single instance. Parameters . config - Wi-Fi Provisioning device configuration structure. callback - The client callback function pointer. cookie - The pointer which will be passed to the client application when the client callback function is invoked. Returns . If successful, returns a valid handle to an object. Otherwise, it returns SYS_MODULE_OBJ_INVALID. Example . #define WIFI_DEV_SSID \\\"DEMO_AP\\\" #define WIFI_DEV_PSK \\\"password\\\" SYS_WIFIPROV_CONFIG wifiProvConfig; SYS_MODULE_OBJ wifiProvServHandle; // Set mode as STA wifiProvConfig.mode = SYS_WIFI_STA; // Disable saving wifi configuration wifiProvConfig.saveConfig = false; //Set the auth type to SYS_WIFI_WPA2 wifiProvConfig.staConfig.authType = SYS_WIFI_WPA2; // Enable all the channels(0) wifiProvConfig.staConfig.channel = 0; // Device doesn't wait for user request. wifiProvConfig.staConfig.autoConnect = 1; // Set SSID memcpy(wifiProvConfig.staConfig.ssid,WIFI_DEV_SSID,sizeof(WIFI_DEV_SSID)); // Set PSK memcpy(wifiProvConfig.staConfig.psk,WIFI_DEV_PSK,sizeof(WIFI_DEV_PSK)); wifiProvServHandle = SYS_WIFIPROV_Initialize(&amp;wifiProvConfig, WiFiProvServCallback, 0); if (wifiProvServHandle == SYS_MODULE_OBJ_INVALID) { // Handle error } . Remarks . Client can auto enable the Provisioning service functionality by selecting MHC configuration option of Wi-Fi Service. SYS_WIFIPROV_Deinitialize . Function . SYS_WIFIPROV_RESULT SYS_WIFIPROV_Deinitialize (SYS_MODULE_OBJ object) . Summary . Deinitializes the module instance of the SYS WIFIPROV module . Description . This function deinitializes the module instance disabling its operation. Resets all of the internal data structures and fields to the default settings. Precondition . The SYS_WIFIPROV_Initialize function should have been called before calling this function. Parameters . object - SYS WIFIPROV object handle, returned from SYS_WIFIPROV_Initialize . Returns . return SYS_WIFIPROV_RESULT . Example . if (SYS_WIFI_SUCCESS == SYS_WIFIPROV_Deinitialize (wifiProvServHandle)) { // when the SYS WIFI is De-initialized. } . Remarks . Deinitialize should be called if the WiFi Provisioning service is no longer going to be used. ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/interface.html#initialization-functions",
    "relUrl": "/system/wifiprov/docs/interface.html#initialization-functions"
  },"15": {
    "doc": "Wi-Fi provisioning System Service Interface",
    "title": "Status functions",
    "content": "SYS_WIFIPROV_GetStatus . Function . uint8_t SYS_WIFIPROV_GetStatus ( SYS_MODULE_OBJ object) . Summary . Returns System Wi-Fi Provisioning service status. Description . This function returns the current status of the System Wi-Fi Provisioning service. Precondition . The SYS_WIFIPROV_Initialize function should have been called before calling this function. Parameters . object - SYS WIFIPROV object handle, returned from SYS_WIFIPROV_Initialize . Returns . return SYS_WIFIPROV_STATUS if client provided object is valid, else return SYS_WIFIPROV_OBJ_INVALID. Example . if (SYS_WIFIPROV_STATE_WAITFORREQ == SYS_WIFIPROV_GetStatus (wifiProvServHandle)) { // when the SYS WIFI Provisioning module in wait for client request } . Remarks . None . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/interface.html#status-functions",
    "relUrl": "/system/wifiprov/docs/interface.html#status-functions"
  },"16": {
    "doc": "Wi-Fi provisioning System Service Interface",
    "title": "Setup functions",
    "content": "SYS_WIFIPROV_Tasks . Function . uint8_t SYS_WIFIPROV_Tasks ( SYS_MODULE_OBJ object) . Summary . Maintains the Wi-Fi Provisioning System tasks and functionalities. Description . This function is used to run the various tasks and functionalities of Wi-Fi Provisioning system service. Precondition . The SYS_WIFIPROV_Initialize function should have been called before calling this function. Parameters . object - SYS WIFI Provisioning object handle, returned from SYS_WIFIPROV_Initialize . Returns . return SYS_WIFIPROV_STATUS if client provided object is valid, else return SYS_WIFIPROV_OBJ_INVALID. Example . if (SYS_WIFIPROV_OBJ_INVALID != SYS_WIFIPROV_Tasks (wifiProvServHandle)) { } . Remarks . None . SYS_WIFIPROV_CtrlMsg . Function . SYS_WIFIPROV_RESULT SYS_WIFIPROV_CtrlMsg (SYS_MODULE_OBJ object,uint32_t event,void *buffer,uint32_t length ) . Summary . Request Wi-Fi Provisioning system service control request interface . Description . This function is used to make control request to Wi-Fi Provisioning system service. Precondition . The SYS_WIFIPROV_Initialize function should have been called before calling this function. Parameters . object - SYS WIFIPROV object handle, returned from SYS_WIFIPROV_Initialize . event - A event value, event can be any of SYS_WIFIPROV_CTRLMSG types . buffer - Control message data input. length - size of buffer data . Returns . return SYS_WIFIPROV_RESULT. Example . Details of SYS_WIFIPROV_SETCONFIG: SYS_WIFIPROV_CONFIG wifiProvConfig; SYS_MODULE_OBJ wifiProvServHandle; // Set mode as STA wifiProvConfig.mode = SYS_WIFI_STA; // Disable saving wifi configuration wifiProvConfig.saveConfig = false; // Set the auth type to SYS_WIFI_WPA2 wifiProvConfig.staConfig.authType = SYS_WIFI_WPA2; // Enable all the channels(0) wifiProvConfig.staConfig.channel = 0; // Device doesn't wait for user request wifiProvConfig.staConfig.autoConnect = 1; // Set SSID memcpy(wifiProvConfig.staConfig.ssid,WIFI_DEV_SSID,sizeof(WIFI_DEV_SSID)); // Set PSK memcpy(wifiProvConfig.staConfig.psk,WIFI_DEV_PSK,sizeof(WIFI_DEV_PSK)); if (SYS_WIFIPROV_OBJ_INVALID != SYS_WIFIPROV_CtrlMsg (wifiProvServHandle,SYS_WIFIPROV_SETCONFIG,&amp;wifiProvConfig,sizeof(SYS_WIFIPROV_CONFIG))) { // When Wi-Fi Provisioning Configuration need to be updated } Details of SYS_WIFIPROV_GETCONFIG: SYS_WIFIPROV_CtrlMsg (wifiProvServHandle,SYS_WIFIPROV_GETCONFIG,NULL,0); Details of SYS_WIFIPROV_CONNECT: // Updating Wi-Fi Connected state to Provisioning service bool wifiProvConnectState = true; SYS_WIFIPROV_CtrlMsg (wifiProvServHandle,SYS_WIFIPROV_CONNECT,&amp;wifiProvConnectState,sizeof(wifiProvConnectState)); // Updating Wi-Fi disconnected state to Provisioning service bool wifiProvConnectState = false; SYS_WIFIPROV_CtrlMsg (wifiProvServHandle,SYS_WIFIPROV_CONNECT,&amp;wifiProvConnectState,sizeof(wifiProvConnectState)); . Remarks . None . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/interface.html#setup-functions",
    "relUrl": "/system/wifiprov/docs/interface.html#setup-functions"
  },"17": {
    "doc": "Wi-Fi provisioning System Service Interface",
    "title": "Wi-Fi provisioning System Service Interface",
    "content": " ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/interface.html",
    "relUrl": "/system/wifiprov/docs/interface.html"
  },"18": {
    "doc": "Net System Service Interface",
    "title": "Net System Service Interface",
    "content": ". | Data Types and Constants Summary | Initialization functions Summary | Status functions Summary | Setup functions Summary | Data Exchange functions Summary | Data Types and Constants . | SYS_NET_INTF_WIFI | SYS_NET_INTF_ETHERNET | SYS_NET_MODE_CLIENT | SYS_NET_MODE_SERVER | SYS_NET_MAX_HOSTNAME_LEN | SYS_NET_IP_PROT_UDP | SYS_NET_IP_PROT_TCP | SYS_NET_MAX_NUM_OF_SOCKETS | SYS_NET_DEFAULT_TLS_ENABLE | SYS_NET_DEFAULT_AUTO_RECONNECT | SYS_NET_DEFAULT_NET_INTF | NET_CFG | NET_DATA | SYS_NET_Config | SYS_NET_STATUS | SYS_NET_EVENT | SYS_NET_CTRL_MSG | SYS_NET_RESULT | . | Initialization functions . | SYS_NET_Initialize | SYS_NET_Deinitialize | . | Status functions . | SYS_NET_GetStatus | . | Setup functions . | SYS_NET_Open | SYS_NET_Close | SYS_NET_Task | SYS_NET_CtrlMsg | SYS_NET_SetConfigParam | . | Data Exchange functions . | SYS_NET_SendMsg | SYS_NET_RecvMsg | SYS_NET_CALLBACK | . | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/net/docs/interface.html",
    "relUrl": "/system/net/docs/interface.html"
  },"19": {
    "doc": "Net System Service Interface",
    "title": "Data Types and Constants Summary",
    "content": "| Name | Description | . | SYS_NET_INTF_WIFI | Net Socket Intf - Wifi | . | SYS_NET_INTF_ETHERNET | Net Socket Intf - Ethernet | . | SYS_NET_MODE_CLIENT | Net Socket Mode - Client | . | SYS_NET_MODE_SERVER | Net Socket Mode - Server | . | SYS_NET_MAX_HOSTNAME_LEN | Max Host Name Length | . | SYS_NET_IP_PROT_UDP | Ip Protocol Mode - UDP | . | SYS_NET_IP_PROT_TCP | Ip Protocol Mode - TCP | . | SYS_NET_MAX_NUM_OF_SOCKETS | Number of Instances Supported by the NET System Service | . | SYS_NET_DEFAULT_TLS_ENABLE | Default Values for TLS - False | . | SYS_NET_DEFAULT_AUTO_RECONNECT | Default Values for Auto Reconnect - True | . | SYS_NET_DEFAULT_NET_INTF | Default Values for Interface - 0 (Wifi) | . | NET_CFG | AppDebug Flow for the Logs - Configuration | . | NET_DATA | AppDebug Flow for the Logs - Data | . | SYS_NET_Config | Used for passing on the configuration related to the Net Socket that needs | . | SYS_NET_STATUS | Identifies the current status of the Sys Net Instance. | . | SYS_NET_EVENT | Identifies the event type for which the User Callback is called. | . | SYS_NET_CTRL_MSG | Identifies the control message for which the User has called the SYS_NET_CtrlMsg(). | . | SYS_NET_RESULT | Identifies the return values for the Sys Net APIs. | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/net/docs/interface.html#data-types-and-constants-summary",
    "relUrl": "/system/net/docs/interface.html#data-types-and-constants-summary"
  },"20": {
    "doc": "Net System Service Interface",
    "title": "Initialization functions Summary",
    "content": "| Name | Description | . | SYS_NET_Initialize | Returns success/ failure for initialization of data structures of the NET service | . | SYS_NET_Deinitialize | Deinitialization of data structures of the NET service | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/net/docs/interface.html#initialization-functions-summary",
    "relUrl": "/system/net/docs/interface.html#initialization-functions-summary"
  },"21": {
    "doc": "Net System Service Interface",
    "title": "Status functions Summary",
    "content": "| Name | Description | . | SYS_NET_GetStatus | Returns System NET instance status. | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/net/docs/interface.html#status-functions-summary",
    "relUrl": "/system/net/docs/interface.html#status-functions-summary"
  },"22": {
    "doc": "Net System Service Interface",
    "title": "Setup functions Summary",
    "content": "| Name | Description | . | SYS_NET_Open | Opens a new NET System Service instance. | . | SYS_NET_Close | Deinitializes the specific instance of the NET System service | . | SYS_NET_Task | Executes the SYS NET service state machine for the instance | . | SYS_NET_CtrlMsg | Returns success/ failure for the disconnect/ reconnect operation asked by the user. | . | SYS_NET_SetConfigParam | Returns success on setting a configuration parameter for Net System Service. | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/net/docs/interface.html#setup-functions-summary",
    "relUrl": "/system/net/docs/interface.html#setup-functions-summary"
  },"23": {
    "doc": "Net System Service Interface",
    "title": "Data Exchange functions Summary",
    "content": "| Name | Description | . | SYS_NET_SendMsg | Returns No of Bytes sent to peer using the System NET instance. | . | SYS_NET_RecvMsg | Returns No of Bytes received from peer using the System NET instance. | . | SYS_NET_CALLBACK | Pointer to a Net system service callback function. | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/net/docs/interface.html#data-exchange-functions-summary",
    "relUrl": "/system/net/docs/interface.html#data-exchange-functions-summary"
  },"24": {
    "doc": "Net System Service Interface",
    "title": "Data Types and Constants",
    "content": "SYS_NET_INTF_WIFI . Summary . Net Socket Intf - Wifi . Remarks . None. #define SYS_NET_INTF_WIFI 0 // Wifi Intf Value . SYS_NET_INTF_ETHERNET . Summary . Net Socket Intf - Ethernet . Remarks . None. #define SYS_NET_INTF_ETHERNET 1 // Ethernet Intf Value . SYS_NET_MODE_CLIENT . Summary . Net Socket Mode - Client . Remarks . None. #define SYS_NET_MODE_CLIENT 0 // Client Mode Value . SYS_NET_MODE_SERVER . Summary . Net Socket Mode - Server . Remarks . None. #define SYS_NET_MODE_SERVER 1 // Server Mode Value . SYS_NET_MAX_HOSTNAME_LEN . Summary . Max Host Name Length . Remarks . None. #define SYS_NET_MAX_HOSTNAME_LEN 256 // Max Host Name Length . SYS_NET_IP_PROT_UDP . Summary . Ip Protocol Mode - UDP . Remarks . None. #define SYS_NET_IP_PROT_UDP 0 // UDP - Ip Protocol Value . SYS_NET_IP_PROT_TCP . Summary . Ip Protocol Mode - TCP . Remarks . None. #define SYS_NET_IP_PROT_TCP 1 // TCP - Ip Protocol Value . SYS_NET_MAX_NUM_OF_SOCKETS . Summary . Number of Instances Supported by the NET System Service . Remarks . None. #define SYS_NET_MAX_NUM_OF_SOCKETS 2 // umber of Instances Supported by the NET System Service . SYS_NET_DEFAULT_TLS_ENABLE . Summary . Default Values for TLS - False . Remarks . None. #define SYS_NET_DEFAULT_TLS_ENABLE 0 // TLS Disabled by default . SYS_NET_DEFAULT_AUTO_RECONNECT . Summary . Default Values for Auto Reconnect - True . Remarks . None. #define SYS_NET_DEFAULT_AUTO_RECONNECT 1 // Auto Reconnect Enabled by default . SYS_NET_DEFAULT_NET_INTF . Summary . Default Values for Interface - 0 (Wifi) . Remarks . None. #define SYS_NET_DEFAULT_NET_INTF 0 // Interface 0 by default . NET_CFG . Summary . AppDebug Flow for the Logs - Configuration . Remarks . None. #define NET_CFG 0x1 // App Debug Print Flows - CFG . NET_DATA . Summary . AppDebug Flow for the Logs - Data . Remarks . None. #define NET_DATA 0x2 // App Debug Print Flows - DATA . SYS_NET_Config . Summary . Used for passing on the configuration related to the Net Socket that needs to be opened via the Sys Net Service . Remarks . None. typedef struct { // Net Socket Mode to Open - SYS_NET_MODE_CLIENT(0)/ SYS_NET_MODE_SERVER(1) uint8_t mode; // WiFi or Eth Interface to be used for Opening the socket uint8_t intf; // Net Server Port uint16_t port; // Reconnect in case of disconnection happening - 1(Reconnect Enabled)/ 0(Reconnect Disabled) bool enable_reconnect; // Net Socket with 1(TLS Enabled)/ 0(TLS Disabled) bool enable_tls; // Socket IP Protocol - SYS_NET_IP_PROT_UDP(0) or SYS_NET_IP_PROT_TCP(1) uint8_t ip_prot; // Host Name - could have the server name or IP char host_name[SYS_NET_MAX_HOSTNAME_LEN]; } SYS_NET_Config; . SYS_NET_STATUS . Summary . Identifies the current status of the Sys Net Instance. Remarks . None. typedef enum { // Net Instance is Idle/ Not in Use SYS_NET_STATUS_IDLE = 0, // Lower Layer is Down SYS_NET_STATUS_LOWER_LAYER_DOWN, // Resolving DNS of NET Server for the Client to connect SYS_NET_STATUS_RESOLVING_DNS, // Net Server IP Available for the Client to connect SYS_NET_STATUS_DNS_RESOLVED, // Net Server Awaiting Connection SYS_NET_STATUS_SERVER_AWAITING_CONNECTION, // Net Client connecting to Server SYS_NET_STATUS_CLIENT_CONNECTING, // Net Client Waiting for SNTP Time Stamp SYS_NET_STATUS_WAIT_FOR_SNTP, // Net Client Starting TLS Negotiations SYS_NET_STATUS_TLS_NEGOTIATING, // Net Instance TLS Negotiation Failed SYS_NET_STATUS_TLS_NEGOTIATION_FAILED, // Net Instance connected to the peer SYS_NET_STATUS_CONNECTED, // Net Instance Failed to open socket SYS_NET_STATUS_SOCK_OPEN_FAILED, // Net Instance Failed to Resolve DNS SYS_NET_STATUS_DNS_RESOLVE_FAILED, // Net Instance in disconnected state SYS_NET_STATUS_DISCONNECTED, // Net Instance received FIN from peer SYS_NET_STATUS_PEER_SENT_FIN, } SYS_NET_STATUS; . SYS_NET_EVENT . Summary . Identifies the event type for which the User Callback is called. Remarks . None. typedef enum { // NET Socket connected to Peer SYS_NET_EVNT_CONNECTED = 0, // NET Socket disconnected SYS_NET_EVNT_DISCONNECTED, // Received Data on NET Socket connected to Peer SYS_NET_EVNT_RCVD_DATA, // SSL Negotiation Failed SYS_NET_EVNT_SSL_FAILED, // DNS Resolve Failed SYS_NET_EVNT_DNS_RESOLVE_FAILED, // Socket Open Failed SYS_NET_EVNT_SOCK_OPEN_FAILED, } SYS_NET_EVENT; . SYS_NET_CTRL_MSG . Summary . Identifies the control message for which the User has called the SYS_NET_CtrlMsg(). Remarks . None. typedef enum { // NET Socket should reconnect to Peer, the User is expected to pass pointer to SYS_NET_Config for the configuration of the new Connection. SYS_NET_CTRL_MSG_RECONNECT = 0, // NET Socket disconnect request from the user SYS_NET_CTRL_MSG_DISCONNECT, } SYS_NET_CTRL_MSG; . SYS_NET_RESULT . Summary . Identifies the return values for the Sys Net APIs. Remarks . None. typedef enum { // Success SYS_NET_SUCCESS = 0, // Failure SYS_NET_FAILURE = -1, // Sys NET Service Down SYS_NET_SERVICE_DOWN = -2, // Enough space not available in the transmit buffer to send the message. Application should try again later SYS_NET_PUT_NOT_READY = -3, // Sys NET No Data Available for receiving SYS_NET_GET_NOT_READY = -4, // Sys NET Semaphore Operation of Take/ Release Failed SYS_NET_SEM_OPERATION_FAILURE = -5, // Sys NET Invalid Handle SYS_NET_INVALID_HANDLE = -6, } SYS_NET_RESULT; . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/net/docs/interface.html#data-types-and-constants",
    "relUrl": "/system/net/docs/interface.html#data-types-and-constants"
  },"25": {
    "doc": "Net System Service Interface",
    "title": "Initialization functions",
    "content": "SYS_NET_Initialize . Function . int32_t SYS_NET_Initialize() . Summary . Returns success/ failure for initialization of data structures of the NET service . Description . This function is used for initializing the data structures of the NET service and is called from within the System Task. Returns . SYS_NET_SUCCESS - Indicates the data structures were initialized successfully . SYS_NET_FAILURE - Indicates that it failed to initialize the data structures. Example . if( SYS_NET_Initialize() == SYS_NET_SUCCESS) { } . Remarks . If the Net system service is enabled using MHC, then auto generated code will take care of Net System Service initialization. SYS_NET_Deinitialize . Function . void SYS_NET_Deinitialize() . Summary . Deinitialization of data structures of the NET service . Description . This function is used for freeing the allocated data structures for the NET service. Example . SYS_NET_Deinitialize() . Remarks . None . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/net/docs/interface.html#initialization-functions",
    "relUrl": "/system/net/docs/interface.html#initialization-functions"
  },"26": {
    "doc": "Net System Service Interface",
    "title": "Status functions",
    "content": "SYS_NET_GetStatus . Function . SYS_NET_STATUS SYS_NET_GetStatus ( SYS_MODULE_OBJ object ) . Summary . Returns System NET instance status. Description . This function returns the current status of the System NET instance. Precondition . SYS_NET_Open should have been called before calling this function . Parameters . object - SYS NET object handle, returned from SYS_NET_Open . Returns . SYS_NET_STATUS . Example . // Handle \\\"objSysNet\\\" value must have been returned from SYS_NET_Open. if (SYS_NET_GetStatus (objSysNet) == SYS_NET_STATUS_SERVER_AWAITING_CONNECTION) { // NET system service is initialized and the NET server is ready to accept new connection. } . Remarks . None. ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/net/docs/interface.html#status-functions",
    "relUrl": "/system/net/docs/interface.html#status-functions"
  },"27": {
    "doc": "Net System Service Interface",
    "title": "Setup functions",
    "content": "SYS_NET_Open . Function . SYS_MODULE_OBJ SYS_NET_Open (SYS_NET_Config *cfg, SYS_NET_CALLBACK Net_cb, void *cookie) . Summary . Opens a new NET System Service instance. Description . This function opens the instance of the NET System Service. Parameters . cfg - Configuration for which the NET Socket needs to be opened Net_cb - Function pointer to the Callback to be called in case of an event cookie - Cookie passed as one of the params in the Callback which was registered by the user in SYS_NET_Open Returns . Returns: If successful, returns a valid handle to an object. Otherwise, it returns SYS_MODULE_OBJ_INVALID. Example . SYS_NET_Config g_NetServCfg; SYS_MODULE_OBJ g_NetServHandle; memset(&amp;g_NetServCfg, 0, sizeof(g_NetServCfg)); g_NetServCfg.mode = SYS_NET_MODE_CLIENT; strcpy(g_NetServCfg.host_name, APP_HOST_NAME); g_NetServCfg.port = APP_HOST_PORT; g_NetServCfg.enable_tls = 0; g_NetServCfg.ip_prot = SYS_NET_IP_PROT_UDP; g_NetServHandle = SYS_NET_Open(&amp;g_NetServCfg, NetServCallback, 0); if (g_NetServHandle == SYS_MODULE_OBJ_INVALID) { // Handle error } . Remarks . This routine should be called everytime a user wants to open a new NET socket . SYS_NET_Close . Function . void SYS_NET_Close ( SYS_MODULE_OBJ object ) . Summary . Deinitializes the specific instance of the NET System service . Description . This function deinitializes the specific module instance disabling its operation. Resets all of the internal data structures and fields for the specified instance to the default settings. Precondition . The SYS_NET_Open function should have been called before calling this function. Parameters . object - SYS NET object handle, returned from SYS_NET_Open . Returns . None. Example . // Handle \\\"objSysNet\\\" value must have been returned from SYS_NET_Open. SYS_NET_Close (objSysNet); . Remarks . Once the Open operation has been called, the Close operation must be called before the Open operation can be called again. SYS_NET_Task . Function . void SYS_NET_Task(SYS_MODULE_OBJ obj) . Summary . Executes the SYS NET service state machine for the instance . Description . This function ensures that the Net system service is able to execute its state machine to process any messages and invoke the user callback for any events. Precondition . SYS_NET_Open should have been called before calling this function . Parameters . obj - SYS NET object handle, returned from SYS_NET_Open . Returns . None . Example . // Handle \\\"objSysNet\\\" value must have been returned from SYS_NET_Open. while(1) { ... SYS_NET_Task(objSysNet); ... } . SYS_NET_CtrlMsg . Function . int32_t SYS_NET_CtrlMsg(SYS_MODULE_OBJ obj, SYS_NET_CTRL_MSG msg_type, void *data, uint16_t len) . Summary . Returns success/ failure for the disconnect/ reconnect operation asked by the user. Description . This function is used for disconnecting or reconnecting to the peer. Precondition . SYS_NET_Open should have been called. Parameters . obj - SYS NET object handle, returned from SYS_NET_Open msg_type - valid Msg Type SYS_NET_CTRL_MSG . data - valid data buffer pointer based on the Msg Type - NULL for DISCONNECT, Pointer to SYS_NET_Config for RECONNECT len - length of the data buffer the pointer is pointing to . Returns . SYS_NET_SUCCESS - Indicates that the Request was catered to successfully . SYS_NET_FAILURE - Indicates that the Request failed . Example . // Handle \\\"objSysNet\\\" value must have been returned from SYS_NET_Open. if( SYS_NET_CtrlMsg(objSysNet, SYS_NET_CTRL_MSG_DISCONNECT, NULL, 0) == SYS_NET_SUCCESS) { } . Remarks . None. SYS_NET_SetConfigParam . Function . int32_t SYS_NET_SetConfigParam(SYS_MODULE_OBJ obj, uint32_t paramType, void *data) . Summary . Returns success on setting a configuration parameter for Net System Service. Description . This function is currently used for enabling/ disabling the Auto Reconnect feature for the Net Socket. Precondition . SYS_NET_Open should have been called. Parameters . obj - SYS NET object handle, returned from SYS_NET_Open paramType - Reserved for future use data - 0/ 1 currently used only for enabling/ disabling the auto reconnect feature . Returns . SYS_NET_SUCCESS - Indicates that the Request was catered to successfully . Example . bool auto_reconnect = true; // Handle \\\"objSysNet\\\" value must have been returned from SYS_NET_Open. if( SYS_NET_SetConfigParam(objSysNet, 0, &amp;auto_reconnect) == SYS_NET_SUCCESS) { } . Remarks . None. ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/net/docs/interface.html#setup-functions",
    "relUrl": "/system/net/docs/interface.html#setup-functions"
  },"28": {
    "doc": "Net System Service Interface",
    "title": "Data Exchange functions",
    "content": "SYS_NET_SendMsg . Function . int32_t SYS_NET_SendMsg(SYS_MODULE_OBJ obj, uint8_t *buffer, uint16_t len) . Summary . Returns No of Bytes sent to peer using the System NET instance. Description . This function returns the number of bytes transmitted to the peer. Precondition . SYS_NET_Open should have been called. Parameters . object - SYS NET object handle, returned from SYS_NET_Open data - valid data buffer pointer len - length of the data to be transmitted . Returns . SYS_NET_SERVICE_DOWN - Indicates that the System NET instance is not connected to the peer . SYS_NET_PUT_NOT_READY - Indicates that the System NET instance Put is NOT ready . SYS_NET_PUT_BUFFER_NOT_ENOUGH - Indicates that the System NET instance cannot transmit as the available buffer is less than the bytes to be transmitted . Positive Non-Zero - Indicates the number of bytes transmitted to the peer . Example . // Handle \\\"objSysNet\\\" value must have been returned from SYS_NET_Open. while(SYS_NET_SendMsg(objSysNet, \\\"hello\\\", 5) &lt;= 0); . Remarks . None. SYS_NET_RecvMsg . Function . int32_t SYS_NET_RecvMsg(SYS_MODULE_OBJ obj, void *data, uint16_t len) . Summary . Returns No of Bytes received from peer using the System NET instance. Description . This function returns the number of bytes received from the peer. Precondition . SYS_NET_Open should have been called. Parameters . obj - SYS NET object handle, returned from SYS_NET_Open data - valid data buffer pointer len - length of the data to be transmitted . Returns . SYS_NET_SERVICE_DOWN - Indicates that the System NET instance is not connected to the peer . SYS_NET_GET_NOT_READY - Indicates that the System NET instance No Data to GET . Positive Non-Zero - Indicates the number of bytes received from the peer, which may be less than the “len” of the buffer passed as the param. Example . // Handle \\\"objSysNet\\\" value must have been returned from SYS_NET_Open. int32_t len = 32; uint8_t buffer[32] = {0}; len = SYS_NET_RecvMsg(objSysNet, buffer, len); if(len &gt; 0) { } . Remarks . None. SYS_NET_CALLBACK . Function . void (*SYS_NET_CALLBACK) (uint32_t event, void *data, void* cookie) . Summary . Pointer to a Net system service callback function. Description . This data type defines a pointer to a Net service callback function, thus defining the function signature. Callback functions may be registered by clients of the net service when opening a Net socket via the Initialize call. Precondition . Is a part of the Net service initialization using the SYS_NET_Open function. Parameters . event - An event (SYS_NET_EVENT) for which the callback was called. data - Data (if any) related to the Event cookie - A context value, returned untouched to the client when the callback occurs. Returns . None. Example . void NetServCallback(uint32_t event, void *data, void* cookie, ) { switch(event) { case SYS_NET_EVNT_CONNECTED: { SYS_CONSOLE_PRINT(\\\"NetServCallback(): Status UP\\\"); while(SYS_NET_SendMsg(g_NetServHandle, \\\"hello\\\", 5) == 0); break; } case SYS_NET_EVNT_DISCONNECTED: { SYS_CONSOLE_PRINT(\\\"NetServCallback(): Status DOWN\\\"); break; } case SYS_NET_EVNT_RCVD_DATA: { int32_t len = 32; uint8_t buffer[32] = {0}; len = SYS_NET_RecvMsg(g_NetServHandle, buffer, len); SYS_CONSOLE_PRINT(\\\"NetServCallback(): Data Rcvd = %s\\\", buffer); break; } } } . Remarks . None. ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/net/docs/interface.html#data-exchange-functions",
    "relUrl": "/system/net/docs/interface.html#data-exchange-functions"
  },"29": {
    "doc": "Wi-Fi System Service Interface",
    "title": "Wi-Fi System Service Interface",
    "content": ". | Data Types and Constants Summary | Initialization functions Summary | Status functions Summary | Setup functions Summary | Data Types and Constants . | SYS_WIFI_AUTH | SYS_WIFI_CTRLMSG | SYS_WIFI_MODE | SYS_WIFI_STA_CONFIG | SYS_WIFI_AP_CONFIG | SYS_WIFI_CONFIG | SYS_WIFI_STATUS | SYS_WIFI_RESULT | SYS_WIFI_CALLBACK | . | Initialization functions . | SYS_WIFI_Initialize | SYS_WIFI_Deinitialize | . | Status functions . | SYS_WIFI_GetStatus | . | Setup functions . | SYS_WIFI_Tasks | SYS_WIFI_CtrlMsg | . | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/wifi/docs/interface.html",
    "relUrl": "/system/wifi/docs/interface.html"
  },"30": {
    "doc": "Wi-Fi System Service Interface",
    "title": "Data Types and Constants Summary",
    "content": "| Name | Description | . | SYS_WIFI_AUTH | Identifies the type of Authentication requested. | . | SYS_WIFI_CTRLMSG | Identifies the control message for which the client has called | . | SYS_WIFI_MODE | Identifies the Wi-Fi operating mode. | . | SYS_WIFI_STA_CONFIG | Configuration of station parameters. | . | SYS_WIFI_AP_CONFIG | Configuration of access point mode parameters. | . | SYS_WIFI_CONFIG | Configuration of device configuration parameters. | . | SYS_WIFI_STATUS | Result of a Wi-Fi service client interface get status | . | SYS_WIFI_RESULT | Result of a Wi-Fi system service client interface operation. | . | SYS_WIFI_CALLBACK | Pointer to a Wi-Fi system service callback function. | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/wifi/docs/interface.html#data-types-and-constants-summary",
    "relUrl": "/system/wifi/docs/interface.html#data-types-and-constants-summary"
  },"31": {
    "doc": "Wi-Fi System Service Interface",
    "title": "Initialization functions Summary",
    "content": "| Name | Description | . | SYS_WIFI_Initialize | Initializes the System Wi-Fi module. | . | SYS_WIFI_Deinitialize | Deinitializes the module instance of the system Wi-Fi service | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/wifi/docs/interface.html#initialization-functions-summary",
    "relUrl": "/system/wifi/docs/interface.html#initialization-functions-summary"
  },"32": {
    "doc": "Wi-Fi System Service Interface",
    "title": "Status functions Summary",
    "content": "| Name | Description | . | SYS_WIFI_GetStatus | Returns Wi-Fi system service status. | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/wifi/docs/interface.html#status-functions-summary",
    "relUrl": "/system/wifi/docs/interface.html#status-functions-summary"
  },"33": {
    "doc": "Wi-Fi System Service Interface",
    "title": "Setup functions Summary",
    "content": "| Name | Description | . | SYS_WIFI_Tasks | Maintains the Wi-Fi System tasks and functionalities. | . | SYS_WIFI_CtrlMsg | Returns success/ failure for the connect/disconnect/scan operation asked by client. | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/wifi/docs/interface.html#setup-functions-summary",
    "relUrl": "/system/wifi/docs/interface.html#setup-functions-summary"
  },"34": {
    "doc": "Wi-Fi System Service Interface",
    "title": "Data Types and Constants",
    "content": "SYS_WIFI_AUTH . Summary . Identifies the type of Authentication requested. Description . Identifies the type of Authentication requested. Remarks . None. typedef enum { /* Requesting a Open Authentication types */ SYS_WIFI_OPEN = 1, /* Requesting a WEP Authentication types */ SYS_WIFI_WEP, /* Requesting a WPA/WPA2(Mixed) Authentication types */ SYS_WIFI_WPAWPA2MIXED, /* Requesting a WPA2 Authentication types */ SYS_WIFI_WPA2, /* Requesting a WPA2/WPA3(Mixed) Authentication types */ SYS_WIFI_WPA2WPA3MIXED, /* Requesting a WPA3 Authentication types */ SYS_WIFI_WPA3 } SYS_WIFI_AUTH ; . SYS_WIFI_CTRLMSG . Summary . Identifies the control message for which the client has called the SYS_WIFI_CtrlMsg(). Description . Identifies the control message for which the client has called the SYS_WIFI_CtrlMsg(). Remarks . The different control messages which can be invoked by the client. typedef enum { /* Control message type for requesting a Wi-Fi Configuration set(for connect) */ SYS_WIFI_CONNECT = 0, /*Control message type for requesting a Wi-Fi device disconnect */ SYS_WIFI_DISCONNECT, /* Control message type for requesting a Wi-Fi configuration information */ SYS_WIFI_GETCONFIG, /* Control message type for updating a Provisioning Wi-Fi configuration information */ SYS_WIFI_PROVCONFIG, /* Control message type for registering a Wi-Fi system service client callback */ SYS_WIFI_REGCALLBACK, /* Control message type for requesting a Wi-Fi scan.In Scan request, client can set channel number and type of scan(active/passive). */ SYS_WIFI_SCANREQ } SYS_WIFI_CTRLMSG ; . SYS_WIFI_MODE . Summary . Identifies the Wi-Fi operating mode. Description . Identifies the Wi-Fi operating mode. Remarks . Client need to manually reboot device after switching mode. For example, changing operating mode to STA to AP or AP to STA. typedef enum { /* Requesting a operating mode a station */ SYS_WIFI_STA = 0, /* Requesting a operating mode a AP access point. */ SYS_WIFI_AP } SYS_WIFI_MODE ; . SYS_WIFI_STA_CONFIG . Summary . Configuration of station parameters. Description . Configuration of station parameters. Remarks . None. typedef struct { /* Wi-Fi station mode SSID */ uint8_t ssid[32]; /* Wi-Fi station mode passphrase */ uint8_t psk[64]; /* Wi-Fi station mode authentication type */ SYS_WIFI_AUTH authType; /* Wi-Fi station mode channel number. values of channel: 0 - scan and connect to all the channels 1 to 13 - - scan and connect to specified channel */ uint8_t channel; /* Wi-Fi station mode auto connect flag. value 0- Don't connect to AP, wait for client request. value 1- Connect to AP immediately */ bool autoConnect; } SYS_WIFI_STA_CONFIG; . SYS_WIFI_AP_CONFIG . Summary . Configuration of access point mode parameters. Description . Configuration of access point mode parameters. Remarks . None. typedef struct { /* Wi-Fi access point mode SSID */ uint8_t ssid[32]; /* Wi-Fi access point mode passphrase */ uint8_t psk[64]; /* Wi-Fi access point mode authentication type */ SYS_WIFI_AUTH authType; /* Wi-Fi access point mode channel number. values of channel: 1 to 13 - - operating channel of access point */ uint8_t channel; /* Wi-Fi access point mode SSID visibility value of ssidVisibility: 0 - Hidden SSID 1 - broadcast the SSID */ bool ssidVisibility; } SYS_WIFI_AP_CONFIG; . SYS_WIFI_CONFIG . Summary . Configuration of device configuration parameters. Description . Configuration of device configuration parameters. Remarks . None. typedef struct { /* Operating mode of the device */ SYS_WIFI_MODE mode; /* Flag to identify if configuration needs to be saved in NVM. 0 - Do not save configuration in NVM. 1 - Save configuration in NVM. */ uint8_t saveConfig; /* Country Code configuration */ uint8_t countryCode[5]; /* Wi-Fi station mode configuration structure */ SYS_WIFI_STA_CONFIG staConfig; /* Wi-Fi access point mode configuration structure */ SYS_WIFI_AP_CONFIG apConfig; }SYS_WIFI_CONFIG; . SYS_WIFI_STATUS . Summary . Result of a Wi-Fi service client interface get status operation(SYS_WIFI_GetStatus()). Description . Result of a Wi-Fi service client interface get status operation(SYS_WIFI_GetStatus()). Remarks . None. typedef enum { /* Wi-Fi system service is in init status */ SYS_WIFI_STATUS_INIT = 1, /* Wi-Fi system service is in driver open status */ SYS_WIFI_STATUS_WDRV_OPEN_REQ, /* Wi-Fi system service is in auto connect wait status */ SYS_WIFI_STATUS_AUTOCONNECT_WAIT, /* Wi-Fi system service is in wait for TCPIP stack init status */ SYS_WIFI_STATUS_TCPIP_WAIT_FOR_TCPIP_INIT, /* Wi-Fi system service is in Wi-Fi connect request status */ SYS_WIFI_STATUS_CONNECT_REQ, /* In AP mode,Wi-Fi system service is in wait for AP IP address */ SYS_WIFI_STATUS_WAIT_FOR_AP_IP, /* In AP mode,Wi-Fi system service is in wait for connecting STA IP address */ SYS_WIFI_STATUS_WAIT_FOR_STA_IP, /* Wi-Fi system service is in TCPIP ready status, waiting for client request.*/ SYS_WIFI_STATUS_TCPIP_READY, /* Wi-Fi system service is in TCPIP error status */ SYS_WIFI_STATUS_TCPIP_ERROR, /* Wi-Fi system service is in config error status */ SYS_WIFI_STATUS_CONFIG_ERROR, /* Wi-Fi system service is in connection error status */ SYS_WIFI_STATUS_CONNECT_ERROR, /* Wi-Fi system service is in not in valid status */ SYS_WIFI_STATUS_NONE =255 } SYS_WIFI_STATUS; . SYS_WIFI_RESULT . Summary . Result of a Wi-Fi system service client interface operation. Description . Identifies the result of Wi-Fi service operations . Remarks . None. typedef enum{ /* Operation completed with success */ SYS_WIFI_SUCCESS = 0, /* Operation Failed.*/ SYS_WIFI_FAILURE, /* Wi-Fi service un-initialize */ SYS_WIFI_SERVICE_UNINITIALIZE, /*Wi-Fi configuration request failed */ SYS_WIFI_CONFIG_FAILURE, //Wi-Fi Connect request failed SYS_WIFI_CONNECT_FAILURE, //Wi-Fi Save request failed SYS_WIFI_SAVE_FAILURE, //Operation request object is invalid SYS_WIFI_OBJ_INVALID=255 }SYS_WIFI_RESULT; . SYS_WIFI_CALLBACK . Function . typedef void (*SYS_WIFI_CALLBACK )(uint32_t event, void * data,void *cookie ) . Summary . Pointer to a Wi-Fi system service callback function. Description . This data type defines a pointer to a Wi-Fi service callback function. Callback functions can be registered by client at initialization or using control message type. Precondition . The Wi-Fi service must have been initialized using the SYS_WIFI_Initialize function if client registering callback using control message. Parameters . event - A event value, event can be any of SYS_WIFI_CTRLMSG types. data - Wi-Fi service Data. cookie - Client register cookie. Returns . None. Example . APP_DATA appData; void WiFiServCallback (uint32_t event, void * data,void *cookie ) { IPV4_ADDR *IPAddr; switch(event) { case SYS_WIFI_CONNECT: { IPAddr = (IPV4_ADDR *)data; SYS_CONSOLE_PRINT(\\\"IP address obtained = %d.%d.%d.%d \\\\r\\\\n\\\",IPAddr-&gt;v[0], IPAddr-&gt;v[1], IPAddr-&gt;v[2], IPAddr-&gt;v[3]); break; } case SYS_WIFI_DISCONNECT: { SYS_CONSOLE_PRINT(\\\"Device DISCONNECTED \\\\r\\\\n\\\"); break; } case SYS_WIFI_PROVCONFIG: { SYS_CONSOLE_PRINT(\\\"Received the Provisioning data \\\\r\\\\n\\\"); break; } } } void APP_Initialize(void) { appData.state = APP_STATE_INIT; } void APP_Tasks(void) { switch (appData.state) { case APP_STATE_INIT: { SYS_WIFI_CtrlMsg(sysObj.syswifi,SYS_WIFI_REGCALLBACK,WiFiServCallback,sizeof(uint8_t *)); appData.state=APP_STATE_SERVICE_TASKS; break; } case APP_STATE_SERVICE_TASKS: { break; } default: { break; } } } . Remarks . None. typedef void (*SYS_WIFI_CALLBACK )(uint32_t event, void * data,void *cookie ); . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/wifi/docs/interface.html#data-types-and-constants",
    "relUrl": "/system/wifi/docs/interface.html#data-types-and-constants"
  },"35": {
    "doc": "Wi-Fi System Service Interface",
    "title": "Initialization functions",
    "content": "SYS_WIFI_Initialize . Function . SYS_MODULE_OBJ SYS_WIFI_Initialize ( SYS_WIFI_CONFIG *config, SYS_WIFI_CALLBACK callback, void *cookie ) . Summary . Initializes the System Wi-Fi module. Description . Wi-Fi service supports only one single instance of Wi-Fi. Parameters . config - Wi-Fi device configuration structure. callback - The client callback function pointer. cookie - The pointer which will be passed to the customer application when the customer callback function is invoked. Returns . If successful, returns a valid handle to an object. Otherwise, it returns SYS_MODULE_OBJ_INVALID. Example . #define WIFI_DEV_SSID \\\"DEMO_AP\\\" #define WIFI_DEV_PSK \\\"password\\\" SYS_WIFI_CONFIG wifiSrvcConfig; // Set mode as STA wifiSrvcConfig.mode = SYS_WIFI_STA; // Disable saving wifi configuration wifiSrvcConfig.saveConfig = false; // Set the auth type to SYS_WIFI_WPA2 wifiSrvcConfig.staConfig.authType = SYS_WIFI_WPA2; // Enable all the channels(0) wifiSrvcConfig.staConfig.channel = 0; // Device doesn't wait for user request wifiSrvcConfig.staConfig.autoConnect = 1; // Set SSID memcpy(wifiSrvcConfig.staConfig.ssid,WIFI_DEV_SSID,sizeof(WIFI_DEV_SSID)); // Set PSK memcpy(wifiSrvcConfig.staConfig.psk,WIFI_DEV_PSK,sizeof(WIFI_DEV_PSK)); sysObj.syswifi = SYS_WIFI_Initialize(&amp;wifiSrvcConfig, WiFiServCallback, 0); if (sysObj.syswifi == SYS_MODULE_OBJ_INVALID) { // Handle error } . Remarks . This routine can only be called once during system initialization. If the Wi-Fi system service is enabled using MHC, then auto generated code will take care of system wi-fi initialization. SYS_WIFI_Deinitialize . Function . SYS_WIFI_RESULT SYS_WIFI_Deinitialize (SYS_MODULE_OBJ object) . Summary . Deinitializes the module instance of the system Wi-Fi service . Description . This function deinitializes the module instance disabling its operation. Resets all of the internal data structures and fields to the default settings. Precondition . The SYS_WIFI_Initialize function should have been called before calling this function. Parameters . object - SYS WIFI object handle, returned from SYS_WIFI_Initialize . Returns . return SYS_WIFI_RESULT . Example . if (SYS_WIFI_SUCCESS == SYS_WIFI_Deinitialize (sysObj.syswifi)) { // when the SYS WIFI is De-initialized. } . Remarks . Deinitialize should be called if the WiFi service is no longer going to be used. ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/wifi/docs/interface.html#initialization-functions",
    "relUrl": "/system/wifi/docs/interface.html#initialization-functions"
  },"36": {
    "doc": "Wi-Fi System Service Interface",
    "title": "Status functions",
    "content": "SYS_WIFI_GetStatus . Function . uint8_t SYS_WIFI_GetStatus ( SYS_MODULE_OBJ object) . Summary . Returns Wi-Fi system service status. Description . This function returns the current status of the System Wi-Fi service. This function help user to perform synchronize functionality with Wi-Fi service. Precondition . The SYS_WIFI_Initialize function should have been called before calling this function. Parameters . object - SYS WIFI object handle, returned from SYS_WIFI_Initialize . Returns . return SYS_WIFI_STATUS if client provided object is valid, else return SYS_WIFI_OBJ_INVALID. Example . // For example,User want to perform the Scan request when auto connect is disabled. // So user has to make sure service is in right state, // where Wi-Fi service has started and waiting in the Auto connect // state(SYS_WIFI_STATUS_AUTOCONNECT_WAIT) before making scan request. if (SYS_WIFI_STATUS_AUTOCONNECT_WAIT == SYS_WIFI_GetStatus (sysObj.syswifi)) { uint8_t buff[2]; // Scan all the channels buff[0] = 0 ; // Set the Scan type as passive (false- passive scan,true -active scan) buff[1] = false; SYS_WIFI_CtrlMsg(sysObj.syswifi,SYS_WIFI_SCANREQ,buff,2); } //Wi-Fi system service is in TCPIP ready status, waiting for client request. if (SYS_WIFI_STATUS_TCPIP_READY == SYS_WIFI_GetStatus (sysObj.syswifi)) { // when the SYS WIFI module in TCPIP ready STATUS } . Remarks . None . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/wifi/docs/interface.html#status-functions",
    "relUrl": "/system/wifi/docs/interface.html#status-functions"
  },"37": {
    "doc": "Wi-Fi System Service Interface",
    "title": "Setup functions",
    "content": "SYS_WIFI_Tasks . Function . uint8_t SYS_WIFI_Tasks ( SYS_MODULE_OBJ object) . Summary . Maintains the Wi-Fi System tasks and functionalities. Description . This function is used to run the various tasks and functionalities of Wi-Fi system service. Precondition . The SYS_WIFI_Initialize function should have been called before calling this function. Parameters . object - SYS WIFI object handle, returned from SYS_WIFI_Initialize . Returns . return SYS_WIFI_STATUS if client provided object is valid, else return SYS_WIFI_OBJ_INVALID. Example . if (SYS_WIFI_OBJ_INVALID != SYS_WIFI_Tasks (sysObj.syswifi)) { } . Remarks . If the Wi-Fi system service is enabled using MHC, then auto generated code will take care of system task execution. SYS_WIFI_CtrlMsg . Function . SYS_WIFI_RESULT SYS_WIFI_CtrlMsg ( SYS_MODULE_OBJ object, uint32_t event, void *buffer, uint32_t length ) . Summary . Returns success/ failure for the connect/disconnect/scan operation asked by client. Description . This function is used to make control message request (connect,disconnect,scan,register callback) to Wi-Fi system service. Precondition . The SYS_WIFI_Initialize function should have been called before calling this function. Parameters . object - SYS WIFI object handle, returned from SYS_WIFI_Initialize . event - A event value, event can be any of SYS_WIFI_CTRLMSG types . buffer - Control message data input. length - size of buffer data . Returns . return SYS_WIFI_RESULT. Example . Details of SYS_WIFI_CONNECT: SYS_WIFI_CONFIG wifiSrvcConfig; SYS_MODULE_OBJ WiFiServHandle; // Set mode as STA wifiSrvcConfig.mode = SYS_WIFI_STA; // Disable saving wifi configuration wifiSrvcConfig.saveConfig = false; // Set the auth type to SYS_WIFI_WPA2 wifiSrvcConfig.staConfig.authType = SYS_WIFI_WPA2; // Enable all the channels(0) wifiSrvcConfig.staConfig.channel = 0; // Device doesn't wait for user request wifiSrvcConfig.staConfig.autoConnect = 1; // Set SSID memcpy(wifiSrvcConfig.staConfig.ssid, WIFI_DEV_SSID, sizeof(WIFI_DEV_SSID)); // Set PSK memcpy(wifiSrvcConfig.staConfig.psk, WIFI_DEV_PSK, sizeof(WIFI_DEV_PSK)); // sysObj.syswifi return from SYS_WIFI_Initialize() if (SYS_WIFI_OBJ_INVALID != SYS_WIFI_CtrlMsg (sysObj.syswifi, SYS_WIFI_CONNECT, wifiSrvcConfig, sizeof(SYS_WIFI_CONFIG))) { } Details of SYS_WIFI_SCANREQ: // In Scan request, user can set channel number and type of scan. uint8_t buff[2]; // Scan all the channels buff[0] = 0 ; // Set the Scan type as passive: // false- passive scan, // true -active scan) buff[1] = false; SYS_WIFI_CtrlMsg(sysObj.syswifi, SYS_WIFI_SCANREQ, buff, 2); Details of SYS_WIFI_REGCALLBACK: // Client can register multiple callback.Number of supported // callback registration is a MHC configuration. SYS_WIFI_CtrlMsg(sysObj.syswifi, SYS_WIFI_REGCALLBACK, WiFiServCallback, sizeof(uint8_t *)); Details of SYS_WIFI_GETCONFIG: // Get Wi-Fi Configuration using control message request. // The information of configuration is updated in the wifiSrvcConfig. SYS_WIFI_CONFIG wifiSrvcConfig; if(SYS_WIFI_SUCCESS == SYS_WIFI_CtrlMsg(sysObj.syswifi, SYS_WIFI_GETCONFIG, &amp;wifiSrvcConfig, sizeof(SYS_WIFI_CONFIG))) { //Received the wifiSrvcConfig data } Details of SYS_WIFI_DISCONNECT: // Device Disconnect request using control message request. SYS_WIFI_CtrlMsg(sysObj.syswifi, SYS_WIFI_DISCONNECT, NULL, 0); . Remarks . None . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/wifi/docs/interface.html#setup-functions",
    "relUrl": "/system/wifi/docs/interface.html#setup-functions"
  },"38": {
    "doc": "App Debug System Service Interface",
    "title": "App Debug System Service Interface",
    "content": ". | Data Types and Constants Summary | Initialization functions Summary | Setup functions Summary | Data Types and Constants . | APP_LOG_LVL_DISABLE | APP_LOG_ERROR_LVL | APP_LOG_DBG_LVL | APP_LOG_INFO_LVL | APP_LOG_FN_EE_LVL | SYS_APPDEBUG_MAX_NUM_OF_USERS | SYS_APPDEBUG_CONFIG | SYS_APPDEBUG_CtrlMsgType | SYS_APPDEBUG_RESULT | . | Initialization functions . | SYS_APPDEBUG_Initialize | SYS_APPDEBUG_Deinitialize | . | Setup functions . | SYS_APPDEBUG_Open | SYS_APPDEBUG_Close | SYS_APPDEBUG_CtrlMsg | SYS_APPDEBUG_ERR_PRINT | SYS_APPDEBUG_DBG_PRINT | SYS_APPDEBUG_INFO_PRINT | SYS_APPDEBUG_FN_ENTER_PRINT | SYS_APPDEBUG_FN_EXIT_PRINT | . | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/appdebug/docs/interface.html",
    "relUrl": "/system/appdebug/docs/interface.html"
  },"39": {
    "doc": "App Debug System Service Interface",
    "title": "Data Types and Constants Summary",
    "content": "| Name | Description | . | APP_LOG_LVL_DISABLE | App Debug Service Logging Disabled | . | APP_LOG_ERROR_LVL | App Debug Service Error Log Level | . | APP_LOG_DBG_LVL | App Debug Service Debug Log Level | . | APP_LOG_INFO_LVL | App Debug Service Info Log Level | . | APP_LOG_FN_EE_LVL | App Debug Service Service Entry/ Exit Log Level | . | SYS_APPDEBUG_MAX_NUM_OF_USERS | Number of instances of App Debug Service supported | . | SYS_APPDEBUG_CONFIG | Defines the data required to initialize the app debug system service. | . | SYS_APPDEBUG_CtrlMsgType | Identifies the control message for which the User has called the SYS_APPDEBUG_CtrlMsg(). | . | SYS_APPDEBUG_RESULT | Identifies the return values for the Sys App Debug APIs. | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/appdebug/docs/interface.html#data-types-and-constants-summary",
    "relUrl": "/system/appdebug/docs/interface.html#data-types-and-constants-summary"
  },"40": {
    "doc": "App Debug System Service Interface",
    "title": "Initialization functions Summary",
    "content": "| Name | Description | . | SYS_APPDEBUG_Initialize | Returns success/ failure for initialization of data structures of the | . | SYS_APPDEBUG_Deinitialize | Returns success/ failure for deinitialization of data structures of the | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/appdebug/docs/interface.html#initialization-functions-summary",
    "relUrl": "/system/appdebug/docs/interface.html#initialization-functions-summary"
  },"41": {
    "doc": "App Debug System Service Interface",
    "title": "Setup functions Summary",
    "content": "| Name | Description | . | SYS_APPDEBUG_Open | Open an instance of the System App Debug service. | . | SYS_APPDEBUG_Close | Close the specific module instance of the SYS App Debug service | . | SYS_APPDEBUG_CtrlMsg | Returns success/ failure for the flow/ level set operation asked by the user. | . | SYS_APPDEBUG_ERR_PRINT | Used for logging Error Level Logs | . | SYS_APPDEBUG_DBG_PRINT | Used for logging Debug Level Logs | . | SYS_APPDEBUG_INFO_PRINT | Used for logging Info Level Logs | . | SYS_APPDEBUG_FN_ENTER_PRINT | Used for logging Function Entry Logs | . | SYS_APPDEBUG_FN_EXIT_PRINT | Used for logging Function Exit Logs | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/appdebug/docs/interface.html#setup-functions-summary",
    "relUrl": "/system/appdebug/docs/interface.html#setup-functions-summary"
  },"42": {
    "doc": "App Debug System Service Interface",
    "title": "Data Types and Constants",
    "content": "APP_LOG_LVL_DISABLE . Summary . App Debug Service Logging Disabled . Remarks . None. #define APP_LOG_LVL_DISABLE 0x0 . APP_LOG_ERROR_LVL . Summary . App Debug Service Error Log Level . Remarks . None. #define APP_LOG_ERROR_LVL 0x1 . APP_LOG_DBG_LVL . Summary . App Debug Service Debug Log Level . Remarks . None. #define APP_LOG_DBG_LVL 0x2 . APP_LOG_INFO_LVL . Summary . App Debug Service Info Log Level . Remarks . None. #define APP_LOG_INFO_LVL 0x4 . APP_LOG_FN_EE_LVL . Summary . App Debug Service Service Entry/ Exit Log Level . Remarks . None. #define APP_LOG_FN_EE_LVL 0x8 . SYS_APPDEBUG_MAX_NUM_OF_USERS . Summary . Number of instances of App Debug Service supported . Remarks . None. #define SYS_APPDEBUG_MAX_NUM_OF_USERS 8 . SYS_APPDEBUG_CONFIG . Summary . Defines the data required to initialize the app debug system service. Description . This structure defines the data required to initialize the app debug system service. Remarks . None. typedef struct { /* Initial system Log level setting. */ unsigned int logLevel; /* Initial system Log level setting. */ unsigned int logFlow; /* Initial system Log level setting. */ const char *prefixString; } SYS_APPDEBUG_CONFIG; . SYS_APPDEBUG_CtrlMsgType . Summary . Identifies the control message for which the User has called the SYS_APPDEBUG_CtrlMsg(). Remarks . None. typedef enum { SYS_APPDEBUG_CTRL_MSG_TYPE_SET_LEVEL, SYS_APPDEBUG_CTRL_MSG_TYPE_SET_FLOW, } SYS_APPDEBUG_CtrlMsgType; . SYS_APPDEBUG_RESULT . Summary . Identifies the return values for the Sys App Debug APIs. Remarks . None. typedef enum { SYS_APPDEBUG_SUCCESS = 0, // Success SYS_APPDEBUG_FAILURE = -1, // Failure } SYS_APPDEBUG_RESULT; . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/appdebug/docs/interface.html#data-types-and-constants",
    "relUrl": "/system/appdebug/docs/interface.html#data-types-and-constants"
  },"43": {
    "doc": "App Debug System Service Interface",
    "title": "Initialization functions",
    "content": "SYS_APPDEBUG_Initialize . Function . int32_t SYS_APPDEBUG_Initialize() . Summary . Returns success/ failure for initialization of data structures of the App Debug service . Description . This function is used for initializing the data structures of the App Debug service and is called from within the System Task. Parameters . index - NULL; reserved for future use init - NULL; reserved for future use . Returns . SYS_APPDEBUG_SUCCESS - Indicates the data structures were initialized successfully . SYS_APPDEBUG_FAILURE - Indicates that it failed to initialize the data structures . Example . if( SYS_APPDEBUG_Initialize(NULL, NULL) == SYS_APPDEBUG_SUCCESS) { } . Remarks . If the Net system service is enabled using MHC, then auto generated code will take care of system task execution. SYS_APPDEBUG_Deinitialize . Function . int32_t SYS_APPDEBUG_Deinitialize() . Summary . Returns success/ failure for deinitialization of data structures of the App Debug service . Description . This function is used for deinitializing the data structures of the App Debug service and is called from within the System Task. Parameters . None . Returns . SYS_APPDEBUG_SUCCESS - Indicates the data structures were deinitialized successfully . SYS_APPDEBUG_FAILURE - Indicates that it failed to deinitialize the data structures. Example . if( SYS_APPDEBUG_Deinitialize() == SYS_APPDEBUG_SUCCESS) { } . Remarks . If the Net system service is enabled using MHC, then auto generated code will take care of system task execution. ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/appdebug/docs/interface.html#initialization-functions",
    "relUrl": "/system/appdebug/docs/interface.html#initialization-functions"
  },"44": {
    "doc": "App Debug System Service Interface",
    "title": "Setup functions",
    "content": "SYS_APPDEBUG_Open . Function . SYS_MODULE_OBJ SYS_APPDEBUG_Open (SYS_APPDEBUG_CONFIG *cfg) . Summary . Open an instance of the System App Debug service. Description . This function initializes the instance of the System App Debug Service. Parameters . cfg - Configuration with which the App Debug Service needs to be opened Returns . Returns:If successful, returns a valid handle to an object. Otherwise, it returns SYS_MODULE_OBJ_INVALID. Example . SYS_APPDEBUG_CONFIG g_AppDebugServCfg; SYS_MODULE_OBJ g_AppDebugServHandle; memset(&amp;g_AppDebugServCfg, 0, sizeof(g_AppDebugServCfg)); g_AppDebugServCfg.logLevel |= APP_LOG_ERROR_LVL; g_AppDebugServCfg.prefixString = \\\"MY_APP\\\"; g_AppDebugServCfg.logFlow |= 0x1; g_AppDebugServHandle = SYS_NET_Open(&amp;g_AppDebugServCfg); if (g_AppDebugServHandle == SYS_MODULE_OBJ_INVALID) { // Handle error } . Remarks . This routine should be called everytime a user wants to open a new NET socket . SYS_APPDEBUG_Close . Function . void SYS_APPDEBUG_Close ( SYS_MODULE_OBJ object ) . Summary . Close the specific module instance of the SYS App Debug service . Description . This function clsoes the specific module instance disabling its operation. Resets all of the internal data structures and fields for the specified instance to the default settings. Precondition . The SYS_APPDEBUG_Open function should have been called before calling this function. Parameters . object - SYS App Debug object handle, returned from SYS_APPDEBUG_Open . Returns . None. Example . // Handle \\\"objSysAppDebug\\\" value must have been returned from SYS_APPDEBUG_Open. SYS_APPDEBUG_Close (objSysAppDebug); . Remarks . Once the Open operation has been called, the Close operation must be called before the Open operation can be called again. SYS_APPDEBUG_CtrlMsg . Function . int32_t SYS_APPDEBUG_CtrlMsg(SYS_MODULE_OBJ obj, SYS_APPDEBUG_CtrlMsgType eCtrlMsgType, void *data, uint16_t len) . Summary . Returns success/ failure for the flow/ level set operation asked by the user. Description . This function is used for setting the value of floe/ level for the app debug logs. Precondition . SYS_APPDEBUG_Open should have been called. Parameters . obj - SYS App Debug object handle, returned from SYS_APPDEBUG_Open eCtrlMsgType - valid Msg Type data - valid data buffer pointer based on the Msg Type len - length of the data buffer the pointer is pointing to . Returns . SYS_APPDEBUG_SUCCESS - Indicates that the Request was catered to successfully . SYS_APPDEBUG_FAILURE - Indicates that the Request failed . Example . // Handle \\\"objSysAppDebug\\\" value must have been returned from SYS_APPDEBUG_Open. uint32_t logLevel = 0x3; if( SYS_APPDEBUG_CtrlMsg(objSysAppDebug, SYS_APPDEBUG_CTRL_MSG_TYPE_SET_LEVEL, &amp;logLevel, 4) == SYS_APPDEBUG_SUCCESS) { } . Remarks . None. uint32_t linenum, char *msg, ...); void SYS_APPDEBUG_PRINT_FN_ENTER(SYS_MODULE_OBJ obj, uint32_t flow, const char *function, uint32_t linenum); void SYS_APPDEBUG_PRINT_FN_EXIT(SYS_MODULE_OBJ obj, uint32_t flow, const char *function, uint32_t linenum); . SYS_APPDEBUG_ERR_PRINT . Summary . Used for logging Error Level Logs . Description . This macro function is used for logging error level logs. Precondition . SYS_APPDEBUG_Open should have been called. Parameters . obj - SYS App Debug object handle, returned from SYS_APPDEBUG_Open flow - valid flow defined by the User, log will come only if this flow is enabled data - valid string … - any variable arguments if present . Returns . None. Example . // Handle \\\"objSysAppDebug\\\" value must have been returned from SYS_APPDEBUG_Open. SYS_APPDEBUG_ERR_PRINT(objSysAppDebug, MY_APP_FLOW_DATA, \\\"Failed to allocate memory of size %d\\\", size); . Remarks . None. #define SYS_APPDEBUG_ERR_PRINT(obj, flow, fmt, …) SYS_APPDEBUG_PRINT(obj, flow, APP_LOG_ERROR_LVL, FUNCTION, LINE, fmt, ##VA_ARGS) . SYS_APPDEBUG_DBG_PRINT . Summary . Used for logging Debug Level Logs . Description . This macro function is used for logging debug level logs. Precondition . SYS_APPDEBUG_Open should have been called. Parameters . obj - SYS App Debug object handle, returned from SYS_APPDEBUG_Open flow - valid flow defined by the User, log will come only if this flow is enabled data - valid string … - any variable arguments if present . Returns . None. Example . // Handle \\\"objSysAppDebug\\\" value must have been returned from SYS_APPDEBUG_Open. SYS_APPDEBUG_DBG_PRINT(objSysAppDebug, MY_APP_FLOW_DATA, \\\"memory allocation reached Threshold\\\"); . Remarks . None. #define SYS_APPDEBUG_DBG_PRINT(obj, flow, fmt, …) SYS_APPDEBUG_PRINT(obj, flow, APP_LOG_DBG_LVL, FUNCTION, LINE, fmt, ##VA_ARGS) . SYS_APPDEBUG_INFO_PRINT . Summary . Used for logging Info Level Logs . Description . This macro function is used for logging info level logs. Precondition . SYS_APPDEBUG_Open should have been called. Parameters . obj - SYS App Debug object handle, returned from SYS_APPDEBUG_Open flow - valid flow defined by the User, log will come only if this flow is enabled data - valid string … - any variable arguments if present . Returns . None. Example . // Handle \\\"objSysAppDebug\\\" value must have been returned from SYS_APPDEBUG_Open. SYS_APPDEBUG_INFO_PRINT(objSysAppDebug, MY_APP_FLOW_DATA, \\\"Allocate memory of size %d\\\", size); . Remarks . None. #define SYS_APPDEBUG_INFO_PRINT(obj, flow, fmt, …) SYS_APPDEBUG_PRINT(obj, flow, APP_LOG_INFO_LVL, FUNCTION, LINE, fmt, ##VA_ARGS) . SYS_APPDEBUG_FN_ENTER_PRINT . Summary . Used for logging Function Entry Logs . Description . This macro function is used for logging function entry level logs. Precondition . SYS_APPDEBUG_Open should have been called. Parameters . obj - SYS App Debug object handle, returned from SYS_APPDEBUG_Open flow - valid flow defined by the User, log will come only if this flow is enabled data - valid string … - any variable arguments if present . Returns . None. Example . // Handle \\\"objSysAppDebug\\\" value must have been returned from SYS_APPDEBUG_Open. SYS_APPDEBUG_FN_ENTER_PRINT(objSysAppDebug, MY_APP_FLOW_DATA); . Remarks . None. #define SYS_APPDEBUG_FN_ENTER_PRINT(obj, flow) SYS_APPDEBUG_PRINT_FN_ENTER(obj, flow, FUNCTION, LINE) . SYS_APPDEBUG_FN_EXIT_PRINT . Summary . Used for logging Function Exit Logs . Description . This macro function is used for logging function exit level logs. Precondition . SYS_APPDEBUG_Open should have been called. Parameters . obj - SYS App Debug object handle, returned from SYS_APPDEBUG_Open flow - valid flow defined by the User, log will come only if this flow is enabled data - valid string … - any variable arguments if present . Returns . None. Example . // Handle \\\"objSysAppDebug\\\" value must have been returned from SYS_APPDEBUG_Open. SYS_APPDEBUG_FN_EXIT_PRINT(objSysAppDebug, MY_APP_FLOW_DATA); . Remarks . None. #define SYS_APPDEBUG_FN_EXIT_PRINT(obj, flow) SYS_APPDEBUG_PRINT_FN_EXIT(obj, flow, FUNCTION, LINE) . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/appdebug/docs/interface.html#setup-functions",
    "relUrl": "/system/appdebug/docs/interface.html#setup-functions"
  },"45": {
    "doc": "MQTT System Service Interface",
    "title": "MQTT System Service Interface",
    "content": ". | Data Types and Constants Summary | Initialization functions Summary | Status functions Summary | Setup functions Summary | Data Exchange functions Summary | Data Types and Constants . | SYS_MQTT_INTF_WIFI | SYS_MQTT_INTF_ETHERNET | SYS_MQTT_STATUS | SYS_MQTT_RESULT | SYS_MQTT_BrokerConfig | SYS_MQTT_SubscribeConfig | SYS_MQTT_PublishConfig | SYS_MQTT_PublishTopicCfg | SYS_MQTT_EVENT_TYPE | SYS_MQTT_Config | . | Initialization functions . | SYS_MQTT_Initialize | SYS_MQTT_Deinitialize | . | Status functions . | SYS_MQTT_GetStatus | . | Setup functions . | SYS_MQTT_Connect | SYS_MQTT_Disconnect | SYS_MQTT_Task | SYS_MQTT_Subscribe | SYS_MQTT_Unsubscribe | . | Data Exchange functions . | SYS_MQTT_Publish | SYS_MQTT_CALLBACK | . | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/mqtt/docs/interface.html",
    "relUrl": "/system/mqtt/docs/interface.html"
  },"46": {
    "doc": "MQTT System Service Interface",
    "title": "Data Types and Constants Summary",
    "content": "| Name | Description | . | SYS_MQTT_INTF_WIFI | Mqtt Socket Intf - Wifi | . | SYS_MQTT_INTF_ETHERNET | Mqtt Socket Intf - Ethernet | . | SYS_MQTT_STATUS | Identifies the current status of the Sys Mqtt Instance. | . | SYS_MQTT_RESULT | Identifies the return values for the Sys Mqtt APIs. | . | SYS_MQTT_BrokerConfig | Used for passing on the configuration related to the MQTT Broker | . | SYS_MQTT_SubscribeConfig | Used for passing on the configuration related to the MQTT Subtopics the user | . | SYS_MQTT_PublishConfig | Used for Reading the message that has been received on a topic subscribed to. | . | SYS_MQTT_PublishTopicCfg | Used for publishing a message on a topic. It contains the config related to the Topic | . | SYS_MQTT_EVENT_TYPE | Event Message Type which comes with the Callback SYS_MQTT_CALLBACK() | . | SYS_MQTT_Config | Used for passing on the configuration related to the either MQTT Broker, | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/mqtt/docs/interface.html#data-types-and-constants-summary",
    "relUrl": "/system/mqtt/docs/interface.html#data-types-and-constants-summary"
  },"47": {
    "doc": "MQTT System Service Interface",
    "title": "Initialization functions Summary",
    "content": "| Name | Description | . | SYS_MQTT_Initialize | Returns success/ failure for initialization of data structures of the MQTT service | . | SYS_MQTT_Deinitialize | Deinitialization of data structures of the MQTT service | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/mqtt/docs/interface.html#initialization-functions-summary",
    "relUrl": "/system/mqtt/docs/interface.html#initialization-functions-summary"
  },"48": {
    "doc": "MQTT System Service Interface",
    "title": "Status functions Summary",
    "content": "| Name | Description | . | SYS_MQTT_GetStatus | Returns System MQTT instance status. | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/mqtt/docs/interface.html#status-functions-summary",
    "relUrl": "/system/mqtt/docs/interface.html#status-functions-summary"
  },"49": {
    "doc": "MQTT System Service Interface",
    "title": "Setup functions Summary",
    "content": "| Name | Description | . | SYS_MQTT_Connect | Connects to the configured MQTT Broker. | . | SYS_MQTT_Disconnect | Disconnects from the MQTT Server | . | SYS_MQTT_Task | Executes the MQTT Service State Machine | . | SYS_MQTT_Subscribe | Returns success/ failure for the subscribing to a Topic by the user. | . | SYS_MQTT_Unsubscribe | Returns success/ failure for the unsubscribing to a Topic by the user. | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/mqtt/docs/interface.html#setup-functions-summary",
    "relUrl": "/system/mqtt/docs/interface.html#setup-functions-summary"
  },"50": {
    "doc": "MQTT System Service Interface",
    "title": "Data Exchange functions Summary",
    "content": "| Name | Description | . | SYS_MQTT_Publish | Returns success/ failure for the publishing of message asked by the user. | . | SYS_MQTT_CALLBACK | Pointer to a MQTT system service callback function. | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/mqtt/docs/interface.html#data-exchange-functions-summary",
    "relUrl": "/system/mqtt/docs/interface.html#data-exchange-functions-summary"
  },"51": {
    "doc": "MQTT System Service Interface",
    "title": "Data Types and Constants",
    "content": "SYS_MQTT_INTF_WIFI . Summary . Mqtt Socket Intf - Wifi . Remarks . None. #define SYS_MQTT_INTF_WIFI SYS_NET_INTF_WIFI // Wifi Intf Value . SYS_MQTT_INTF_ETHERNET . Summary . Mqtt Socket Intf - Ethernet . Remarks . None. #define SYS_MQTT_INTF_ETHERNET SYS_NET_INTF_ETHERNET // Ethernet Intf Value . SYS_MQTT_STATUS . Summary . Identifies the current status of the Sys Mqtt Instance. Remarks . None. typedef enum { // Idle SYS_MQTT_STATUS_IDLE = 0, // Lower Layer is DOWN SYS_MQTT_STATUS_LOWER_LAYER_DOWN, // Net Client connecting to Net Server SYS_MQTT_STATUS_SOCK_CLIENT_CONNECTING, // Net Instance connected to the peer SYS_MQTT_STATUS_SOCK_CONNECTED, // Net Instance Failed to open socket SYS_MQTT_STATUS_SOCK_OPEN_FAILED, // Lower Layer is DOWN SYS_MQTT_STATUS_MQTT_CONNECTED, // Net Instance in disconnected state SYS_MQTT_STATUS_MQTT_DISCONNECTING, // Net Instance in disconnected state SYS_MQTT_STATUS_MQTT_DISCONNECTED, // Lower Layer is DOWN SYS_MQTT_STATUS_MQTT_CONN_FAILED, // Wait for Connect Ack from Broker SYS_MQTT_STATUS_WAIT_FOR_MQTT_CONACK, // Send Mqtt Connect to Broker SYS_MQTT_STATUS_SEND_MQTT_CONN, // Wait for Subscribe Ack from Broker SYS_MQTT_STATUS_WAIT_FOR_MQTT_SUBACK, // Wait for Publish Ack from Broker SYS_MQTT_STATUS_WAIT_FOR_MQTT_PUBACK, // Wait for Unsibscribe Ack from Broker SYS_MQTT_STATUS_WAIT_FOR_MQTT_UNSUBACK, } SYS_MQTT_STATUS; . SYS_MQTT_RESULT . Summary . Identifies the return values for the Sys Mqtt APIs. Remarks . None. typedef enum { // Success SYS_MQTT_SUCCESS = 0, // Failure SYS_MQTT_FAILURE = -1, // Sys NET Service Down SYS_MQTT_SERVICE_DOWN = -2, // Sys NET Available Put Buffer not enough for xmitting the Data SYS_MQTT_SEM_OPERATION_FAILURE = -5, // Sys NET Invalid Handle SYS_MQTT_INVALID_HANDLE = -6, } SYS_MQTT_RESULT; . SYS_MQTT_BrokerConfig . Summary . Used for passing on the configuration related to the MQTT Broker . Remarks . None. typedef struct { //to know which of the Configurations are valid SYS_MQTT_Vendor_Type eVendorType; // MQTT Broker/ Server Name char brokerName[SYS_MQTT_MAX_BROKER_NAME_LEN]; // MQTT Server Port uint16_t serverPort; // Keep Alive Interval for the Mqtt Session uint16_t keepAliveInterval; // MQTT Client ID char clientId[SYS_MQTT_CLIENT_ID_MAX_LEN]; // MQTT Username char username[SYS_MQTT_USER_NAME_MAX_LEN]; // MQTT password char password[SYS_MQTT_PASSWORD_MAX_LEN]; // TLS is Enabled bool tlsEnabled; // AutoConnect is Enabled bool autoConnect; } SYS_MQTT_BrokerConfig; . SYS_MQTT_SubscribeConfig . Summary . Used for passing on the configuration related to the MQTT Subtopics the user wants to subscribe to. Remarks . This Configuration is passed via the SYS_MQTT_Connect() function or the SYS_MQTT_CtrlMsg() function . typedef struct { uint8_t entryValid; //Qos (0/ 1/ 2) uint8_t qos; //Name of the Topic Subscribing to char topicName[SYS_MQTT_TOPIC_NAME_MAX_LEN]; } SYS_MQTT_SubscribeConfig; . SYS_MQTT_PublishConfig . Summary . Used for Reading the message that has been received on a topic subscribed to. The structure is also used for passing on the LWT config when connecting to MQTT Broker. Remarks . This Message is passed to the Application via the SYS_MQTT_CALLBACK() function . typedef struct { //Qos (0/ 1/ 2) uint8_t qos; //Retain (0/1) - Message needs to be retained by the Broker till every subscriber receives it uint8_t retain; //Message to be Published uint8_t message[SYS_MQTT_MSG_MAX_LEN]; //Message Length uint16_t messageLength; //Topic on which to Publish the message char *topicName; //Topic Length uint16_t topicLength; } SYS_MQTT_PublishConfig; . SYS_MQTT_PublishTopicCfg . Summary . Used for publishing a message on a topic. It contains the config related to the Topic . Remarks . This Message is passed from the Application to the MQTT servuce via the SYS_MQTT_Publish() function . typedef struct { //Qos (0/ 1/ 2) uint8_t qos; //Retain (0/1) - Message needs to be retained by the Broker till every subscriber receives it uint8_t retain; //Topic on which to Publish the message char topicName[SYS_MQTT_TOPIC_NAME_MAX_LEN]; //Topic Length uint16_t topicLength; } SYS_MQTT_PublishTopicCfg; . SYS_MQTT_EVENT_TYPE . Summary . Event Message Type which comes with the Callback SYS_MQTT_CALLBACK() informing the user of the event that has occured. Remarks . None. typedef enum { //Message received on a topic subscribed to SYS_MQTT_EVENT_MSG_RCVD = 0, //MQTT Client for Disconnected SYS_MQTT_EVENT_MSG_DISCONNECTED, //MQTT Client Connected SYS_MQTT_EVENT_MSG_CONNECTED, //MQTT Client Subscribed to a Grp SYS_MQTT_EVENT_MSG_SUBSCRIBED, //MQTT Client UnSubscribed from a Grp SYS_MQTT_EVENT_MSG_UNSUBSCRIBED, //MQTT Client Published to a Grp SYS_MQTT_EVENT_MSG_PUBLISHED, //MQTT Client ConnAck TimeOut SYS_MQTT_EVENT_MSG_CONNACK_TO, //MQTT Client SubAck TimeOut SYS_MQTT_EVENT_MSG_SUBACK_TO, //MQTT Client PubAck TimeOut SYS_MQTT_EVENT_MSG_PUBACK_TO, //MQTT Client PubAck TimeOut SYS_MQTT_EVENT_MSG_UNSUBACK_TO, } SYS_MQTT_EVENT_TYPE; . SYS_MQTT_Config . Summary . Used for passing on the configuration related to the either MQTT Broker, or the Cloud Vendors AWS/ Azure, etc. Remarks . None. typedef struct { //MQTT Broker Configuration SYS_MQTT_BrokerConfig sBrokerConfig; //Number of Topis Subscribed to (0-SYS_MQTT_MAX_TOPICS) uint8_t subscribeCount; //Config for all the Topics Subscribed to SYS_MQTT_SubscribeConfig sSubscribeConfig[SYS_MQTT_SUB_MAX_TOPICS]; //If last will and testament(LWT) is enabled or not bool bLwtEnabled; // LWT Configuration SYS_MQTT_PublishConfig sLwtConfig; //Network Interface - Wifi or Ethernet uint8_t intf; } SYS_MQTT_Config; . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/mqtt/docs/interface.html#data-types-and-constants",
    "relUrl": "/system/mqtt/docs/interface.html#data-types-and-constants"
  },"52": {
    "doc": "MQTT System Service Interface",
    "title": "Initialization functions",
    "content": "SYS_MQTT_Initialize . Function . int32_t SYS_MQTT_Initialize() . Summary . Returns success/ failure for initialization of data structures of the MQTT service . Description . This function is used for initializing the data structures of the MQTT service and is called from within the System Task. Returns . SYS_NET_SUCCESS - Indicates the data structures were initialized successfully . SYS_NET_FAILURE - Indicates that it failed to initialize the data structures. Example . if( SYS_MQTT_Initialize() == SYS_MQTT_SUCCESS) { } . Remarks . If the MQTT system service is enabled using MHC, then auto generated code will take care of its initialization. SYS_MQTT_Deinitialize . Function . void SYS_MQTT_Deinitialize() . Summary . Deinitialization of data structures of the MQTT service . Description . This function is used for freeing the allocated data structures for the MQTT service. Example . SYS_MQTT_Deinitialize() . Remarks . None . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/mqtt/docs/interface.html#initialization-functions",
    "relUrl": "/system/mqtt/docs/interface.html#initialization-functions"
  },"53": {
    "doc": "MQTT System Service Interface",
    "title": "Status functions",
    "content": "SYS_MQTT_GetStatus . Function . SYS_MQTT_STATUS SYS_MQTT_GetStatus ( SYS_MODULE_OBJ object ) . Summary . Returns System MQTT instance status. Description . This function returns the current status of the System MQTT instance. Precondition . SYS_MQTT_Connect should have been called before calling this function . Parameters . object - SYS MQTT object handle, returned from SYS_MQTT_Connect . Returns . SYS_MQTT_STATUS . Example . // Handle \\\"objSysMqtt\\\" value must have been returned from SYS_MQTT_Connect. if (SYS_MQTT_GetStatus (objSysMqtt) == SYS_MQTT_STATUS_WAIT_FOR_MQTT_CONACK) { // MQTT system service is initialized, and Waiting for the Connect Ack // from the Broker for the Connect Packet sent by DUT to it. } . Remarks . None. ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/mqtt/docs/interface.html#status-functions",
    "relUrl": "/system/mqtt/docs/interface.html#status-functions"
  },"54": {
    "doc": "MQTT System Service Interface",
    "title": "Setup functions",
    "content": "SYS_MQTT_Connect . Function . SYS_MODULE_OBJSYS_MODULE_OBJ* SYS_MQTT_Connect(SYS_MQTT_Config *cfg, SYS_MQTT_CALLBACK fn MqttFn, void *cookie); . Summary . Connects to the configured MQTT Broker. Description . This function opens a new instance and connects to the configured MQTT Broker. Parameters . cfg - Configuration based on which the Cloud Service needs to Open MqttFn - Function pointer to the Callback to be called in case of an event cookie - Cookie passed as one of the params in the Callback for the user to identify the service instance . Returns . If successful, returns a valid handle to an object. Otherwise, it returns SYS_MODULE_OBJ_INVALID. Example . SYS_MQTT_Config g_sMqttSrvcCfg; SYS_MODULE_OBJ g_MqttSrvcHandle; memset(&amp;g_sMqttSrvcCfg, 0, sizeof(g_sMqttSrvcCfg)); g_sMattSrvcCfg.configBitmask |= SYS_MQTT_CONFIG_MASK_MQTT; strcpy(g_sMqttSrvcCfg.mqttConfig.brokerConfig.brokerName, \\\"test.mosquitto.org\\\", strlen(\\\"test.mosquitto.org\\\")); g_sMqttSrvcCfg.mqttConfig.brokerConfig.serverPort = 1883; strcpy(g_sMqttSrvcCfg.mqttConfig.brokerConfig.clientId, \\\"pic32mzw1\\\", strlen(\\\"pic32maw1\\\")); g_sMqttSrvcCfg.mqttConfig.brokerConfig.autoConnect = 1; g_sMqttSrvcCfg.mqttConfig.brokerConfig.tlsEnabled = 0; g_sMqttSrvcCfg.mqttConfig.subscribeCount = 1; strcpy(g_sMqttSrvcCfg.mqttConfig.subscribeConfig[0].topicName, \\\"house/temperature/first_floor/kitchen\\\", strlen(\\\"house/temperature/first_floor/kitchen\\\")); g_sMqttSrvcCfg.mqttConfig.subscribeConfig[0].qos = 1; g_MqttSrvcHandle = SYS_MQTT_Connect(&amp;g_sMqttSrvcCfg, MqttSrvcCallback, 0); if (g_MqttSrvcHandle == SYS_MODULE_OBJ_INVALID) { // Handle error } . Remarks . This routine should be called only once when the user is configuring the Mqtt service . SYS_MQTT_Disconnect . Function . void SYS_MQTT_Disconnect(SYS_MODULE_OBJ obj) . Summary . Disconnects from the MQTT Server . Description . This function is used for disconnecting from the MQTT Server. Precondition . SYS_MQTT_Connect should have been called. Parameters . obj - SYS_MQTT object handle, returned from SYS_MQTT_Connect . Returns . None . Example . // Handle \\\"objSysMqtt\\\" value must have been returned from SYS_MQTT_Connect. SYS_MQTT_Disconnect(objSysMqtt); . Remarks . None. SYS_MQTT_Task . Function . void SYS_MQTT_Task(SYS_MODULE_OBJ obj) . Summary . Executes the MQTT Service State Machine . Description . This function ensures that the MQTT service is able to execute its state machine to process any messages and invoke the user callback for any events. Precondition . SYS_MQTT_Connect should have been called before calling this function . Parameters . obj - SYS MQTT object handle, returned from SYS_MQTT_Connect . Returns . None . Example . // Handle \\\"objSysMqtt\\\" value must have been returned from SYS_MQTT_Connect. while(1) { ... SYS_MQTT_Task(objSysMqtt); ... } . SYS_MQTT_Subscribe . Function . int32_t SYS_MQTT_Subscribe(SYS_MODULE_OBJ obj, SYS_MQTT_SubscribeConfig *subConfig); . Summary . Returns success/ failure for the subscribing to a Topic by the user. Description . This function is used for subscribing to a Topic. Precondition . SYS_MQTT_Connect should have been called before calling this function . Parameters . obj - SYS MQTT object handle, returned from SYS_MQTT_Connect subConfig - valid pointer to the Topic details on which to Subscribe . Returns . SYS_MQTT_SUCCESS - Indicates that the Request was catered to successfully . SYS_MQTT_FAILURE - Indicates that the Request failed . Example . SYS_MQTT_SubscribeConfig sSubscribeCfg; memset(&amp;sSubscribeCfg, 0, sizeof(sSubscribeCfg)); sSubscribeCfg.qos = 1; strcpy(sSubscribeCfg.topicName, \\\"house/temperature/first_floor/kitchen\\\"); // Handle \\\"objSysMqtt\\\" value must have been returned from SYS_MQTT_Connect. if( SYS_MQTT_Subscribe(objSysMqtt, &amp;sSubscribeCfg) == SYS_MQTT_SUCCESS) { } . SYS_MQTT_Unsubscribe . Function . int32_t SYS_MQTT_Unsubscribe(SYS_MODULE_OBJ obj, char *subTopic); . Summary . Returns success/ failure for the unsubscribing to a Topic by the user. Description . This function is used for Unsubscribing from a Topic. Precondition . SYS_MQTT_Connect should have been called before calling this function . Parameters . obj - SYS MQTT object handle, returned from SYS_MQTT_Connect subtopic - Topic from which to unsubscribe . Returns . SYS_MQTT_SUCCESS - Indicates that the Request was catered to successfully . SYS_MQTT_FAILURE - Indicates that the Request failed . Example . // Handle \\\"objSysMqtt\\\" value must have been returned from SYS_MQTT_Connect. if( SYS_MQTT_Unsubscribe(objSysMqtt, \\\"house/temperature/first_floor/kitchen\\\") == SYS_MQTT_SUCCESS) { } . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/mqtt/docs/interface.html#setup-functions",
    "relUrl": "/system/mqtt/docs/interface.html#setup-functions"
  },"55": {
    "doc": "MQTT System Service Interface",
    "title": "Data Exchange functions",
    "content": "SYS_MQTT_Publish . Function . int32_t SYS_MQTT_Publish(SYS_MODULE_OBJ obj, SYS_MQTT_PublishTopicCfg *psPubCfg, char *message, uint16_t message_len); . Summary . Returns success/ failure for the publishing of message on a topic by the user. Description . This function is used for Publishing a message on a Topic. Precondition . SYS_MQTT_Connect should have been called before calling this function . Parameters . obj - SYS MQTT object handle, returned from SYS_MQTT_Connect psPubCfg - valid pointer to the Topic details on which to Publish message - Message to be published . message_len - Message length . Returns . SYS_MQTT_SUCCESS - Indicates that the Request was catered to successfully . SYS_MQTT_FAILURE - Indicates that the Request failed . Example . SYS_MQTT_PublishTopicCfg sTopicCfg; memset(&amp;sTopicCfg, 0, sizeof(sTopicCfg)); sTopicCfg.qos = 1; sTopicCfg.retain = 1; strcpy(sTopicCfg.topicName, \\\"house/temperature/first_floor/kitchen\\\"); sTopicCfg.topicLength = strlen(\\\"house/temperature/first_floor/kitchen\\\"); // Handle \\\"objSysMqtt\\\" value must have been returned from SYS_MQTT_Connect. if( SYS_MQTT_Publish(objSysMqtt, &amp;sPublishCfg, \\\"80.17\\\", strlen(\\\"80.17\\\")) == SYS_MQTT_SUCCESS) { } . SYS_MQTT_CALLBACK . Function . int32_t SYS_MQTT_CALLBACK(SYS_MQTT_EVENT_TYPE eEventType, void *data, uint16_t len, void* cookie); . Summary . Pointer to a MQTT system service callback function. Description . This data type defines a pointer to a Mqtt service callback function, thus defining the function signature. Callback functions may be registered by mqtt clients of the Mqtt service via the SYS_MQTT_Connect call. Precondition . Is a part of the Mqtt service Setup using the SYS_MQTT_Connect function . Parameters . eEventType - event (SYS_MQTT_EVENT_TYPE) - Message Received/ Got Disconnected data - Data (if any) related to the Event len - Length of the Data received cookie - A context value, returned untouched to the client when the callback occurs. It can be used to identify the instance of the client who registered the callback. Returns . None. Example . void MqttSrvcCallback(SYS_MQTT_EVENT_TYPE event, void *data, uint16_t len, void* cookie, ) { switch(event) { case SYS_MQTT_EVENT_MSG_RCVD: { SYS_MQTT_PublishConfig *psMsg = (SYS_MQTT_PublishConfig *)data; psMsg-&gt;message[psMsg-&gt;messageLength] = 0; psMsg-&gt;topicName[psMsg-&gt;topicLength] = 0; SYS_CONSOLE_PRINT(\\\"\\nMqttCallback(): Msg received on Topic: %s ; Msg: %s\\r\\n\\\", psMsg-&gt;topicName, psMsg-&gt;message); break; } case SYS_MQTT_EVENT_MSG_DISCONNECT: { SYS_CONSOLE_PRINT(\\\"CloudSrvcCallback(): MQTT DOWN\\\"); break; } } } . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/mqtt/docs/interface.html#data-exchange-functions",
    "relUrl": "/system/mqtt/docs/interface.html#data-exchange-functions"
  },"56": {
    "doc": "License",
    "title": "License",
    "content": "IMPORTANT: READ CAREFULLY . MICROCHIP IS WILLING TO LICENSE THIS INTEGRATED SOFTWARE FRAMEWORK SOFTWARE AND ACCOMPANYING DOCUMENTATION OFFERED TO YOU ONLY ON THE CONDITION THAT YOU ACCEPT ALL OF THE FOLLOWING TERMS. TO ACCEPT THE TERMS OF THIS LICENSE, CLICK “I ACCEPT” AND PROCEED WITH THE DOWNLOAD OR INSTALL. IF YOU DO NOT ACCEPT THESE LICENSE TERMS, CLICK “I DO NOT ACCEPT,” AND DO NOT DOWNLOAD OR INSTALL THIS SOFTWARE. NON-EXCLUSIVE SOFTWARE LICENSE AGREEMENT FOR MICROCHIP MPLAB HARMONY INTEGRATED SOFTWARE FRAMEWORK . This Nonexclusive Software License Agreement (“Agreement”) is between you, your heirs, agents, successors and assigns (“Licensee”) and Microchip Technology Incorporated, a Delaware corporation, with a principal place of business at 2355 W. Chandler Blvd., Chandler, AZ 85224-6199, and its subsidiary, Microchip Technology (Barbados) II Incorporated (collectively, “Microchip”) for Microchip’s MPLAB Harmony Integrated Software Framework (“Software”) and accompanying documentation (“Documentation”). The Software and Documentation are licensed under this Agreement and not sold. U.S. copyright laws and international copyright treaties, and other intellectual property laws and treaties protect the Software and Documentation. Microchip reserves all rights not expressly granted to Licensee in this Agreement. | License and Sublicense Grant. (a) Definitions. As used this Agreement, the following terms shall have the meanings defined below: . (i) \\\"Licensee Products\\\" means Licensee products that use or incorporate Microchip Products. (ii) \\\"Microchip Product\\\" means Microchip 16-bit and 32-bit microcontrollers, digital signal controllers or other Microchip semiconductor products with PIC16 and PIC18 prefix and specifically excepting the CX870 and CY920, which are not covered under this Agreement, that use or implement the Software. (iii) \\\"Object Code\\\" means the Software computer programming code provided by Microchip that is in binary form (including related documentation, if any) and error corrections, improvements and updates to such code provided by Microchip in its sole discretion, if any. (iv) \\\"Source Code\\\" means the Software computer programming code provided by Microchip that may be printed out or displayed in human readable form (including related programmer comments and documentation, if any), and error corrections, improvements, updates, modifications and derivatives of such code developed by Microchip, Licensee or Third Party. (v) \\\"Third Party\\\" means Licensee's agents, representatives, consultants, clients, customers, or contract manufacturers. (vi) \\\"Third Party Products\\\" means Third Party products that use or incorporate Microchip Products. (b) Software License Grant. Subject to the terms of this Agreement, Microchip grants strictly to Licensee a personal, worldwide, non-exclusive, non-transferable limited license to use, modify (except as limited by Section 1(f) below), copy and distribute the Software only when the Software is embedded on a Microchip Product that is integrated into Licensee Product or Third Party Product pursuant to Section 2(d) below. Any portion of the Software (including derivatives or modifications thereof) may not be: . (i) embedded on a non-Microchip microcontroller or digital signal controller; (ii) distributed (in Source Code or Object Code), except as described in Section 2(d) below. (c) Documentation License Grant. Subject to all of the terms and conditions of this Agreement, Microchip grants strictly to Licensee a perpetual, worldwide, non-exclusive license to use the Documentation in support of Licensee’s use of the Software. (d) Sublicense Grants. Subject to terms of this Agreement, Licensee may grant a limited sublicense to a Third Party to use the Software as described below only if such Third Party expressly agrees to be bound by terms of confidentiality and limited use that are no broader in scope and duration than the confidentiality and limited use terms of this Agreement: . (i) Third Party may modify Source Code for Licensee, except as limited by Section 1(f) below. (ii) Third Party may program Software into Microchip Products for Licensee. (iii) Third Party may use Software to develop and/or manufacture Licensee Product. (iv) Third Party may use Software to develop and/or manufacture Third Party Products where either: (x) the sublicensed Software contains Source Code modified or otherwise optimized by Licensee for Third Party use; or (y) the sublicensed Software is programmed into Microchip Products by Licensee on behalf of such Third Party. (v) Third Party may use the Documentation in support of Third Party's authorized use of the Software in conformance with this Section 2(d). (e) Audit. Authorized representatives of Microchip shall have the right to reasonably inspect Licensee’s premises and to audit Licensee’s records and inventory of Licensee Products, whether located on Licensee’s premises or elsewhere at any time, announced or unannounced, and in its sole and absolute discretion, in order to ensure Licensee’s adherence to the terms of this Agreement. (f) License and Sublicense Limitation. This Section 1 does not grant Licensee or any Third Party the right to modify any dotstack™ Bluetooth® stack, profile, or iAP protocol included in the Software. | Third Party Requirements. Licensee acknowledges that it is Licensee’s responsibility to comply with any third party license terms or requirements applicable to the use of such third party software, specifications, systems, or tools, including but not limited to SEGGER Microcontroller GmbH &amp; Co. KG’s rights in the emWin software and certain libraries included herein. Microchip is not responsible and will not be held responsible in any manner for Licensee’s failure to comply with such applicable terms or requirements. | Open Source Components. Notwithstanding the license grants contained herein, Licensee acknowledges that certain components of the Software may be covered by so-called “open source” software licenses (“Open Source Components”). Open Source Components means any software licenses approved as open source licenses by the Open Source Initiative or any substantially similar licenses, including any license that, as a condition of distribution, requires Microchip to provide Licensee with certain notices and/or information related to such Open Source Components, or requires that the distributor make the software available in source code format. Microchip will use commercially reasonable efforts to identify such Open Source Components in a text file or “About Box” or in a file or files referenced thereby (and will include any associated license agreement, notices, and other related information therein), or the Open Source Components will contain or be accompanied by its own license agreement. To the extent required by the licenses covering Open Source Components, the terms of such licenses will apply in lieu of the terms of this Agreement, and Microchip hereby represents and warrants that the licenses granted to such Open Source Components will be no less broad than the license granted in Section 1(b). To the extent the terms of the licenses applicable to Open Source Components prohibit any of the restrictions in this Agreement with respect to such Open Source Components, such restrictions will not apply to such Open Source Components. | Licensee’s Obligations. (a) Licensee will ensure Third Party compliance with the terms of this Agreement. (b) Licensee will not: (i) engage in unauthorized use, modification, disclosure or distribution of Software or Documentation, or its derivatives; (ii) use all or any portion of the Software, Documentation, or its derivatives except in conjunction with Microchip Products; or (iii) reverse engineer (by disassembly, decompilation or otherwise) Software or any portion thereof; or (iv) copy or reproduce all or any portion of Software, except as specifically allowed by this Agreement or expressly permitted by applicable law notwithstanding the foregoing limitations. (c) Licensee must include Microchip’s copyright, trademark and other proprietary notices in all copies of the Software, Documentation, and its derivatives. Licensee may not remove or alter any Microchip copyright or other proprietary rights notice posted in any portion of the Software or Documentation. (d) Licensee will defend, indemnify and hold Microchip and its subsidiaries harmless from and against any and all claims, costs, damages, expenses (including reasonable attorney’s fees), liabilities, and losses, including without limitation product liability claims, directly or indirectly arising from or related to: (i) the use, modification, disclosure or distribution of the Software, Documentation or any intellectual property rights related thereto; (ii) the use, sale, and distribution of Licensee Products or Third Party Products, and (iii) breach of this Agreement. THE FOREGOING STATES THE SOLE AND EXCLUSIVE LIABILITY OF THE PARTIES FOR INTELLECTUAL PROPERTY RIGHTS INFRINGEMENT. | Confidentiality. (a) Licensee agrees that the Software (including but not limited to the Source Code, Object Code and library files) and its derivatives, Documentation and underlying inventions, algorithms, know-how and ideas relating to the Software and the Documentation are proprietary information belonging to Microchip and its licensors (“Proprietary Information”). Except as expressly and unambiguously allowed herein, Licensee will hold in confidence and not use or disclose any Proprietary Information and shall similarly bind its employees and Third Party(ies) in writing. Proprietary Information shall not include information that: (i) is in or enters the public domain without breach of this Agreement and through no fault of the receiving party; (ii) the receiving party was legally in possession of prior to receiving it; (iii) the receiving party can demonstrate was developed by it independently and without use of or reference to the disclosing party’s Proprietary Information; or (iv) the receiving party receives from a third party without restriction on disclosure. If Licensee is required to disclose Proprietary Information by law, court order, or government agency, such disclosure shall not be deemed a breach of this Agreement provided that Licensee gives Microchip prompt notice of such requirement in order to allow Microchip to object or limit such disclosure, Licensee cooperates with Microchip to protect Proprietary Information, and Licensee complies with any protective order in place and discloses only the information required by process of law. (b) Licensee agrees that the provisions of this Agreement regarding unauthorized use and nondisclosure of the Software, Documentation and related Proprietary Rights are necessary to protect the legitimate business interests of Microchip and its licensors and that monetary damages alone cannot adequately compensate Microchip or its licensors if such provisions are violated. Licensee, therefore, agrees that if Microchip alleges that Licensee or Third Party has breached or violated such provision then Microchip will have the right to petition for injunctive relief, without the requirement for the posting of a bond, in addition to all other remedies at law or in equity. | Ownership of Proprietary Rights. (a) Microchip and its licensors retain all right, title and interest in and to the Software and Documentation (“Proprietary Rights”) including, but not limited to: (i) patent, copyright, trade secret and other intellectual property rights in the Software, Documentation, and underlying technology; (ii) the Software as implemented in any device or system, all hardware and software implementations of the Software technology (expressly excluding Licensee and Third Party code developed and used in conformance with this Agreement solely to interface with the Software and Licensee Products and/or Third Party Products); and (iii) all modifications and derivative works thereof (by whomever produced). Further, modifications and derivative works shall be considered works made for hire with ownership vesting in Microchip on creation. To the extent such modifications and derivatives do not qualify as a “work for hire,” Licensee hereby irrevocably transfers, assigns and conveys the exclusive copyright thereof to Microchip, free and clear of any and all liens, claims or other encumbrances, to the fullest extent permitted by law. Licensee and Third Party use of such modifications and derivatives is limited to the license rights described in Section 1 above. (b) Licensee shall have no right to sell, assign or otherwise transfer all or any portion of the Software, Documentation or any related intellectual property rights except as expressly set forth in this Agreement. | Termination of Agreement. Without prejudice to any other rights, this Agreement terminates immediately, without notice by Microchip, upon a failure by License or Third Party to comply with any provision of this Agreement. Further, Microchip may also terminate this Agreement upon reasonable belief that Licensee or Third Party have failed to comply with this Agreement. Upon termination, Licensee and Third Party will immediately stop using the Software, Documentation, and derivatives thereof, and immediately destroy all such copies, remove Software from any of Licensee’s tangible media and from systems on which the Software exists, and stop using, disclosing, copying, or reproducing Software (even as may be permitted by this Agreement). Termination of this Agreement will not affect the right of any end user or consumer to use Licensee Products or Third Party Products provided that such products were purchased prior to the termination of this Agreement. | Dangerous Applications. The Software is not fault-tolerant and is not designed, manufactured, or intended for use in hazardous environments requiring failsafe performance (“Dangerous Applications”). Dangerous Applications include the operation of nuclear facilities, aircraft navigation, aircraft communication systems, air traffic control, direct life support machines, weapons systems, or any environment or system in which the failure of the Software could lead directly or indirectly to death, personal injury, or severe physical or environmental damage. Microchip specifically disclaims (a) any express or implied warranty of fitness for use of the Software in Dangerous Applications; and (b) any and all liability for loss, damages and claims resulting from the use of the Software in Dangerous Applications. | Warranties and Disclaimers. THE SOFTWARE AND DOCUMENTATION ARE PROVIDED “AS IS” WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE. MICROCHIP AND ITS LICENSORS ASSUME NO RESPONSIBILITY FOR THE ACCURACY, RELIABILITY OR APPLICATION OF THE SOFTWARE OR DOCUMENTATION. MICROCHIP AND ITS LICENSORS DO NOT WARRANT THAT THE SOFTWARE WILL MEET REQUIREMENTS OF LICENSEE OR THIRD PARTY, BE UNINTERRUPTED OR ERROR-FREE. MICROCHIP AND ITS LICENSORS HAVE NO OBLIGATION TO CORRECT ANY DEFECTS IN THE SOFTWARE. LICENSEE AND THIRD PARTY ASSUME THE ENTIRE RISK ARISING OUT OF USE OR PERFORMANCE OF THE SOFTWARE AND DOCUMENTATION PROVIDED UNDER THIS AGREEMENT. | Limited Liability. IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR OTHER LEGAL OR EQUITABLE THEORY FOR ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES INCLUDING BUT NOT LIMITED TO INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES (INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS. The aggregate and cumulative liability of Microchip and its licensors for damages hereunder will in no event exceed $1000 or the amount Licensee paid Microchip for the Software and Documentation, whichever is greater. Licensee acknowledges that the foregoing limitations are reasonable and an essential part of this Agreement. | General. (a) Governing Law, Venue and Waiver of Trial by Jury. THIS AGREEMENT SHALL BE GOVERNED BY AND CONSTRUED UNDER THE LAWS OF THE STATE OF ARIZONA AND THE UNITED STATES WITHOUT REGARD TO CONFLICTS OF LAWS PROVISIONS. Licensee agrees that any disputes arising out of or related to this Agreement, Software or Documentation shall be brought in the courts of State of Arizona. The parties agree to waive their rights to a jury trial in actions relating to this Agreement. (b) Attorneys’ Fees. If either Microchip or Licensee employs attorneys to enforce any rights arising out of or relating to this Agreement, the prevailing party shall be entitled to recover its reasonable attorneys’ fees, costs and other expenses. (c) Entire Agreement. This Agreement shall constitute the entire agreement between the parties with respect to the subject matter hereof. It shall not be modified except by a written agreement signed by an authorized representative of Microchip. (d) Severability. If any provision of this Agreement shall be held by a court of competent jurisdiction to be illegal, invalid or unenforceable, that provision shall be limited or eliminated to the minimum extent necessary so that this Agreement shall otherwise remain in full force and effect and enforceable. (e) Waiver. No waiver of any breach of any provision of this Agreement shall constitute a waiver of any prior, concurrent or subsequent breach of the same or any other provisions hereof, and no waiver shall be effective unless made in writing and signed by an authorized representative of the waiving party. (f) Export Regulation. Licensee agrees to comply with all export laws and restrictions and regulations of the Department of Commerce or other United States or foreign agency or authority. (g) Survival. The indemnities, obligations of confidentiality, and limitations on liability described herein, and any right of action for breach of this Agreement prior to termination shall survive any termination of this Agreement. (h) Assignment. Neither this Agreement nor any rights, licenses or obligations hereunder, may be assigned by Licensee without the prior written approval of Microchip except pursuant to a merger, sale of all assets of Licensee or other corporate reorganization, provided that assignee agrees in writing to be bound by the Agreement. (i) Restricted Rights. Use, duplication or disclosure by the United States Government is subject to restrictions set forth in subparagraphs (a) through (d) of the Commercial Computer-Restricted Rights clause of FAR 52.227-19 when applicable, or in subparagraph (c)(1)(ii) of the Rights in Technical Data and Computer Software clause at DFARS 252.227-7013, and in similar clauses in the NASA FAR Supplement. Contractor/manufacturer is Microchip Technology Inc., 2355 W. Chandler Blvd., Chandler, AZ 85225-6199. | . If Licensee has any questions about this Agreement, please write to Microchip Technology Inc., 2355 W. Chandler Blvd., Chandler, AZ 85224-6199 USA, ATTN: Marketing. Microchip MPLAB Harmony Integrated Software Framework. Copyright © 2015 Microchip Technology Inc. All rights reserved. License Rev. 11/2015 . Copyright © 2015 Qualcomm Atheros, Inc. All Rights Reserved. Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted, provided that the above copyright notice and this permission notice appear in all copies. THE SOFTWARE IS PROVIDED “AS IS” AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE. ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/mplab_harmony_license.html",
    "relUrl": "/mplab_harmony_license.html"
  },"57": {
    "doc": "MQTT Service",
    "title": "MQTT System Service",
    "content": "MQTT System Service Library provides an application programming interface (API) to manage MQTT functionalities. The MQTT System Service internally uses the third party Paho MQTT software for MQTT support. Key Features: . | Supports MQTT Client | Supports TLS for MQTT Connection | Supports Self Healing, that is if the connection for some reason breaks, the service shall take care of reconnecting the same internally. | . The MQTT System Service provides simple API’s to enable MQTT functionalities like publishing, and subscribing to a topic. | Using the library . | Configuring the library . | Library interface . | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/mqtt/docs/readme.html#mqtt-system-service",
    "relUrl": "/system/mqtt/docs/readme.html#mqtt-system-service"
  },"58": {
    "doc": "MQTT Service",
    "title": "MQTT Service",
    "content": " ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/mqtt/docs/readme.html",
    "relUrl": "/system/mqtt/docs/readme.html"
  },"59": {
    "doc": "App Debug Service",
    "title": "App Debug System Service",
    "content": "App Debug System Service Library provides an application programming interface (API) to manage debug logs at runtime. Key Features: . | Supports Enabling/ Disabling of logs at runtime | Supports Enabling/ Disabling of logs based on severity level | Supports Enabling/ Disabling of logs based on logical flow | . The App Debug System Service provides simple API’s to enable/diable system console logs functionalities. Multiple users can request the App Debug system service functionalities simultaneously. | Using the library . | Configuring the library . | Library interface . | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/appdebug/docs/readme.html#app-debug-system-service",
    "relUrl": "/system/appdebug/docs/readme.html#app-debug-system-service"
  },"60": {
    "doc": "App Debug Service",
    "title": "App Debug Service",
    "content": " ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/appdebug/docs/readme.html",
    "relUrl": "/system/appdebug/docs/readme.html"
  },"61": {
    "doc": "Wi-Fi provisioning Service",
    "title": "Wi-Fi provisioning System Service",
    "content": "Wi-Fi Provisioning System Service Library is used to enable Wi-Fi provisioning method. Wi-Fi Provisioning is the process of configuring desired Wi-Fi SSID and related security credentials of the Home AP into the device. This system service provides different methods that can be used to provide this information to the core stack. Key Features: . | Wi-Fi Provisioning using command line. | Wi-Fi Provisioning using TCP Socket . | JSON | Mobile Application | . | Wi-Fi Provisioning using webpage(HTTP page). | Configuring the library . | Using the library . | Library interface | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/readme.html#wi-fi-provisioning-system-service",
    "relUrl": "/system/wifiprov/docs/readme.html#wi-fi-provisioning-system-service"
  },"62": {
    "doc": "Wi-Fi provisioning Service",
    "title": "Wi-Fi provisioning Service",
    "content": " ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/readme.html",
    "relUrl": "/system/wifiprov/docs/readme.html"
  },"63": {
    "doc": "Net Service",
    "title": "Net System Service",
    "content": "Net System Service Library provides an application programming interface (API) to manage TCPIP Networking functionalities. The Net System Service uses the NetPres APIs for achieving these functionalities. Key Features: . | Supports Client/ Server Mode for IP Network Connectivity | Supports TCP and UDP Protocols of IP | Supports TLS for TCP Connection | Supports Self Healing, that is if the connection for some reason breaks, the service shall take care of reconnecting the same internally. | . The Net System Service provides simple API’s to enable network stack functionalities. Multiple clients can request the Net system service functionalities like tcp/udp connection request, tcp/udp disconnect request, sending and receiving data, etc. | Using the library . | Configuring the library . | Library interface . | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/net/docs/readme.html#net-system-service",
    "relUrl": "/system/net/docs/readme.html#net-system-service"
  },"64": {
    "doc": "Net Service",
    "title": "Net Service",
    "content": " ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/net/docs/readme.html",
    "relUrl": "/system/net/docs/readme.html"
  },"65": {
    "doc": "Wi-Fi Service",
    "title": "Wi-Fi System Service",
    "content": "Wi-Fi System Service Library provides an application programming interface (API) through which user can request Wi-Fi connectivity functionalities.The Wi-Fi System Service use Wi-Fi driver APIs. Key Features: . | Configuration of Station mode(STA) . | Security Support: . | Open - No security | WPA2 | WPAWPA2(Mixed) mode | WPA2WPA3(Mixed) | WPA3 | . | Self Healing . | if the connection for some reason breaks, the service shall take care of reconnecting the same internally. | . | . | Configuration of Soft Access point mode(AP) . | Security Support: . | Open - No security | WPA2 | WPAWPA2(Mixed) | WPA2WPA3(Mixed) | WPA3 | Hidden Access Point(AP) | . | . | . The Wi-Fi System Service provides simple API’s to enable Station(STA) or Access Point(AP) functionalities. Multiple clients can request the Wi-Fi system service functionalities like connection request,disconnect request,scan request,etc. User is not required to have Wi-Fi domain knowledge to developed station(STA) or access point(AP) application using Wi-Fi System Service. | Using the library . | Configuring the library . | Library interface . | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/wifi/docs/readme.html#wi-fi-system-service",
    "relUrl": "/system/wifi/docs/readme.html#wi-fi-system-service"
  },"66": {
    "doc": "Wi-Fi Service",
    "title": "Wi-Fi Service",
    "content": " ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/wifi/docs/readme.html",
    "relUrl": "/system/wifi/docs/readme.html"
  },"67": {
    "doc": "Release notes",
    "title": "Microchip MPLAB® Harmony 3 Release Notes",
    "content": " ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/release_notes.html#microchip-mplab-harmony-3-release-notes",
    "relUrl": "/release_notes.html#microchip-mplab-harmony-3-release-notes"
  },"68": {
    "doc": "Release notes",
    "title": "Harmony 3 Wireless system services for the PIc32MZW1/WFI32 family  v3.4.1",
    "content": "New Features . | Split wireless system services into a seperate repo | . Bug fixes . | None | . Known Issues . | None | . Development Tools . | MPLAB® X IDE v5.40 | MPLAB® X IDE plug-ins: . | MPLAB® Harmony Configurator (MHC) v3.6.2 | . | MPLAB® XC32 C/C++ Compiler v2.50 | . ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/release_notes.html#harmony-3-wireless-system-services-for-the-pic32mzw1wfi32-family--v341",
    "relUrl": "/release_notes.html#harmony-3-wireless-system-services-for-the-pic32mzw1wfi32-family--v341"
  },"69": {
    "doc": "Release notes",
    "title": "Release notes",
    "content": ". ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/release_notes.html",
    "relUrl": "/release_notes.html"
  },"70": {
    "doc": "App Debug System Service Usage",
    "title": "App Debug System Service Usage",
    "content": "# App Debug System Service Usage ## Description The App Debug System Service provides simple APIs to enable/ disable logs at runtime based on the log levels and flow. More on how any component using this library can enabling/ disable logs at runtime can go through the system services like the MQTT, NET, and Wifi System Service. ## Abstraction Model The App Debug System Service library provides an abstraction to the System Console Lohs to provide following functionalities. - Enabling/ disabling of logs at runtime. - Enabling/ disabling of logs based on severity level - Enabling/ disabling of logs based on logical flows, e.g., Data Flow, Control Flow, etc ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/appdebug/docs/usage.html",
    "relUrl": "/system/appdebug/docs/usage.html"
  },"71": {
    "doc": "MQTT System Service Usage",
    "title": "MQTT System Service Usage",
    "content": "# MQTT System Service Usage ## Description The MQTT System Service provides simple APIs to enable MQTT Client Connectivity to a configured MQTT Broker. The User need not take care of intermediate states of a MQTT Connection, as the Service internally takes care of that. User is not required to have Security domain knowledge to establish a secured connection via the application using MQTT System Service library. ### Command Line: User can follow below commands for MQTT System Service: 1. sysmqtthelp MQTT System Service help command which displays the supported CLI commands ![](/wireless_system_pic32mzw1_wfi32e01/system/mqtt/docs/images/sysmqtthelp_cli.png) 2. sysmqtt open Command for Reconfiguring an already open instance of MQTT System Service ![](/wireless_system_pic32mzw1_wfi32e01/system/mqtt/docs/images/sysmqttopen_cli.png) Note: Once the User has configured all the params, the last command for opening the new connection should 'sysmqtt open apply' 3. sysmqtt close Command to close the instance of MQTT System Service ![](/wireless_system_pic32mzw1_wfi32e01/system/mqtt/docs/images/sysmqttclose_cli.png) 4. sysmqtt send Command to send message on a topic for the instance of MQTT System Service ![](/wireless_system_pic32mzw1_wfi32e01/system/mqtt/docs/images/sysmqttsend_cli.png) 5. sysmqtt sunbscribe Command to subscribe to a topic to receive message coming on that topic ![](/wireless_system_pic32mzw1_wfi32e01/system/mqtt/docs/images/sysmqttsubscribe_cli.png) 6. sysmqtt unsunbscribe Command to unsubscribe from a topic ![](/wireless_system_pic32mzw1_wfi32e01/system/mqtt/docs/images/sysmqttunsubscribe_cli.png) 7. sysmqtt get info Command for knowing the Current Information for all the Instances of Net System Service ![](/wireless_system_pic32mzw1_wfi32e01/system/mqtt/docs/images/sysmqttgetinfo_cli.png) ## Abstraction Model The MQTT System Service library provides an abstraction to the MQTT APIs to provide following functionalities. - Connectivity for MQTT Client - Secured Connectivity using TLS - Self Healing - Reduce code user has to write - Reduce time to develop and maintain The following diagram depicts the MQTT System Service abstraction model. ![](/wireless_system_pic32mzw1_wfi32e01/system/mqtt/docs/images/MqttService_abstract.png) ## How The Library Works By default MHC generated code provides all the functionalities to enable MQTT Client applicatation, with secured or unsecured connectivity. User needs to configure the required MQTT Brokerconfiguration using MHC. User needs to call the SYS_MQTT_Connect() API with a valid callback to open an instance of the MQTT Client configured in the MHC.  ![](/wireless_system_pic32mzw1_wfi32e01/system/mqtt/docs/images/MqttConnect.png) The User Application is expected to call SYS_MQTT_Task() API periodically as this API ensures that the MQTT System service is able to execute its state machine to process any messages and invoke the user callback for any events.  The User Application can call SYS_MQTT_Publish()/ SYS_MQTT_Subscribe() API in case it wants to publish message to a topic or receive messages on a topic. ![](/wireless_system_pic32mzw1_wfi32e01/system/mqtt/docs/images/MqttPublish.png) ![](/wireless_system_pic32mzw1_wfi32e01/system/mqtt/docs/images/MqttSubscribe.png) The User Application when enables Auto-Reconnect, it enables the self healing feature of the MQTT Service. When this feature is enabled, the service will automatically try to establish connection with the MQTT Broker whenever a connection breaks. ![](/wireless_system_pic32mzw1_wfi32e01/system/mqtt/docs/images/MqttSelfHealing.png) ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/mqtt/docs/usage.html",
    "relUrl": "/system/mqtt/docs/usage.html"
  },"72": {
    "doc": "Net System Service Usage",
    "title": "Net System Service Usage",
    "content": "# Net System Service Usage ## Description The NET System Service provides simple APIs to enable Server or Client Connectivity for either TCP or UDP. The User need not take care of intermediate states of a TCPIP Connection, as the Service internally takes care of that. User is not required to have Security domain knowledge to establish a secured connection via the application using NET System Service library. ### Command Line: User can follow below commands for NET System Service: 1. sysnethelp NET System Service help command which displays the supported CLI commands ![](/wireless_system_pic32mzw1_wfi32e01/system/net/docs/images/sysnethelp_cli.png) 2. sysnet open Command for Reconfiguring an already open instance of Net System Service ![](/wireless_system_pic32mzw1_wfi32e01/system/net/docs/images/sysnetopen_cli.png) 3. sysnet close Command to close the instance of Net System Service ![](/wireless_system_pic32mzw1_wfi32e01/system/net/docs/images/sysnetclose_cli.png) 4. sysnet send Command to send message on the network connection established by the instance of Net System Service ![](/wireless_system_pic32mzw1_wfi32e01/system/net/docs/images/sysnetsend_cli.png) 5. sysnet get info Command for knowing the Current Information for all the Instances of Net System Service ![](/wireless_system_pic32mzw1_wfi32e01/system/net/docs/images/sysnetgetinfo_cli.png) ## Abstraction Model The NET System Service library provides an abstraction to the NetPres/ TCPIP APIs to provide following functionalities. - Connectivity for TCP Client - Connectivity for TCP Server - Connectivity for UDP Client - Connectivity for UDP Server - Self Healing - Reduce code user has to write - Reduce time to develop and maintain The following diagram depicts the Net System Service abstraction model. ![](/wireless_system_pic32mzw1_wfi32e01/system/net/docs/images/NetService_abstract.png) ## How The Library Works By default MHC generated code provides all the functionalities to enable Client or Server mode applicatation, with TCP or UDP as the IP Protocol. User needs to configure the required Client or Server mode configuration using MHC. User needs to call the SYS_NET_Open() API with a valid callback to open an instance of the Client/ Server configured in the MHC.  ![](/wireless_system_pic32mzw1_wfi32e01/system/net/docs/images/NetOpen.png) The User Application is expected to call SYS_NET_Task() API periodically as this API ensures that the Net System service is able to execute its state machine to process any messages and invoke the user callback for any events.  ![](/wireless_system_pic32mzw1_wfi32e01/system/net/docs/images/NetTask.png) The User Application can call SYS_NET_CtrlMsg() API in case it wants to disconnect the opened connection or to reconnect using different configuration. ![](/wireless_system_pic32mzw1_wfi32e01/system/net/docs/images/NetCtrlMsg.png) ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/net/docs/usage.html",
    "relUrl": "/system/net/docs/usage.html"
  },"73": {
    "doc": "Wi-Fi System Service Usage",
    "title": "Wi-Fi System Service Usage",
    "content": "# Wi-Fi System Service Usage ## Abstraction Model The Wi-Fi System Service library provides an abstraction to the Wi-Fi driver API's to provide following functionalities. - Simple APIs to enable/disable STA mode - Simple APIs to enable/disable AP mode - Self Healing - Reduce code user has to write - Reduce time to develop and maintain The following diagram depicts the Wi-Fi System Service abstraction model. ![](/wireless_system_pic32mzw1_wfi32e01/system/wifi/docs/images/Wifiservice_abstract.png) ## How The Library Works By default, MHC generated code provides all the functionalities to enable STA or AP mode application. User needs to configure the required STA or AP mode configuration using MHC.  ![](/wireless_system_pic32mzw1_wfi32e01/system/wifi/docs/images/Seqdig_WiFi_Initialization.png) Multiple clients can register for callbacks to the Wi-Fi System Service Library for getting Wi-Fi connectivity update information. Additionally clients can make request to the Wi-Fi System Service Library using SYS\\_WIFI\\_CtrlMsg() API. More information can be found in the SYS\\_WIFI\\_CtrlMsg examples.  ![](/wireless_system_pic32mzw1_wfi32e01/system/wifi/docs/images/seqdig_WiFi_Multiclient.png) ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/wifi/docs/usage.html",
    "relUrl": "/system/wifi/docs/usage.html"
  },"74": {
    "doc": "Wi-Fi provisioning System Service Usage",
    "title": "Wi-Fi provisioning System Service Usage",
    "content": "# Wi-Fi provisioning System Service Usage {: .no_toc } ### {: .no_toc .text-delta } 1. TOC {:toc} --- The Wi-Fi Provisioning System Service povides below methods to configuring desired Wi-Fi SSID and related security credentials of the Home AP into the device. # Wi-Fi Provisioning Methods ## Command line MHC configuration menu for Command line(CLI): ![](/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/images/SYS_Wi-Fi_Provision_MHC_diagram_1.png) - Enable Check box \\\"Command Line(CLI)\\\" to include CLI Wi-Fi provisioning method. - After making configuration changes, generate the code. - Compile the project and load the image into device. Wi-Fi Provisioning commands Details | Command | Details | Example | ----------------| ---------------|------------------------------- | wifiprovhelp | Wi-Fi Provision System Service help command | wifiprovhelp | wifiprov set \\\\ \\\\ \\\\ \\\\ \\\\ \\\\ \\\\ \\\\ | Set Wi-Fi Configuration for Station(STA) mode | wifiprov set 0 1 \\\"GEN\\\" 0 1 3 \\\"DEMO_AP\\\" \\\"password\\\" | wifiprowifiprov set \\\\ \\\\ \\\\ \\\\ \\\\ \\\\ \\\\ \\\\ | Set Wi-Fi Configuration for Access point(AP) mode | wifiprov set 1 1 \\\"GEN\\\" 1 1 3 \\\"DEMO_SOFTAP\\\" \\\"password\\\" | wifiprov get | Get Wi-Fi Configuration | wifiprov get ||| Wi-Fi Provisioning commands command parameters information, | Parameter | Sub Parameter | ----------------| ----------------------------------------------------- | bootmode | 0 - Station(STA) mode.1- Access point(AP) mode. | save config | 0 - Do not save configuration in NVM(Program Flash Memory). 1- Save configuration in NVM . | country code | country code configuration: GEN - General USA - North America EMEA - Europe CUST1,CUST2 - Customer custom regulatory configuration | Channel | In Station mode value range from 0-13, 0 - select all the channels.1-13 - select specified channel. In Access point mode value range from 1-13. |auto connect(only applicable in STA mode)| 0 - Don't connect to AP, wait for client request.1 - Connect to AP. |ssid visibility (only applicable in AP mode)| 0 - Hidden SSID.1 - Broadcast SSID . |authtype(Security type) | 1 - OPEN Mode. 3 - WPAWPA2 (Mixed) mode. 4 - WPA2 mode. 5 - WPA2WPA3 (Mixed) mode. 6 - WPA3 mode. |ssid(ssid name) | SSID name |psk name(password)| Password/passphrase ||| Note: - Wi-Fi Provisioning using command line method is not recommended in production release due to security concerns. - All commands the parameters are mandatory, and none are optional except for password in case of \\\"open\\\" authentication. ## TCP Socket mode MHC configuration menu for TCP Socket: ![](/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/images/SYS_Wi-Fi_Provision_MHC_diagram_1.png) - Enable Check box \\\"TCP Socket\\\" to include TCP Socket Wi-Fi provisioning method. - Modifiy the \\\"Socket Server Port\\\".Defult port number is 6666. - After making configuration changes, generate the code. - Compile the project and load the image into device. Wi-Fi provisioning service can be configured to use TCP socket, a socket server is activated when the device boots.Use a laptop or mobile phone as a TCP client to connect to the device's socket server. Wi-Fi provisioning service defult TCP server port is 6666. ### Wi-Fi provisioning with JSON format User can send the below JSON format data from TCP Client to provisioning the device. Example: ```json { \\\"mode\\\": 0, \\\"save_config\\\": 1,\\\"countrycode\\\":\\\"GEN\\\", \\\"STA\\\": { \\\"ch\\\": 0, \\\"auto\\\": 1, \\\"auth\\\": 3, \\\"SSID\\\": \\\"DEMO_AP\\\", \\\"PWD\\\":\\\"password\\\"}, \\\"AP\\\": {\\\"ch\\\": 2, \\\"ssidv\\\": 1, \\\"auth\\\": 4, \\\"SSID\\\": \\\"DEMO_AP_SOFTAP\\\", \\\"PWD\\\": \\\"password\\\" } } ``` Details of JSON Parameters, | Parameter | Sub Parameter | Value Details | ----------------| ---------------|------------------------------- | mode | 0 - Station(STA) mode. 1- Access point(AP) mode.| save_config | 0 - Do not save configuration in NVM. 1- Save configuration in NVM . | STA | ch (Channel) | In Station mode value range from 0-13,0 - select all the channels.1-13 - select specified channel. | |auto(auto connect)| 0 - Don't connect to AP, wait for client request. 1 - Connect to AP. | |Auth(Security type) | 1 - OPEN Mode.3 - WPAWPA2 (Mixed) mode. 4 - WPA2 mode. 5 - WPA3 mode. | |SSID(ssid name) | SSID name | |PWD(password) | Password/passphrase | AP |ch (Channel) | In Access point mode value range from 1-13 | |ssidv(ssid visibility) | 0 - Hidden SSID. 1 - Broadcast SSID . | |Auth(Security type) | 1 - OPEN Mode. 3 - WPAWPA2 (Mixed) mode. 4 - WPA2 mode. 5 - WPA2WPA3 (Mixed) mode. 6 - WPA3 mode. | |SSID(ssid name) | SSID name | |PWD(password) | Password/passphrase ||| ### Wi-Fi provisioning with Mobile Application Follow below steps to provisioning the device using mobile application: - Download and install the mobile application \\\"Wi-Fi Provisioning\\\" from Android play store. - Start PIC32MZW1 device in AP mode (Configure Wi-Fi Service \\\"Device Mode\\\" as \\\"AP\\\"). - Using mobile Wi-Fi setting, make a Wi-Fi connection to PIC32MZW1 AP Mode. ![](/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/images/SYS_Wi-Fi_Provision_Mobile_connect.png) - Open the \\\"Wi-Fi Provisioning\\\" application. - Enter PIC32MZW1 IP address as Server IP in the mobile application. - Enter the Wi-Fi provisioning System Service configured port number. ![](/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/images/SYS_Wi-Fi_Provision_Mobile_app_home.png) - SCAN near by HOMEAP and select the desired HOMEAP. - Enter the password. ![](/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/images/SYS_Wi-Fi_Provision_Mobile_app_scan_connect.png) - User can manually add provisioning information using \\\"Add New Network\\\" option also. ![](/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/images/SYS_Wi-Fi_Provision_Mobile_app_add_new_network.png) - After provisioning the device reboot and connect to HOMEAP. Sending the TCP data without mobile application: Using laptop or mobile phone as TCP client,user can send the TCP data in below format to provisioning the device. TCP Data Format : apply,\\,\\,\\,NULL | Parameter | Details | ---------------- | ------------------------------------- |ssid(ssid name) | SSID name |Auth (security type) | 1- OPEN MODE 2 - WPA2 Mode |psk name(password) | Password/passphrase ||| ## HTTP ### Webpage using HTTP MHC configuration menu for HTTP (unsecure): ![](/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/images/SYS_Wi-Fi_Provision_MHC_diagram_2.png) - Enable Check box \\\"HTTP\\\" to include Wi-Fi provisioning using webpage. - press \\\"Yes\\\"for components inclusion pop-up. - When user enable \\\"HTTP\\\" checkbox only, defualt wi-f provising method enable with port number 80. - After making configuration changes, generate the code. - Compile the project and load the image into device. Follow below steps to provisioning the device using HTTP: - Start PIC32MZW1 device in AP mode (Configure Wi-Fi Service \\\"Device Mode\\\" as \\\"AP\\\"). - Connect Laptop or mobile phone to PIC32MZW1 AP device. - Open the browser and enter the PIC32MZW1 AP IP address(example: http://192.168.1.1/). ![](/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/images/SYS_Wi-Fi_Provision_HTTP_HOME.png) - Goto \\\"Network Configuratio\\\" page. - Update the Configuration details and click on \\\"Apply Wi-Fi Configuration\\\" ![](/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/images/SYS_Wi-Fi_Provision_HTTP_Networkconfig.png) - Device will reboot and apply configuration in the device. HTTP functionality is also supported in station(STA) mode. ### Webpage using HTTPNET (Un-Secure) MHC configuration menu for HTTPNET(Unsecure): ![](/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/images/SYS_Wi-Fi_Provision_MHC_diagram_3.png) Follow below steps to enable to HTTPNET unsecure, - Enable Check box \\\"Enable HTTPNET\\\". - Configure \\\"Server port\\\".User can configure any valid port number. - Enable Check box \\\"HTTP\\\" and press \\\"Yes\\\"for components inclusion pop-up. - After making configuration changes, generate the code. - Compile the project and load the image into device. Follow below steps to provisioning the device using HTTP: - Start PIC32MZW1 device in AP mode (Configure Wi-Fi Service \\\"Device Mode\\\" as \\\"AP\\\"). - Connect Laptop or mobile phone to PIC32MZW1 AP device. - Open the browser and enter the PIC32MZW1 AP IP address with port number(example: http://192.168.1.1:401/). ![](/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/images/SYS_Wi-Fi_Provision_HTTP_HOME.png) - Goto \\\"Network Configuratio\\\" page. - Update the Configuration details and click on \\\"Apply Wi-Fi Configuration\\\" ![](/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/images/SYS_Wi-Fi_Provision_HTTP_Networkconfig.png) - Device will reboot and apply configuration in the device. ### Webpage using HTTPNET (Secure) MHC configuration menu for HTTPNET(secure): ![](/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/images/SYS_Wi-Fi_Provision_MHC_diagram_4.png) Follow below steps to enable HTTPNET secure, - Enable Check box \\\"Enable HTTPNET\\\". - Enable check box \\\"Enable Secure Connection with HTTPNET\\\" - Configure \\\"Server port\\\".User can configure any valid port number. - Enable Check box \\\"HTTP\\\" and press \\\"Yes\\\"for components inclusion pop-up. - After making configuration changes, generate the code. - Compile the project and load the image into device. Follow below steps to provisioning the device using HTTP: - Start PIC32MZW1 device in AP mode (Configure Wi-Fi Service \\\"Device Mode\\\" as \\\"AP\\\"). - Connect Laptop or mobile phone to PIC32MZW1 AP device. - Open the browser and enter the PIC32MZW1 AP IP address with port number(example: https://192.168.1.1:443/). ![](/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/images/SYS_Wi-Fi_Provision_HTTP_HOME.png) - Goto \\\"Network Configuratio\\\" page. - Update the Configuration details and click on \\\"Apply Wi-Fi Configuration\\\" ![](/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/images/SYS_Wi-Fi_Provision_HTTP_Networkconfig.png) - Device will reboot and apply configuration in the device. # How The Library Works The Wi-Fi Provisioning System Service implemented Command line,HTTP and Socket mode Wi-Fi Provisioning method.Wi-Fi Provisioning System Service by default enabled along Wi-Fi System Service.User can make configuration changes as per their application requirement ## Execution Flow The following diagram shows how the Command line and Socket mode Wi-Fi Provisioning methods are enabled. ![](/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/images/SYS_Wi-Fi_Provision_Seq.png) ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/usage.html",
    "relUrl": "/system/wifiprov/docs/usage.html"
  },"75": {
    "doc": "Harmony 3 PIC32MZW1 wireless system services package",
    "title": "Harmony 3 PIC32MZW1 wireless system services package",
    "content": "![Microchip logo](https://raw.githubusercontent.com/wiki/Microchip-MPLAB-Harmony/Microchip-MPLAB-Harmony.github.io/images/microchip_logo.png) ![Harmony logo small](https://raw.githubusercontent.com/wiki/Microchip-MPLAB-Harmony/Microchip-MPLAB-Harmony.github.io/images/microchip_mplab_harmony_logo_small.png) # MPLAB® Harmony 3 PIC32MZW1/WFI32 wireless system services MPLAB® Harmony 3 is an extension of the MPLAB® ecosystem for creating embedded firmware solutions for Microchip 32-bit SAM and PIC® microcontroller and microprocessor devices. Refer to the following links for more information. - [Microchip 32-bit MCUs](https://www.microchip.com/design-centers/32-bit) - [Microchip 32-bit MPUs](https://www.microchip.com/design-centers/32-bit-mpus) - [Microchip MPLAB X IDE](https://www.microchip.com/mplab/mplab-x-ide) - [Microchip MPLAB® Harmony](https://www.microchip.com/mplab/mplab-harmony) - [Microchip MPLAB® Harmony Pages](https://microchip-mplab-harmony.github.io/) This repository contains the MPLAB® Harmony 3 Wireless wireless system services for the PIc32MZW1/WFI32 family of devices. Wireless system services absstracts out the complexities of a networked system design and simplifies development using PIC32MZW1 and WFI32. Refer to the following links for more information about each system service. * [Wi-Fi Service](/wireless_system_pic32mzw1_wfi32e01/system/wifi/docs/readme.html) * [Wi-Fi provisioning Service](/wireless_system_pic32mzw1_wfi32e01/system/wifiprov/docs/readme.html) * [Net Service](/wireless_system_pic32mzw1_wfi32e01/system/net/docs/readme.html) * [Mqtt Service](/wireless_system_pic32mzw1_wfi32e01/system/mqtt/docs/readme.html) * [App Debug Service](/wireless_system_pic32mzw1_wfi32e01/system/appdebug/docs/readme.html) Refer to the following links for release notes, training materials, and interface reference information. - [Release Notes](/wireless_system_pic32mzw1_wfi32e01/release_notes.html) - [MPLAB® Harmony License](/wireless_system_pic32mzw1_wfi32e01/mplab_harmony_license.html) - [MPLAB® Harmony 3 Wireless API Help](https://microchip-mplab-harmony.github.io/wireless) - [PIc32MZW1 / WFI32 Software Users Guide](https://ww1.microchip.com/downloads/en/DeviceDoc/PIC32MZ_W1_Software_User_Guide.pdf) ## Contents Summary | Folder | Description | --- | --- | system | Contains Wireless service code and configuration files. | docs | Contains documentation in html format for offline viewing (to be used only after cloning this repository onto a local machine). Use [github pages](https://microchip-mplab-harmony.github.io/wireless_system_pic32mzw1_wfi32e01/) of this repository for viewing it online. | ## Code Examples Wireless subsystem code examples for PIC32MZW1/WFI32 can be found in the [wireless_apps_pic32mzw1_wfi32e01](https://github.com/Microchip-MPLAB-Harmony/wireless_apps_pic32mzw1_wfi32e01) repo. ____ [![License](https://img.shields.io/badge/license-Harmony%20license-orange.svg)](https://github.com/Microchip-MPLAB-Harmony/wireless_system_pic32mzw1_wfi32e01/blob/master/mplab_harmony_license.md) [![Latest release](https://img.shields.io/github/release/Microchip-MPLAB-Harmony/wireless_system_pic32mzw1_wfi32e01.svg)](https://github.com/Microchip-MPLAB-Harmony/wireless_system_pic32mzw1_wfi32e01/releases/latest) [![Latest release date](https://img.shields.io/github/release-date/Microchip-MPLAB-Harmony/wireless_system_pic32mzw1_wfi32e01.svg)](https://github.com/Microchip-MPLAB-Harmony/wireless_system_pic32mzw1_wfi32e01/releases/latest) [![Commit activity](https://img.shields.io/github/commit-activity/y/Microchip-MPLAB-Harmony/wireless_system_pic32mzw1_wfi32e01.svg)](https://github.com/Microchip-MPLAB-Harmony/wireless_system_pic32mzw1_wfi32e01/graphs/commit-activity) [![Contributors](https://img.shields.io/github/contributors-anon/Microchip-MPLAB-Harmony/wireless_system_pic32mzw1_wfi32e01.svg)]() ____ [![Follow us on Youtube](https://img.shields.io/badge/Youtube-Follow%20us%20on%20Youtube-red.svg)](https://www.youtube.com/user/MicrochipTechnology) [![Follow us on LinkedIn](https://img.shields.io/badge/LinkedIn-Follow%20us%20on%20LinkedIn-blue.svg)](https://www.linkedin.com/company/microchip-technology) [![Follow us on Facebook](https://img.shields.io/badge/Facebook-Follow%20us%20on%20Facebook-blue.svg)](https://www.facebook.com/microchiptechnology/) [![Follow us on Twitter](https://img.shields.io/twitter/follow/MicrochipTech.svg?style=social)](https://twitter.com/MicrochipTech) [![](https://img.shields.io/github/stars/Microchip-MPLAB-Harmony/wireless_system_pic32mzw1_wfi32e01.svg?style=social)]() [![](https://img.shields.io/github/watchers/Microchip-MPLAB-Harmony/wireless_system_pic32mzw1_wfi32e01.svg?style=social)]() ",
    "url": "http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/",
    "relUrl": "/"
  }
}
`;
var data_for_search

var repo_name = "wireless_system_pic32mzw1_wfi32e01";
var doc_folder_name = "docs";
var localhost_path = "http://localhost:4000/";
var home_index_string = "Wireless System Services";

(function (jtd, undefined) {

// Event handling

jtd.addEvent = function(el, type, handler) {
  if (el.attachEvent) el.attachEvent('on'+type, handler); else el.addEventListener(type, handler);
}
jtd.removeEvent = function(el, type, handler) {
  if (el.detachEvent) el.detachEvent('on'+type, handler); else el.removeEventListener(type, handler);
}
jtd.onReady = function(ready) {
  // in case the document is already rendered
  if (document.readyState!='loading') ready();
  // modern browsers
  else if (document.addEventListener) document.addEventListener('DOMContentLoaded', ready);
  // IE <= 8
  else document.attachEvent('onreadystatechange', function(){
      if (document.readyState=='complete') ready();
  });
}

// Show/hide mobile menu

function initNav() {
  jtd.addEvent(document, 'click', function(e){
    var target = e.target;
    while (target && !(target.classList && target.classList.contains('nav-list-expander'))) {
      target = target.parentNode;
    }
    if (target) {
      e.preventDefault();
      target.parentNode.classList.toggle('active');
    }
  });

  const siteNav = document.getElementById('site-nav');
  const mainHeader = document.getElementById('main-header');
  const menuButton = document.getElementById('menu-button');

  jtd.addEvent(menuButton, 'click', function(e){
    e.preventDefault();

    if (menuButton.classList.toggle('nav-open')) {
      siteNav.classList.add('nav-open');
      mainHeader.classList.add('nav-open');
    } else {
      siteNav.classList.remove('nav-open');
      mainHeader.classList.remove('nav-open');
    }
  });
}
// Site search

function initSearch() {

    data_for_search = JSON.parse(myVariable);
    lunr.tokenizer.separator = /[\s/]+/

    var index = lunr(function () {
        this.ref('id');
        this.field('title', { boost: 200 });
        this.field('content', { boost: 2 });
        this.field('url');
        this.metadataWhitelist = ['position']

        var location = document.location.pathname;
        var path = location.substring(0, location.lastIndexOf("/"));
        var directoryName = path.substring(path.lastIndexOf("/")+1);

        var cur_path_from_repo = path.substring(path.lastIndexOf(repo_name));

        // Decrement depth by 2 as HTML files are placed in repo_name/doc_folder_name
        var cur_depth_from_doc_folder = (cur_path_from_repo.split("/").length - 2);

        var rel_path_to_doc_folder = "";

        if (cur_depth_from_doc_folder == 0) {
            rel_path_to_doc_folder = "./"
        }
        else {
            for (var i = 0; i < cur_depth_from_doc_folder; i++)
            {
                rel_path_to_doc_folder = rel_path_to_doc_folder + "../"
            }
        }

        for (var i in data_for_search) {

            data_for_search[i].url = data_for_search[i].url.replace(localhost_path + repo_name, rel_path_to_doc_folder);

            if (data_for_search[i].title == home_index_string)
            {
                data_for_search[i].url = data_for_search[i].url + "index.html"
            }

            this.add({
                id: i,
                title: data_for_search[i].title,
                content: data_for_search[i].content,
                url: data_for_search[i].url
            });
        }
    });

    searchLoaded(index, data_for_search);
}function searchLoaded(index, docs) {
  var index = index;
  var docs = docs;
  var searchInput = document.getElementById('search-input');
  var searchResults = document.getElementById('search-results');
  var mainHeader = document.getElementById('main-header');
  var currentInput;
  var currentSearchIndex = 0;

  function showSearch() {
    document.documentElement.classList.add('search-active');
  }

  function hideSearch() {
    document.documentElement.classList.remove('search-active');
  }

  function update() {
    currentSearchIndex++;

    var input = searchInput.value;
    if (input === '') {
      hideSearch();
    } else {
      showSearch();
      // scroll search input into view, workaround for iOS Safari
      window.scroll(0, -1);
      setTimeout(function(){ window.scroll(0, 0); }, 0);
    }
    if (input === currentInput) {
      return;
    }
    currentInput = input;
    searchResults.innerHTML = '';
    if (input === '') {
      return;
    }

    var results = index.query(function (query) {
      var tokens = lunr.tokenizer(input)
      query.term(tokens, {
        boost: 10
      });
      query.term(tokens, {
        wildcard: lunr.Query.wildcard.TRAILING
      });
    });

    if ((results.length == 0) && (input.length > 2)) {
      var tokens = lunr.tokenizer(input).filter(function(token, i) {
        return token.str.length < 20;
      })
      if (tokens.length > 0) {
        results = index.query(function (query) {
          query.term(tokens, {
            editDistance: Math.round(Math.sqrt(input.length / 2 - 1))
          });
        });
      }
    }

    if (results.length == 0) {
      var noResultsDiv = document.createElement('div');
      noResultsDiv.classList.add('search-no-result');
      noResultsDiv.innerText = 'No results found';
      searchResults.appendChild(noResultsDiv);

    } else {
      var resultsList = document.createElement('ul');
      resultsList.classList.add('search-results-list');
      searchResults.appendChild(resultsList);

      addResults(resultsList, results, 0, 10, 100, currentSearchIndex);
    }

    function addResults(resultsList, results, start, batchSize, batchMillis, searchIndex) {
      if (searchIndex != currentSearchIndex) {
        return;
      }
      for (var i = start; i < (start + batchSize); i++) {
        if (i == results.length) {
          return;
        }
        addResult(resultsList, results[i]);
      }
      setTimeout(function() {
        addResults(resultsList, results, start + batchSize, batchSize, batchMillis, searchIndex);
      }, batchMillis);
    }

    function addResult(resultsList, result) {
      var doc = docs[result.ref];

      var resultsListItem = document.createElement('li');
      resultsListItem.classList.add('search-results-list-item');
      resultsList.appendChild(resultsListItem);

      var resultLink = document.createElement('a');
      resultLink.classList.add('search-result');
      resultLink.setAttribute('href', doc.url);
      resultsListItem.appendChild(resultLink);

      var resultTitle = document.createElement('div');
      resultTitle.classList.add('search-result-title');
      resultLink.appendChild(resultTitle);

      var resultDoc = document.createElement('div');
      resultDoc.classList.add('search-result-doc');
      resultDoc.innerHTML = '<svg viewBox="0 0 24 24" class="search-result-icon"><use xlink:href="#svg-doc"></use></svg>';
      resultTitle.appendChild(resultDoc);

      var resultDocTitle = document.createElement('div');
      resultDocTitle.classList.add('search-result-doc-title');
      resultDocTitle.innerHTML = doc.doc;
      resultDoc.appendChild(resultDocTitle);
      var resultDocOrSection = resultDocTitle;

      if (doc.doc != doc.title) {
        resultDoc.classList.add('search-result-doc-parent');
        var resultSection = document.createElement('div');
        resultSection.classList.add('search-result-section');
        resultSection.innerHTML = doc.title;
        resultTitle.appendChild(resultSection);
        resultDocOrSection = resultSection;
      }

      var metadata = result.matchData.metadata;
      var titlePositions = [];
      var contentPositions = [];
      for (var j in metadata) {
        var meta = metadata[j];
        if (meta.title) {
          var positions = meta.title.position;
          for (var k in positions) {
            titlePositions.push(positions[k]);
          }
        }
        if (meta.content) {
          var positions = meta.content.position;
          for (var k in positions) {
            var position = positions[k];
            var previewStart = position[0];
            var previewEnd = position[0] + position[1];
            var ellipsesBefore = true;
            var ellipsesAfter = true;
            for (var k = 0; k < 5; k++) {
              var nextSpace = doc.content.lastIndexOf(' ', previewStart - 2);
              var nextDot = doc.content.lastIndexOf('. ', previewStart - 2);
              if ((nextDot >= 0) && (nextDot > nextSpace)) {
                previewStart = nextDot + 1;
                ellipsesBefore = false;
                break;
              }
              if (nextSpace < 0) {
                previewStart = 0;
                ellipsesBefore = false;
                break;
              }
              previewStart = nextSpace + 1;
            }
            for (var k = 0; k < 10; k++) {
              var nextSpace = doc.content.indexOf(' ', previewEnd + 1);
              var nextDot = doc.content.indexOf('. ', previewEnd + 1);
              if ((nextDot >= 0) && (nextDot < nextSpace)) {
                previewEnd = nextDot;
                ellipsesAfter = false;
                break;
              }
              if (nextSpace < 0) {
                previewEnd = doc.content.length;
                ellipsesAfter = false;
                break;
              }
              previewEnd = nextSpace;
            }
            contentPositions.push({
              highlight: position,
              previewStart: previewStart, previewEnd: previewEnd,
              ellipsesBefore: ellipsesBefore, ellipsesAfter: ellipsesAfter
            });
          }
        }
      }

      if (titlePositions.length > 0) {
        titlePositions.sort(function(p1, p2){ return p1[0] - p2[0] });
        resultDocOrSection.innerHTML = '';
        addHighlightedText(resultDocOrSection, doc.title, 0, doc.title.length, titlePositions);
      }

      if (contentPositions.length > 0) {
        contentPositions.sort(function(p1, p2){ return p1.highlight[0] - p2.highlight[0] });
        var contentPosition = contentPositions[0];
        var previewPosition = {
          highlight: [contentPosition.highlight],
          previewStart: contentPosition.previewStart, previewEnd: contentPosition.previewEnd,
          ellipsesBefore: contentPosition.ellipsesBefore, ellipsesAfter: contentPosition.ellipsesAfter
        };
        var previewPositions = [previewPosition];
        for (var j = 1; j < contentPositions.length; j++) {
          contentPosition = contentPositions[j];
          if (previewPosition.previewEnd < contentPosition.previewStart) {
            previewPosition = {
              highlight: [contentPosition.highlight],
              previewStart: contentPosition.previewStart, previewEnd: contentPosition.previewEnd,
              ellipsesBefore: contentPosition.ellipsesBefore, ellipsesAfter: contentPosition.ellipsesAfter
            }
            previewPositions.push(previewPosition);
          } else {
            previewPosition.highlight.push(contentPosition.highlight);
            previewPosition.previewEnd = contentPosition.previewEnd;
            previewPosition.ellipsesAfter = contentPosition.ellipsesAfter;
          }
        }

        var resultPreviews = document.createElement('div');
        resultPreviews.classList.add('search-result-previews');
        resultLink.appendChild(resultPreviews);

        var content = doc.content;
        for (var j = 0; j < Math.min(previewPositions.length, 3); j++) {
          var position = previewPositions[j];

          var resultPreview = document.createElement('div');
          resultPreview.classList.add('search-result-preview');
          resultPreviews.appendChild(resultPreview);

          if (position.ellipsesBefore) {
            resultPreview.appendChild(document.createTextNode('... '));
          }
          addHighlightedText(resultPreview, content, position.previewStart, position.previewEnd, position.highlight);
          if (position.ellipsesAfter) {
            resultPreview.appendChild(document.createTextNode(' ...'));
          }
        }
      }
      var resultRelUrl = document.createElement('span');
      resultRelUrl.classList.add('search-result-rel-url');
      resultRelUrl.innerText = doc.relUrl;
      resultTitle.appendChild(resultRelUrl);
    }

    function addHighlightedText(parent, text, start, end, positions) {
      var index = start;
      for (var i in positions) {
        var position = positions[i];
        var span = document.createElement('span');
        span.innerHTML = text.substring(index, position[0]);
        parent.appendChild(span);
        index = position[0] + position[1];
        var highlight = document.createElement('span');
        highlight.classList.add('search-result-highlight');
        highlight.innerHTML = text.substring(position[0], index);
        parent.appendChild(highlight);
      }
      var span = document.createElement('span');
      span.innerHTML = text.substring(index, end);
      parent.appendChild(span);
    }
  }

  jtd.addEvent(searchInput, 'focus', function(){
    setTimeout(update, 0);
  });

  jtd.addEvent(searchInput, 'keyup', function(e){
    switch (e.keyCode) {
      case 27: // When esc key is pressed, hide the results and clear the field
        searchInput.value = '';
        break;
      case 38: // arrow up
      case 40: // arrow down
      case 13: // enter
        e.preventDefault();
        return;
    }
    update();
  });

  jtd.addEvent(searchInput, 'keydown', function(e){
    switch (e.keyCode) {
      case 38: // arrow up
        e.preventDefault();
        var active = document.querySelector('.search-result.active');
        if (active) {
          active.classList.remove('active');
          if (active.parentElement.previousSibling) {
            var previous = active.parentElement.previousSibling.querySelector('.search-result');
            previous.classList.add('active');
          }
        }
        return;
      case 40: // arrow down
        e.preventDefault();
        var active = document.querySelector('.search-result.active');
        if (active) {
          if (active.parentElement.nextSibling) {
            var next = active.parentElement.nextSibling.querySelector('.search-result');
            active.classList.remove('active');
            next.classList.add('active');
          }
        } else {
          var next = document.querySelector('.search-result');
          if (next) {
            next.classList.add('active');
          }
        }
        return;
      case 13: // enter
        e.preventDefault();
        var active = document.querySelector('.search-result.active');
        if (active) {
          active.click();
        } else {
          var first = document.querySelector('.search-result');
          if (first) {
            first.click();
          }
        }
        return;
    }
  });

  jtd.addEvent(document, 'click', function(e){
    if (e.target != searchInput) {
      hideSearch();
    }
  });
}

// Switch theme

jtd.getTheme = function() {
  var cssFileHref = document.querySelector('[rel="stylesheet"]').getAttribute('href');
  return cssFileHref.substring(cssFileHref.lastIndexOf('-') + 1, cssFileHref.length - 4);
}

jtd.setTheme = function(theme) {
  var cssFile = document.querySelector('[rel="stylesheet"]');
  cssFile.setAttribute('href', 'http://localhost:4000/wireless_system_pic32mzw1_wfi32e01/assets/css/just-the-docs-' + theme + '.css');
}

// Document ready

jtd.onReady(function(){
  initNav();
  initSearch();
});

})(window.jtd = window.jtd || {});

