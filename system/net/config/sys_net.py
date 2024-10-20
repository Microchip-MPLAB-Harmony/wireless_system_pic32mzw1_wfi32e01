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
global net_helpkeyword

net_helpkeyword = "mcc_h3_pic32mzw1_net_system_service_configurations"
################################################################################
#### Business Logic ####
################################################################################

################################################################################
#### Component ####
################################################################################
def instantiateComponent(netComponent):
    global net_helpkeyword
    sysnetEnableErrMsg = netComponent.createCommentSymbol("SYS_NET_ERR", None)
    sysnetEnableErrMsg.setLabel("**Placeholder for error display")
    sysnetEnableErrMsg.setHelp(net_helpkeyword)
    sysnetEnableErrMsg.setVisible(False)

    netGenerateAppCode = netComponent.createBooleanSymbol("SYS_NET_ENABLE_APP_CODE_GENERATION", None)
    netGenerateAppCode.setLabel("Enable App Code Generation")
    netGenerateAppCode.setDescription("For Generating Application Code")
    netGenerateAppCode.setDefaultValue(True)
    netGenerateAppCode.setHelp(net_helpkeyword)
    netGenerateAppCode.setVisible(True)

    netSuppIntf = netComponent.createKeyValueSetSymbol("SYS_NET_SUPP_INTF", None)
    netSuppIntf.setLabel("Supported Interfaces")
    netSuppIntf.setHelp(net_helpkeyword)
    netSuppIntf.addKey("WIFI_ONLY", "0", "Wifi Intf Supported")
    netSuppIntf.addKey("WIFI_ETHERNET", "1", "Wifi and Ethernet Intf Supported")
    netSuppIntf.addKey("ETHERNET_ONLY", "2", "Ethernet Intf Supported")
    netSuppIntf.setDisplayMode("Key")
    netSuppIntf.setOutputMode("Key")
    netSuppIntf.setDefaultValue(0)
    netSuppIntf.setDependencies(netIntfAutoMenu, ["SYS_NET_SUPP_INTF"])

    netSuppNoOfSocks = netComponent.createIntegerSymbol("SYS_NET_SUPP_NO_OF_SOCKS", None)
    netSuppNoOfSocks.setLabel("No Of Sockets Supported")
    netSuppNoOfSocks.setHelp(net_helpkeyword)
    netSuppNoOfSocks.setMin(2)
    netSuppNoOfSocks.setMax(8)
    netSuppNoOfSocks.setDefaultValue(2)
    
    netDebugEnable = netComponent.createBooleanSymbol("SYS_NET_ENABLE_DEBUG", None)
    netDebugEnable.setLabel("Debug")
    netDebugEnable.setHelp(net_helpkeyword)
    netDebugEnable.setDescription("Debug - Logs and CLI commands")
    netDebugEnable.setDefaultValue(True)
	
    netCliCmdEnable = netComponent.createBooleanSymbol("SYS_NET_ENABLE_CLICMD", netDebugEnable)
    netCliCmdEnable.setLabel("Enable CLI Commands")
    netCliCmdEnable.setHelp(net_helpkeyword)
    netCliCmdEnable.setDefaultValue(True)

    netDebugLogEnable = netComponent.createBooleanSymbol("SYS_NET_APPDEBUG_ENABLE", netDebugEnable)
    netDebugLogEnable.setLabel("Enable Debug Logs")
    netDebugLogEnable.setHelp(net_helpkeyword)
    netDebugLogEnable.setDefaultValue(False)
    
    netDebugBasicMenu = netComponent.createMenuSymbol("SYS_NET_APPDEBUG_LEVEL_CONFIG_MENU", netDebugLogEnable)
    netDebugBasicMenu.setLabel("Debug Level Configuration")
    netDebugBasicMenu.setHelp(net_helpkeyword)
    netDebugBasicMenu.setVisible(False)
    netDebugBasicMenu.setDependencies(netDebugMenuVisible, ["SYS_NET_APPDEBUG_ENABLE"])
		
    netDebugErrLevel = netComponent.createBooleanSymbol("SYS_NET_APPDEBUG_ERR_LEVEL", netDebugBasicMenu)
    netDebugErrLevel.setLabel("Enable Error Level")
    netDebugErrLevel.setHelp(net_helpkeyword)
    netDebugErrLevel.setDefaultValue(True)
