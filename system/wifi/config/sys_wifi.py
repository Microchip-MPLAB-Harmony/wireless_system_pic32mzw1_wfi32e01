# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
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
def instantiateComponent(syswifiComponent):

    syswifiEnable = syswifiComponent.createBooleanSymbol("SYS_WIFI_ENABLE", None)
    #syswifiEnable.setLabel("Enable WiFi Service")
    syswifiEnable.setVisible(False)
    syswifiEnable.setDefaultValue(True)

    syswifiEnableErrMsg = syswifiComponent.createCommentSymbol("SYS_WIFI_ERR", None)
    syswifiEnableErrMsg.setLabel("**Placeholder for error display")
    syswifiEnableErrMsg.setVisible(False)

    syswifiMode = syswifiComponent.createComboSymbol("SYS_WIFI_MODE", None, ["STA", "AP"])
    syswifiMode.setLabel("Device Mode")
    syswifiMode.setDescription("Select the Device Boot Mode ")
    syswifiMode.setDefaultValue("STA")

    syswifistaEnable = syswifiComponent.createBooleanSymbol("SYS_WIFI_STA_ENABLE", syswifiMode)
    syswifistaEnable.setLabel("STA Mode")
    syswifistaEnable.setDefaultValue(True)
    #syswifistaEnable.setVisible(True)
