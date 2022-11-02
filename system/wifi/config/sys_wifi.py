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
global wifi_helpkeyword

wifi_helpkeyword = "mcc_h3_pic32mzw1_wifi_system_service_configurations"
################################################################################
#### Business Logic ####
################################################################################

################################################################################
#### Component ####
################################################################################

from datetime import datetime


def instantiateComponent(syswifiComponent):
    global wifi_helpkeyword
	
    syswifiEnable = syswifiComponent.createBooleanSymbol("SYS_WIFI_ENABLE", None)
    #syswifiEnable.setLabel("Enable WiFi Service")
    syswifiEnable.setHelp(wifi_helpkeyword)
    syswifiEnable.setVisible(False)
    syswifiEnable.setDefaultValue(True)

    syswifiEnableErrMsg = syswifiComponent.createCommentSymbol("SYS_WIFI_ERR", None)
    syswifiEnableErrMsg.setLabel("**Placeholder for error display")
    syswifiEnableErrMsg.setHelp(wifi_helpkeyword)
    syswifiEnableErrMsg.setVisible(False)

    syswifiMode = syswifiComponent.createComboSymbol("SYS_WIFI_MODE", None, ["STA", "AP"])
    syswifiMode.setLabel("Device Mode")
    syswifiMode.setHelp(wifi_helpkeyword)
    syswifiMode.setDescription("Select the Device Boot Mode ")
    syswifiMode.setDefaultValue("STA")

    syswifistaEnable = syswifiComponent.createBooleanSymbol("SYS_WIFI_STA_ENABLE", syswifiMode)
    syswifistaEnable.setLabel("STA Mode")
    syswifistaEnable.setHelp(wifi_helpkeyword)
    syswifistaEnable.setDefaultValue(True)
    #syswifistaEnable.setVisible(True)
    #syswifistaEnable.setDependencies(syswifiSTAMenu, ["SYS_WIFI_MODE"])
    syswifistaEnable.setDescription("Enable STA mode Configuration ")
    syswifistaEnable.setDependencies(syswifiSTAautoMenu, ["SYS_WIFI_STA_ENABLE"])

    syswifistaSsid = syswifiComponent.createStringSymbol("SYS_WIFI_STA_SSID_NAME", syswifistaEnable)
    syswifistaSsid.setLabel("SSID")
    syswifistaSsid.setHelp(wifi_helpkeyword)
    syswifistaSsid.setVisible(True)
    syswifistaSsid.setDescription("Enter STA Mode SSID.The maximum length is 32 characters.")
    syswifistaSsid.setDefaultValue("DEMO_AP")

    syswifistaAuth = syswifiComponent.createComboSymbol("SYS_WIFI_STA_AUTH", syswifistaEnable, ["OPEN", "WPA2","WPA2WPA3","WPA3","WPAWPA2-Enterprise","WPA2-Enterprise","WPA2WPA3-Enterprise","WPA3-Enterprise"])
    syswifistaAuth.setLabel("Security type")
    syswifistaAuth.setHelp(wifi_helpkeyword)
    syswifistaAuth.setDescription("Enter STA Mode Security type")
    syswifistaAuth.setDefaultValue("WPA2")
    syswifistaAuth.setDependencies(syswifiSTAMenu,["SYS_WIFI_STA_AUTH"])

    syswifistaEnt = syswifiComponent.createBooleanSymbol("SYS_WIFI_SUPPORT_ENTERPRISE", syswifistaEnable)
    syswifistaEnt.setDefaultValue(False)
    syswifistaEnt.setVisible(False)
    syswifistaEnt.setDescription("Support Enterprise Mode ? ")
    syswifistaEnt.setDependencies(syswifiSTAMenu, ["SYS_WIFI_STA_AUTH"])

    syswifistaPwd = syswifiComponent.createStringSymbol("SYS_WIFI_STA_PWD_NAME", syswifistaEnable)
    syswifistaPwd.setLabel("Password")
    syswifistaPwd.setHelp(wifi_helpkeyword)
    syswifistaPwd.setVisible(True)
    syswifistaPwd.setDescription("Enter STA Mode Password.WPA2/WPA3 - Maximum key length is 63 characters.Minimum key length is 8 characters.")
    syswifistaPwd.setDefaultValue("password")
    syswifistaPwd.setDependencies(syswifiSTASecurityMenu, ["SYS_WIFI_STA_AUTH","SYS_WIFI_STA_PWD_NAME"])