#    netDebugErrLevel.setDependencies(netDebugMenuVisible, ["SYS_NET_APPDEBUG_ENABLE"])

    netDebugDbgLevel = netComponent.createBooleanSymbol("SYS_NET_APPDEBUG_DBG_LEVEL", netDebugBasicMenu)
    netDebugDbgLevel.setLabel("Enable Debug Level")
    netDebugDbgLevel.setHelp(net_helpkeyword)
    netDebugDbgLevel.setDefaultValue(False)
#    netDebugDbgLevel.setDependencies(netDebugMenuVisible, ["SYS_NET_APPDEBUG_ENABLE"])
	
    netDebugInfoLevel = netComponent.createBooleanSymbol("SYS_NET_APPDEBUG_INFO_LEVEL", netDebugBasicMenu)
    netDebugInfoLevel.setLabel("Enable Info Level")
    netDebugInfoLevel.setHelp(net_helpkeyword)
    netDebugInfoLevel.setDefaultValue(False)
#    netDebugInfoLevel.setDependencies(netDebugMenuVisible, ["SYS_NET_APPDEBUG_ENABLE"])
	
    netDebugFuncLevel = netComponent.createBooleanSymbol("SYS_NET_APPDEBUG_FUNC_LEVEL", netDebugBasicMenu)
    netDebugFuncLevel.setLabel("Enable Function Entry/Exit Level")
    netDebugFuncLevel.setHelp(net_helpkeyword)
    netDebugFuncLevel.setDefaultValue(False)