#    syswifistaEnable.setDependencies(syswifiSTAMenu, ["SYS_WIFI_MODE"])
    syswifistaEnable.setDescription("Enable STA mode Configuration ")
    syswifistaEnable.setDependencies(syswifiSTAautoMenu, ["SYS_WIFI_STA_ENABLE"])

    syswifistaSsid = syswifiComponent.createStringSymbol("SYS_WIFI_STA_SSID_NAME", syswifistaEnable)
    syswifistaSsid.setLabel("SSID")
    syswifistaSsid.setVisible(True)
    syswifistaSsid.setDescription("Enter STA Mode SSID.The maximum length is 32 characters.")
    syswifistaSsid.setDefaultValue("DEMO_AP")

    syswifistaAuth = syswifiComponent.createComboSymbol("SYS_WIFI_STA_AUTH", syswifistaEnable, ["OPEN", "WPA2","WPA2WPA3","WPA3"])
    syswifistaAuth.setLabel("Security type")
    syswifistaAuth.setDescription("Enter STA Mode Security type")
    syswifistaAuth.setDefaultValue("WPA2")

    syswifistaPwd = syswifiComponent.createStringSymbol("SYS_WIFI_STA_PWD_NAME", syswifistaEnable)
    syswifistaPwd.setLabel("Password")
    syswifistaPwd.setVisible(True)
    syswifistaPwd.setDescription("Enter STA Mode Password.WPA2/WPA3 - Maximum key length is 63 characters.Minimum key length is 8 characters.")
    syswifistaPwd.setDefaultValue("password")
    syswifistaPwd.setDependencies(syswifiSTASecurityMenu, ["SYS_WIFI_STA_AUTH","SYS_WIFI_STA_PWD_NAME"])

    syswifistaAuto = syswifiComponent.createBooleanSymbol("SYS_WIFI_STA_AUTOCONNECT", syswifistaEnable)
    syswifistaAuto.setLabel("Auto Connect")
    syswifistaAuto.setDescription("Enable Auto Connect Feature")
    syswifistaAuto.setDefaultValue(True)

    syswifiapEnable = syswifiComponent.createBooleanSymbol("SYS_WIFI_AP_ENABLE", syswifiMode)
    syswifiapEnable.setLabel("AP Mode")
    syswifiapEnable.setDefaultValue(True)
    #syswifiapEnable.setVisible(Database.getSymbolValue("sysWifiPic32mzw1","SYS_WIFI_MODE") == "STA")
    #syswifiapEnable.setDependencies(syswifiAPMenu, ["SYS_WIFI_MODE"])
    syswifiapEnable.setDescription("Enable AP Mode Configuration")
    syswifiapEnable.setDependencies(syswifiAPautoMenu, ["SYS_WIFI_AP_ENABLE"])

    syswifiapSsid = syswifiComponent.createStringSymbol("SYS_WIFI_AP_SSID_NAME", syswifiapEnable)
    syswifiapSsid.setLabel("SSID")
    syswifiapSsid.setVisible(True)
    syswifiapSsid.setDescription("Enter AP Mode SSID.The maximum length is 32 characters")
    syswifiapSsid.setDefaultValue("DEMO_AP_SOFTAP")

    syswifiapAuth = syswifiComponent.createComboSymbol("SYS_WIFI_AP_AUTH", syswifiapEnable, ["OPEN", "WPA2","WPAWPA2(Mixed)","WPA2WPA3","WPA3"])
    syswifiapAuth.setLabel("Security")
    syswifiapAuth.setDescription("Enter AP Mode Security")
    syswifiapAuth.setDefaultValue("WPA2")

    syswifiapPwd = syswifiComponent.createStringSymbol("SYS_WIFI_AP_PWD_NAME", syswifiapEnable)
    syswifiapPwd.setLabel("Password")
    syswifiapPwd.setVisible(True)
    syswifiapPwd.setDescription("Enter AP Mode Password.WPA2/WPA3 - Maximum key length is 63 characters.Minimum key length is 8 characters.")
    syswifiapPwd.setDefaultValue("password")
    syswifiapPwd.setDependencies(syswifiAPSecurityMenu, ["SYS_WIFI_AP_AUTH","SYS_WIFI_AP_PWD_NAME"])

    syswifiapSsidv = syswifiComponent.createBooleanSymbol("SYS_WIFI_AP_SSIDVISIBILE", syswifiapEnable)
    syswifiapSsidv.setLabel("SSID Visibility")
    syswifiapSsidv.setDefaultValue(True)
    syswifiapSsidv.setDescription("Enable AP Mode SSID Visibility")
    syswifiapSsidv.setDependencies(syswifiMenuVisible, ["SYS_WIFI_ENABLE"])
    syswifiapSsidv.setDependencies(syswifiMenuVisible, ["SYS_WIFI_AP_ENABLE"])

    syswifiapChannel = syswifiComponent.createIntegerSymbol("SYS_WIFI_AP_CHANNEL", syswifiapEnable)
    syswifiapChannel.setLabel("Channel Number")
    syswifiapChannel.setMin(1)
    syswifiapChannel.setMax(13)
    syswifiapChannel.setDescription("Enable AP Mode Channel")
    syswifiapChannel.setDefaultValue(1)
    syswifiapChannel.setDependencies(syswifiChannelErr, ["SYS_WIFI_AP_CHANNEL","SYS_WIFI_COUNTRYCODE"])

    # Advanced Configuration
    syswifiAdvMenu = syswifiComponent.createCommentSymbol("SYS_WIFI_ADVANCED_CONFIG_MENU", None)
    syswifiAdvMenu.setLabel("Advanced Configuration")
    syswifiAdvMenu.setVisible(True)
    #syswifiAdvMenu.setDefaultValue(False)

    syswificountrycode = syswifiComponent.createComboSymbol("SYS_WIFI_COUNTRYCODE", syswifiAdvMenu, ["GEN", "USA", "EMEA", "CUST1", "CUST2"])
    syswificountrycode.setLabel("Country Code")
    syswificountrycode.setDefaultValue("GEN")
    syswificountrycode.setDescription("Enable Country Code. \n Support channels per Country code: \n GEN - 1 to 13, \n USA - 1 to 11, \n EMEA - 1 to 13, \n CUST1,CUST2 - Dependent on user configuration")
    syswificountrycode.setDependencies(syswifiMenuVisible, ["SYS_WIFI_ENABLE"])

    syswifiCB = syswifiComponent.createIntegerSymbol("SYS_WIFI_MAX_CBS", syswifiAdvMenu)
    syswifiCB.setLabel("Number of Clients")
    syswifiCB.setMin(1)
    syswifiCB.setMax(5)
    syswifiCB.setDefaultValue(2)
    syswifiCB.setDescription("Enter Number of Clients want callback from Wi-Fi Service")
    syswifiCB.setDependencies(syswifiMenuVisible, ["SYS_WIFI_ENABLE"])

    syswifiprovEnable = syswifiComponent.createBooleanSymbol("SYS_WIFI_PROVISION_ENABLE", syswifiAdvMenu)
    syswifiprovEnable.setLabel("Enable WiFi Provisioning Service")
    syswifiprovEnable.setDefaultValue(True)
    syswifiprovEnable.setVisible(True)
    syswifiprovEnable.setDescription("Enable WiFi Provisioning Service")
    syswifiprovEnable.setDependencies(syswifiprovMenuVisible, ["SYS_WIFI_PROVISION_ENABLE"])

    syswifiScanEnable = syswifiComponent.createBooleanSymbol("SYS_WIFI_SCAN_ENABLE", syswifiAdvMenu)
    syswifiScanEnable.setLabel("Enable WiFi Scanning")
    syswifiScanEnable.setDefaultValue(False)
    syswifiScanEnable.setVisible(True)
    syswifiScanEnable.setDescription("Enable WiFi Scanning")

    syswifiScanChannel = syswifiComponent.createIntegerSymbol("SYS_WIFI_SCAN_CHANNEL", syswifiScanEnable)
    syswifiScanChannel.setLabel("Channel Number")
    syswifiScanChannel.setVisible(False)
    syswifiScanChannel.setMin(0)
    syswifiScanChannel.setMax(13)
    syswifiScanChannel.setDescription("Scan Channel 1-to-13 (0 = Scan all)")
    syswifiScanChannel.setDefaultValue(0)
    syswifiScanChannel.setDependencies(syswifiMenuVisible, ["SYS_WIFI_SCAN_ENABLE"])

    syswifiScanMode = syswifiComponent.createComboSymbol("SYS_WIFI_SCAN_MODE", syswifiScanEnable, ["PASSIVE", "ACTIVE"])
    syswifiScanMode.setLabel("Scan Mode")
    syswifiScanMode.setVisible(False)
    syswifiScanMode.setDescription("Select the Scan Mode ")
    syswifiScanMode.setDefaultValue("ACTIVE")
    syswifiScanMode.setDependencies(syswifiMenuVisible, ["SYS_WIFI_SCAN_ENABLE"])

    syswifiScanSsidList = syswifiComponent.createStringSymbol("SYS_WIFI_SCAN_SSID_LIST", syswifiScanEnable)
    syswifiScanSsidList.setLabel("SSID List (Active Scan Only)")
    syswifiScanSsidList.setVisible(False)
    syswifiScanSsidList.setDescription("**Only for Active Scan** Maximum 4 SSIDs of maximum 32 characters. (e.g. ssid01,myopenap,demo_ap,securedap)")
    syswifiScanSsidList.setDefaultValue("")
    syswifiScanSsidList.setDependencies(syswifiMenuVisible, ["SYS_WIFI_SCAN_ENABLE"])

    syswifiScanSsidDelim = syswifiComponent.createStringSymbol("SYS_WIFI_SCAN_SSID_DELIM_CHAR", syswifiScanEnable)
    syswifiScanSsidDelim.setLabel("SSID List Delimiter character")
    syswifiScanSsidDelim.setVisible(False)
    syswifiScanSsidDelim.setDescription("Specify the delimiter used for separating AP names in the SSID List above")
    syswifiScanSsidDelim.setDefaultValue(",")
    syswifiScanSsidDelim.setDependencies(syswifiMenuVisible, ["SYS_WIFI_SCAN_ENABLE"])

    syswifiScanChannelMask = syswifiComponent.createHexSymbol("SYS_WIFI_SCAN_CHAN_MASK", syswifiScanEnable)
    syswifiScanChannelMask.setLabel("Bitwise Channel Scan Mask")
    syswifiScanChannelMask.setVisible(False)
    syswifiScanChannelMask.setDescription("Enter Hex Value for Bitwise desired Channels. (e.g. 0x1fff: channel 1-13")
    syswifiScanChannelMask.setMin(0x1)
    syswifiScanChannelMask.setMax(0x3fff)
    syswifiScanChannelMask.setDefaultValue(0x1fff)
    syswifiScanChannelMask.setHexOutputMode(True)
    syswifiScanChannelMask.setDependencies(syswifiMenuVisible, ["SYS_WIFI_SCAN_ENABLE"])

    syswifiScanNumSlots = syswifiComponent.createIntegerSymbol("SYS_WIFI_SCAN_NUM_SLOTS", syswifiScanEnable)
    syswifiScanNumSlots.setLabel("Number Of Slots")
    syswifiScanNumSlots.setVisible(False)
    syswifiScanNumSlots.setMin(1)
    syswifiScanNumSlots.setMax(4)
    syswifiScanNumSlots.setDescription("Number Of Slots")
    syswifiScanNumSlots.setDefaultValue(1)
    syswifiScanNumSlots.setDependencies(syswifiMenuVisible, ["SYS_WIFI_SCAN_ENABLE"])

    syswifiScanActiveSlotTime = syswifiComponent.createIntegerSymbol("SYS_WIFI_SCAN_ACTIVE_SLOT_TIME", syswifiScanEnable)
    syswifiScanActiveSlotTime.setLabel("Active Slot Time")
    syswifiScanActiveSlotTime.setVisible(False)
    syswifiScanActiveSlotTime.setMin(10)
    syswifiScanActiveSlotTime.setMax(1500)
    syswifiScanActiveSlotTime.setDescription("Time spent on each active channel probing for BSS's.")
    syswifiScanActiveSlotTime.setDefaultValue(20)
    syswifiScanActiveSlotTime.setDependencies(syswifiMenuVisible, ["SYS_WIFI_SCAN_ENABLE"])

    syswifiScanPassiveSlotTime = syswifiComponent.createIntegerSymbol("SYS_WIFI_SCAN_PASSIVE_SLOT_TIME", syswifiScanEnable)
    syswifiScanPassiveSlotTime.setLabel("Passive Slot Time")
    syswifiScanPassiveSlotTime.setVisible(False)
    syswifiScanPassiveSlotTime.setMin(10)
    syswifiScanPassiveSlotTime.setMax(1500)
    syswifiScanPassiveSlotTime.setDescription("Time spent on each passive channel listening for beacons")
    syswifiScanPassiveSlotTime.setDefaultValue(120)
    syswifiScanPassiveSlotTime.setDependencies(syswifiMenuVisible, ["SYS_WIFI_SCAN_ENABLE"])

    syswifiScanNumProbes = syswifiComponent.createIntegerSymbol("SYS_WIFI_SCAN_NUM_PROBES", syswifiScanEnable)
    syswifiScanNumProbes.setLabel("Number Of Probes")
    syswifiScanNumProbes.setVisible(False)
    syswifiScanNumProbes.setMin(1)
    syswifiScanNumProbes.setMax(2)
    syswifiScanNumProbes.setDescription("Number of probes per slot")
    syswifiScanNumProbes.setDefaultValue(1)
    syswifiScanNumProbes.setDependencies(syswifiMenuVisible, ["SYS_WIFI_SCAN_ENABLE"])

    syswifiScanMatchMode = syswifiComponent.createComboSymbol("SYS_WIFI_SCAN_MATCH_MODE", syswifiScanEnable, ["STOP_ON_FIRST", "FIND_ALL"])
    syswifiScanMatchMode.setLabel("Scan Match Mode")
    syswifiScanMatchMode.setVisible(False)
    syswifiScanMatchMode.setDescription("The scan matching mode can be to stop on first match or match all")
    syswifiScanMatchMode.setDefaultValue("FIND_ALL")
    syswifiScanMatchMode.setDependencies(syswifiMenuVisible, ["SYS_WIFI_SCAN_ENABLE"])
    
    syswifiDebugLogEnable = syswifiComponent.createBooleanSymbol("SYS_WIFI_APPDEBUG_ENABLE", syswifiAdvMenu)
    syswifiDebugLogEnable.setLabel("Enable Debug Logs")
    syswifiDebugLogEnable.setVisible(True)
    syswifiDebugLogEnable.setDefaultValue(False)
