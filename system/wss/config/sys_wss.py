# coding: utf-8
"""*****************************************************************************
Copyright (C) 2020 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*****************************************************************************"""

################################################################################
#### Global Variables ####
################################################################################
global wss_helpkeyword

wss_helpkeyword = "mcc_h3_pic32mzw1_wss_system_service_configurations"
################################################################################
#### Business Logic ####
################################################################################

################################################################################
#### Component ####
################################################################################
def instantiateComponent(wssComponent):
    global wss_helpkeyword
    wssMode = wssComponent.createComboSymbol("SYS_WSS_MODE", None, ["SYS_WSS_CLIENT", "SYS_WSS_SERVER"])
    wssMode.setLabel("WebSocket Service Mode")
    wssMode.setHelp(wss_helpkeyword)
    wssMode.setDefaultValue("SYS_WSS_SERVER")
    wssMode.setDependencies(wssSetMode, ["SYS_WSS_MODE"])
    
    wssPort = wssComponent.createIntegerSymbol("SYS_WSS_PORT", None)
    wssPort.setLabel("WebSocket Server Port")
    wssPort.setHelp(wss_helpkeyword)
    wssPort.setMin(1)
    wssPort.setMax(65535)
    wssPort.setDefaultValue(8000)
    wssPort.setDependencies(wssSetPort, ["SYS_WSS_PORT"])
    
    wssServerIP = wssComponent.createStringSymbol("SYS_WSS_SERVER_IP", None)
    wssServerIP.setLabel("WebSocket Server IP")
    wssServerIP.setHelp(wss_helpkeyword)
    wssServerIP.setVisible(False)
    wssServerIP.setDescription("IP address of the websocket server")
    wssServerIP.setDefaultValue("192.168.1.1")
    wssServerIP.setDependencies(wssSetIP, ["SYS_WSS_SERVER_IP"])
    wssServerIP.setDependencies(wssSetClientMenuVisible, ["SYS_WSS_MODE"])
    
    wssHostName = wssComponent.createStringSymbol("SYS_WSS_HOST_NAME", None)
    wssHostName.setLabel("Host Name/ URL")
    wssHostName.setHelp(wss_helpkeyword)
    wssHostName.setVisible(False)
    wssHostName.setDescription("Host Name/ URL")
    wssHostName.setDefaultValue("ws://192.168.1.1:8000")
    wssHostName.setDependencies(wssSetClientMenuVisible, ["SYS_WSS_MODE"])
    
    
    # wssIntf = wssComponent.createKeyValueSetSymbol("SYS_WSS_INTF", None)
    # wssIntf.setLabel("Supported Interface for websocket client")
    # wssIntf.setHelp(wss_helpkeyword)
    # wssIntf.addKey("WIFI", "0", "Websocket connection over WiFi")
    # wssIntf.addKey("ETHERNET", "1", "Websocket connection over Ethernet")
    # wssIntf.setDisplayMode("Key")
    # wssIntf.setOutputMode("Key")
    # wssIntf.setDefaultValue(0)
    # #wssIntf.setDependencies(wssSetIntf, ["SYS_WSS_INTF"])
    
    wssIntf = wssComponent.createComboSymbol("SYS_WSS_INTF", None, ["SYS_WSS_WIFI", "SYS_WSS_ETHERNET"])
    wssIntf.setLabel("Interface supported")
    wssIntf.setHelp(wss_helpkeyword)
    wssIntf.setDefaultValue("SYS_WSS_WIFI")
    wssIntf.setDependencies(wssSetIntf, ["SYS_WSS_INTF"])

    wssEnableTls = wssComponent.createBooleanSymbol("SYS_WSS_ENABLE_TLS", None)
    wssEnableTls.setLabel("Enable TLS")
    wssEnableTls.setHelp(wss_helpkeyword)
    wssEnableTls.setDefaultValue(False)
    wssEnableTls.setDependencies(wssSetTLS, ["SYS_WSS_ENABLE_TLS"])

    wssDebugEnable = wssComponent.createBooleanSymbol("SYS_WSS_ENABLE_DEBUG", None)
    wssDebugEnable.setLabel("Debug")
    wssDebugEnable.setHelp(wss_helpkeyword)
    wssDebugEnable.setDescription("WSS Debug - Logs ")
    wssDebugEnable.setDefaultValue(False)
    
    wssAppTemplate = wssComponent.createBooleanSymbol("SYS_WSS_GEN_APP_TEMPLATE", None)
    wssAppTemplate.setLabel("Generate Application Template")
    wssAppTemplate.setHelp(wss_helpkeyword)
    wssAppTemplate.setDefaultValue(True)

    # Advanced configurations
    wssADVMenu = wssComponent.createMenuSymbol('WSS_ADVANCED', None)
    wssADVMenu.setLabel("Advanced Configuration")
    wssADVMenu.setHelp(wss_helpkeyword)
    wssADVMenu.setDescription("Advanced Configuration")
    wssADVMenu.setVisible(True)

    wssRxBuffLen = wssComponent.createIntegerSymbol("SYS_WSS_MAX_RX_BUFFER", wssADVMenu)
    wssRxBuffLen.setLabel("Max Rx buffer length")
    wssRxBuffLen.setHelp(wss_helpkeyword)
    wssRxBuffLen.setMin(256)
    wssRxBuffLen.setMax(65535)
    wssRxBuffLen.setDefaultValue(True)
    wssRxBuffLen.setDefaultValue(1400)
    
    wssNumClients = wssComponent.createIntegerSymbol("SYS_WSS_MAX_NUM_CLIENTS", wssADVMenu)
    wssNumClients.setLabel("Max number of clients")
    wssNumClients.setHelp(wss_helpkeyword)
    wssNumClients.setMin(1)
    wssNumClients.setMax(4)
    wssNumClients.setDefaultValue(2)
    wssNumClients.setDependencies(wssSetMaxSocket, ["SYS_WSS_MAX_NUM_CLIENTS"])
    wssNumClients.setDependencies(wssSetServerMenuVisible, ["SYS_WSS_MODE"])

    wssNumClients = wssComponent.createIntegerSymbol("SYS_WSS_CLIENT_TIMEOUT", wssADVMenu)
    wssNumClients.setLabel("Client timeout in ms")
    wssNumClients.setHelp(wss_helpkeyword)
    wssNumClients.setMin(100)
    wssNumClients.setMax(65535)
    wssNumClients.setDefaultValue(30000)

    wssStartAtBoot = wssComponent.createBooleanSymbol("SYS_WSS_START_AT_BOOT", wssADVMenu)
    wssStartAtBoot.setLabel("Start at boot?")
    wssStartAtBoot.setHelp(wss_helpkeyword)
    wssStartAtBoot.setDefaultValue(True)
    wssStartAtBoot.setDependencies(wssSetTLS, ["SYS_WSS_START_AT_BOOT"])