#    netDebugFuncLevel.setDependencies(netDebugMenuVisible, ["SYS_NET_APPDEBUG_ENABLE"])
	
    netDebugFlowBasicMenu = netComponent.createMenuSymbol("SYS_NET_APPDEBUG_FLOW_CONFIG_MENU", netDebugLogEnable)
    netDebugFlowBasicMenu.setLabel("Debug Flow Configuration")
    netDebugFlowBasicMenu.setHelp(net_helpkeyword)
    netDebugFlowBasicMenu.setVisible(True)
    netDebugFlowBasicMenu.setDependencies(netDebugMenuVisible, ["SYS_NET_APPDEBUG_ENABLE"])
		
    netDebugCfgFlow = netComponent.createBooleanSymbol("SYS_NET_APPDEBUG_CFG_FLOW", netDebugFlowBasicMenu)
    netDebugCfgFlow.setLabel("Enable NET Cfg Flow")
    netDebugCfgFlow.setHelp(net_helpkeyword)
    netDebugCfgFlow.setDefaultValue(True)

    netDebugDataFlow = netComponent.createBooleanSymbol("SYS_NET_APPDEBUG_DATA_FLOW", netDebugFlowBasicMenu)
    netDebugDataFlow.setLabel("Enable NET Data Flow")
    netDebugDataFlow.setHelp(net_helpkeyword)
    netDebugDataFlow.setDefaultValue(True)
	
    netDebugPreStr = netComponent.createStringSymbol("SYS_NET_APPDEBUG_PRESTR", netDebugLogEnable)
    netDebugPreStr.setLabel("Prefix String")
    netDebugPreStr.setHelp(net_helpkeyword)
    netDebugPreStr.setVisible(True)
    netDebugPreStr.setDescription("Prefix String")
    netDebugPreStr.setDefaultValue("NET_SRVC")
    netDebugPreStr.setDependencies(netDebugMenuVisible, ["SYS_NET_APPDEBUG_ENABLE"])

    netInstance0 = netComponent.createBooleanSymbol("SYS_NET_IDX0", None)
    netInstance0.setLabel("Instance 0")
    netInstance0.setHelp(net_helpkeyword)
    netInstance0.setDescription("Debug - Logs and CLI commands")
    netInstance0.setDefaultValue(True)

    netIntf0 = netComponent.createComboSymbol("SYS_NET_INTF", netInstance0, ["WIFI", "ETHERNET"])
    netIntf0.setLabel("Intf")
    netIntf0.setHelp(net_helpkeyword)
    netIntf0.setDefaultValue("WIFI")

    netIpProt0 = netComponent.createComboSymbol("SYS_NET_IPPROT", netInstance0, ["UDP", "TCP"])
    netIpProt0.setLabel("Ip Protocol")
    netIpProt0.setHelp(net_helpkeyword)
    netIpProt0.setDefaultValue("TCP")
	
    netMode0 = netComponent.createComboSymbol("SYS_NET_MODE", netInstance0, ["CLIENT", "SERVER"])
    netMode0.setLabel("Mode")
    netMode0.setHelp(net_helpkeyword)
    netMode0.setDefaultValue("CLIENT")

    netReConnect0 = netComponent.createBooleanSymbol("SYS_NET_RECONNECT", netInstance0)
    netReConnect0.setLabel("Enable Auto Connect")
    netReConnect0.setHelp(net_helpkeyword)
    netReConnect0.setDefaultValue(True)
	
    netEnableTls0 = netComponent.createBooleanSymbol("SYS_NET_ENABLE_TLS", netInstance0)
    netEnableTls0.setLabel("Enable TLS")
    netEnableTls0.setHelp(net_helpkeyword)
    netEnableTls0.setDefaultValue(False)
    netEnableTls0.setDependencies(netTLSautoMenu, ["SYS_NET_ENABLE_TLS"])

    netEnableSNI0 = netComponent.createBooleanSymbol("SYS_NET_ENABLE_SNI", netEnableTls0)
    netEnableSNI0.setLabel("Enable SNI")
    netEnableSNI0.setHelp(net_helpkeyword)
    netEnableSNI0.setDescription("For SNI support in TLS NET Connection")
    netEnableSNI0.setDefaultValue(False)
    netEnableSNI0.setDependencies(netSNIAutoMenu0, ["SYS_NET_ENABLE_SNI"])

    netEnableALPN0 = netComponent.createBooleanSymbol("SYS_NET_ENABLE_ALPN", netEnableTls0)
    netEnableALPN0.setLabel("Enable ALPN")
    netEnableALPN0.setHelp(net_helpkeyword)
    netEnableALPN0.setDescription("For ALPN support in TLS NET Connection")
    netEnableALPN0.setDefaultValue(False)

    netEnableALPNProtocolName0 = netComponent.createStringSymbol("SYS_NET_ENABLE_ALPN_PROTOCOL_NAME", netEnableALPN0)
    netEnableALPNProtocolName0.setLabel("Enable ALPN Protocol Name List")
    netEnableALPNProtocolName0.setHelp(net_helpkeyword)
    netEnableALPNProtocolName0.setDescription("For ALPN support in TLS NET Connection")
    netEnableALPNProtocolName0.setDefaultValue("x-amzn-mqtt-ca")
    netEnableALPNProtocolName0.setDependencies(netALPNAutoMenu0, ["SYS_NET_ENABLE_ALPN"])

    netPort0 = netComponent.createIntegerSymbol("SYS_NET_PORT", netInstance0)
    netPort0.setLabel("Server Port")
    netPort0.setHelp(net_helpkeyword)
    netPort0.setMin(1)
    netPort0.setMax(65535)
	
    netHostName0 = netComponent.createStringSymbol("SYS_NET_HOST_NAME", netInstance0)
    netHostName0.setLabel("Host Name/ IP Address")
    netHostName0.setHelp(net_helpkeyword)
    netHostName0.setVisible(True)
    netHostName0.setDescription("Host Name/ IP")
    netHostName0.setDefaultValue("192.168.1.1")
	
    netInstance1 = netComponent.createBooleanSymbol("SYS_NET_IDX1", None)
    netInstance1.setLabel("Instance 1")
    netInstance1.setHelp(net_helpkeyword)
    netInstance1.setDescription("Debug - Logs and CLI commands")
    netInstance1.setDefaultValue(False)

    netIntf1 = netComponent.createComboSymbol("SYS_NET_IDX1_INTF", netInstance1, ["WIFI", "ETHERNET"])
    netIntf1.setLabel("Intf")
    netIntf1.setHelp(net_helpkeyword)
    netIntf1.setDefaultValue("WIFI")
    netIntf1.setVisible(False)
    netIntf1.setDependencies(netInst1MenuVisible, ["SYS_NET_IDX1"])

    netIpProt1 = netComponent.createComboSymbol("SYS_NET_IDX1_IPPROT", netInstance1, ["UDP", "TCP"])
    netIpProt1.setLabel("Ip Protocol")
    netIpProt1.setHelp(net_helpkeyword)
    netIpProt1.setDefaultValue("TCP")
    netIpProt1.setVisible(False)
    netIpProt1.setDependencies(netInst1MenuVisible, ["SYS_NET_IDX1"])
	
    netMode1 = netComponent.createComboSymbol("SYS_NET_IDX1_MODE", netInstance1, ["CLIENT", "SERVER"])
    netMode1.setLabel("Mode")
    netMode1.setHelp(net_helpkeyword)
    netMode1.setDefaultValue("CLIENT")
    netMode1.setVisible(False)
    netMode1.setDependencies(netInst1MenuVisible, ["SYS_NET_IDX1"])

    netReConnect1 = netComponent.createBooleanSymbol("SYS_NET_IDX1_RECONNECT", netInstance1)
    netReConnect1.setLabel("Enable Auto Connect")
    netReConnect1.setHelp(net_helpkeyword)
    netReConnect1.setDefaultValue(True)
    netReConnect1.setVisible(False)
    netReConnect1.setDependencies(netInst1MenuVisible, ["SYS_NET_IDX1"])
	
    netEnableTls1 = netComponent.createBooleanSymbol("SYS_NET_IDX1_ENABLE_TLS", netInstance1)
    netEnableTls1.setLabel("Enable TLS")
    netEnableTls1.setHelp(net_helpkeyword)
    netEnableTls1.setDefaultValue(False)
    netEnableTls1.setDependencies(netTLSautoMenu, ["SYS_NET_IDX1_ENABLE_TLS"])
    netEnableTls1.setVisible(False)
    netEnableTls1.setDependencies(netInst1MenuVisible, ["SYS_NET_IDX1"])

    netEnableSNI1 = netComponent.createBooleanSymbol("SYS_NET_IDX1_ENABLE_SNI", netEnableTls1)
    netEnableSNI1.setLabel("Enable SNI")
    netEnableSNI1.setHelp(net_helpkeyword)
    netEnableSNI1.setDescription("For SNI support in TLS NET Connection")
    netEnableSNI1.setDefaultValue(False)
    netEnableSNI1.setDependencies(netSNIAutoMenu1, ["SYS_NET_IDX1_ENABLE_SNI"])

    netEnableALPN1 = netComponent.createBooleanSymbol("SYS_NET_IDX1_ENABLE_ALPN", netEnableTls1)
    netEnableALPN1.setLabel("Enable ALPN")
    netEnableALPN1.setHelp(net_helpkeyword)
    netEnableALPN1.setDescription("For ALPN support in TLS NET Connection")
    netEnableALPN1.setDefaultValue(False)

    netEnableALPNProtocolName1 = netComponent.createStringSymbol("SYS_NET_IDX1_ENABLE_ALPN_PROTOCOL_NAME", netEnableALPN1)
    netEnableALPNProtocolName1.setLabel("Enable ALPN Protocol Name List")
    netEnableALPNProtocolName1.setHelp(net_helpkeyword)
    netEnableALPNProtocolName1.setDescription("For ALPN support in TLS NET Connection")
    netEnableALPNProtocolName1.setDefaultValue("x-amzn-mqtt-ca")
    netEnableALPNProtocolName1.setDependencies(netALPNAutoMenu1, ["SYS_NET_IDX1_ENABLE_ALPN"])

    netPort1 = netComponent.createIntegerSymbol("SYS_NET_IDX1_PORT", netInstance1)
    netPort1.setLabel("Server Port")
    netPort1.setHelp(net_helpkeyword)
    netPort1.setMin(1)
    netPort1.setMax(65535)
    netPort1.setVisible(False)
    netPort1.setDependencies(netInst1MenuVisible, ["SYS_NET_IDX1"])
	
    netHostName1 = netComponent.createStringSymbol("SYS_NET_IDX1_HOST_NAME", netInstance1)
    netHostName1.setLabel("Host Name/ IP Address")
    netHostName1.setHelp(net_helpkeyword)
    netHostName1.setVisible(True)
    netHostName1.setDescription("Host Name/ IP")
    netHostName1.setDefaultValue("192.168.1.1")
    netHostName1.setVisible(False)
    netHostName1.setDependencies(netInst1MenuVisible, ["SYS_NET_IDX1"])

    netEnableTNGTLS = netComponent.createBooleanSymbol("SYS_NET_TNGTLS", None)
    netEnableTNGTLS.setLabel("Trust&Go client certificate")
    netEnableTNGTLS.setHelp(net_helpkeyword)
    netEnableTNGTLS.setDefaultValue(False)
    netEnableTNGTLS.setDependencies(netTLSTNGTLS, ["SYS_NET_TNGTLS"])

    ############################################################################
    #### Code Generation ####
    ############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    netHeaderFile = netComponent.createFileSymbol("SYS_NET_HEADER", None)
    netHeaderFile.setSourcePath("../wireless_system_pic32mzw1_wfi32e01/system/net/sys_net.h")
    netHeaderFile.setOutputName("sys_net.h")
    netHeaderFile.setDestPath("system/net/")
    netHeaderFile.setProjectPath("config/" + configName + "/system/net/")
    netHeaderFile.setType("HEADER")
    netHeaderFile.setOverwrite(True)

    print("Network Service Component Header Path %s", netHeaderFile.getProjectPath())
	
    netSourceFile = netComponent.createFileSymbol("SYS_NET_SOURCE", None)
    netSourceFile.setSourcePath("../wireless_system_pic32mzw1_wfi32e01/system/net/src/sys_net.c")
    netSourceFile.setOutputName("sys_net.c")
    netSourceFile.setDestPath("system/net/src")
    netSourceFile.setProjectPath("config/" + configName + "/system/net/")
    netSourceFile.setType("SOURCE")
    netSourceFile.setOverwrite(True)

    netSystemDefFile = netComponent.createFileSymbol("SYS_NET_DEF", None)
    netSystemDefFile.setType("STRING")
    netSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    netSystemDefFile.setSourcePath("../wireless_system_pic32mzw1_wfi32e01/system/net/templates/system/system_definitions.h.ftl")
    netSystemDefFile.setMarkup(True)
	