#    syswifiDebugLogEnable.setDependencies(syswifiDebugMenuVisible, ["SYS_WIFI_APPDEBUG_ENABLE"])

    syswifiDebugBasicMenu = syswifiComponent.createMenuSymbol("SYS_WIFI_APPDEBUG_LEVEL_CONFIG_MENU", syswifiDebugLogEnable)
    syswifiDebugBasicMenu.setLabel("Debug Level Configuration")
    syswifiDebugBasicMenu.setVisible(True)
    syswifiDebugBasicMenu.setDependencies(syswifiMenuVisible, ["SYS_WIFI_APPDEBUG_ENABLE"])

    syswifiDebugErrLevel = syswifiComponent.createBooleanSymbol("SYS_WIFI_APPDEBUG_ERR_LEVEL", syswifiDebugBasicMenu)
    syswifiDebugErrLevel.setLabel("Enable Error Level")
    syswifiDebugErrLevel.setVisible(True)
    syswifiDebugErrLevel.setDefaultValue(False)
    #syswifiDebugErrLevel.setDependencies(syswifiMenuVisible, ["SYS_WIFI_APPDEBUG_ENABLE"])

    syswifiDebugDbgLevel = syswifiComponent.createBooleanSymbol("SYS_WIFI_APPDEBUG_DBG_LEVEL", syswifiDebugBasicMenu)
    syswifiDebugDbgLevel.setLabel("Enable Debug Level")
    syswifiDebugDbgLevel.setVisible(True)
    syswifiDebugDbgLevel.setDefaultValue(False)
    #syswifiDebugDbgLevel.setDependencies(syswifiMenuVisible, ["SYS_WIFI_APPDEBUG_ENABLE"])

    syswifiDebugInfoLevel = syswifiComponent.createBooleanSymbol("SYS_WIFI_APPDEBUG_INFO_LEVEL", syswifiDebugBasicMenu)
    syswifiDebugInfoLevel.setLabel("Enable Info Level")
    syswifiDebugInfoLevel.setVisible(True)
    syswifiDebugInfoLevel.setDefaultValue(False)
    #syswifiDebugInfoLevel.setDependencies(syswifiMenuVisible, ["SYS_WIFI_APPDEBUG_ENABLE"])

    syswifiDebugFuncLevel = syswifiComponent.createBooleanSymbol("SYS_WIFI_APPDEBUG_FUNC_LEVEL", syswifiDebugBasicMenu)
    syswifiDebugFuncLevel.setLabel("Enable Function Entry/Exit Level")
    syswifiDebugFuncLevel.setVisible(True)
    syswifiDebugFuncLevel.setDefaultValue(False)
    #syswifiDebugFuncLevel.setDependencies(syswifiMenuVisible, ["SYS_WIFI_APPDEBUG_ENABLE"])

    #syswifiDebugFlow = syswifiComponent.createIntegerSymbol("SYS_WIFI_APPDEBUG_FLOW", syswifiDebugLogEnable)
    #syswifiDebugFlow.setLabel("Flow")
    #syswifiDebugFlow.setMin(1)
    #syswifiDebugFlow.setMax(65535)
    #syswifiDebugFlow.setDefaultValue(65535)
    #syswifiDebugFlow.setDependencies(syswifiMenuVisible, ["SYS_WIFI_APPDEBUG_ENABLE"])

    syswifiDebugFlowBasicMenu = syswifiComponent.createMenuSymbol("SYS_WIFI_APPDEBUG_FLOW_CONFIG_MENU", syswifiDebugLogEnable)
    syswifiDebugFlowBasicMenu.setLabel("Debug Flow Configuration")
    syswifiDebugFlowBasicMenu.setVisible(True)
    #syswifiDebugFlowBasicMenu.setDefaultValue(False)
    syswifiDebugFlowBasicMenu.setDependencies(syswifiMenuVisible, ["SYS_WIFI_APPDEBUG_ENABLE"])

    syswifiDebugFlowCfgFlow = syswifiComponent.createBooleanSymbol("SYS_WIFI_APPDEBUG_CFG_FLOW", syswifiDebugFlowBasicMenu)
    syswifiDebugFlowCfgFlow.setLabel("Enable WiFi Cfg Flow")
    syswifiDebugFlowCfgFlow.setDefaultValue(False)
    syswifiDebugFlowCfgFlow.setVisible(True)

    syswifiDebugConnectFlow = syswifiComponent.createBooleanSymbol("SYS_WIFI_APPDEBUG_CONNECT_FLOW", syswifiDebugFlowBasicMenu)
    syswifiDebugConnectFlow.setLabel("Enable WiFi Connect Flow")
    syswifiDebugConnectFlow.setDefaultValue(False)
    syswifiDebugConnectFlow.setVisible(True)

    syswifiDebugProvFlow = syswifiComponent.createBooleanSymbol("SYS_WIFI_APPDEBUG_PROVISIONING_FLOW", syswifiDebugFlowBasicMenu)
    syswifiDebugProvFlow.setLabel("Enable WiFi Provisioning Flow")
    syswifiDebugProvFlow.setDefaultValue(False)
    syswifiDebugProvFlow.setVisible(True)

    syswifiDebugProvCMDFlow = syswifiComponent.createBooleanSymbol("SYS_WIFI_APPDEBUG_PROVISIONINGCMD_FLOW", syswifiDebugFlowBasicMenu)
    syswifiDebugProvCMDFlow.setLabel("Enable WiFi Provisioning Command Flow")
    syswifiDebugProvCMDFlow.setDefaultValue(False)
    syswifiDebugProvCMDFlow.setVisible(True)

    syswifiDebugProvSOCKFlow = syswifiComponent.createBooleanSymbol("SYS_WIFI_APPDEBUG_PROVISIONINGSOCK_FLOW", syswifiDebugFlowBasicMenu)
    syswifiDebugProvSOCKFlow.setLabel("Enable WiFi Provisioning Socket Flow")
    syswifiDebugProvSOCKFlow.setDefaultValue(False)
    syswifiDebugProvSOCKFlow.setVisible(True)

    syswifiDebugPreStr = syswifiComponent.createStringSymbol("SYS_WIFI_APPDEBUG_PRESTR", syswifiDebugLogEnable)
    syswifiDebugPreStr.setLabel("Prefix String")
    syswifiDebugPreStr.setVisible(True)
    syswifiDebugPreStr.setDescription("Prefix String")
    syswifiDebugPreStr.setDefaultValue("WIFI_SRVC")
    syswifiDebugPreStr.setDependencies(syswifiMenuVisible, ["SYS_WIFI_APPDEBUG_ENABLE"])


    # RTOS Configuration
    syswifiRtosMenu = syswifiComponent.createMenuSymbol("SYS_WIFI_RTOS_MENU", syswifiAdvMenu)
    syswifiRtosMenu.setLabel("RTOS Configuration")
    syswifiRtosMenu.setDescription("RTOS Configuration")
    syswifiRtosMenu.setVisible(False)
    syswifiRtosMenu.setVisible((Database.getSymbolValue("HarmonyCore", "SELECT_RTOS") != "BareMetal") and (Database.getSymbolValue("HarmonyCore", "SELECT_RTOS") != None))
    syswifiRtosMenu.setDependencies(syswifishowRTOSMenu, ["HarmonyCore.SELECT_RTOS"])


    # Menu for RTOS options
    syswifiInstnExecMode = syswifiComponent.createComboSymbol("SYS_WIFI_RTOS", syswifiRtosMenu, ["Standalone"]) 
    syswifiInstnExecMode.setLabel("Run Library Tasks as")
    syswifiInstnExecMode.setVisible(False)
    syswifiInstnExecMode.setDescription("Rtos Options")
    syswifiInstnExecMode.setDefaultValue("Standalone")

    # RTOS Task Stack Size
    syswifiTaskSize = syswifiComponent.createIntegerSymbol("SYS_WIFI_RTOS_TASK_STACK_SIZE", syswifiRtosMenu)
    syswifiTaskSize.setLabel("Stack Size")
    syswifiTaskSize.setVisible(True)
    syswifiTaskSize.setDescription("Rtos Task Stack Size")
    syswifiTaskSize.setDefaultValue(1024)
    syswifiTaskSize.setDependencies(syswifiRTOSStandaloneMenu, ["SYS_WIFI_RTOS"])

    # RTOS Task Priority
    syswifiTaskPriority = syswifiComponent.createIntegerSymbol("SYS_WIFI_RTOS_TASK_PRIORITY", syswifiRtosMenu)
    syswifiTaskPriority.setLabel("Task Priority")
    syswifiTaskPriority.setVisible(True)
    syswifiTaskPriority.setDescription("Rtos Task Priority")
    syswifiTaskPriority.setDefaultValue(1)
    syswifiTaskPriority.setDependencies(syswifiRTOSStandaloneMenu, ["SYS_WIFI_RTOS"])

    # RTOS Use Task Delay?
    syswifiUseTaskDelay = syswifiComponent.createBooleanSymbol("SYS_WIFI_RTOS_USE_DELAY", syswifiRtosMenu)
    syswifiUseTaskDelay.setLabel("Use Task Delay?")
    syswifiUseTaskDelay.setVisible(True)
    syswifiUseTaskDelay.setDescription("Rtos Use Task Delay?")
    syswifiUseTaskDelay.setDefaultValue(True)
    syswifiUseTaskDelay.setDependencies(syswifiRTOSStandaloneMenu, ["SYS_WIFI_RTOS"])

    # RTOS Task Delay
    syswifiTaskDelay = syswifiComponent.createIntegerSymbol("SYS_WIFI_RTOS_DELAY", syswifiRtosMenu)
    syswifiTaskDelay.setLabel("Task Delay")
    syswifiTaskDelay.setVisible(True)
    syswifiTaskDelay.setDescription("WiFi Driver Task Delay")
    syswifiTaskDelay.setDefaultValue(1)
    syswifiTaskDelay.setDependencies(syswifiRTOSTaskDelayMenu, ["SYS_WIFI_RTOS", "SYS_WIFI_RTOS_USE_DELAY"])

    ############################################################################
    #### Code Generation ####
    ############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")


    syswifiSourceFile = syswifiComponent.createFileSymbol("SYS_WIFI_SOURCE", None)
    syswifiSourceFile.setSourcePath("system/wifi/templates/src/sys_wifi.c.ftl")
    syswifiSourceFile.setOutputName("sys_wifi.c")
    syswifiSourceFile.setDestPath("system/wifi/src")
    syswifiSourceFile.setProjectPath("config/" + configName + "/system/wifi/")
    syswifiSourceFile.setType("SOURCE")
    syswifiSourceFile.setMarkup(True)
    syswifiSourceFile.setEnabled(True)

    syswifiHeaderFile = syswifiComponent.createFileSymbol("SYS_WIFI_HEADER", None)
    syswifiHeaderFile.setSourcePath("system/wifi/templates/sys_wifi.h.ftl")
    syswifiHeaderFile.setOutputName("sys_wifi.h")
    syswifiHeaderFile.setDestPath("system/wifi/")
    syswifiHeaderFile.setProjectPath("config/" + configName + "/system/wifi/")
    syswifiHeaderFile.setType("HEADER")
    syswifiHeaderFile.setMarkup(True)
    syswifiHeaderFile.setEnabled(True)

    syswifiSystemDefFile = syswifiComponent.createFileSymbol("SYS_WIFI_DEF", None)
    syswifiSystemDefFile.setType("STRING")
    syswifiSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    syswifiSystemDefFile.setSourcePath("system/wifi/templates/system/system_definitions.h.ftl")
    syswifiSystemDefFile.setMarkup(True)

    syswifiSystemInitFile = syswifiComponent.createFileSymbol("SYS_WIFI_INIT", None)
    syswifiSystemInitFile.setType("STRING")
    syswifiSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_INITIALIZE_SYSTEM_SERVICES")
    syswifiSystemInitFile.setSourcePath("system/wifi/templates/system/system_initialize.c.ftl")
    syswifiSystemInitFile.setMarkup(True)

    syswifiSystemConfFile = syswifiComponent.createFileSymbol("SYS_WIFI_CONFIGURATION_H", None)
    syswifiSystemConfFile.setType("STRING")
    syswifiSystemConfFile.setOutputName("core.LIST_SYSTEM_CONFIG_H_MIDDLEWARE_CONFIGURATION")
    syswifiSystemConfFile.setSourcePath("system/wifi/templates/system/system_config.h.ftl")
    syswifiSystemConfFile.setMarkup(True)


    syswifiSystemTaskFile = syswifiComponent.createFileSymbol("SYS_WIFI_SYSTEM_TASKS_C", None)
    syswifiSystemTaskFile.setType("STRING")
    syswifiSystemTaskFile.setOutputName("core.LIST_SYSTEM_TASKS_C_CALL_LIB_TASKS")
    syswifiSystemTaskFile.setSourcePath("system/wifi/templates/system/system_tasks.c.ftl")
    syswifiSystemTaskFile.setMarkup(True)

    syswifiSystemDefFile = syswifiComponent.createFileSymbol('SYS_WIFI_SYSTEM_DEF', None)
    syswifiSystemDefFile.setType('STRING')
    syswifiSystemDefFile.setOutputName('core.LIST_SYSTEM_DEFINITIONS_H_OBJECTS')
    syswifiSystemDefFile.setSourcePath('system/wifi/templates/system/system_definitions_objects.h.ftl')
    syswifiSystemDefFile.setMarkup(True)

    syswifiSystemRtosTasksFile = syswifiComponent.createFileSymbol("SYS_WIFI_SYS_RTOS_TASK", None)
    syswifiSystemRtosTasksFile.setType("STRING")
    syswifiSystemRtosTasksFile.setOutputName("core.LIST_SYSTEM_RTOS_TASKS_C_DEFINITIONS")
    syswifiSystemRtosTasksFile.setSourcePath("system/wifi/templates/system/system_rtos_tasks.c.ftl")
    syswifiSystemRtosTasksFile.setMarkup(True)
    syswifiSystemRtosTasksFile.setEnabled((Database.getSymbolValue("HarmonyCore", "SELECT_RTOS") != "BareMetal"))
    syswifiSystemRtosTasksFile.setDependencies(genRtosTask, ["HarmonyCore.SELECT_RTOS"])

    #Set back active to root.
    Database.setActiveGroup(None)
    if (Database.getSymbolValue("HarmonyCore", "ENABLE_SYS_RESET") == False):
        Database.clearSymbolValue("HarmonyCore", "ENABLE_SYS_RESET")
        Database.setSymbolValue("HarmonyCore", "ENABLE_SYS_RESET", True)
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