#    wssRxQueueLen = wssComponent.createIntegerSymbol("SYS_WSS_RX_QUEUE_LEN", wssADVMenu)
#    wssRxQueueLen.setLabel("Rx Queue length")
#    wssRxQueueLen.setMin(0)
#    wssRxQueueLen.setMax(65535)
#    wssRxQueueLen.setDefaultValue(True)
#    wssRxQueueLen.setDefaultValue(4)
    
    # RTOS Configuration
    sysWssRTOSMenu = wssComponent.createMenuSymbol('WSS_RTOS', None)
    sysWssRTOSMenu.setLabel("RTOS Configuration")
    sysWssRTOSMenu.setHelp(wss_helpkeyword)
    sysWssRTOSMenu.setDescription("RTOS Configuration")
    sysWssRTOSMenu.setVisible(False)
    sysWssRTOSMenu.setDependencies(sysWssShowRTOSMenu, ["HarmonyCore.SELECT_RTOS"])
    
    wssTaskDelay = wssComponent.createIntegerSymbol("SYS_WSS_RTOS_TASK_DELAY", sysWssRTOSMenu)
    wssTaskDelay.setLabel("RTOS Task Delay (ms)")
    wssTaskDelay.setHelp(wss_helpkeyword)
    wssTaskDelay.setMin(0)
    wssTaskDelay.setMax(100)
    wssTaskDelay.setDefaultValue(1)

    wssRtosStackSize = wssComponent.createIntegerSymbol("SYS_WSS_RTOS_STACK_SIZE", sysWssRTOSMenu)
    wssRtosStackSize.setLabel("RTOS Task Stack Size")
    wssRtosStackSize.setHelp(wss_helpkeyword)
    wssRtosStackSize.setDefaultValue(4096)

    wssRtosPrio = wssComponent.createIntegerSymbol("SYS_WSS_RTOS_TASK_PRIORITY", sysWssRTOSMenu)
    wssRtosPrio.setLabel("RTOS Task Priority")
    wssRtosPrio.setHelp(wss_helpkeyword)
    wssRtosPrio.setDefaultValue(1)


    ############################################################################
    #### Code Generation ####
    ############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    wssHeaderFile = wssComponent.createFileSymbol("SYS_WSS_HEADER", None)
    wssHeaderFile.setSourcePath("../wireless_system_pic32mzw1_wfi32e01/system/wss/src/sys_wss.h")
    wssHeaderFile.setOutputName("sys_wss.h")
    wssHeaderFile.setDestPath("system/wss/")
    wssHeaderFile.setProjectPath("config/" + configName + "/system/wss/")
    wssHeaderFile.setType("HEADER")
    wssHeaderFile.setOverwrite(True)

    wssSourceFile = wssComponent.createFileSymbol("SYS_WSS_SOURCE", None)
    wssSourceFile.setSourcePath("../wireless_system_pic32mzw1_wfi32e01/system/wss/src/sys_wss.c")
    wssSourceFile.setOutputName("sys_wss.c")
    wssSourceFile.setDestPath("system/wss/src")
    wssSourceFile.setProjectPath("config/" + configName + "/system/wss/")
    wssSourceFile.setType("SOURCE")
    wssSourceFile.setOverwrite(True)

    wssHeaderFile = wssComponent.createFileSymbol("SYS_WSS_APP_HEADER", None)
    wssHeaderFile.setSourcePath("system/wss/src/app_wss.h")
    wssHeaderFile.setOutputName("app_wss.h")
    wssHeaderFile.setDestPath("system/wss/")
    wssHeaderFile.setProjectPath("config/" + configName)
    wssHeaderFile.setType("HEADER")
    wssHeaderFile.setEnabled(True)

    wssSourceFile = wssComponent.createFileSymbol("SYS_WSS_APP_SOURCE", None)
    wssSourceFile.setSourcePath("system/wss/src/app_wss.c")
    wssSourceFile.setOutputName("app_wss.c")
    wssSourceFile.setDestPath("system/wss/src/")
    wssSourceFile.setProjectPath("config/" + configName)
    wssSourceFile.setType("SOURCE")
    wssSourceFile.setOverwrite(True)

    wssSystemDefFile = wssComponent.createFileSymbol("SYS_WSS_DEF", None)
    wssSystemDefFile.setType("STRING")
    wssSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    wssSystemDefFile.setSourcePath("../wireless_system_pic32mzw1_wfi32e01/system/wss/templates/system/system_definitions.h.ftl")
    wssSystemDefFile.setMarkup(True)	

    wssSystemConfigFile = wssComponent.createFileSymbol("SYS_WSS_SYS_CONFIG", None)
    wssSystemConfigFile.setType("STRING")
    wssSystemConfigFile.setOutputName("core.LIST_SYSTEM_CONFIG_H_SYSTEM_SERVICE_CONFIGURATION")
    wssSystemConfigFile.setSourcePath("../wireless_system_pic32mzw1_wfi32e01/system/wss/templates/system/system_config.h.ftl")
    wssSystemConfigFile.setMarkup(True)

    wssSystemInitFile = wssComponent.createFileSymbol("SYS_WSS_INIT", None)
    wssSystemInitFile.setType("STRING")
    wssSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_INITIALIZE_SYSTEM_SERVICES")
    wssSystemInitFile.setSourcePath("../wireless_system_pic32mzw1_wfi32e01/system/wss/templates/system/system_initialize.c.ftl")
    wssSystemInitFile.setMarkup(True)

    wssSystemObjectFile = wssComponent.createFileSymbol("SYS_WSS_OBJ", None)
    wssSystemObjectFile.setType("STRING")
    wssSystemObjectFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_OBJECTS")
    wssSystemObjectFile.setSourcePath("../wireless_system_pic32mzw1_wfi32e01/system/wss/templates/system/system_definitions_objects.h.ftl")
    wssSystemObjectFile.setMarkup(True)

    wssSourceFile = wssComponent.createFileSymbol("WSS_SYS_RTOS_TASK", None)
    wssSourceFile.setType("STRING")
    wssSourceFile.setOutputName("core.LIST_SYSTEM_RTOS_TASKS_C_DEFINITIONS")
    wssSourceFile.setSourcePath("system/wss/templates/system/system_rtos_tasks.c.ftl")
    wssSourceFile.setMarkup(True)

    wssSourceFile = wssComponent.createFileSymbol("OTA_SYS_TASK", None)
    wssSourceFile.setType("STRING")
    wssSourceFile.setOutputName("core.LIST_SYSTEM_TASKS_C_CALL_DRIVER_TASKS")
    wssSourceFile.setSourcePath("system/wss/templates/system/system_tasks.c.ftl")
    wssSourceFile.setMarkup(True)