#	netSystemConfigFile = netComponent.createFileSymbol("SYS_NET_SYS_CONFIG", None)
#	netSystemConfigFile.setType("STRING")
#	netSystemConfigFile.setOutputName("core.LIST_SYSTEM_CONFIG_H_SYSTEM_SERVICE_CONFIGURATION")
#	netSystemConfigFile.setSourcePath("../wireless_system_pic32mzw1_wfi32e01/system/net/templates/system/system_config.h.ftl")
#	netSystemConfigFile.setMarkup(True)

    netSystemConfigFile = netComponent.createFileSymbol("SYS_CONSOLE_SYS_CONFIG", None)
    netSystemConfigFile.setType("STRING")
    netSystemConfigFile.setOutputName("core.LIST_SYSTEM_CONFIG_H_SYSTEM_SERVICE_CONFIGURATION")
    netSystemConfigFile.setSourcePath("../wireless_system_pic32mzw1_wfi32e01/system/net/templates/system/system_config.h.ftl")
    netSystemConfigFile.setMarkup(True)

    netSystemInitDataFile = netComponent.createFileSymbol("SYS_NET_INIT_DATA", None)
    netSystemInitDataFile.setType("STRING")
    netSystemInitDataFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYSTEM_INITIALIZATION")
    netSystemInitDataFile.setSourcePath("../wireless_system_pic32mzw1_wfi32e01/system/net/templates/system/system_initialize_data.c.ftl")
    netSystemInitDataFile.setMarkup(True)

    netSystemInitFile = netComponent.createFileSymbol("SYS_NET_INIT", None)
    netSystemInitFile.setType("STRING")
    netSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_INITIALIZE_SYSTEM_SERVICES")
    netSystemInitFile.setSourcePath("../wireless_system_pic32mzw1_wfi32e01/system/net/templates/system/system_initialize.c.ftl")
    netSystemInitFile.setMarkup(True)

    tngtlsPortHdr = netComponent.createFileSymbol("WOLFSSL_PORT_HEADER", None)
    tngtlsPortHdr.setSourcePath("./system/net/patch/atmel.h")
    tngtlsPortHdr.setOutputName("atmel.h")
    tngtlsPortHdr.setDestPath("../../third_party/wolfssl/wolfssl/wolfcrypt/port/atmel/")
    tngtlsPortHdr.setOutputName("atmel.h")
    tngtlsPortHdr.setProjectPath("wolfcrypt/port/atmel")
    tngtlsPortHdr.setType("HEADER")
    tngtlsPortHdr.setMarkup(False)
    tngtlsPortHdr.setEnabled(True)
    tngtlsPortHdr.setOverwrite(True)

    tngtlsPortSrc = netComponent.createFileSymbol("WOLFSSL_PORT_SOURCE", None)
    tngtlsPortSrc.setSourcePath("./system/net/patch/atmel.c")
    tngtlsPortSrc.setOutputName("atmel.c")
    tngtlsPortSrc.setDestPath("../../third_party/wolfssl/wolfssl/wolfcrypt/src/port/atmel/")
    tngtlsPortSrc.setOutputName("atmel.c")
    tngtlsPortSrc.setProjectPath("wolfcrypt/port/atmel")
    tngtlsPortSrc.setType("SOURCE")
    tngtlsPortSrc.setMarkup(False)
    tngtlsPortSrc.setEnabled(True)
    tngtlsPortSrc.setOverwrite(True)

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
        