def syswifiMenuVisible(symbol, event):
    if (event["value"] == True):
        print("WIFI Menu Visible.")
        symbol.setVisible(True)
    else:
        print("WIFI Menu Invisible.")
        symbol.setVisible(False)

def syswifishowRTOSMenu(symbol, event):
    if (event["value"] == None):
        symbol.setVisible(False)
        print("SYS WIFI: OSAL Disabled")
    elif (event["value"] != "BareMetal"):
        # If not Bare Metal
        symbol.setVisible(True)
        print("SYS WIFI rtos")
        Database.setSymbolValue("tcpipStack", "TCPIP_STACK_MALLOC_FUNC", "malloc")
        Database.setSymbolValue("tcpipStack", "TCPIP_STACK_FREE_FUNC", "free")
        Database.setSymbolValue("tcpipStack", "TCPIP_STACK_CALLOC_FUNC", "calloc")
        Database.setSymbolValue("tcpipStack", "TCPIP_STACK_DRAM_SIZE", 65000)
        Database.setSymbolValue("tcpipStack", "TCPIP_STACK_USER_NOTIFICATION", True)
        #Database.setSymbolValue("core", "XC32_HEAP_SIZE", 160000)
        triggerDict = {}
        triggerDict = Database.sendMessage("core", "HEAP_SIZE", {"heap_size" : 160000})
        if (Database.getSymbolValue("HarmonyCore", "ENABLE_SYS_RESET") == False):
            Database.clearSymbolValue("HarmonyCore", "ENABLE_SYS_RESET")
            Database.setSymbolValue("HarmonyCore", "ENABLE_SYS_RESET", True)

        Database.setSymbolValue("core", "WIFI_CLOCK_ENABLE", True)
    else:
        symbol.setVisible(False)
        print("SYS WIFI Bare Metal")
        #Database.setSymbolValue("tcpipStack", "TCPIP_STACK_MALLOC_FUNC", "pvPortMalloc")
        #Database.setSymbolValue("tcpipStack", "TCPIP_STACK_FREE_FUNC", "vPortFree")
        #Database.setSymbolValue("tcpipStack", "TCPIP_STACK_CALLOC_FUNC", "APP_Calloc")
        #Database.setSymbolValue("tcpipStack", "TCPIP_STACK_DRAM_SIZE", 75000)
        #Database.setSymbolValue("tcpipStack", "TCPIP_STACK_USER_NOTIFICATION", True)
        #Database.setSymbolValue("core", "XC32_HEAP_SIZE", 10240)
        #Database.setSymbolValue("FreeRTOS", "FREERTOS_TOTAL_HEAP_SIZE",160000)
        Database.setSymbolValue("tcpipStack", "TCPIP_STACK_MALLOC_FUNC", "malloc")
        Database.setSymbolValue("tcpipStack", "TCPIP_STACK_FREE_FUNC", "free")
        Database.setSymbolValue("tcpipStack", "TCPIP_STACK_CALLOC_FUNC", "calloc")
        Database.setSymbolValue("tcpipStack", "TCPIP_STACK_DRAM_SIZE", 65000)
        Database.setSymbolValue("tcpipStack", "TCPIP_STACK_USER_NOTIFICATION", True)
        #Database.setSymbolValue("core", "XC32_HEAP_SIZE", 150000)
        triggerDict = {}
        triggerDict = Database.sendMessage("core", "HEAP_SIZE", {"heap_size" : 160000})
        Database.setSymbolValue("core", "WIFI_CLOCK_ENABLE", True)
        if (Database.getSymbolValue("HarmonyCore", "ENABLE_SYS_RESET") == False):
            Database.clearSymbolValue("HarmonyCore", "ENABLE_SYS_RESET")
            Database.setSymbolValue("HarmonyCore", "ENABLE_SYS_RESET", True)