#### ENTERPRISE ####

    syswifistaEntUserName = syswifiComponent.createStringSymbol("SYS_WIFI_STA_ENT_USER_NAME", syswifistaEnable)
    syswifistaEntUserName.setLabel("Username & Domainname")
    syswifistaEntUserName.setHelp(wifi_helpkeyword)
    syswifistaEntUserName.setVisible(False)
    syswifistaEntUserName.setDescription("Enter [username][domainname] or [domainname][username]")
    syswifistaEntUserName.setDefaultValue("DEMO_USER")
    syswifistaEntUserName.setDependencies(syswifiSTASecurityMenu, ["SYS_WIFI_STA_AUTH","SYS_WIFI_STA_ENT_USER_NAME"])

    syswifistaEntServerDomainSAN = syswifiComponent.createStringSymbol("SYS_WIFI_STA_ENT_SERVER_DOMAIN_SAN", syswifistaEnable)
    syswifistaEntServerDomainSAN.setLabel("Server Domain Name SAN")
    syswifistaEntServerDomainSAN.setHelp(wifi_helpkeyword)
    syswifistaEntServerDomainSAN.setVisible(False)
    syswifistaEntServerDomainSAN.setDescription("Enter Server Domain SAN")
    syswifistaEntServerDomainSAN.setDefaultValue("")
    syswifistaEntServerDomainSAN.setDependencies(syswifiSTASecurityMenu, ["SYS_WIFI_STA_AUTH","SYS_WIFI_STA_ENT_SERVER_DOMAIN_SAN"])

    syswifistaEntServerDomainCN = syswifiComponent.createStringSymbol("SYS_WIFI_STA_ENT_SERVER_DOMAIN_CN", syswifistaEnable)
    syswifistaEntServerDomainCN.setLabel("Server Domain Name CN")
    syswifistaEntServerDomainCN.setHelp(wifi_helpkeyword)
    syswifistaEntServerDomainCN.setVisible(False)
    syswifistaEntServerDomainCN.setDescription("Enter Server Domain CN")
    syswifistaEntServerDomainCN.setDefaultValue("")
    syswifistaEntServerDomainCN.setDependencies(syswifiSTASecurityMenu, ["SYS_WIFI_STA_AUTH","SYS_WIFI_STA_ENT_SERVER_DOMAIN_CN"])


    syswifistaEntDate = syswifiComponent.createStringSymbol("SYS_WIFI_STA_ENT_DATE", syswifistaEnable)
    syswifistaEntDate.setLabel("Certificate Date")
    syswifistaEntDate.setHelp(wifi_helpkeyword)
    syswifistaEntDate.setVisible(False)
    syswifistaEntDate.setDescription("Enter valid date for certificates")
    syswifistaEntDate.setDefaultValue("2022-07-21T19:21:00.00Z")
    syswifistaEntDate.setDependencies(syswifiSTASecurityMenu, ["SYS_WIFI_STA_AUTH","SYS_WIFI_STA_ENT_DATE"])

    syswifistaEntDateEpoch = syswifiComponent.createIntegerSymbol("SYS_WIFI_STA_ENT_DATE_EPOCH", syswifistaEnable)
    syswifistaEntDateEpoch.setLabel("Certificate Date Epoch")
    syswifistaEntDateEpoch.setHelp(wifi_helpkeyword)
    syswifistaEntDateEpoch.setVisible(False)
    syswifistaEntDateEpoch.setDescription("Enter valid date for certificates Epoch")
    syswifistaEntDateEpoch.setDefaultValue(0)
    syswifistaEntDateEpoch.setDependencies(syswifiSTASecurityMenu, ["SYS_WIFI_STA_AUTH","SYS_WIFI_STA_ENT_DATE_EPOCH"])

    syswifistaCaCertFormat = syswifiComponent.createComboSymbol("SYS_WIFI_STA_CACERT_FORMAT",syswifistaEnable, ["DER","PEM"])
    syswifistaCaCertFormat.setVisible(False)
    syswifistaCaCertFormat.setLabel("CA Certificate Format")
    syswifistaCaCertFormat.setHelp(wifi_helpkeyword)
    syswifistaCaCertFormat.setDescription("Select the Certificate Format")
    syswifistaCaCertFormat.setDefaultValue("DER")

    syswifistaEntCACertFileName = syswifiComponent.createStringSymbol("SYS_WIFI_STA_ENT_CACERT_FILE_NAME", syswifistaEnable)
    syswifistaEntCACertFileName.setLabel("CA Certificate File Name")
    syswifistaEntCACertFileName.setHelp(wifi_helpkeyword)
    syswifistaEntCACertFileName.setVisible(False)
    syswifistaEntCACertFileName.setDescription("Enter CA Certificate File Name")
    syswifistaEntCACertFileName.setDefaultValue("wfi_root.h")
    syswifistaEntCACertFileName.setDependencies(syswifiSTASecurityMenu, ["SYS_WIFI_STA_AUTH","SYS_WIFI_STA_ENT_CACERT_FILE_NAME"])

    syswifistaEntCACertModuleName = syswifiComponent.createStringSymbol("SYS_WIFI_STA_ENT_CACERT_MODULE_NAME", syswifistaEnable)
    syswifistaEntCACertModuleName.setLabel("CA Certificate Module Name")
    syswifistaEntCACertModuleName.setHelp(wifi_helpkeyword)
    syswifistaEntCACertModuleName.setVisible(False)
    syswifistaEntCACertModuleName.setDescription("Enter CA Certificate Module Name")
    syswifistaEntCACertModuleName.setDefaultValue("wfi_root")
    syswifistaEntCACertModuleName.setDependencies(syswifiSTASecurityMenu, ["SYS_WIFI_STA_AUTH","SYS_WIFI_STA_ENT_CACERT_MODULE_NAME"])

    syswifistaPrivateCertFormat = syswifiComponent.createComboSymbol("SYS_WIFI_STA_PRIVATE_CERT_FORMAT",syswifistaEnable, ["DER","PEM"])
    syswifistaPrivateCertFormat.setVisible(False)
    syswifistaPrivateCertFormat.setLabel("Private Certificate Format")
    syswifistaPrivateCertFormat.setHelp(wifi_helpkeyword)
    syswifistaPrivateCertFormat.setDescription("Select the Certificate Format")
    syswifistaPrivateCertFormat.setDefaultValue("DER")

    syswifistaEntPrivateCertFileName = syswifiComponent.createStringSymbol("SYS_WIFI_STA_ENT_PRIVATE_CERT_FILE_NAME", syswifistaEnable)
    syswifistaEntPrivateCertFileName.setLabel("Private Certificate File Name")
    syswifistaEntPrivateCertFileName.setHelp(wifi_helpkeyword)
    syswifistaEntPrivateCertFileName.setVisible(False)
    syswifistaEntPrivateCertFileName.setDescription("Enter Private Certificate File Name")
    syswifistaEntPrivateCertFileName.setDefaultValue("private_cert.h")
    syswifistaEntPrivateCertFileName.setDependencies(syswifiSTASecurityMenu, ["SYS_WIFI_STA_AUTH","SYS_WIFI_STA_ENT_PRIVATE_CERT_FILE_NAME"])

    syswifistaEntPrivateCertModuleName = syswifiComponent.createStringSymbol("SYS_WIFI_STA_ENT_PRIVATE_CERT_MODULE_NAME", syswifistaEnable)
    syswifistaEntPrivateCertModuleName.setLabel("Private Certificate Module Name")
    syswifistaEntPrivateCertModuleName.setHelp(wifi_helpkeyword)
    syswifistaEntPrivateCertModuleName.setVisible(False)
    syswifistaEntPrivateCertModuleName.setDescription("Enter Private Certificate Module Name")
    syswifistaEntPrivateCertModuleName.setDefaultValue("private_cert")
    syswifistaEntPrivateCertModuleName.setDependencies(syswifiSTASecurityMenu, ["SYS_WIFI_STA_AUTH","SYS_WIFI_STA_ENT_PRIVATE_CERT_MODULE_NAME"])

    syswifistaPrivateKeyFormat = syswifiComponent.createComboSymbol("SYS_WIFI_STA_PRIVATE_KEY_FORMAT",syswifistaEnable, ["DER","PEM"])
    syswifistaPrivateKeyFormat.setVisible(False)
    syswifistaPrivateKeyFormat.setLabel("Private Key Format")
    syswifistaPrivateKeyFormat.setHelp(wifi_helpkeyword)
    syswifistaPrivateKeyFormat.setDescription("Select the Certificate Format")
    syswifistaPrivateKeyFormat.setDefaultValue("DER")
    
    syswifistaEntPrivateKeyFileName = syswifiComponent.createStringSymbol("SYS_WIFI_STA_ENT_PRIVATE_KEY_FILE_NAME", syswifistaEnable)
    syswifistaEntPrivateKeyFileName.setLabel("Private Key File Name")
    syswifistaEntPrivateKeyFileName.setHelp(wifi_helpkeyword)
    syswifistaEntPrivateKeyFileName.setVisible(False)
    syswifistaEntPrivateKeyFileName.setDescription("Enter Private Key File Name")
    syswifistaEntPrivateKeyFileName.setDefaultValue("private_key.h")
    syswifistaEntPrivateKeyFileName.setDependencies(syswifiSTASecurityMenu, ["SYS_WIFI_STA_AUTH","SYS_WIFI_STA_ENT_PRIVATE_KEY_FILE_NAME"])

    syswifistaEntPrivateKeyModuleName = syswifiComponent.createStringSymbol("SYS_WIFI_STA_ENT_PRIVATE_KEY_MODULE_NAME", syswifistaEnable)
    syswifistaEntPrivateKeyModuleName.setLabel("Private Key Module Name")
    syswifistaEntPrivateKeyModuleName.setHelp(wifi_helpkeyword)
    syswifistaEntPrivateKeyModuleName.setVisible(False)
    syswifistaEntPrivateKeyModuleName.setDescription("Enter Private Key Module Name")
    syswifistaEntPrivateKeyModuleName.setDefaultValue("private_key")
    syswifistaEntPrivateKeyModuleName.setDependencies(syswifiSTASecurityMenu, ["SYS_WIFI_STA_AUTH","SYS_WIFI_STA_ENT_PRIVATE_KEY_MODULE_NAME"])