def netDebugMenuVisible(symbol, event):
    if (event["value"] == True):
        print("Debug Log Menu Visible")
        symbol.setVisible(True)
    else:
        print("Debug Log Menu Invisible")
        symbol.setVisible(False)

def netInst1MenuVisible(symbol, event):
    if (event["value"] == True):
        print("Skt Instance 1 Menu Visible")
        symbol.setVisible(True)
    else:
        print("Skt Instance 1 Menu Invisible")
        symbol.setVisible(False)

def onAttachmentConnected(source, target):
    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]


def onAttachmentDisconnected(source, target):
    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]

def netIntfAutoMenu(symbol, event):
#    if (event["value"] == "WIFI_ETHERNET"):
    if (event["value"] == 1):
        res = Database.activateComponents(["drvPic32mEthmac"],"System Configuration", True)
        res = Database.activateComponents(["drvMiim"],"System Configuration", True)
        res = Database.activateComponents(["drvExtPhyLan8740"],"System Configuration", True)
        data = symbol.getComponent()
        ErrCommSymbol = data.getSymbolByID("SYS_NET_ERR")
        ErrCommSymbol.setVisible(False)
#        res = Database.activateComponents(["tcpipNetConfig"],"System Configuration", True)
    else:
        if (event["value"] == 2):
            res = Database.activateComponents(["drvPic32mEthmac"],"System Configuration", True)
            res = Database.activateComponents(["drvMiim"],"System Configuration", True)
            res = Database.activateComponents(["drvExtPhyLan8740"],"System Configuration", True)
            setVal("sysWifiPic32mzw1", "SYS_WIFI_STA_AUTOCONNECT", False)
            data = symbol.getComponent()
            ErrCommSymbol = data.getSymbolByID("SYS_NET_ERR")
            ErrCommSymbol.setLabel("****Note: 'Intf' in Instance 0/ 1 should be ETHERNET when Supported Interface is ETHERNET_ONLY")
            ErrCommSymbol.setVisible(True)
        else:
            res = Database.deactivateComponents(["drvExtPhyLan8740"])
            res = Database.deactivateComponents(["drvMiim"])
            res = Database.deactivateComponents(["drvPic32mEthmac"])
            data = symbol.getComponent()
            ErrCommSymbol = data.getSymbolByID("SYS_NET_ERR")
            ErrCommSymbol.setLabel("****Note: 'Intf' in Instance 0/ 1 should be WIFI when Supported Interface is WIFI_ONLY")
            ErrCommSymbol.setVisible(True)

