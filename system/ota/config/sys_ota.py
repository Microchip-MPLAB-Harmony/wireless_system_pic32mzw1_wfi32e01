# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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
global ota_helpkeyword

ota_helpkeyword = "mcc_h3_pic32mzw1_ota_system_service_configurations"
################################################################################
#### Business Logic ####
################################################################################

################################################################################
#### Component ####
################################################################################
def dependencyOnValueChanged(symbol, event):
    symbol.setEnabled(True)
    
def setVisible_OnValueChanged(symbol, event):
    symbol.setVisible(event['value'])

def instantiateComponent(sysOTAPic32mzw1Component):
    
    global ota_helpkeyword
    #-------------------------------------------------------------------------#
    #                           OTA main menu                        #
    #-------------------------------------------------------------------------#
    sysotaResetEnable = sysOTAPic32mzw1Component.createBooleanSymbol("SYS_OTA_AUTORESET_ENABLE", None)
    sysotaResetEnable.setLabel("Auto reset")
    sysotaResetEnable.setHelp(ota_helpkeyword)
    sysotaResetEnable.setDescription('enable auto system reset after new image downloaded')
    sysotaResetEnable.setVisible(True)
    sysotaResetEnable.setDefaultValue(True)
    
    sysotaURL = sysOTAPic32mzw1Component.createStringSymbol("SYS_OTA_URL", None)
    sysotaURL.setLabel("server URL")
    sysotaURL.setHelp(ota_helpkeyword)
    sysotaURL.setVisible(True)
    sysotaURL.setDescription("Server address (http://server addr../ota.json)")
    sysotaURL.setDefaultValue("http://192.168.43.173:8000/ota.json")

    sysotaAutoUpdateEnable = sysOTAPic32mzw1Component.createBooleanSymbol("SYS_OTA_AUTOUPDATE_ENABLE", None)
    sysotaAutoUpdateEnable.setLabel("Auto OTA update")
    sysotaAutoUpdateEnable.setHelp(ota_helpkeyword)
    sysotaAutoUpdateEnable.setDescription('enable auto ota update')
    sysotaAutoUpdateEnable.setVisible(True)
    sysotaAutoUpdateEnable.setDefaultValue(True)
        
    symbol = sysOTAPic32mzw1Component.createBooleanSymbol("SYS_OTA_PERODIC_UPDATE", None)
    symbol.setLabel("Periodic OTA check")
    symbol.setHelp(ota_helpkeyword)
    symbol.setDescription("System checks update with server periodically if enables this option")
    symbol.setVisible(True)
    symbol.setDefaultValue(True)
        
    symbol_interval = sysOTAPic32mzw1Component.createIntegerSymbol("SYS_OTA_TIME_INTERVAL", symbol)
    symbol_interval.setLabel("Time inerval(sec)")
    symbol_interval.setHelp(ota_helpkeyword)
    symbol_interval.setMin(0)
    symbol_interval.setMax(7200)
    symbol_interval.setDefaultValue(60)
    symbol_interval.setDescription("Periodic check time interval")
    symbol_interval.setDependencies(setVisible_OnValueChanged, ['SYS_OTA_PERODIC_UPDATE'])
    symbol_interval.setVisible(True)
    
    sysotaAppVersion = sysOTAPic32mzw1Component.createIntegerSymbol("SYS_OTA_APP_VER_NUM", None)
    sysotaAppVersion.setLabel("Application version")
    sysotaAppVersion.setHelp(ota_helpkeyword)
    sysotaAppVersion.setMin(0)
    sysotaAppVersion.setMax(255)
    sysotaAppVersion.setDefaultValue(1)
    sysotaAppVersion.setDescription("Version number of ota application image")
    sysotaAppVersion.setVisible(True)

    symbol_debug = sysOTAPic32mzw1Component.createCommentSymbol("SYS_OTA_DEBUG_MENU", None)
    symbol_debug.setLabel("DEBUG")
    symbol_debug.setHelp(ota_helpkeyword)
    symbol_debug.setVisible(True)
    
    symbol_CLICMD_enabling = sysOTAPic32mzw1Component.createBooleanSymbol("SYS_OTA_CLICMD_ENABLED", symbol_debug)
    symbol_CLICMD_enabling.setLabel("Enable CLI commands")
    symbol_CLICMD_enabling.setHelp(ota_helpkeyword)
    symbol_CLICMD_enabling.setVisible(True)
    symbol_CLICMD_enabling.setDefaultValue(True)
    symbol_CLICMD_enabling.setDescription("Enable OTA CLI command")
    
    symbol_APPDEBUG_enabling = sysOTAPic32mzw1Component.createBooleanSymbol("SYS_OTA_APPDEBUG_ENABLED", symbol_debug)
    symbol_APPDEBUG_enabling.setLabel("Enable Debug Logs")
    symbol_APPDEBUG_enabling.setHelp(ota_helpkeyword)
    symbol_APPDEBUG_enabling.setVisible(True)
    symbol_APPDEBUG_enabling.setDefaultValue(False)
    symbol_APPDEBUG_enabling.setDescription("Enable OTA debug log")
    
    menu = sysOTAPic32mzw1Component.createMenuSymbol('OTA_RTOS', None)
    menu.setVisible(False)
    if menu != None:

        symbol = sysOTAPic32mzw1Component.createIntegerSymbol("OTA_RTOS_TASK_DELAY", menu)
        symbol.setLabel("RTOS Task Delay (ms)")
        symbol.setHelp(ota_helpkeyword)
        symbol.setMin(0)
        symbol.setMax(100)
        symbol.setDefaultValue(1)
        symbol.setReadOnly(True)
        symbol.setVisible(False)

        symbol = sysOTAPic32mzw1Component.createIntegerSymbol("OTA_RTOS_STACK_SIZE", menu)
        symbol.setLabel("RTOS Task Stack Size")
        symbol.setHelp(ota_helpkeyword)
        symbol.setDefaultValue(1024)
        symbol.setReadOnly(True)
        symbol.setVisible(False)

        symbol = sysOTAPic32mzw1Component.createIntegerSymbol("OTA_RTOS_TASK_PRIORITY", menu)
        symbol.setLabel("RTOS Task Priority")
        symbol.setHelp(ota_helpkeyword)
        symbol.setDefaultValue(1)
        symbol.setReadOnly(True)
        symbol.setVisible(False)   
        
    #-------------------------------------------------------------------------#
    #                           Advanced configuration                         #
    #-------------------------------------------------------------------------#
    
    symbol = sysOTAPic32mzw1Component.createCommentSymbol("SYS_OTA_ADVANCED_CONFIG_MENU", None)
    symbol.setLabel("Advanced Configuration")
    symbol.setHelp(ota_helpkeyword)
    symbol.setVisible(True)
    #syswifiAdvMenu.setDefaultValue(False)
        
    symbol_max_img = sysOTAPic32mzw1Component.createIntegerSymbol("SYS_OTA_NUM_IMGS", symbol)
    symbol_max_img.setLabel("Number of images")
    symbol_max_img.setHelp(ota_helpkeyword)
    symbol_max_img.setMin(0)
    symbol_max_img.setMax(5)
    symbol_max_img.setDefaultValue(2)
    symbol_max_img.setDescription("Number of images entry supported by database in external flash")
    symbol_max_img.setVisible(True)
    
    symbol_JSON_buf_size = sysOTAPic32mzw1Component.createIntegerSymbol("SYS_OTA_JSON_FILE_MAXSIZE", symbol)
    symbol_JSON_buf_size.setLabel("Set JSON file size in bytes")
    symbol_JSON_buf_size.setHelp(ota_helpkeyword)
    symbol_JSON_buf_size.setMin(0)
    symbol_JSON_buf_size.setMax(1000)
    symbol_JSON_buf_size.setDefaultValue(1000)
    symbol_JSON_buf_size.setDescription("Set JSON file size in bytes")
    symbol_JSON_buf_size.setVisible(True)
    
    symbol_tls_enabling = sysOTAPic32mzw1Component.createBooleanSymbol("SYS_OTA_ENFORCE_TLS", symbol)
    symbol_tls_enabling.setLabel("Enforce TLS")
    symbol_tls_enabling.setHelp(ota_helpkeyword)
    symbol_tls_enabling.setVisible(True)
    #symbol_tls_enabling.setDefaultValue(True)
    symbol_tls_enabling.setDescription("Enforcing TLS for OTA")
    
    symbol_sector_check_enabling = sysOTAPic32mzw1Component.createBooleanSymbol("SYS_OTA_FREE_SECTOR_CHECK_ENABLE", symbol)
    symbol_sector_check_enabling.setLabel("Disk space check")
    symbol_sector_check_enabling.setHelp(ota_helpkeyword)
    symbol_sector_check_enabling.setVisible(True)
    symbol_sector_check_enabling.setDefaultValue(False)
    symbol_sector_check_enabling.setDescription("To Enable free sector check in ext flash before download starts")
    
    symbol_patch_enabling = sysOTAPic32mzw1Component.createBooleanSymbol("SYS_OTA_PATCH_ENABLE", symbol)
    symbol_patch_enabling.setLabel("Enable/Disable Patch Functionality")
    symbol_patch_enabling.setHelp(ota_helpkeyword)
    symbol_patch_enabling.setVisible(True)
    symbol_patch_enabling.setDefaultValue(False)
    symbol_patch_enabling.setDescription("To Enable patch functionality support")
    
    symbol_secure_ota_enabling = sysOTAPic32mzw1Component.createBooleanSymbol("SYS_OTA_SECURE_BOOT_ENABLED", symbol)
    symbol_secure_ota_enabling.setLabel("Enable/Disable Secure OTA Functionality")
    symbol_secure_ota_enabling.setVisible(True)
    symbol_secure_ota_enabling.setHelp(ota_helpkeyword)
    symbol_secure_ota_enabling.setDefaultValue(False)
    symbol_secure_ota_enabling.setDescription("To Enable Secure OTA functionality support")

    ############################################################################
    #### Code Generation ####
    ############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")
    
    sysotaSourceFile = sysOTAPic32mzw1Component.createFileSymbol("SYS_OTA_SOURCE", None)
    sysotaSourceFile.setSourcePath("system/ota/framework/sys_ota.c")
    sysotaSourceFile.setOutputName("sys_ota.c")
    sysotaSourceFile.setDestPath("system/ota/")
    sysotaSourceFile.setProjectPath("config/" + configName + "/system/ota/")
    sysotaSourceFile.setType("SOURCE")
    sysotaSourceFile.setMarkup(True)
    sysotaSourceFile.setEnabled(True)
    
    ########### system header #################
    sysotaHeaderFile = sysOTAPic32mzw1Component.createFileSymbol("SYS_OTA_HEADER", None)
    sysotaHeaderFile.setSourcePath("system/ota/framework/sys_ota.h")
    sysotaHeaderFile.setOutputName("sys_ota.h")
    sysotaHeaderFile.setDestPath("system/ota/")
    sysotaHeaderFile.setProjectPath("config/" + configName + "/system/ota/")
    sysotaHeaderFile.setType("HEADER")
    sysotaHeaderFile.setMarkup(True)
    sysotaHeaderFile.setEnabled(True)
    ########### system header end #################
    
    sysotaSourceFile = sysOTAPic32mzw1Component.createFileSymbol("OTA_SOURCE", None)
    sysotaSourceFile.setSourcePath("system/ota/framework/ota.c")
    sysotaSourceFile.setOutputName("ota.c")
    sysotaSourceFile.setDestPath("system/ota/framework/")
    sysotaSourceFile.setProjectPath("config/" + configName + "/system/ota/framework/")
    sysotaSourceFile.setType("SOURCE")
    sysotaSourceFile.setMarkup(True)
    sysotaSourceFile.setEnabled(True)

    sysotaHeaderFile = sysOTAPic32mzw1Component.createFileSymbol("OTA_HEADER", None)
    sysotaHeaderFile.setSourcePath("system/ota/framework/ota.h")
    sysotaHeaderFile.setOutputName("ota.h")
    sysotaHeaderFile.setDestPath("system/ota/framework/")
    sysotaHeaderFile.setProjectPath("config/" + configName + "/system/ota/framework/")
    sysotaHeaderFile.setType("HEADER")
    sysotaHeaderFile.setMarkup(True)
    sysotaHeaderFile.setEnabled(True)
    
    sysotaSourceFile = sysOTAPic32mzw1Component.createFileSymbol("OTA_DOWNLOADER_SOURCE", None)
    sysotaSourceFile.setSourcePath("system/ota/framework/downloader.c")
    sysotaSourceFile.setOutputName("downloader.c")
    sysotaSourceFile.setDestPath("system/ota/framework/")
    sysotaSourceFile.setProjectPath("config/" + configName + "/system/ota/framework/")
    sysotaSourceFile.setType("SOURCE")
    sysotaSourceFile.setMarkup(True)
    sysotaSourceFile.setEnabled(True)

    sysotaHeaderFile = sysOTAPic32mzw1Component.createFileSymbol("OTA_DOWNLOADER_HEADER", None)
    sysotaHeaderFile.setSourcePath("system/ota/framework/downloader.h")
    sysotaHeaderFile.setOutputName("downloader.h")
    sysotaHeaderFile.setDestPath("system/ota/framework")
    sysotaHeaderFile.setProjectPath("config/" + configName + "/system/ota/framework/")
    sysotaHeaderFile.setType("HEADER")
    sysotaHeaderFile.setMarkup(True)
    sysotaHeaderFile.setEnabled(True)
    
    
    sysotaHeaderFile = sysOTAPic32mzw1Component.createFileSymbol("OTA_IMG_HEADER", None)
    sysotaHeaderFile.setSourcePath("system/ota/framework/ota_image.h")
    sysotaHeaderFile.setOutputName("ota_image.h")
    sysotaHeaderFile.setDestPath("system/ota/framework/")
    sysotaHeaderFile.setProjectPath("config/" + configName + "/system/ota/framework/")
    sysotaHeaderFile.setType("HEADER")
    sysotaHeaderFile.setMarkup(True)
    sysotaHeaderFile.setEnabled(True)

    sysotaHeaderFile = sysOTAPic32mzw1Component.createFileSymbol("OTA_INT_FLASH_HEADER", None)
    sysotaHeaderFile.setSourcePath("system/ota/framework/int_flash.h")
    sysotaHeaderFile.setOutputName("int_flash.h")
    sysotaHeaderFile.setDestPath("system/ota/framework/")
    sysotaHeaderFile.setProjectPath("config/" + configName + "/system/ota/framework/")
    sysotaHeaderFile.setType("HEADER")
    sysotaHeaderFile.setMarkup(True)
    sysotaHeaderFile.setEnabled(True)
    
    sysotaSourceFile = sysOTAPic32mzw1Component.createFileSymbol("OTA_INT_FLASH_SOURCE", None)
    sysotaSourceFile.setSourcePath("system/ota/framework/int_flash.c")
    sysotaSourceFile.setOutputName("int_flash.c")
    sysotaSourceFile.setDestPath("system/ota/framework/")
    sysotaSourceFile.setProjectPath("config/" + configName + "/system/ota/framework/")
    sysotaSourceFile.setType("SOURCE")
    sysotaSourceFile.setMarkup(True)
    sysotaSourceFile.setEnabled(True)
    
    sysotaHeaderFile = sysOTAPic32mzw1Component.createFileSymbol("OTA_SHA_HEADER", None)
    sysotaHeaderFile.setSourcePath("system/ota/framework/sha256.h")
    sysotaHeaderFile.setOutputName("sha256.h")
    sysotaHeaderFile.setDestPath("system/ota/framework/")
    sysotaHeaderFile.setProjectPath("config/" + configName + "/system/ota/framework/")
    sysotaHeaderFile.setType("HEADER")
    sysotaHeaderFile.setMarkup(True)
    sysotaHeaderFile.setEnabled(True)
    
    sysotaSourceFile = sysOTAPic32mzw1Component.createFileSymbol("SHA_SOURCE", None)
    sysotaSourceFile.setSourcePath("system/ota/framework/sha256.c")
    sysotaSourceFile.setOutputName("sha256.c")
    sysotaSourceFile.setDestPath("system/ota/framework/")
    sysotaSourceFile.setProjectPath("config/" + configName + "/system/ota/framework/")
    sysotaSourceFile.setType("SOURCE")
    sysotaSourceFile.setMarkup(True)
    sysotaSourceFile.setEnabled(True)
    
    sysotaHeaderFile = sysOTAPic32mzw1Component.createFileSymbol("OTA_CONFIG_HEADER", None)
    sysotaHeaderFile.setSourcePath("system/ota/framework/ota_config.h")
    sysotaHeaderFile.setOutputName("ota_config.h")
    sysotaHeaderFile.setDestPath("system/ota/framework/")
    sysotaHeaderFile.setProjectPath("config/" + configName + "/system/ota/framework/")
    sysotaHeaderFile.setType("HEADER")
    sysotaHeaderFile.setMarkup(True)
    sysotaHeaderFile.setEnabled(True)
    
    sysotaSourceFile = sysOTAPic32mzw1Component.createFileSymbol("OTA_DATABASE_PARSER_SOURCE", None)
    sysotaSourceFile.setSourcePath("system/ota/framework/ota_database_parser.c")
    sysotaSourceFile.setOutputName("ota_database_parser.c")
    sysotaSourceFile.setDestPath("system/ota/framework/")
    sysotaSourceFile.setProjectPath("config/" + configName + "/system/ota/framework/")
    sysotaSourceFile.setType("SOURCE")
    sysotaSourceFile.setMarkup(True)
    sysotaSourceFile.setEnabled(True)
    
    sysotaHeaderFile = sysOTAPic32mzw1Component.createFileSymbol("OTA_DATABASE_PARSER_HEADER", None)
    sysotaHeaderFile.setSourcePath("system/ota/framework/ota_database_parser.h")
    sysotaHeaderFile.setOutputName("ota_database_parser.h")
    sysotaHeaderFile.setDestPath("system/ota/framework/")
    sysotaHeaderFile.setProjectPath("config/" + configName + "/system/ota/framework/")
    sysotaHeaderFile.setType("HEADER")
    sysotaHeaderFile.setMarkup(True)
    sysotaHeaderFile.setEnabled(True)
    
    sysotaSourceFile = sysOTAPic32mzw1Component.createFileSymbol("OTA_PATCH_SOURCE", None)
    sysotaSourceFile.setSourcePath("system/ota/framework/ota_patch.c.ftl")
    sysotaSourceFile.setOutputName("ota_patch.c")
    sysotaSourceFile.setDestPath("system/ota/framework/")
    sysotaSourceFile.setProjectPath("config/" + configName + "/system/ota/framework/")
    sysotaSourceFile.setType("SOURCE")
    sysotaSourceFile.setMarkup(True)
    sysotaSourceFile.setEnabled(True)
    
    sysotaHeaderFile = sysOTAPic32mzw1Component.createFileSymbol("OTA_PATCH_HEADER", None)
    sysotaHeaderFile.setSourcePath("system/ota/framework/ota_patch.h.ftl")
    sysotaHeaderFile.setOutputName("ota_patch.h")
    sysotaHeaderFile.setDestPath("system/ota/framework/")
    sysotaHeaderFile.setProjectPath("config/" + configName + "/system/ota/framework/")
    sysotaHeaderFile.setType("HEADER")
    sysotaHeaderFile.setMarkup(True)
    sysotaHeaderFile.setEnabled(True)
    
    ################################### SYSTEM ######################################
    sysotaHeaderFile = sysOTAPic32mzw1Component.createFileSymbol("OTA_SYS_DEF", None)
    sysotaHeaderFile.setType("STRING")
    sysotaHeaderFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    sysotaHeaderFile.setSourcePath("system/ota/templates/system/system_definitions.h.ftl")
    sysotaHeaderFile.setMarkup(True)

    sysotaHeaderFile = sysOTAPic32mzw1Component.createFileSymbol("OTA_SYS_CONFIG", None)
    sysotaHeaderFile.setType("STRING")
    sysotaHeaderFile.setOutputName("core.LIST_SYSTEM_CONFIG_H_SYSTEM_SERVICE_CONFIGURATION")
    sysotaHeaderFile.setSourcePath("system/ota/templates/system/system_config.h.ftl")
    sysotaHeaderFile.setMarkup(True)

    
    sysotaSourceFile = sysOTAPic32mzw1Component.createFileSymbol("OTA_SYS_INIT", None)
    sysotaSourceFile.setType("STRING")
    sysotaSourceFile.setOutputName("core.LIST_SYSTEM_INIT_C_INITIALIZE_SYSTEM_SERVICES")
    sysotaSourceFile.setSourcePath("system/ota/templates/system/system_initialize.c.ftl")
    sysotaSourceFile.setMarkup(True)
    
    
    sysotaSourceFile = sysOTAPic32mzw1Component.createFileSymbol("OTA_SYS_RTOS_TASK", None)
    sysotaSourceFile.setType("STRING")
    sysotaSourceFile.setOutputName("core.LIST_SYSTEM_RTOS_TASKS_C_DEFINITIONS")
    sysotaSourceFile.setSourcePath("system/ota/templates/system/system_rtos_tasks.c.ftl")
    sysotaSourceFile.setMarkup(True)
    #src.setDependencies(dependencyOnValueChanged, ["OTA_RESIGTER_SYSTEM_FILES"])

    sysotaSourceFile = sysOTAPic32mzw1Component.createFileSymbol("OTA_SYS_TASK", None)
    sysotaSourceFile.setType("STRING")
    sysotaSourceFile.setOutputName("core.LIST_SYSTEM_TASKS_C_CALL_DRIVER_TASKS")
    sysotaSourceFile.setSourcePath("system/ota/templates/system/system_tasks.c.ftl")
    sysotaSourceFile.setMarkup(True)
    #src.setDependencies(dependencyOnValueChanged, ["OTA_RESIGTER_SYSTEM_FILES"])
    
    
    ################################### LINKER ######################################
    projPath = 'ota_linker'
    
    for name in ["p32MZ1025W104132_application.ld"]:
        src = sysOTAPic32mzw1Component.createFileSymbol(None, None)
        src.setSourcePath("system/ota/framework/" + name)
        src.setOutputName(name)
        src.setDestPath("ota_linker")
        src.setProjectPath(projPath)
        src.setType(getFileType(name))
        src.setOverwrite(True)
        
        
    ################################### CJSON ######################################
    
    sysotaSourceFile = sysOTAPic32mzw1Component.createFileSymbol("SYS_CJSON_SOURCE", None)
    sysotaSourceFile.setSourcePath("system/ota/framework/cjson/cjson.c")
    sysotaSourceFile.setOutputName("cjson.c")
    sysotaSourceFile.setDestPath("system/ota/framework/cjson/")
    sysotaSourceFile.setProjectPath("config/" + configName + "/system/ota/framework/cjson")
    sysotaSourceFile.setType("SOURCE")
    sysotaSourceFile.setOverwrite(True)
    
    sysotaHeaderFile = sysOTAPic32mzw1Component.createFileSymbol("SYS_CJSON_JEADER", None)
    sysotaHeaderFile.setSourcePath("system/ota/framework/cjson/cjson.h")
    sysotaHeaderFile.setOutputName("cjson.h")
    sysotaHeaderFile.setDestPath("system/ota/framework/cjson/")
    sysotaHeaderFile.setProjectPath("config/" + configName + "/system/ota/framework/cjson")
    sysotaHeaderFile.setType("HEADER")
    sysotaHeaderFile.setMarkup(True)
    sysotaHeaderFile.setEnabled(True)
    
    ###################################  CSV ######################################
    
    sysotaSourceFile = sysOTAPic32mzw1Component.createFileSymbol("SYS_CSV_SOURCE", None)
    sysotaSourceFile.setSourcePath("system/ota/framework/csv/csv.c")
    sysotaSourceFile.setOutputName("csv.c")
    sysotaSourceFile.setDestPath("system/ota/framework/csv/")
    sysotaSourceFile.setProjectPath("config/" + configName + "/system/ota/framework/csv")
    sysotaSourceFile.setType("SOURCE")
    sysotaSourceFile.setOverwrite(True)
    
    sysotaHeaderFile = sysOTAPic32mzw1Component.createFileSymbol("SYS_CSV_HEADER", None)
    sysotaHeaderFile.setSourcePath("system/ota/framework//csv/csv.h")
    sysotaHeaderFile.setOutputName("csv.h")
    sysotaHeaderFile.setDestPath("system/ota/framework/csv/")
    sysotaHeaderFile.setProjectPath("config/" + configName + "/system/ota/framework/csv")
    sysotaHeaderFile.setType("HEADER")
    sysotaHeaderFile.setMarkup(True)
    sysotaHeaderFile.setEnabled(True)
    
    ###################################  PATCH ######################################
    sysotaHeaderFile = sysOTAPic32mzw1Component.createFileSymbol("SYS_PATCH_HEADER", None)
    sysotaHeaderFile.setSourcePath("system/ota/framework//patch/janpatch.h.ftl")
    sysotaHeaderFile.setOutputName("janpatch.h")
    sysotaHeaderFile.setDestPath("system/ota/framework/patch/")
    sysotaHeaderFile.setProjectPath("config/" + configName + "/system/ota/framework/patch")
    sysotaHeaderFile.setType("HEADER")
    sysotaHeaderFile.setMarkup(True)
    sysotaHeaderFile.setEnabled(True)
    
    ################################### HTTP client ######################################
    
    sysotaSourceFile = sysOTAPic32mzw1Component.createFileSymbol("SYS_HTTP_SOURCE", None)
    sysotaSourceFile.setSourcePath("system/ota/framework/http_client/http_client.c")
    sysotaSourceFile.setOutputName("http_client.c")
    sysotaSourceFile.setDestPath("system/ota/framework/http_client/")
    sysotaSourceFile.setProjectPath("config/" + configName + "/system/ota/framework/http_client")
    sysotaSourceFile.setType("SOURCE")
    sysotaSourceFile.setOverwrite(True)
    
    sysotaHeaderFile = sysOTAPic32mzw1Component.createFileSymbol("SYS_HTTP_HEADER", None)
    sysotaHeaderFile.setSourcePath("system/ota/framework/http_client/http_client.h")
    sysotaHeaderFile.setOutputName("http_client.h")
    sysotaHeaderFile.setDestPath("system/ota/framework/http_client/")
    sysotaHeaderFile.setProjectPath("config/" + configName + "/system/ota/framework/http_client")
    sysotaHeaderFile.setType("HEADER")
    sysotaHeaderFile.setMarkup(True)
    sysotaHeaderFile.setEnabled(True)
    
    ################################### hex2bin tool ######################################
    
    src = sysOTAPic32mzw1Component.createFileSymbol("SYS_BIN_EXE", None)
    src.setSourcePath("system/ota/framework/tools/hex2bin/hex2bin.exe")
    src.setOutputName("hex2bin.exe")
    src.setDestPath("../../../../tools/hex2bin/")
    src.setType("IMPORTANT")
    src.setMarkup(False)
    src.setEnabled(True)
    
    src = sysOTAPic32mzw1Component.createFileSymbol("SYS_BIN_PY", None)
    src.setSourcePath("system/ota/framework/tools/hex2bin/hex2bin.py")
    src.setOutputName("hex2bin.py")
    src.setDestPath("../../../../tools/hex2bin/")
    src.setType("IMPORTANT")
    src.setMarkup(False)
    src.setEnabled(True)
    
    ################################### ecdsaSign.py file ######################################
    
    src = sysOTAPic32mzw1Component.createFileSymbol("SYS_ECDSASIGN_PY", None)
    src.setSourcePath("system/ota/framework/tools/ecdsaSign.py")
    src.setOutputName("ecdsaSign.py")
    src.setDestPath("../../../../tools/")
    src.setType("IMPORTANT")
    src.setMarkup(False)
    src.setEnabled(True)
    
    ################################### OTA application ######################################
    
    sysotaSourceFile = sysOTAPic32mzw1Component.createFileSymbol("SYS_OTA_APP_SOURCE", None)
    sysotaSourceFile.setSourcePath("system/ota/framework/ota_app/app_ota.c")
    sysotaSourceFile.setOutputName("app_ota.c")
    sysotaSourceFile.setDestPath("system/ota/framework/ota_app/")
    #sysotaSourceFile.setProjectPath("config/" + configName + "/system/ota/framework/ota_app")
    sysotaSourceFile.setType("SOURCE")
    sysotaSourceFile.setOverwrite(True)
    
    sysotaHeaderFile = sysOTAPic32mzw1Component.createFileSymbol("SYS_OTA_APP_HEADER", None)
    sysotaHeaderFile.setSourcePath("system/ota/framework/ota_app/app_ota.h")
    sysotaHeaderFile.setOutputName("app_ota.h")
    sysotaHeaderFile.setDestPath("system/ota/framework/ota_app/")
    #sysotaHeaderFile.setProjectPath("config/" + configName + "/system/ota/framework/ota_app")
    sysotaHeaderFile.setType("HEADER")
    sysotaHeaderFile.setMarkup(True)
    sysotaHeaderFile.setEnabled(True)
    
    
    