#### ENTERPRISE END####

    syswifistaAuto = syswifiComponent.createBooleanSymbol("SYS_WIFI_STA_AUTOCONNECT", syswifistaEnable)
    syswifistaAuto.setLabel("Auto Connect")
    syswifistaAuto.setHelp(wifi_helpkeyword)
    syswifistaAuto.setDescription("Enable Auto Connect Feature")
    syswifistaAuto.setDefaultValue(True)

    syswifiapEnable = syswifiComponent.createBooleanSymbol("SYS_WIFI_AP_ENABLE", syswifiMode)
    syswifiapEnable.setLabel("AP Mode")
    syswifiapEnable.setHelp(wifi_helpkeyword)
    syswifiapEnable.setDefaultValue(True)
    #syswifiapEnable.setVisible(Database.getSymbolValue("sysWifiPic32mzw1","SYS_WIFI_MODE") == "STA")
    #syswifiapEnable.setDependencies(syswifiAPMenu, ["SYS_WIFI_MODE"])
    syswifiapEnable.setDescription("Enable AP Mode Configuration")
    syswifiapEnable.setDependencies(syswifiAPautoMenu, ["SYS_WIFI_AP_ENABLE"])

    syswifiapSsid = syswifiComponent.createStringSymbol("SYS_WIFI_AP_SSID_NAME", syswifiapEnable)
    syswifiapSsid.setLabel("SSID")
    syswifiapSsid.setHelp(wifi_helpkeyword)
    syswifiapSsid.setVisible(True)
    syswifiapSsid.setDescription("Enter AP Mode SSID.The maximum length is 32 characters")
    syswifiapSsid.setDefaultValue("DEMO_AP_SOFTAP")

    syswifiapAuth = syswifiComponent.createComboSymbol("SYS_WIFI_AP_AUTH", syswifiapEnable, ["OPEN", "WPA2","WPAWPA2(Mixed)","WPA2WPA3","WPA3"])
    syswifiapAuth.setLabel("Security")
    syswifiapAuth.setHelp(wifi_helpkeyword)
    syswifiapAuth.setDescription("Enter AP Mode Security")
    syswifiapAuth.setDefaultValue("WPA2")

    syswifiapPwd = syswifiComponent.createStringSymbol("SYS_WIFI_AP_PWD_NAME", syswifiapEnable)
    syswifiapPwd.setLabel("Password")
    syswifiapPwd.setHelp(wifi_helpkeyword)
    syswifiapPwd.setVisible(True)
    syswifiapPwd.setDescription("Enter AP Mode Password.WPA2/WPA3 - Maximum key length is 63 characters.Minimum key length is 8 characters.")
    syswifiapPwd.setDefaultValue("password")
    syswifiapPwd.setDependencies(syswifiAPSecurityMenu, ["SYS_WIFI_AP_AUTH","SYS_WIFI_AP_PWD_NAME"])

    syswifiapSsidv = syswifiComponent.createBooleanSymbol("SYS_WIFI_AP_SSIDVISIBILE", syswifiapEnable)
    syswifiapSsidv.setLabel("SSID Visibility")
    syswifiapSsidv.setHelp(wifi_helpkeyword)
    syswifiapSsidv.setDefaultValue(True)
    syswifiapSsidv.setDescription("Enable AP Mode SSID Visibility")
    syswifiapSsidv.setDependencies(syswifiMenuVisible, ["SYS_WIFI_ENABLE"])
    syswifiapSsidv.setDependencies(syswifiMenuVisible, ["SYS_WIFI_AP_ENABLE"])

    syswifiapChannel = syswifiComponent.createIntegerSymbol("SYS_WIFI_AP_CHANNEL", syswifiapEnable)
    syswifiapChannel.setLabel("Channel Number")
    syswifiapChannel.setHelp(wifi_helpkeyword)
    syswifiapChannel.setMin(1)
    syswifiapChannel.setMax(13)
    syswifiapChannel.setDescription("Enable AP Mode Channel")
    syswifiapChannel.setDefaultValue(1)
    syswifiapChannel.setDependencies(syswifiChannelErr, ["SYS_WIFI_AP_CHANNEL","SYS_WIFI_COUNTRYCODE"])

    # Advanced Configuration
    syswifiAdvMenu = syswifiComponent.createCommentSymbol("SYS_WIFI_ADVANCED_CONFIG_MENU", None)
    syswifiAdvMenu.setLabel("Advanced Configuration")
    syswifiAdvMenu.setHelp(wifi_helpkeyword)
    syswifiAdvMenu.setVisible(True)
    #syswifiAdvMenu.setDefaultValue(False)

    syswificountrycode = syswifiComponent.createComboSymbol("SYS_WIFI_COUNTRYCODE", syswifiAdvMenu, ["GEN", "USA", "EMEA", "CUST1", "CUST2"])
    syswificountrycode.setLabel("Country Code")
    syswificountrycode.setHelp(wifi_helpkeyword)
    syswificountrycode.setDefaultValue("GEN")
    syswificountrycode.setDescription("Enable Country Code. \n Support channels per Country code: \n GEN - 1 to 13, \n USA - 1 to 11, \n EMEA - 1 to 13, \n CUST1,CUST2 - Dependent on user configuration")
    syswificountrycode.setDependencies(syswifiMenuVisible, ["SYS_WIFI_ENABLE"])

    syswifiCB = syswifiComponent.createIntegerSymbol("SYS_WIFI_MAX_CBS", syswifiAdvMenu)
    syswifiCB.setLabel("Number of Clients")
    syswifiCB.setHelp(wifi_helpkeyword)
    syswifiCB.setMin(1)
    syswifiCB.setMax(5)
    syswifiCB.setDefaultValue(2)
    syswifiCB.setDescription("Enter Number of Clients want callback from Wi-Fi Service")
    syswifiCB.setDependencies(syswifiMenuVisible, ["SYS_WIFI_ENABLE"])

    syswifiprovEnable = syswifiComponent.createBooleanSymbol("SYS_WIFI_PROVISION_ENABLE", syswifiAdvMenu)
    syswifiprovEnable.setLabel("Enable WiFi Provisioning Service")
    syswifiprovEnable.setHelp(wifi_helpkeyword)
    syswifiprovEnable.setDefaultValue(True)
    syswifiprovEnable.setVisible(True)
    syswifiprovEnable.setDescription("Enable WiFi Provisioning Service")
    syswifiprovEnable.setDependencies(syswifiprovMenuVisible, ["SYS_WIFI_PROVISION_ENABLE"])

    syswifiPwrSaveEnable = syswifiComponent.createBooleanSymbol("SYS_WIFI_POWERSAVE_ENABLE", syswifiAdvMenu)
    syswifiPwrSaveEnable.setLabel("Enable Power Save")
    syswifiPwrSaveEnable.setHelp(wifi_helpkeyword)
    syswifiPwrSaveEnable.setDefaultValue(False)
    syswifiPwrSaveEnable.setVisible(True)
    syswifiPwrSaveEnable.setDescription("Enable Power Save")

    syswifiPICMode = syswifiComponent.createComboSymbol("SYS_WIFI_PIC_MODE", syswifiPwrSaveEnable, ["XDS", "DS", "SLEEP", "IDLE", "DREAM"])
    syswifiPICMode.setLabel("Set PIC Power Save Mode")
    syswifiPICMode.setHelp(wifi_helpkeyword)
    syswifiPICMode.setDefaultValue("DS")
    syswifiPICMode.setDescription("Set PIC Power Save Mode")
    syswifiPICMode.setDependencies(syswifiMenuVisible, ["SYS_WIFI_POWERSAVE_ENABLE"])

    syswifiPICCorMode = syswifiComponent.createComboSymbol("SYS_PIC_WIFI_CORRELATION_MODE", syswifiPwrSaveEnable, ["SYNC", "ASYNC"])
    syswifiPICCorMode.setLabel("Set PIC Wi-Fi correlation Mode")
    syswifiPICCorMode.setHelp(wifi_helpkeyword)
    syswifiPICCorMode.setDefaultValue("SYNC")
    syswifiPICCorMode.setDescription("Set PIC Wi-Fi correlation Mode")
    syswifiPICCorMode.setDependencies(syswifiMenuVisible, ["SYS_WIFI_POWERSAVE_ENABLE"])

    syswifiPwrSaveMode = syswifiComponent.createComboSymbol("SYS_WIFI_LOWPOWER_MODE", syswifiPwrSaveEnable, ["RUN", "WSM", "WDS", "WOFF"])
    syswifiPwrSaveMode.setLabel("Set Wi-Fi Power Save Mode")
    syswifiPwrSaveMode.setHelp(wifi_helpkeyword)
    syswifiPwrSaveMode.setDefaultValue("WSM")
    syswifiPwrSaveMode.setDescription("Set Wi-Fi Power Save Mode")
    syswifiPwrSaveMode.setDependencies(syswifiMenuVisible, ["SYS_WIFI_POWERSAVE_ENABLE"])

    syswifiWakeUp = syswifiComponent.createComboSymbol("SYS_WIFI_WAKEUP", syswifiPwrSaveEnable, ["LISTEN INTERVAL","DTIM"])
    syswifiWakeUp.setLabel("Set Wi-Fi Wakeup Source")
    syswifiWakeUp.setHelp(wifi_helpkeyword)
    syswifiWakeUp.setDefaultValue("LISTEN INTERVAL")
    syswifiWakeUp.setDescription("Set Wi-Fi Wakeup Source")
    syswifiWakeUp.setDependencies(syswifiMenuVisible, ["SYS_WIFI_POWERSAVE_ENABLE"])

    syswifiLisInterval = syswifiComponent.createIntegerSymbol("SYS_WIFI_LISTENINTERVAL", syswifiPwrSaveEnable)
    syswifiLisInterval.setLabel("Set Wi-Fi Listen Interval")
    syswifiLisInterval.setHelp(wifi_helpkeyword)
    syswifiLisInterval.setVisible(False)
    syswifiLisInterval.setMin(1)
    syswifiLisInterval.setMax(600)
    syswifiLisInterval.setDescription("Set Wi-Fi Listen Interval")
    syswifiLisInterval.setDefaultValue(500)
    syswifiLisInterval.setDependencies(syswifiMenuVisible, ["SYS_WIFI_POWERSAVE_ENABLE"])

    syswifiSleepInact = syswifiComponent.createIntegerSymbol("SYS_WIFI_SLEEPINACTLIMIT", syswifiPwrSaveEnable)
    syswifiSleepInact.setLabel("Set Wi-Fi Sleep Inactivity Threshold/Limit Value")
    syswifiSleepInact.setHelp(wifi_helpkeyword)
    syswifiLisInterval.setVisible(False)
    syswifiSleepInact.setMin(1)
    syswifiSleepInact.setMax(1000)
    syswifiSleepInact.setDescription("Set Wi-Fi sleep inactivity threshold/limit value")
    syswifiSleepInact.setDefaultValue(500)
    syswifiSleepInact.setDependencies(syswifiMenuVisible, ["SYS_WIFI_POWERSAVE_ENABLE"])

    syswifiScanEnable = syswifiComponent.createBooleanSymbol("SYS_WIFI_SCAN_ENABLE", syswifiAdvMenu)
    syswifiScanEnable.setLabel("Enable WiFi Scanning")
    syswifiScanEnable.setHelp(wifi_helpkeyword)
    syswifiScanEnable.setDefaultValue(False)
    syswifiScanEnable.setVisible(True)
    syswifiScanEnable.setDescription("Enable WiFi Scanning")

    syswifiScanChannel = syswifiComponent.createIntegerSymbol("SYS_WIFI_SCAN_CHANNEL", syswifiScanEnable)
    syswifiScanChannel.setLabel("Channel Number")
    syswifiScanChannel.setHelp(wifi_helpkeyword)
    syswifiScanChannel.setVisible(False)
    syswifiScanChannel.setMin(0)
    syswifiScanChannel.setMax(13)
    syswifiScanChannel.setDescription("Scan Channel 1-to-13 (0 = Scan all)")
    syswifiScanChannel.setDefaultValue(0)
    syswifiScanChannel.setDependencies(syswifiMenuVisible, ["SYS_WIFI_SCAN_ENABLE"])

    syswifiScanMode = syswifiComponent.createComboSymbol("SYS_WIFI_SCAN_MODE", syswifiScanEnable, ["PASSIVE", "ACTIVE"])
    syswifiScanMode.setLabel("Scan Mode")
    syswifiScanMode.setHelp(wifi_helpkeyword)
    syswifiScanMode.setVisible(False)
    syswifiScanMode.setDescription("Select the Scan Mode ")
    syswifiScanMode.setDefaultValue("ACTIVE")
    syswifiScanMode.setDependencies(syswifiMenuVisible, ["SYS_WIFI_SCAN_ENABLE"])

    syswifiScanSsidList = syswifiComponent.createStringSymbol("SYS_WIFI_SCAN_SSID_LIST", syswifiScanEnable)
    syswifiScanSsidList.setLabel("SSID List (Active Scan Only)")
    syswifiScanSsidList.setHelp(wifi_helpkeyword)
    syswifiScanSsidList.setVisible(False)
    syswifiScanSsidList.setDescription("**Only for Active Scan** Maximum 4 SSIDs of maximum 32 characters. (e.g. ssid01,myopenap,demo_ap,securedap)")
    syswifiScanSsidList.setDefaultValue("")
    syswifiScanSsidList.setDependencies(syswifiMenuVisible, ["SYS_WIFI_SCAN_ENABLE"])

    syswifiScanSsidDelim = syswifiComponent.createStringSymbol("SYS_WIFI_SCAN_SSID_DELIM_CHAR", syswifiScanEnable)
    syswifiScanSsidDelim.setLabel("SSID List Delimiter character")
    syswifiScanSsidDelim.setHelp(wifi_helpkeyword)
    syswifiScanSsidDelim.setVisible(False)
    syswifiScanSsidDelim.setDescription("Specify the delimiter used for separating AP names in the SSID List above")
    syswifiScanSsidDelim.setDefaultValue(",")
    syswifiScanSsidDelim.setDependencies(syswifiMenuVisible, ["SYS_WIFI_SCAN_ENABLE"])

    syswifiScanChannelMask = syswifiComponent.createHexSymbol("SYS_WIFI_SCAN_CHAN_MASK", syswifiScanEnable)
    syswifiScanChannelMask.setLabel("Bitwise Channel Scan Mask")
    syswifiScanChannelMask.setHelp(wifi_helpkeyword)
    syswifiScanChannelMask.setVisible(False)
    syswifiScanChannelMask.setDescription("Enter Hex Value for Bitwise desired Channels. (e.g. 0x1fff: channel 1-13")
    syswifiScanChannelMask.setMin(0x1)
    syswifiScanChannelMask.setMax(0x3fff)
    syswifiScanChannelMask.setDefaultValue(0x1fff)
    syswifiScanChannelMask.setHexOutputMode(True)
    syswifiScanChannelMask.setDependencies(syswifiMenuVisible, ["SYS_WIFI_SCAN_ENABLE"])

    syswifiScanNumSlots = syswifiComponent.createIntegerSymbol("SYS_WIFI_SCAN_NUM_SLOTS", syswifiScanEnable)
    syswifiScanNumSlots.setLabel("Number Of Slots")
    syswifiScanNumSlots.setHelp(wifi_helpkeyword)
    syswifiScanNumSlots.setVisible(False)
    syswifiScanNumSlots.setMin(1)
    syswifiScanNumSlots.setMax(4)
    syswifiScanNumSlots.setDescription("Number Of Slots")
    syswifiScanNumSlots.setDefaultValue(1)
    syswifiScanNumSlots.setDependencies(syswifiMenuVisible, ["SYS_WIFI_SCAN_ENABLE"])

    syswifiScanActiveSlotTime = syswifiComponent.createIntegerSymbol("SYS_WIFI_SCAN_ACTIVE_SLOT_TIME", syswifiScanEnable)
    syswifiScanActiveSlotTime.setLabel("Active Slot Time")
    syswifiScanActiveSlotTime.setHelp(wifi_helpkeyword)
    syswifiScanActiveSlotTime.setVisible(False)
    syswifiScanActiveSlotTime.setMin(10)
    syswifiScanActiveSlotTime.setMax(1500)
    syswifiScanActiveSlotTime.setDescription("Time spent on each active channel probing for BSS's.")
    syswifiScanActiveSlotTime.setDefaultValue(20)
    syswifiScanActiveSlotTime.setDependencies(syswifiMenuVisible, ["SYS_WIFI_SCAN_ENABLE"])

    syswifiScanPassiveSlotTime = syswifiComponent.createIntegerSymbol("SYS_WIFI_SCAN_PASSIVE_SLOT_TIME", syswifiScanEnable)
    syswifiScanPassiveSlotTime.setLabel("Passive Slot Time")
    syswifiScanPassiveSlotTime.setHelp(wifi_helpkeyword)
    syswifiScanPassiveSlotTime.setVisible(False)
    syswifiScanPassiveSlotTime.setMin(10)
    syswifiScanPassiveSlotTime.setMax(1500)
    syswifiScanPassiveSlotTime.setDescription("Time spent on each passive channel listening for beacons")
    syswifiScanPassiveSlotTime.setDefaultValue(120)
    syswifiScanPassiveSlotTime.setDependencies(syswifiMenuVisible, ["SYS_WIFI_SCAN_ENABLE"])

    syswifiScanNumProbes = syswifiComponent.createIntegerSymbol("SYS_WIFI_SCAN_NUM_PROBES", syswifiScanEnable)
    syswifiScanNumProbes.setLabel("Number Of Probes")
    syswifiScanNumProbes.setHelp(wifi_helpkeyword)
    syswifiScanNumProbes.setVisible(False)
    syswifiScanNumProbes.setMin(1)
    syswifiScanNumProbes.setMax(2)
    syswifiScanNumProbes.setDescription("Number of probes per slot")
    syswifiScanNumProbes.setDefaultValue(1)
    syswifiScanNumProbes.setDependencies(syswifiMenuVisible, ["SYS_WIFI_SCAN_ENABLE"])

    syswifiScanMatchMode = syswifiComponent.createComboSymbol("SYS_WIFI_SCAN_MATCH_MODE", syswifiScanEnable, ["STOP_ON_FIRST", "FIND_ALL"])
    syswifiScanMatchMode.setLabel("Scan Match Mode")
    syswifiScanMatchMode.setHelp(wifi_helpkeyword)
    syswifiScanMatchMode.setVisible(False)
    syswifiScanMatchMode.setDescription("The scan matching mode can be to stop on first match or match all")
    syswifiScanMatchMode.setDefaultValue("FIND_ALL")
    syswifiScanMatchMode.setDependencies(syswifiMenuVisible, ["SYS_WIFI_SCAN_ENABLE"])
    
    syswifiDebugLogEnable = syswifiComponent.createBooleanSymbol("SYS_WIFI_APPDEBUG_ENABLE", syswifiAdvMenu)
    syswifiDebugLogEnable.setLabel("Enable Debug Logs")
    syswifiDebugLogEnable.setHelp(wifi_helpkeyword)
    syswifiDebugLogEnable.setVisible(True)
    syswifiDebugLogEnable.setDefaultValue(False)