def syswifiRTOSStandaloneMenu(symbol, event):
    if (event["value"] == 'Standalone'):        
        symbol.setVisible(True)
        print("SYS WIFI Standalone")
    else:
        symbol.setVisible(False)
        print("SYS WIFI Combined")
def syswifiSTASecurityMenu(symbol, event):
    data = symbol.getComponent()
    sysWiFisecurity = data.getSymbolValue("SYS_WIFI_STA_AUTH")
    sysWiFiWPAPwdlen = len(data.getSymbolValue("SYS_WIFI_STA_PWD_NAME"))
    ErrCommSymbol = data.getSymbolByID("SYS_WIFI_ERR")
    if(sysWiFisecurity == "OPEN"):        
        symbol.setVisible(False)
    else:
        if(sysWiFiWPAPwdlen < 8):
            ErrCommSymbol.setLabel("****Error:Minimum STA Password length is 8 characters.")
            ErrCommSymbol.setVisible(True)
        elif(sysWiFiWPAPwdlen > 63):
            ErrCommSymbol.setLabel("****Error:Maximum STA Password length is 63 characters.")
            ErrCommSymbol.setVisible(True)
        else:
            ErrCommSymbol.setLabel("")
            ErrCommSymbol.setVisible(False)
        symbol.setVisible(True)