def netTLSautoMenu(symbol, event):
    if (event["value"] == True):
        res = Database.activateComponents(["lib_wolfssl"],"System Configuration", True)
#        res = Database.activateComponents(["lib_wolfssl"],"System Configuration", True)
#        res = Database.activateComponents(["tcpipSntp"],"System Configuration", True)
#        autoConnectTableWolfSSLcrypto = [["lib_wolfssl", "WolfSSL_Crypto_Dependency", "lib_wolfcrypt","lib_wolfcrypt"]]
#        res = Database.connectDependencies(autoConnectTableWolfSSLcrypto)
        setVal("net_Pres", "NET_PRES_SUPPORT_ENCRYPTION", True)
        setVal("net_Pres", "NET_PRES_ENC_PROVIDE", 0)
        Database.setSymbolValue("lib_wolfssl", "wolfsslDTLS", False)
        Database.setSymbolValue("lib_wolfssl", "wolfsslTLS13", True)
        Database.setSymbolValue("lib_wolfssl", "wolfsslHkdf", True)
        Database.setSymbolValue("lib_wolfssl", "wolfsslNoErrorStrings", True)
        Database.setSymbolValue("lib_wolfssl", "wolfsslUseFastMath", True)
        Database.setSymbolValue("lib_wolfssl", "wolfsslFfdheGroup2048", True)
        # Database.setSymbolValue("lib_wolfcrypt", "wolfcrypt_hw", True)
        Database.setSymbolValue("lib_wolfcrypt", "wolfcrypt_md4", True)
        Database.setSymbolValue("lib_wolfcrypt", "wolfcrypt_md5_hw", True)
        Database.setSymbolValue("lib_wolfcrypt", "wolfcrypt_sha1_hw", True)
        Database.setSymbolValue("lib_wolfcrypt", "wolfcrypt_sha264_hw", True)
        Database.setSymbolValue("lib_wolfcrypt", "wolfcrypt_hmac", True)
        Database.setSymbolValue("lib_wolfcrypt", "wolfcrypt_hkdf", True)
        Database.setSymbolValue("lib_wolfcrypt", "wolfcrypt_tdes", False)
        Database.setSymbolValue("lib_wolfcrypt", "wolfcrypt_aes_hw", True)
        Database.setSymbolValue("lib_wolfcrypt", "wolfcrypt_aes_ecb_hw", True)
        Database.setSymbolValue("lib_wolfcrypt", "wolfcrypt_aes_ccm", False)
        Database.setSymbolValue("lib_wolfcrypt", "wolfcrypt_kdf", True)
        Database.setSymbolValue("lib_wolfcrypt", "wolfcrypt_eccencrypt", True)
        Database.setSymbolValue("lib_wolfcrypt", "wolfcrypt_rsaPss", True)
        Database.setSymbolValue("lib_wolfcrypt", "wolfcrypt_dh", True)
        Database.setSymbolValue("lib_wolfcrypt", "wolfcrypt_keygen", False)
        systemComponentGroup = Database.findGroup("System Configuration")
        if (systemComponentGroup != None):
            res=systemComponentGroup.addComponent("lib_wolfssl")
            autoConnectTableWolfSSLcrypto = [["lib_wolfssl", "WolfSSL_Crypto_Dependency", "lib_wolfcrypt","lib_wolfcrypt"]]
            res = Database.connectDependencies(autoConnectTableWolfSSLcrypto)
                
        # Database.setSymbolValue("lib_wolfcrypt", "wolfcrypt_errorstrings", True)
        # Database.setSymbolValue("lib_wolfcrypt", "wolfcrypt_debug", True)