#    syswifiDebugLogEnable.setDependencies(syswifiDebugMenuVisible, ["SYS_WIFI_APPDEBUG_ENABLE"])

    syswifiDebugBasicMenu = syswifiComponent.createMenuSymbol("SYS_WIFI_APPDEBUG_LEVEL_CONFIG_MENU", syswifiDebugLogEnable)
    syswifiDebugBasicMenu.setLabel("Debug Level Configuration")
    syswifiDebugBasicMenu.setHelp(wifi_helpkeyword)
    syswifiDebugBasicMenu.setVisible(True)
    syswifiDebugBasicMenu.setDependencies(syswifiMenuVisible, ["SYS_WIFI_APPDEBUG_ENABLE"])

    syswifiDebugErrLevel = syswifiComponent.createBooleanSymbol("SYS_WIFI_APPDEBUG_ERR_LEVEL", syswifiDebugBasicMenu)
    syswifiDebugErrLevel.setLabel("Enable Error Level")
    syswifiDebugErrLevel.setHelp(wifi_helpkeyword)
    syswifiDebugErrLevel.setVisible(True)
    syswifiDebugErrLevel.setDefaultValue(False)
    #syswifiDebugErrLevel.setDependencies(syswifiMenuVisible, ["SYS_WIFI_APPDEBUG_ENABLE"])

    syswifiDebugDbgLevel = syswifiComponent.createBooleanSymbol("SYS_WIFI_APPDEBUG_DBG_LEVEL", syswifiDebugBasicMenu)
    syswifiDebugDbgLevel.setLabel("Enable Debug Level")
    syswifiDebugDbgLevel.setHelp(wifi_helpkeyword)
    syswifiDebugDbgLevel.setVisible(True)
    syswifiDebugDbgLevel.setDefaultValue(False)
    #syswifiDebugDbgLevel.setDependencies(syswifiMenuVisible, ["SYS_WIFI_APPDEBUG_ENABLE"])

    syswifiDebugInfoLevel = syswifiComponent.createBooleanSymbol("SYS_WIFI_APPDEBUG_INFO_LEVEL", syswifiDebugBasicMenu)
    syswifiDebugInfoLevel.setLabel("Enable Info Level")
    syswifiDebugInfoLevel.setHelp(wifi_helpkeyword)
    syswifiDebugInfoLevel.setVisible(True)
    syswifiDebugInfoLevel.setDefaultValue(False)
    #syswifiDebugInfoLevel.setDependencies(syswifiMenuVisible, ["SYS_WIFI_APPDEBUG_ENABLE"])

    syswifiDebugFuncLevel = syswifiComponent.createBooleanSymbol("SYS_WIFI_APPDEBUG_FUNC_LEVEL", syswifiDebugBasicMenu)
    syswifiDebugFuncLevel.setLabel("Enable Function Entry/Exit Level")
    syswifiDebugFuncLevel.setHelp(wifi_helpkeyword)
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
    syswifiDebugFlowBasicMenu.setHelp(wifi_helpkeyword)
    syswifiDebugFlowBasicMenu.setVisible(True)
    #syswifiDebugFlowBasicMenu.setDefaultValue(False)
    syswifiDebugFlowBasicMenu.setDependencies(syswifiMenuVisible, ["SYS_WIFI_APPDEBUG_ENABLE"])

    syswifiDebugFlowCfgFlow = syswifiComponent.createBooleanSymbol("SYS_WIFI_APPDEBUG_CFG_FLOW", syswifiDebugFlowBasicMenu)
    syswifiDebugFlowCfgFlow.setLabel("Enable WiFi Cfg Flow")
    syswifiDebugFlowCfgFlow.setHelp(wifi_helpkeyword)
    syswifiDebugFlowCfgFlow.setDefaultValue(False)
    syswifiDebugFlowCfgFlow.setVisible(True)

    syswifiDebugConnectFlow = syswifiComponent.createBooleanSymbol("SYS_WIFI_APPDEBUG_CONNECT_FLOW", syswifiDebugFlowBasicMenu)
    syswifiDebugConnectFlow.setLabel("Enable WiFi Connect Flow")
    syswifiDebugConnectFlow.setHelp(wifi_helpkeyword)
    syswifiDebugConnectFlow.setDefaultValue(False)
    syswifiDebugConnectFlow.setVisible(True)

    syswifiDebugProvFlow = syswifiComponent.createBooleanSymbol("SYS_WIFI_APPDEBUG_PROVISIONING_FLOW", syswifiDebugFlowBasicMenu)
    syswifiDebugProvFlow.setLabel("Enable WiFi Provisioning Flow")
    syswifiDebugProvFlow.setHelp(wifi_helpkeyword)
    syswifiDebugProvFlow.setDefaultValue(False)
    syswifiDebugProvFlow.setVisible(True)

    syswifiDebugProvCMDFlow = syswifiComponent.createBooleanSymbol("SYS_WIFI_APPDEBUG_PROVISIONINGCMD_FLOW", syswifiDebugFlowBasicMenu)
    syswifiDebugProvCMDFlow.setLabel("Enable WiFi Provisioning Command Flow")
    syswifiDebugProvCMDFlow.setHelp(wifi_helpkeyword)
    syswifiDebugProvCMDFlow.setDefaultValue(False)
    syswifiDebugProvCMDFlow.setVisible(True)

    syswifiDebugProvSOCKFlow = syswifiComponent.createBooleanSymbol("SYS_WIFI_APPDEBUG_PROVISIONINGSOCK_FLOW", syswifiDebugFlowBasicMenu)
    syswifiDebugProvSOCKFlow.setLabel("Enable WiFi Provisioning Socket Flow")
    syswifiDebugProvSOCKFlow.setHelp(wifi_helpkeyword)
    syswifiDebugProvSOCKFlow.setDefaultValue(False)
    syswifiDebugProvSOCKFlow.setVisible(True)

    syswifiDebugPreStr = syswifiComponent.createStringSymbol("SYS_WIFI_APPDEBUG_PRESTR", syswifiDebugLogEnable)
    syswifiDebugPreStr.setLabel("Prefix String")
    syswifiDebugPreStr.setHelp(wifi_helpkeyword)
    syswifiDebugPreStr.setVisible(True)
    syswifiDebugPreStr.setDescription("Prefix String")
    syswifiDebugPreStr.setDefaultValue("WIFI_SRVC")
    syswifiDebugPreStr.setDependencies(syswifiMenuVisible, ["SYS_WIFI_APPDEBUG_ENABLE"])


    # RTOS Configuration
    syswifiRtosMenu = syswifiComponent.createMenuSymbol("SYS_WIFI_RTOS_MENU", syswifiAdvMenu)
    syswifiRtosMenu.setLabel("RTOS Configuration")
    syswifiRtosMenu.setHelp(wifi_helpkeyword)
    syswifiRtosMenu.setDescription("RTOS Configuration")
    syswifiRtosMenu.setVisible(False)
    syswifiRtosMenu.setVisible((Database.getSymbolValue("HarmonyCore", "SELECT_RTOS") != "BareMetal") and (Database.getSymbolValue("HarmonyCore", "SELECT_RTOS") != None))
    syswifiRtosMenu.setDependencies(syswifishowRTOSMenu, ["HarmonyCore.SELECT_RTOS"])


    # Menu for RTOS options
    syswifiInstnExecMode = syswifiComponent.createComboSymbol("SYS_WIFI_RTOS", syswifiRtosMenu, ["Standalone"]) 
    syswifiInstnExecMode.setLabel("Run Library Tasks as")
    syswifiInstnExecMode.setHelp(wifi_helpkeyword)
    syswifiInstnExecMode.setVisible(False)
    syswifiInstnExecMode.setDescription("Rtos Options")
    syswifiInstnExecMode.setDefaultValue("Standalone")

    # RTOS Task Stack Size
    syswifiTaskSize = syswifiComponent.createIntegerSymbol("SYS_WIFI_RTOS_TASK_STACK_SIZE", syswifiRtosMenu)
    syswifiTaskSize.setLabel("Stack Size")
    syswifiTaskSize.setHelp(wifi_helpkeyword)
    syswifiTaskSize.setVisible(True)
    syswifiTaskSize.setDescription("Rtos Task Stack Size")
    syswifiTaskSize.setDefaultValue(1024)
    syswifiTaskSize.setDependencies(syswifiRTOSStandaloneMenu, ["SYS_WIFI_RTOS"])

    # RTOS Task Priority
    syswifiTaskPriority = syswifiComponent.createIntegerSymbol("SYS_WIFI_RTOS_TASK_PRIORITY", syswifiRtosMenu)
    syswifiTaskPriority.setLabel("Task Priority")
    syswifiTaskPriority.setHelp(wifi_helpkeyword)
    syswifiTaskPriority.setVisible(True)
    syswifiTaskPriority.setDescription("Rtos Task Priority")
    syswifiTaskPriority.setDefaultValue(1)
    syswifiTaskPriority.setDependencies(syswifiRTOSStandaloneMenu, ["SYS_WIFI_RTOS"])

    # RTOS Use Task Delay?
    syswifiUseTaskDelay = syswifiComponent.createBooleanSymbol("SYS_WIFI_RTOS_USE_DELAY", syswifiRtosMenu)
    syswifiUseTaskDelay.setLabel("Use Task Delay?")
    syswifiUseTaskDelay.setHelp(wifi_helpkeyword)
    syswifiUseTaskDelay.setVisible(True)
    syswifiUseTaskDelay.setDescription("Rtos Use Task Delay?")
    syswifiUseTaskDelay.setDefaultValue(True)
    syswifiUseTaskDelay.setDependencies(syswifiRTOSStandaloneMenu, ["SYS_WIFI_RTOS"])

    # RTOS Task Delay
    syswifiTaskDelay = syswifiComponent.createIntegerSymbol("SYS_WIFI_RTOS_DELAY", syswifiRtosMenu)
    syswifiTaskDelay.setLabel("Task Delay")
    syswifiTaskDelay.setHelp(wifi_helpkeyword)
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
        print("Set Symbol Failure" + component + ":" + symbol + ":" + str(value))
        return False
    else:
        return True