def syswifiAPSecurityMenu(symbol, event):
    data = symbol.getComponent()
    sysWiFisecurity = data.getSymbolValue("SYS_WIFI_AP_AUTH")
    sysWiFiWPAPwdlen = len(data.getSymbolValue("SYS_WIFI_AP_PWD_NAME"))
    ErrCommSymbol = data.getSymbolByID("SYS_WIFI_ERR")
    if(sysWiFisecurity == "OPEN"):        
        symbol.setVisible(False)
        ErrCommSymbol.setVisible(False)
    else:
        if(sysWiFiWPAPwdlen < 8):
            ErrCommSymbol.setLabel("****Error:Minimum AP Password length is 8 characters.")
            ErrCommSymbol.setVisible(True)
        elif(sysWiFiWPAPwdlen > 63):
            ErrCommSymbol.setLabel("****Error:Maximum AP Password length is 63 characters.")
            ErrCommSymbol.setVisible(True)
        else:
            ErrCommSymbol.setLabel("")
            ErrCommSymbol.setVisible(False)
        symbol.setVisible(True)

def syswifiChannelErr(symbol, event):
    data = symbol.getComponent()
    sysWiFiChannelno = data.getSymbolValue("SYS_WIFI_AP_CHANNEL")
    sysWiFiCountrycode = data.getSymbolValue("SYS_WIFI_COUNTRYCODE")
    ErrCommSymbol = data.getSymbolByID("SYS_WIFI_ERR")
    if(sysWiFiCountrycode == "USA"):
        if(sysWiFiChannelno > 11):
            ErrCommSymbol.setLabel("****Error:USA Supported Channels : 1 to 11")
            ErrCommSymbol.setVisible(True)
        else:
            ErrCommSymbol.setLabel("")
            ErrCommSymbol.setVisible(False)
    else:
        ErrCommSymbol.setLabel("")
        ErrCommSymbol.setVisible(False)
    symbol.setVisible(True)

def syswifiSTAMenu(symbol, event):

    if(Database.getSymbolValue("sysWifiPic32mzw1","SYS_WIFI_MODE") == "STA"):        
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def syswifiAPMenu(symbol, event):

    if(Database.getSymbolValue("sysWifiPic32mzw1","SYS_WIFI_MODE") == "AP"):        
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def syswifiSTAautoMenu(symbol, event):
    tcpipAutoConfigAppsGroup = Database.findGroup("APPLICATION LAYER")
    if (event["value"] == True):
        res = Database.activateComponents(["tcpipDns"],"APPLICATION LAYER", False)
        tcpipAutoConfigAppsGroup.setAttachmentVisible("tcpipDns", "libtcpipDns")
        res = Database.activateComponents(["tcpipDhcp"],"APPLICATION LAYER", False)
        tcpipAutoConfigAppsGroup.setAttachmentVisible("tcpipDhcp", "libtcpipDhcp")
        if(Database.getSymbolValue("tcpip_apps_config", "TCPIP_AUTOCONFIG_ENABLE_DHCP_CLIENT") != True):
           Database.setSymbolValue("tcpip_apps_config", "TCPIP_AUTOCONFIG_ENABLE_DHCP_CLIENT", True)
        if(Database.getSymbolValue("tcpip_apps_config", "TCPIP_AUTOCONFIG_ENABLE_DNS_CLIENT") != True):
           Database.setSymbolValue("tcpip_apps_config", "TCPIP_AUTOCONFIG_ENABLE_DNS_CLIENT", True)
    else:
        Database.setSymbolValue("tcpip_apps_config", "TCPIP_AUTOCONFIG_ENABLE_DHCP_CLIENT", False)
        Database.setSymbolValue("tcpip_apps_config", "TCPIP_AUTOCONFIG_ENABLE_DNS_CLIENT", False)
        #res = Database.deactivateComponents(["tcpipDhcp"])
        #res = Database.deactivateComponents(["tcpipDns"])

def syswifiAPautoMenu(symbol, event):
    tcpipAutoConfigAppsGroup = Database.findGroup("APPLICATION LAYER")
    if (event["value"] == True):
        res = Database.activateComponents(["tcpipDhcps"],"APPLICATION LAYER", False)    
        tcpipAutoConfigAppsGroup.setAttachmentVisible("tcpipDhcps", "libtcpipDhcps")
        res = Database.activateComponents(["tcpipDnss"],"APPLICATION LAYER", False)
        tcpipAutoConfigAppsGroup.setAttachmentVisible("tcpipDnss", "libtcpipDnss")
        if(Database.getSymbolValue("tcpip_apps_config", "TCPIP_AUTOCONFIG_ENABLE_DHCP_SERVER") != True):
           Database.setSymbolValue("tcpip_apps_config", "TCPIP_AUTOCONFIG_ENABLE_DHCP_SERVER", True)
        if(Database.getSymbolValue("tcpip_apps_config", "TCPIP_AUTOCONFIG_ENABLE_DNS_SERVER") != True):
           Database.setSymbolValue("tcpip_apps_config", "TCPIP_AUTOCONFIG_ENABLE_DNS_SERVER", True)
    else:
        Database.setSymbolValue("tcpip_apps_config", "TCPIP_AUTOCONFIG_ENABLE_DHCP_SERVER", False)
        Database.setSymbolValue("tcpip_apps_config", "TCPIP_AUTOCONFIG_ENABLE_DNS_SERVER", False)
        #res = Database.deactivateComponents(["tcpipDhcps"])
        #res = Database.deactivateComponents(["tcpipDnss"])


def syswifiprovMenuVisible(symbol, event):
    if (event["value"] == True):
        if(Database.getComponentByID("sysWifiProvPic32mzw1") == None):    
            res = Database.activateComponents(["sysWifiProvPic32mzw1"])
            setVal("sysWifiPic32mzw1", "SYS_WIFI_PROVISION_ENABLE", True)
    else:
        if(Database.getComponentByID("sysWifiProvPic32mzw1") != None):
            res = Database.deactivateComponents(["sysWifiProvPic32mzw1"])
            setVal("sysWifiPic32mzw1", "SYS_WIFI_PROVISION_ENABLE", False)

def syswifiRTOSTaskDelayMenu(symbol, event):
    sysWiFiRtos = Database.getSymbolValue("sysWifiPic32mzw1","SYS_WIFI_RTOS")
    sysWiFiRtosRtosUseDelay = Database.getSymbolValue("sysWifiPic32mzw1","SYS_WIFI_RTOS_USE_DELAY")
    if((sysWiFiRtos == 'Standalone') and sysWiFiRtosRtosUseDelay):        
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)
def genRtosTask(symbol, event):
    symbol.setEnabled((Database.getSymbolValue("HarmonyCore", "SELECT_RTOS") != "BareMetal"))