############################################################################
#### Dependency ####
############################################################################
#Set symbols of other components
def setVal(component, symbol, value):
    triggerSvDict = {"Component":component,"Id":symbol, "Value":value}
    if(Database.sendMessage(component, "SET_SYMBOL", triggerSvDict) == None):
        print "Set Symbol Failure" + component + ":" + symbol + ":" + str(value)
        return False
    else:
        return True      

def finalizeComponent(netComponent):
    res = Database.activateComponents(["sysNetPic32mzw1"])
    res = Database.activateComponents(["lib_wolfcrypt"])
    if (Database.getSymbolValue("lib_wolfcrypt", "wolfcrypt_base64") == False):
        Database.setSymbolValue("lib_wolfcrypt", "wolfcrypt_base64", True)
    if (Database.getSymbolValue("lib_wolfcrypt", "wolfcrypt_sha256") == False):
        Database.setSymbolValue("lib_wolfcrypt", "wolfcrypt_sha256", True)
    if (Database.getSymbolValue("lib_wolfcrypt", "wolfcrypt_sha264_hw") == False):
        Database.setSymbolValue("lib_wolfcrypt", "wolfcrypt_sha264_hw", True)
    if ((Database.getSymbolValue("HarmonyCore", "SELECT_RTOS") != None)and (Database.getSymbolValue("HarmonyCore", "SELECT_RTOS") == "FreeRTOS")):
        setVal("net_Pres", "NET_PRES_RTOS_STACK_SIZE", 20480)
    
    
    