#Handle messages from other components
def handleMessage(messageID, args):
    retDict= {}
    if (messageID == "SET_SYMBOL"):
        print("handleMessage: Set Symbol")
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
    password = data.getSymbolByID("SYS_WIFI_STA_PWD_NAME")
    userDomainName = data.getSymbolByID("SYS_WIFI_STA_ENT_USER_NAME")
    serverDomainNameSAN = data.getSymbolByID("SYS_WIFI_STA_ENT_SERVER_DOMAIN_SAN")
    serverDomainNameCN = data.getSymbolByID("SYS_WIFI_STA_ENT_SERVER_DOMAIN_CN")
    date = data.getSymbolByID("SYS_WIFI_STA_ENT_DATE")
    CACertFormat = data.getSymbolByID("SYS_WIFI_STA_CACERT_FORMAT")
    CACertFileName = data.getSymbolByID("SYS_WIFI_STA_ENT_CACERT_FILE_NAME")
    CACertModuleName = data.getSymbolByID("SYS_WIFI_STA_ENT_CACERT_MODULE_NAME")
    PrivateCertFormat = data.getSymbolByID("SYS_WIFI_STA_PRIVATE_CERT_FORMAT")
    PrivateCertFileName = data.getSymbolByID("SYS_WIFI_STA_ENT_PRIVATE_CERT_FILE_NAME")
    PrivateCertModuleName = data.getSymbolByID("SYS_WIFI_STA_ENT_PRIVATE_CERT_MODULE_NAME")
    PrivateKeyFormat = data.getSymbolByID("SYS_WIFI_STA_PRIVATE_KEY_FORMAT")
    PrivateKeyFileName = data.getSymbolByID("SYS_WIFI_STA_ENT_PRIVATE_KEY_FILE_NAME")
    PrivateKeyModuleName = data.getSymbolByID("SYS_WIFI_STA_ENT_PRIVATE_KEY_MODULE_NAME")
    syswifistaEnt = data.getSymbolByID("SYS_WIFI_SUPPORT_ENTERPRISE")

    utc_dt = datetime.strptime(data.getSymbolValue("SYS_WIFI_STA_ENT_DATE"),'%Y-%m-%dT%H:%M:%S.%fZ')
    unixDate = int((utc_dt - datetime(1970, 1, 1)).total_seconds())
    diff = data.getSymbolValue("SYS_WIFI_STA_ENT_DATE_EPOCH")
    if(diff!=unixDate):
        data.setSymbolValue("SYS_WIFI_STA_ENT_DATE_EPOCH",unixDate)

    if(sysWiFisecurity == "OPEN"):        
        password.setVisible(False)
        userDomainName.setVisible(False)
        serverDomainNameSAN.setVisible(False)
        serverDomainNameCN.setVisible(False)
        date.setVisible(False)
        CACertFormat.setVisible(False)
        CACertFileName.setVisible(False)
        CACertModuleName.setVisible(False)
        PrivateCertFormat.setVisible(False)
        PrivateCertFileName.setVisible(False)
        PrivateCertModuleName.setVisible(False)
        PrivateKeyFormat.setVisible(False)
        PrivateKeyFileName.setVisible(False)
        PrivateKeyModuleName.setVisible(False)
        syswifistaEnt.setVisible(False)
    elif(sysWiFisecurity == "WPA2" or sysWiFisecurity == "WPA3" or sysWiFisecurity == "WPA2WPA3"):        
        if(sysWiFiWPAPwdlen < 8):
            ErrCommSymbol.setLabel("****Error:Minimum STA Password length is 8 characters.")
            ErrCommSymbol.setVisible(True)
        elif(sysWiFiWPAPwdlen > 63):
            ErrCommSymbol.setLabel("****Error:Maximum STA Password length is 63 characters.")
            ErrCommSymbol.setVisible(True)
        else:
            ErrCommSymbol.setLabel("")
            ErrCommSymbol.setVisible(False)
            password.setVisible(True)
            userDomainName.setVisible(False)
            serverDomainNameSAN.setVisible(False)
            serverDomainNameCN.setVisible(False)
            date.setVisible(False)
            CACertFormat.setVisible(False)
            CACertFileName.setVisible(False)
            CACertModuleName.setVisible(False)
            PrivateCertFormat.setVisible(False)
            PrivateCertFileName.setVisible(False)
            PrivateCertModuleName.setVisible(False)
            PrivateKeyFormat.setVisible(False)
            PrivateKeyFileName.setVisible(False)
            PrivateKeyModuleName.setVisible(False)
            syswifistaEnt.setVisible(False)
    else:
        password.setVisible(False)
        userDomainName.setVisible(True)
        serverDomainNameSAN.setVisible(True)
        serverDomainNameCN.setVisible(True)
        date.setVisible(True)
        CACertFormat.setVisible(True)
        CACertFileName.setVisible(True)
        CACertModuleName.setVisible(True)
        PrivateCertFormat.setVisible(True)
        PrivateCertFileName.setVisible(True)
        PrivateCertModuleName.setVisible(True)
        PrivateKeyFormat.setVisible(True)
        PrivateKeyFileName.setVisible(True)
        PrivateKeyModuleName.setVisible(True)
        syswifistaEnt.setVisible(False)

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