def onAttachmentConnected(source, target):
    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    



def onAttachmentDisconnected(source, target):
    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    
    
       
def destroyComponent(component):
    res = Database.deactivateComponents(["nvm"])
    res = Database.deactivateComponents(["spi1"])
    res = Database.deactivateComponents(["System Configuration"])
    res = Database.deactivateComponents(["sysWifiPic32mzw1"])
    res = Database.deactivateComponents(["sysNetPic32mzw1"])



def getFileType(name):
    if name.endswith(".c") or name.endswith(".c.ftl"):
        return "SOURCE"
    if name.endswith(".h") or name.endswith(".h.ftl"):
        return "HEADER"
    if name.endswith(".ld") or name.endswith(".ld.ftl"):
        return "LINKER"
    return None
    
#-----------------------------------------------------------------------------#    
def finalizeComponent(sysOTAPic32mzw1Component):


    triggerDict = {}
    triggerDict = Database.sendMessage("core", "HEAP_SIZE", {"heap_size" : 170000})
    res = Database.activateComponents(["sysWifiPic32mzw1"])
    Database.setSymbolValue("sysWifiPic32mzw1", "SYS_WIFI_AP_ENABLE", False)
    
    sysotasysComponent = Database.createGroup(None,"System Configuration")    
    res = Database.activateComponents(["nvm"],"System Configuration", True)
    res = Database.activateComponents(["spi1"],"System Configuration", True)
    res = Database.activateComponents(["tmr2"],"System Configuration", True)
    res = Database.activateComponents(["rng"],"System Configuration", True)
    res = Database.activateComponents(["rtcc"],"System Configuration", True)
    Database.setSymbolValue("rtcc", "RTCC_INTERRUPT_MODE", True)
    Database.setSymbolValue("rtcc", "RTCC_ALARM_REPEAT_FOREVER", True)
    res = Database.activateComponents(["sys_fs"],"System Configuration", True)
    res = Database.activateComponents(["drv_sst26"],"System Configuration", True)
    res = Database.activateComponents(["drv_memory"],"System Configuration", True)
    
    
    autoConnectTableFilesystem = [["drv_sst26","drv_sst26_SPI_dependency","spi1","SPI1_SPI"]]
    autoConnectTableFilesystem1 = [["drv_memory_0","drv_memory_MEMORY_dependency","drv_sst26","memory"]]
    autoConnectTableFilesystem2 = [["sys_fs","sys_fs_DRV_MEDIA_dependency","drv_memory_0","drv_media"]]
    
    res = Database.connectDependencies(autoConnectTableFilesystem)
    res = Database.connectDependencies(autoConnectTableFilesystem1)
    res = Database.connectDependencies(autoConnectTableFilesystem2)
    
    
    Database.setSymbolValue("drv_memory", "DRV_MEMORY_COMMON_MODE", "Asynchronous")
    Database.setSymbolValue("drv_sst26", "SPI_CHIP_SELECT_PIN", 1)

    
    Database.setSymbolValue("core", "BSP_PIN_14_FUNCTION_TYPE", "GPIO")
    Database.setSymbolValue("core", "BSP_PIN_14_FUNCTION_NAME", "SPI1_CS")
    Database.setSymbolValue("core", "BSP_PIN_14_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_14_DIR", "OUT")
    Database.setSymbolValue("core", "BSP_PIN_14_DIR", "HIGH")
    Database.setSymbolValue("core", "CONFIG_HSSPIEN", "ON")
    Database.setSymbolValue("spi1", "SPI_SPICON_MSSEN", 1)
    Database.setSymbolValue("spi1", "SPI_BAUD_RATE", 30000000)
    Database.setSymbolValue("core", "ADD_LINKER_FILE", False)
    Database.setSymbolValue("rng", "RNGCON_TRNGEN", 1)
    Database.setSymbolValue("rng", "RNGCON_PRNGEN", 1)
    Database.setSymbolValue("rng", "RNGCON_CONT", 1)
    Database.setSymbolValue("sys_fs", "SYS_FS_MAX_FILES", 5)
    Database.setSymbolValue("sys_fs", "SYS_FS_RTOS_DELAY", 1)
    
    res = Database.activateComponents(["sysNetPic32mzw1"])
    Database.setSymbolValue("sysNetPic32mzw1", "SYS_NET_ENABLE_TLS", True)
#-----------------------------------------------------------------------------#
    