#        if (Database.getSymbolValue("HarmonyCore", "SELECT_RTOS") != "BareMetal"):
#            Database.setSymbolValue("lib_wolfcrypt", "wolfSslRTOSSupport", "FreeRTOS")
#        else:
#            Database.setSymbolValue("lib_wolfcrypt", "wolfSslRTOSSupport", "Single Threaded")
    else:
#        Database.setSymbolValue("net_Pres", "NET_PRES_SUPPORT_ENCRYPTION", False)
#        res = Database.deactivateComponents(["lib_wolfssl"])
        setVal("net_Pres", "NET_PRES_SUPPORT_ENCRYPTION", False)
#        res = Database.deactivateComponents(["tcpipSntp"])

def netSNIAutoMenu0(symbol, event):
    data = symbol.getComponent()
    sysNetSni = data.getSymbolValue("SYS_NET_ENABLE_SNI")
    if(sysNetSni == True):        
        setVal("net_Pres", "NET_PRES_SUPPORT_SNI", True)
        setVal("net_Pres", "NET_PRES_SUPPORT_SNI_HOST_NAME", Database.getSymbolValue("sysNetPic32mzw1", "SYS_NET_HOST_NAME"))
    else:
        setVal("net_Pres", "NET_PRES_SUPPORT_SNI", False)

def netSNIAutoMenu1(symbol, event):
    data = symbol.getComponent()
    sysNetSni = data.getSymbolValue("SYS_NET_IDX1_ENABLE_SNI")
    if(sysNetSni == True):        
        setVal("net_Pres", "NET_PRES_SUPPORT_SNI", True)
        setVal("net_Pres", "NET_PRES_SUPPORT_SNI_HOST_NAME", Database.getSymbolValue("sysNetPic32mzw1", "SYS_NET_IDX1_HOST_NAME"))
    else:
        setVal("net_Pres", "NET_PRES_SUPPORT_SNI", False)


