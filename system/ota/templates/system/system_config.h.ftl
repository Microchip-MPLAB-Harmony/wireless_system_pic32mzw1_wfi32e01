/*** OTA Configuration ***/
<#if HarmonyCore.SELECT_RTOS == "FreeRTOS">
#define SYS_OTA_RTOS_STACK_SIZE     6144
#define SYS_OTA_RTOS_TASK_PRIORITY  1
</#if>   

<#if SYS_OTA_AUTORESET_ENABLE == true>
#define SYS_OTA_AUTORESET_ENABLE   			true
<#else>
#define SYS_OTA_AUTORESET_ENABLE   			false
</#if>
<#if SYS_OTA_AUTOUPDATE_ENABLE == true>
#define SYS_OTA_AUTOUPDATE_ENABLE           true
<#else>
#define SYS_OTA_AUTOUPDATE_ENABLE           false
</#if>
<#if SYS_OTA_PERODIC_UPDATE == true>
#define SYS_OTA_PERODIC_UPDATE   			true
<#else>
#define SYS_OTA_PERODIC_UPDATE   			false
</#if>
#define SYS_OTA_APP_VER_NUM                 ${SYS_OTA_APP_VER_NUM}
#define SYS_OTA_TIME_INTERVAL               ${SYS_OTA_TIME_INTERVAL}
#define SYS_OTA_URL                         "${SYS_OTA_URL}"
#define SYS_OTA_JSON_FILE_MAXSIZE           ${SYS_OTA_JSON_FILE_MAXSIZE}
#define SYS_OTA_NUM_IMGS                    ${SYS_OTA_NUM_IMGS}
#define SYS_OTA_INTF                        ${SYS_OTA_INTF}
<#if SYS_OTA_ENFORCE_TLS == true>
#define SYS_OTA_ENFORCE_TLS   			    true
<#else>
#define SYS_OTA_ENFORCE_TLS   			    false
</#if>
<#if SYS_OTA_CLICMD_ENABLED == true>
#define SYS_OTA_CLICMD_ENABLED   			    
</#if>
<#if SYS_OTA_APPDEBUG_ENABLED == true>
#define SYS_OTA_APPDEBUG_ENABLED   	
</#if>
<#if SYS_OTA_FREE_SECTOR_CHECK_ENABLE == true>
#define SYS_OTA_FREE_SECTOR_CHECK_ENABLE   	
</#if>
<#if SYS_OTA_PATCH_ENABLE == true>
#define SYS_OTA_PATCH_ENABLE   	
</#if>
<#if SYS_OTA_SECURE_BOOT_ENABLED == true>
#define SYS_OTA_SECURE_BOOT_ENABLED   	
</#if>
<#if SYS_OTA_HTTP_SECURE == true>
#define SYS_OTA_TLS_ENABLED   	
</#if>
<#if SYS_OTA_FILE_DOWNLOAD_ENABLE == true>
#define SYS_OTA_FILE_DOWNLOAD_ENABLED 
#define SYS_OTA_FILE_DOWNLOAD_START_ADDRESS  ${SYS_OTA_FILE_DOWNLOAD_ADDRESS}
#define SYS_OTA_NUM_OF_SLOTS                 ${SYS_OTA_NO_OF_SLOTS}
</#if>
<#if SYS_OTA_NO_OF_SLOTS == 1>
#define SYS_OTA_SLOT_0_SIZE                  ${SYS_OTA_FILE_SLOT_SIZE0}U
</#if>
<#if SYS_OTA_NO_OF_SLOTS == 2>
#define SYS_OTA_SLOT_0_SIZE                  ${SYS_OTA_FILE_SLOT_SIZE0}U
#define SYS_OTA_SLOT_1_SIZE                  ${SYS_OTA_FILE_SLOT_SIZE1}U
</#if>
<#if SYS_OTA_NO_OF_SLOTS == 3>
#define SYS_OTA_SLOT_0_SIZE                  ${SYS_OTA_FILE_SLOT_SIZE0}U
#define SYS_OTA_SLOT_1_SIZE                  ${SYS_OTA_FILE_SLOT_SIZE1}U
#define SYS_OTA_SLOT_2_SIZE                  ${SYS_OTA_FILE_SLOT_SIZE2}U
</#if>
<#if SYS_OTA_NO_OF_SLOTS == 4>
#define SYS_OTA_SLOT_0_SIZE                  ${SYS_OTA_FILE_SLOT_SIZE0}U
#define SYS_OTA_SLOT_1_SIZE                  ${SYS_OTA_FILE_SLOT_SIZE1}U
#define SYS_OTA_SLOT_2_SIZE                  ${SYS_OTA_FILE_SLOT_SIZE2}U
#define SYS_OTA_SLOT_3_SIZE                  ${SYS_OTA_FILE_SLOT_SIZE3}U
</#if>
<#if SYS_OTA_NO_OF_SLOTS == 5>
#define SYS_OTA_SLOT_0_SIZE                  ${SYS_OTA_FILE_SLOT_SIZE0}U
#define SYS_OTA_SLOT_1_SIZE                  ${SYS_OTA_FILE_SLOT_SIZE1}U
#define SYS_OTA_SLOT_2_SIZE                  ${SYS_OTA_FILE_SLOT_SIZE2}U
#define SYS_OTA_SLOT_3_SIZE                  ${SYS_OTA_FILE_SLOT_SIZE3}U
#define SYS_OTA_SLOT_4_SIZE                  ${SYS_OTA_FILE_SLOT_SIZE4}U
</#if>
<#if SYS_OTA_FILE_JUMP_ENABLE == true>
#define SYS_OTA_JUMP_TO_ADDRESS              ${SYS_OTA_FILE_JUMP_ADDRESS}U
</#if>

<#if SYS_OTA_FS_ENABLED == true>
#define SYS_OTA_ENABLE_FS true
<#else>
#define SYS_OTA_FS_ENABLE false
</#if>
<#if SYS_OTA_BOOTLOAD_FROM_DEDICATED_BOOTFLASH_ENABLED == true>
#define SYS_OTA_BOOTLOAD_FROM_DEDICATED_BOOTFLASH true
<#else>
#define SYS_OTA_BOOTLOAD_FROM_DEDICATED_BOOTFLASH false
</#if>