########################################################################################################
def finalizeComponent(syswifiComponent):
    res = Database.activateComponents(["Root"])
    syswifisysComponent = Database.createGroup(None,"System Configuration")
    res = Database.activateComponents(["dfp"],"System Configuration", True)
    res = Database.activateComponents(["system"],"System Configuration", True)
    res = Database.activateComponents(["core"],"System Configuration", True)
    if(Database.getSymbolValue("sysWifiPic32mzw1", "SYS_WIFI_PROVISION_ENABLE") == True):
       res = Database.activateComponents(["nvm"],"System Configuration", True)
    res = Database.activateComponents(["core_timer"],"System Configuration", True)
    res = Database.activateComponents(["uart1"],"System Configuration", True)
    res = Database.activateComponents(["lib_crypto"],"System Configuration", True)
    res = Database.activateComponents(["lib_wolfcrypt"],"System Configuration", True)
    res = Database.activateComponents(["sys_time"],"System Configuration", True)
    res = Database.activateComponents(["sys_console"],"System Configuration", True)
    res = Database.activateComponents(["sys_command"],"System Configuration", True)
    res = Database.activateComponents(["sys_debug"],"System Configuration", True)
    #Driver layer
    res = Database.activateComponents(["tcpipAutoConfigApps"],"System Configuration", True)
    res = Database.activateComponents(["tcpipAutoConfigBasic"],"System Configuration", True)
    res = Database.activateComponents(["tcpipAutoConfigDriver"],"System Configuration", True)
    res = Database.activateComponents(["tcpipAutoConfigNetwork"],"System Configuration", True)
    res = Database.activateComponents(["drvWifiPic32mzw1"],"System Configuration", True)
    if(Database.getSymbolValue("HarmonyCore", "SELECT_RTOS") != "BareMetal"):
       res = Database.activateComponents(["drv_ba414e"],"System Configuration", True)    