def netALPNAutoMenu0(symbol, event):
    if (event["value"] == True):
        setVal("net_Pres", "NET_PRES_SUPPORT_ALPN", True)
        setVal("net_Pres", "NET_PRES_SUPPORT_ALPN_PROTOCOL_NAME", Database.getSymbolValue("sysNetPic32mzw1", "SYS_NET_ENABLE_ALPN_PROTOCOL_NAME"))
    else:
        setVal("net_Pres", "NET_PRES_SUPPORT_ALPN", False)

def netALPNAutoMenu1(symbol, event):
    if (event["value"] == True):
        setVal("net_Pres", "NET_PRES_SUPPORT_ALPN", True)
        setVal("net_Pres", "NET_PRES_SUPPORT_ALPN_PROTOCOL_NAME", Database.getSymbolValue("sysNetPic32mzw1", "SYS_NET_IDX1_ENABLE_ALPN_PROTOCOL_NAME"))
    else:
        setVal("net_Pres", "NET_PRES_SUPPORT_ALPN", False)

def netTLSTNGTLS(symbol, event):
    if (event["value"] == True):
        setVal("net_Pres", "NET_PRES_BLOB_ENABLE_ATECC_TNGTLS", True)
        Database.activateComponents(["atecc608","i2c2"],"System Configuration", True)
        Database.setSymbolValue("atecc608_0","PART_TYPE",2)
        systemComponentGroup = Database.findGroup("System Configuration")
        if (systemComponentGroup != None):
            systemComponentGroup.addComponent("cryptoauthlib")
            systemComponentGroup.addComponent("cryptoauthlib_tng")
            Database.connectDependencies([["atecc608_0","ATECC608_DEP_PLIB_I2C","i2c2","I2C2_I2C"]])
            #Database.connectDependencies([["lib_wolfcrypt","lib_wolfcrypt","cryptoauthlib","WolfSSL_Crypto_Dependency"]])
    else:
        setVal("net_Pres", "NET_PRES_BLOB_ENABLE_ATECC_TNGTLS", False)
        Database.deactivateComponents(["atecc608","cryptoauthlib","i2c2","cryptoauthlib_tng"])
    

def finalizeComponent(netComponent):
    #Database.setSymbolValue("core", "XC32_HEAP_SIZE", 160000)
    triggerDict = {}
    triggerDict = Database.sendMessage("core", "HEAP_SIZE", {"heap_size" : 160000})

    res = Database.activateComponents(["sysWifiPic32mzw1"])
    res = Database.activateComponents(["net_Pres"],"System Configuration", True)
    res = Database.activateComponents(["tcpipSntp"],"System Configuration", True)

    if (Database.getSymbolValue("sysNetPic32mzw1", "SYS_NET_ENABLE_APP_CODE_GENERATION") == True):
        if (Database.getComponentByID("HarmonyCore") != None):
            Hccomponent = Database.getComponentByID("HarmonyCore")
            fileSymb = Hccomponent.getSymbolByID("APP0_C")
            fileSymb.setSourcePath("../wireless_system_pic32mzw1_wfi32e01/system/net/templates/app.c.ftl")
    
    setVal("tcpipUdp", "TCPIP_UDP_SOCKET_DEFAULT_RX_QUEUE_LIMIT", 16)
    
    # Enable dependent Harmony core components
    if (Database.getSymbolValue("HarmonyCore", "ENABLE_SYS_COMMON") == False):
        Database.clearSymbolValue("HarmonyCore", "ENABLE_SYS_COMMON")
        Database.setSymbolValue("HarmonyCore", "ENABLE_SYS_COMMON", True)

    if (Database.getSymbolValue("HarmonyCore", "ENABLE_DRV_COMMON") == False):
        Database.clearSymbolValue("HarmonyCore", "ENABLE_DRV_COMMON")
        Database.setSymbolValue("HarmonyCore", "ENABLE_DRV_COMMON", True)

    if (Database.getSymbolValue("HarmonyCore", "SELECT_RTOS") != "BareMetal"):
        Database.setSymbolValue("lib_wolfcrypt", "wolfSslRTOSSupport", "FreeRTOS")
        setVal("net_Pres", "NET_PRES_RTOS_STACK_SIZE", 20480)
        #Database.setSymbolValue("sys_command", "SYS_COMMAND_RTOS_STACK_SIZE", 4096)
        #Database.setSymbolValue("FreeRTOS", "FREERTOS_MEMORY_MANAGEMENT_CHOICE", "Heap_3")
    else:
        Database.setSymbolValue("lib_wolfcrypt", "wolfSslRTOSSupport", "Single Threaded")
		
    
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
    