#Handle messages from other components
def handleMessage(messageID, args):
    retDict= {}
    if (messageID == "SET_SYMBOL"):
        print "handleMessage: Set Symbol"
        retDict= {"Return": "Success"}
        Database.setSymbolValue(args["Component"], args["Id"], args["Value"])
    else:
        retDict= {"Return": "UnImplemented Command"}
    return retDict
    
def sysWssShowRTOSMenu(symbol, event):
    if (event["value"] == None):
        symbol.setVisible(False)
    elif (event["value"] != "BareMetal"):
        symbol.setVisible(True)

def wssSetTLS(symbol, event):
    if (event["value"] == True):
        Database.setSymbolValue("sysNetPic32mzw1", "SYS_NET_ENABLE_TLS", True)
        Database.setSymbolValue("net_Pres", "NET_PRES_SUPPORT_SERVER_ENC", True)
        Database.setSymbolValue("net_Pres", "NET_PRES_BLOB_SERVER_SUPPORT", True)
    else:
        Database.setSymbolValue("sysNetPic32mzw1", "SYS_NET_ENABLE_TLS", False)
        
def wssSetMaxSocket(symbol, event):
    if (event["value"]!=None):
        Database.setSymbolValue("sysNetPic32mzw1", "SYS_NET_SUPP_NO_OF_SOCKS", event["value"])
    else:
        pass
def wssSetPort(symbol,event):
    if (event["value"]!=None):
        setVal("sysNetPic32mzw1", "SYS_NET_PORT", Database.getSymbolValue("sysWssPic32mzw1", "SYS_WSS_PORT"))
    else:
        pass
def wssSetIP(symbol,event):
    if (event["value"]!=None):
        setVal("sysNetPic32mzw1", "SYS_NET_HOST_NAME", Database.getSymbolValue("sysWssPic32mzw1", "SYS_WSS_SERVER_IP"))
    else:
        pass
def wssSetMode(symbol,event):
    if (event["value"] == "SYS_WSS_SERVER"):
        setVal("sysNetPic32mzw1", "SYS_NET_MODE", "SERVER")
 
    else:
        if (event["value"] == "SYS_WSS_CLIENT"):
            setVal("sysNetPic32mzw1", "SYS_NET_MODE", "CLIENT")
            #Database.setSymbolValue("sysWssPic32mzw1", "SYS_WSS_MAX_NUM_CLIENTS", wssADVMenu,1)
            #Database.setSymbolValue("sysNetPic32mzw1", "SYS_NET_SUPP_NO_OF_SOCKS", 1)


def wssSetIntf(symbol,event):
    if (event["value"] == "SYS_WSS_WIFI"):
        setVal("sysNetPic32mzw1", "SYS_NET_SUPP_INTF", 1)
        setVal("sysNetPic32mzw1", "SYS_NET_INTF", "WIFI")
   
    else:
        if (event["value"] == "SYS_WSS_ETHERNET"):
            setVal("sysNetPic32mzw1", "SYS_NET_SUPP_INTF", 1) 
            setVal("sysNetPic32mzw1", "SYS_NET_INTF", "ETHERNET")
           
         
def wssSetClientMenuVisible(symbol, event):
    if (event["value"] == "SYS_WSS_CLIENT"):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def wssSetServerMenuVisible(symbol, event):
    if (event["value"] == "SYS_WSS_SERVER"):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)