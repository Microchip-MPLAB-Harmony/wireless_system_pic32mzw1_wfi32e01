######################  PIC32MZ-W1 Wireless System Services  ######################
def loadModule():
    print('Load Module: PIC32MZ-W1 Wireless System Services')

    appdebugComponent = Module.CreateComponent('sysAppDebugPic32mzw1', "App Debug Service", '/Wireless/System Services/', 'system/appdebug/config/sys_appdebug.py')
	
    sysWifiPic32mzw1Component = Module.CreateComponent('sysWifiPic32mzw1', 'WIFI SERVICE', '/Wireless/System Services/', 'system/wifi/config/sys_wifi.py')
    #sysWifiPic32mzw1Component.setDisplayType("WiFi System Service")
    
    sysWifiProvPic32mzw1Component = Module.CreateComponent('sysWifiProvPic32mzw1', 'WIFI PROVISIONING SERVICE', '/Wireless/System Services/', 'system/wifiprov/config/sys_wifiprov.py')
    #sysWifiProvPic32mzw1Component.setDisplayType("WiFi Provision System Service")
	########################## Harmony Network Net Service #################################    
    netComponent = Module.CreateComponent("sysNetPic32mzw1", "Net Service", "/Wireless/System Services/","system/net/config/sys_net.py")
    #netComponent.addCapability("libNet","net",True)    
    #netComponent.addDependency("Net_Crypto_Dependency", "TLS Provider", None, False, False)

    ############################### Third Party wolfSSL Module #####################################
    pahomqttComponent = Module.CreateComponent('lib_pahomqtt', 'Paho MQTT Library', '/Third Party Libraries/PahoMqtt/', 'config/pahomqtt.py')

    mqttComponent = Module.CreateComponent('sysMqttPic32mzw1', 'MQTT Service', '/Wireless/System Services/', 'system/mqtt/config/sys_mqtt.py')
