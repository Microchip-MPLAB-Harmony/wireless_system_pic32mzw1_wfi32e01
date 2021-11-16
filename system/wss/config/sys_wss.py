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

################################################################################
#### Business Logic ####
################################################################################

################################################################################
#### Component ####
################################################################################
def instantiateComponent(wssComponent):
    wssPort = wssComponent.createIntegerSymbol("SYS_WSS_PORT", None)
    wssPort.setLabel("Web Socket Server Server Port")
    wssPort.setMin(1)
    wssPort.setMax(65535)
    wssPort.setDefaultValue(True)
    wssPort.setDefaultValue(8000)

    wssEnableTls = wssComponent.createBooleanSymbol("SYS_WSS_ENABLE_TLS", None)
    wssEnableTls.setLabel("Enable TLS")
    wssEnableTls.setDefaultValue(False)
    wssEnableTls.setDependencies(wssSetTLS, ["SYS_WSS_ENABLE_TLS"])

    wssDebugEnable = wssComponent.createBooleanSymbol("SYS_WSS_ENABLE_DEBUG", None)
    wssDebugEnable.setLabel("Debug")
    wssDebugEnable.setDescription("WSS Debug - Logs ")
    wssDebugEnable.setDefaultValue(False)
	
    wssAppTemplate = wssComponent.createBooleanSymbol("SYS_WSS_GEN_APP_TEMPLATE", None)
    wssAppTemplate.setLabel("Generate Application Template")
    wssAppTemplate.setDefaultValue(True)

    # Advanced configurations
    wssADVMenu = wssComponent.createMenuSymbol('WSS_ADVANCED', None)
    wssADVMenu.setLabel("Advanced Configuration")
    wssADVMenu.setDescription("Advanced Configuration")
    wssADVMenu.setVisible(True)

    wssRxBuffLen = wssComponent.createIntegerSymbol("SYS_WSS_MAX_RX_BUFFER", wssADVMenu)
    wssRxBuffLen.setLabel("Max Rx buffer length")
    wssRxBuffLen.setMin(256)
    wssRxBuffLen.setMax(65535)
    wssRxBuffLen.setDefaultValue(True)
    wssRxBuffLen.setDefaultValue(1400)
    
    wssNumClients = wssComponent.createIntegerSymbol("SYS_WSS_MAX_NUM_CLIENTS", wssADVMenu)
    wssNumClients.setLabel("Max number of clients")
    wssNumClients.setMin(1)
    wssNumClients.setMax(4)
    wssNumClients.setDefaultValue(2)
    wssNumClients.setDependencies(wssSetMaxSocket, ["SYS_WSS_MAX_NUM_CLIENTS"])

    wssNumClients = wssComponent.createIntegerSymbol("SYS_WSS_CLIENT_TIMEOUT", wssADVMenu)
    wssNumClients.setLabel("Client timeout in ms")
    wssNumClients.setMin(100)
    wssNumClients.setMax(65535)
    wssNumClients.setDefaultValue(30000)

    wssStartAtBoot = wssComponent.createBooleanSymbol("SYS_WSS_START_AT_BOOT", wssADVMenu)
    wssStartAtBoot.setLabel("Start at boot?")
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
    sysWssRTOSMenu.setDescription("RTOS Configuration")
    sysWssRTOSMenu.setVisible(False)
    sysWssRTOSMenu.setDependencies(sysWssShowRTOSMenu, ["HarmonyCore.SELECT_RTOS"])
    
    wssTaskDelay = wssComponent.createIntegerSymbol("SYS_WSS_RTOS_TASK_DELAY", sysWssRTOSMenu)
    wssTaskDelay.setLabel("RTOS Task Delay (ms)")
    wssTaskDelay.setMin(0)
    wssTaskDelay.setMax(100)
    wssTaskDelay.setDefaultValue(1)

    wssRtosStackSize = wssComponent.createIntegerSymbol("SYS_WSS_RTOS_STACK_SIZE", sysWssRTOSMenu)
    wssRtosStackSize.setLabel("RTOS Task Stack Size")
    wssRtosStackSize.setDefaultValue(4096)

    wssRtosPrio = wssComponent.createIntegerSymbol("SYS_WSS_RTOS_TASK_PRIORITY", sysWssRTOSMenu)
    wssRtosPrio.setLabel("RTOS Task Priority")
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
    else:
        Database.setSymbolValue("sysNetPic32mzw1", "SYS_NET_ENABLE_TLS", False)
		
def wssSetMaxSocket(symbol, event):
    if (event["value"]!=None):
        Database.setSymbolValue("sysNetPic32mzw1", "SYS_NET_SUPP_NO_OF_SOCKS", event["value"])
    else:
        pass