#Application layer
    res = Database.activateComponents(["tcpip_apps_config"],"System Configuration", True)
    if(Database.getSymbolValue("tcpip_apps_config", "TCPIP_AUTOCONFIG_ENABLE_DHCP_CLIENT") != True):
        Database.setSymbolValue("tcpip_apps_config", "TCPIP_AUTOCONFIG_ENABLE_DHCP_CLIENT", True)
        if ( syswifisysComponent != None ):
            res=syswifisysComponent.addComponent("TCP/IP STACK")
            res=syswifisysComponent.addComponent("tcpipStack")
            res=syswifisysComponent.addComponent("tcpipNetConfig")
            res=syswifisysComponent.addComponent("HarmonyCore")
            res=syswifisysComponent.addComponent("core")
            res=syswifisysComponent.addComponent("dfp")
            res=syswifisysComponent.addComponent("FreeRTOS")
            res=syswifisysComponent.addComponent("sys_console")
            res=syswifisysComponent.addComponent("sys_command")
            res=syswifisysComponent.addComponent("sys_debug")

    if(Database.getSymbolValue("tcpip_apps_config", "TCPIP_AUTOCONFIG_ENABLE_DHCP_SERVER") != True):
            Database.setSymbolValue("tcpip_apps_config", "TCPIP_AUTOCONFIG_ENABLE_DHCP_SERVER", True)

    if(Database.getSymbolValue("tcpip_apps_config", "TCPIP_AUTOCONFIG_ENABLE_DNS_CLIENT") != True):
            Database.setSymbolValue("tcpip_apps_config", "TCPIP_AUTOCONFIG_ENABLE_DNS_CLIENT", True)

    if(Database.getSymbolValue("tcpip_apps_config", "TCPIP_AUTOCONFIG_ENABLE_DNS_SERVER") != True):
            Database.setSymbolValue("tcpip_apps_config", "TCPIP_AUTOCONFIG_ENABLE_DNS_SERVER", True)

    if(Database.getSymbolValue("tcpip_network_config", "TCPIP_AUTOCONFIG_ENABLE_ARP") != True):
        Database.setSymbolValue("tcpip_network_config", "TCPIP_AUTOCONFIG_ENABLE_ARP", True)

    if(Database.getSymbolValue("tcpip_network_config", "TCPIP_AUTOCONFIG_ENABLE_ICMPv4") != True):
        Database.setSymbolValue("tcpip_network_config", "TCPIP_AUTOCONFIG_ENABLE_ICMPv4", True)

    if(Database.getSymbolValue("tcpip_basic_config", "TCPIP_AUTOCONFIG_ENABLE_TCPIPCMD") != True):
        Database.setSymbolValue("tcpip_basic_config", "TCPIP_AUTOCONFIG_ENABLE_TCPIPCMD", True)
        #add connections
        autoConnectTableTime = [["sys_time", "sys_time_TMR_dependency", "core_timer", "CORE_TIMER_TMR"]]
        autoConnectTablenetMAC = [["tcpipNetConfig_0", "NETCONFIG_MAC_Dependency", "drvWifiPic32mzw1","libdrvPic32mzw1Mac"]]
        autoConnectTablecrypto = [["lib_crypto", "LIB_CRYPTO_WOLFCRYPT_Dependency", "lib_wolfcrypt","lib_wolfcrypt"]]
        autoConnectTableuart = [["sys_console_0", "sys_console_UART_dependency", "uart1","UART1_UART"]]
        autoConnectTablecondeb = [["sys_console_0", "sys_console", "sys_debug","sys_debug_SYS_CONSOLE_dependency"]]
        autoConnectTableconcmd = [["sys_console_0", "sys_console", "sys_command","sys_command_SYS_CONSOLE_dependency"]]
        autoConnectTablecontcp = [["sys_console_0", "sys_console", "tcpipStack","Core_SysConsole_Dependency"]]
        res = Database.connectDependencies(autoConnectTablenetMAC)
        res = Database.connectDependencies(autoConnectTablecrypto)
        res = Database.connectDependencies(autoConnectTableuart)
        res = Database.connectDependencies(autoConnectTablecontcp)
        res = Database.connectDependencies(autoConnectTablecondeb)
        res = Database.connectDependencies(autoConnectTableTime)
        res = Database.connectDependencies(autoConnectTableconcmd)
        if(Database.getSymbolValue("HarmonyCore", "SELECT_RTOS") != "BareMetal"):
           autoConnectTableconba414 = [["drvWifiPic32mzw1", "BA414E_Dependency", "drv_ba414e","drv_ba414e"]]
           res = Database.connectDependencies(autoConnectTableconba414)


    if(Database.getSymbolValue("tcpip_transport_config", "TCPIP_AUTOCONFIG_ENABLE_TCP") != True):
        Database.setSymbolValue("tcpip_transport_config", "TCPIP_AUTOCONFIG_ENABLE_TCP", True)       

    # Enable dependent Harmony core components
    if (Database.getSymbolValue("HarmonyCore", "ENABLE_SYS_COMMON") == False):
        Database.clearSymbolValue("HarmonyCore", "ENABLE_SYS_COMMON")
        Database.setSymbolValue("HarmonyCore", "ENABLE_SYS_COMMON", True)

    if (Database.getSymbolValue("HarmonyCore", "ENABLE_DRV_COMMON") == False):
        Database.clearSymbolValue("HarmonyCore", "ENABLE_DRV_COMMON")
        Database.setSymbolValue("HarmonyCore", "ENABLE_DRV_COMMON", True)


    # memory configurations
    if(Database.getSymbolValue("HarmonyCore", "SELECT_RTOS") == "BareMetal"):
        Database.setSymbolValue("tcpipStack", "TCPIP_STACK_MALLOC_FUNC", "malloc")
        Database.setSymbolValue("tcpipStack", "TCPIP_STACK_FREE_FUNC", "free")
        Database.setSymbolValue("tcpipStack", "TCPIP_STACK_CALLOC_FUNC", "calloc")
        Database.setSymbolValue("tcpipStack", "TCPIP_STACK_DRAM_SIZE", 65000)
        Database.setSymbolValue("tcpipStack", "TCPIP_STACK_USER_NOTIFICATION", True)
        #Database.setSymbolValue("core", "XC32_HEAP_SIZE", 150000)
        triggerDict = {}
        triggerDict = Database.sendMessage("core", "HEAP_SIZE", {"heap_size" : 160000})
        Database.setSymbolValue("core", "WIFI_CLOCK_ENABLE", True)
        Database.setSymbolValue("core", "EWPLL_ENABLE", True)        
        Database.setSymbolValue("tcpipIcmp", "TCPIP_ICMP_CLIENT_USER_NOTIFICATION", True)
        Database.setSymbolValue("tcpipIcmp", "TCPIP_STACK_USE_ICMP_CLIENT", True)
        Database.setSymbolValue("lib_wolfcrypt", "wolfcrypt_hw", True)
        Database.setSymbolValue("uart1", "UART_TX_RING_BUFFER_SIZE", 2048)
        Database.setSymbolValue("core", "CRYPTO_CLOCK_ENABLE", True)
        Database.setSymbolValue("core", "RNG_CLOCK_ENABLE", True)
        Database.setSymbolValue("sys_console", "SYS_CONSOLE_PRINT_BUFFER_SIZE", 256)
        if (Database.getSymbolValue("HarmonyCore", "ENABLE_SYS_RESET") == False):
            Database.clearSymbolValue("HarmonyCore", "ENABLE_SYS_RESET")
            Database.setSymbolValue("HarmonyCore", "ENABLE_SYS_RESET", True)
    else:
        Database.setSymbolValue("tcpipStack", "TCPIP_STACK_MALLOC_FUNC", "malloc")
        Database.setSymbolValue("tcpipStack", "TCPIP_STACK_FREE_FUNC", "free")
        Database.setSymbolValue("tcpipStack", "TCPIP_STACK_CALLOC_FUNC", "calloc")
        Database.setSymbolValue("tcpipStack", "TCPIP_STACK_DRAM_SIZE", 65000)
        if (Database.getSymbolValue("HarmonyCore", "ENABLE_SYS_RESET") == False):
            Database.clearSymbolValue("HarmonyCore", "ENABLE_SYS_RESET")
            Database.setSymbolValue("HarmonyCore", "ENABLE_SYS_RESET", True)

        Database.setSymbolValue("tcpipStack", "TCPIP_STACK_USER_NOTIFICATION", True)
        triggerDict = {}
        triggerDict = Database.sendMessage("core", "HEAP_SIZE", {"heap_size" : 160000})
        Database.setSymbolValue("core", "WIFI_CLOCK_ENABLE", True)
        Database.setSymbolValue("core", "OSCCON_NOSC_VALUE", "SPLL")
        Database.setSymbolValue("core", "EWPLL_ENABLE", True)
        Database.setSymbolValue("tcpipIcmp", "TCPIP_ICMP_CLIENT_USER_NOTIFICATION", True)
        Database.setSymbolValue("tcpipIcmp", "TCPIP_STACK_USE_ICMP_CLIENT", True)
        Database.setSymbolValue("lib_wolfcrypt", "wolfcrypt_hw", True)
        Database.setSymbolValue("uart1", "UART_TX_RING_BUFFER_SIZE", 2048)
        Database.setSymbolValue("core", "CRYPTO_CLOCK_ENABLE", True)
        Database.setSymbolValue("core", "RNG_CLOCK_ENABLE", True)
        Database.setSymbolValue("sys_console", "SYS_CONSOLE_PRINT_BUFFER_SIZE", 256)
        Database.setSymbolValue("sys_command", "SYS_COMMAND_RTOS_STACK_SIZE", 4096)
        Database.setSymbolValue("FreeRTOS", "FREERTOS_MEMORY_MANAGEMENT_CHOICE", "Heap_3")
        Database.setSymbolValue("tcpipStack", "TCPIP_STACK_USE_HEAP_CONFIG", "TCPIP_STACK_HEAP_TYPE_EXTERNAL_HEAP")
        if (Database.getSymbolValue("HarmonyCore", "ENABLE_SYS_RESET") == False):
            Database.clearSymbolValue("HarmonyCore", "ENABLE_SYS_RESET")
            Database.setSymbolValue("HarmonyCore", "ENABLE_SYS_RESET", True)

    if(Database.getSymbolValue("sysWifiPic32mzw1", "SYS_WIFI_PROVISION_ENABLE") == True):
       res = Database.activateComponents(["sysWifiProvPic32mzw1"])
    if(Database.getSymbolValue("sysWifiPic32mzw1", "SYS_WIFI_APPDEBUG_ENABLE") == True):
       res = Database.activateComponents(["sysAppDebugPic32mzw1"])
########################################################################################################    
def destroyComponent(component):
    if(Database.getSymbolValue("sysWifiPic32mzw1", "SYS_WIFI_PROVISION_ENABLE") == True):
       res = Database.deactivateComponents(["sysWifiProvPic32mzw1"])
       res = Database.deactivateComponents(["nvm"])
    if(Database.getSymbolValue("sysWifiPic32mzw1", "SYS_WIFI_STA_ENABLE") == True):
        Database.setSymbolValue("tcpip_apps_config", "TCPIP_AUTOCONFIG_ENABLE_DHCP_CLIENT", False)
        Database.setSymbolValue("tcpip_apps_config", "TCPIP_AUTOCONFIG_ENABLE_DNS_CLIENT", False)
    if(Database.getSymbolValue("sysWifiPic32mzw1", "SYS_WIFI_AP_ENABLE") == True):
        Database.setSymbolValue("tcpip_apps_config", "TCPIP_AUTOCONFIG_ENABLE_DHCP_SERVER", False)
        Database.setSymbolValue("tcpip_apps_config", "TCPIP_AUTOCONFIG_ENABLE_DNS_SERVER", False)
    if(Database.getSymbolValue("sysWifiPic32mzw1", "SYS_WIFI_APPDEBUG_ENABLE") == True):
       res = Database.deactivateComponents(["sysAppDebugPic32mzw1"])
    res = Database.deactivateComponents(["System Configuration"])