wolfssl = False
pic32 = False

def syswifiSTAMenu(symbol, event):
    autoConnectTableCrypto = [["lib_crypto", "LIB_CRYPTO_WOLFCRYPT_Dependency", "lib_wolfcrypt", "lib_wolfcrypt"]] 
    autoConnectTableWolfssl = [["lib_wolfssl", "WolfSSL_Crypto_Dependency", "lib_wolfcrypt", "lib_wolfcrypt"]]
    autoConnectTablePIC32 = [["drvWifiPic32mzw1","BigIntSw_Dependency", "lib_wolfcrypt", "lib_wolfcrypt"]]
    
    if (event["value"] == "WPAWPA2-Enterprise" or event["value"] == "WPA2-Enterprise" or event["value"] == "WPA2WPA3-Enterprise" or event["value"] == "WPA3-Enterprise"):
        global wolfssl, pic32
        if(Database.getSymbolValue("drvWifiPic32mzw1","DRV_WIFI_PIC32MZW1_SUPPORT_ENTERPRISE") == True):        
            Database.setSymbolValue("sysWifiPic32mzw1", "SYS_WIFI_SUPPORT_ENTERPRISE", True)
        else:
            Database.setSymbolValue("sysWifiPic32mzw1", "SYS_WIFI_SUPPORT_ENTERPRISE", False)
        
        if(Database.getComponentByID("lib_wolfcrypt") == None):
            res = Database.activateComponents(["lib_wolfcrypt"],"System Configuration")

        if(Database.getComponentByID("lib_wolfssl") == None):
            res = Database.activateComponents(["lib_wolfssl"],"System Configuration")
            res = Database.connectDependencies(autoConnectTableWolfssl)
            wolfssl=True

        if(Database.getComponentByID("lib_crypto") == None):
            print(True)
            res = Database.activateComponents(["lib_crypto"],"System Configuration") 

        if(Database.getComponentByID("drv_ba414e") == None):
            res = Database.activateComponents(["drv_ba414e"],"System Configuration") 
            
        if(Database.getComponentByID("tcpipSntp") == None):
            res = Database.activateComponents(["tcpipSntp"],"APPLICATION LAYER")
        

        if(wolfssl==False):
            res = Database.connectDependencies(autoConnectTableWolfssl)
            wolfssl=True

        if(pic32==False):
            res = Database.connectDependencies(autoConnectTablePIC32)
            pic32=True

        if(Database.getSymbolValue("lib_wolfssl", "wolfsslSmallStackSupport") != True ):
            Database.setSymbolValue("lib_wolfssl", "wolfsslSmallStackSupport", True)
        if(Database.getSymbolValue("lib_wolfssl", "wolfsslOsalHeapKeys") != True):
            Database.setSymbolValue("lib_wolfssl", "wolfsslOsalHeapKeys", True)
        if(Database.getSymbolValue("lib_wolfssl", "wolfsslUseFastMath") != True):
            Database.setSymbolValue("lib_wolfssl", "wolfsslUseFastMath", True)
        if(Database.getSymbolValue("lib_wolfcrypt", "wolfcrypt_hw") != True):
            Database.setSymbolValue("lib_wolfcrypt","wolfcrypt_hw", True)
        if(Database.getSymbolValue("lib_wolfcrypt", "wolfcrypt_md4") != True):
            Database.setSymbolValue("lib_wolfcrypt","wolfcrypt_md4", True)
        if(Database.getSymbolValue("lib_wolfcrypt", "wolfcrypt_dsa") != True):
            Database.setSymbolValue("lib_wolfcrypt","wolfcrypt_dsa", True)
        if(Database.getSymbolValue("lib_wolfcrypt", "cryptoRsaStatic") != True):
            Database.setSymbolValue("lib_wolfcrypt","cryptoRsaStatic", True)
        if(Database.getSymbolValue("lib_wolfcrypt", "wolfcrypt_rsaKeySize") != "4096 bits"):
            Database.setSymbolValue("lib_wolfcrypt","wolfcrypt_rsaKeySize", "4096 bits")
        if(Database.getSymbolValue("lib_wolfcrypt", "wolfcrypt_dh") != True):
            Database.setSymbolValue("lib_wolfcrypt","wolfcrypt_dh", True)
        if(Database.getSymbolValue("lib_wolfcrypt", "wolfcrypt_dh_old_prime") != True):    
            Database.setSymbolValue("lib_wolfcrypt","wolfcrypt_dh_old_prime", True)
        if(Database.getSymbolValue("lib_wolfcrypt", "wolfSslRTOSSupport") != "FreeRTOS"):
            Database.setSymbolValue("lib_wolfcrypt","wolfSslRTOSSupport", "FreeRTOS")
        if(Database.getSymbolValue("lib_wolfcrypt", "wolfcrypt_aes_ccm") == True):
            Database.setSymbolValue("lib_wolfcrypt","wolfcrypt_aes_ccm", False)
    else:
        if(Database.getComponentByID("lib_wolfssl") != None):
            print("Deactivating WolfSSL")
            Database.setSymbolValue("lib_wolfssl","wolfssl", False)
            res = Database.deactivateComponents(["lib_wolfssl"])

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
        if(Database.getSymbolValue("sysWifiPic32mzw1", "SYS_WIFI_STA_ENABLE") == True):
           if(Database.getSymbolValue("tcpipSntp", "TCPIP_NTP_TASK_TICK_RATE" == 1100 )):
               Database.clearSymbolValue("tcpipSntp", "TCPIP_NTP_TASK_TICK_RATE")
               Database.setSymbolValue("tcpipSntp", "TCPIP_NTP_TASK_TICK_RATE", 10)
           if(Database.getSymbolValue("HarmonyCore", "SELECT_RTOS") != "BareMetal"):
               Database.setSymbolValue("FreeRTOS", "FREERTOS_TICK_RATE_HZ", 250)
               ret = Database.getSymbolValue("HarmonyCore", "GEN_APP_TASK_COUNT")
               for count in range(0, ret):   
                   Database.setSymbolValue("HarmonyCore", "GEN_APP_RTOS_TASK_" + str(count) + "_USE_DELAY" ,True)
                   Database.setSymbolValue("HarmonyCore", "GEN_APP_RTOS_TASK_" + str(count) + "_DELAY" ,4000)
               if(Database.getSymbolValue("sysWifiPic32mzw1", "SYS_WIFI_RTOS_USE_DELAY") == True):
                   Database.setSymbolValue("sysWifiPic32mzw1", "SYS_WIFI_RTOS_DELAY", 4)
               if(Database.getSymbolValue("tcpipStack", "TCPIP_STACK_RTOS_USE_DELAY") == True):
                   Database.setSymbolValue("tcpipStack", "TCPIP_STACK_RTOS_DELAY", 4)

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
    if(Database.getSymbolValue("sysWifiPic32mzw1", "SYS_WIFI_STA_ENABLE") == True):
        if(Database.getSymbolValue("tcpipSntp", "TCPIP_NTP_TASK_TICK_RATE") == 1100 ):
           Database.clearSymbolValue("tcpipSntp", "TCPIP_NTP_TASK_TICK_RATE")
           Database.setSymbolValue("tcpipSntp", "TCPIP_NTP_TASK_TICK_RATE", 10)
           if(Database.getSymbolValue("HarmonyCore", "SELECT_RTOS") != "BareMetal"):
               Database.setSymbolValue("FreeRTOS", "FREERTOS_TICK_RATE_HZ", 250)
               Database.setSymbolValue("HarmonyCore", "GEN_APP_RTOS_TASK_USE_DELAY" ,True)
               Database.setSymbolValue("HarmonyCore", "GEN_APP_RTOS_TASK_DELAY" ,4000)
               ret = Database.getSymbolValue("HarmonyCore", "GEN_APP_TASK_COUNT")
               for count in range(0, ret):   
                   Database.setSymbolValue("HarmonyCore", "GEN_APP_RTOS_TASK_" + str(count) + "_USE_DELAY" ,True)
                   Database.setSymbolValue("HarmonyCore", "GEN_APP_RTOS_TASK_" + str(count) + "_DELAY" ,4000)
               if(Database.getSymbolValue("sysWifiPic32mzw1", "SYS_WIFI_RTOS_USE_DELAY") == True):
                   Database.setSymbolValue("sysWifiPic32mzw1", "SYS_WIFI_RTOS_DELAY", 4)
               if(Database.getSymbolValue("tcpipStack", "TCPIP_STACK_RTOS_USE_DELAY") == True):
                   Database.setSymbolValue("tcpipStack", "TCPIP_STACK_RTOS_DELAY", 4)
        

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