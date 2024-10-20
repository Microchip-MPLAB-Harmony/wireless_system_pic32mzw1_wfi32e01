/* WIFI System Service Configuration Options */
<#if SYS_WIFI_ENABLE == true>
<#if SYS_WIFI_MODE == "STA">
#define SYS_WIFI_DEVMODE        			SYS_WIFI_STA
<#elseif SYS_WIFI_MODE == "AP">
#define SYS_WIFI_DEVMODE        			SYS_WIFI_AP
</#if>


#define SYS_WIFI_MAX_CBS					${SYS_WIFI_MAX_CBS}
#define SYS_WIFI_COUNTRYCODE        	   "${SYS_WIFI_COUNTRYCODE}"
<#if SYS_WIFI_STA_ENABLE == true>
#define SYS_WIFI_STA_SSID        			"${SYS_WIFI_STA_SSID_NAME}"
#define SYS_WIFI_STA_PWD        			"${SYS_WIFI_STA_PWD_NAME}"

<#if SYS_WIFI_STA_AUTH == "WPAWPA2-Enterprise" || SYS_WIFI_STA_AUTH == "WPA2-Enterprise" || SYS_WIFI_STA_AUTH == "WPA2WPA3-Enterprise" || SYS_WIFI_STA_AUTH == "WPA3-Enterprise" >
#define SYS_WIFI_STA_ENT_USER        			        "${SYS_WIFI_STA_ENT_USER_NAME}"

<#if "${SYS_WIFI_STA_CACERT_FORMAT}" == "DER">
#define SYS_WIFI_STA_ENT_CACERT_FORMAT        	        2
<#elseif "${SYS_WIFI_STA_CACERT_FORMAT}" == "PEM">
#define SYS_WIFI_STA_ENT_CACERT_FORMAT        	        1
</#if>

<#if "${SYS_WIFI_STA_PRIVATE_CERT_FORMAT}" == "DER">
#define SYS_WIFI_STA_ENT_PRIVATE_CERT_FORMAT        	2
<#elseif "${SYS_WIFI_STA_PRIVATE_CERT_FORMAT}" == "PEM">
#define SYS_WIFI_STA_ENT_PRIVATE_CERT_FORMAT        	1
</#if>

<#if "${SYS_WIFI_STA_PRIVATE_KEY_FORMAT}" == "DER">
#define SYS_WIFI_STA_ENT_PRIVATE_FORMAT        	        2
<#elseif "${SYS_WIFI_STA_PRIVATE_KEY_FORMAT}" == "PEM">
#define SYS_WIFI_STA_ENT_PRIVATE_FORMAT        	        1
</#if>

#define SYS_WIFI_STA_ENT_CACERT_MODULE_NAME             ${SYS_WIFI_STA_ENT_CACERT_MODULE_NAME}
<#if SYS_WIFI_ENT_METHOD == "TLS">
#define SYS_WIFI_STA_ENT_PRIVATE_CERT_MODULE_NAME       ${SYS_WIFI_STA_ENT_PRIVATE_CERT_MODULE_NAME}
#define SYS_WIFI_STA_ENT_PRIVATE_KEY_MODULE_NAME        ${SYS_WIFI_STA_ENT_PRIVATE_KEY_MODULE_NAME}
<#elseif SYS_WIFI_ENT_METHOD == "TTLS">
#define SYS_WIFI_STA_ENT_PRIVATE_CERT_MODULE_NAME       NULL
#define SYS_WIFI_STA_ENT_PRIVATE_KEY_MODULE_NAME        NULL
</#if>


<#if "${SYS_WIFI_STA_ENT_SERVER_DOMAIN_SAN}" != "" && "${SYS_WIFI_STA_ENT_SERVER_DOMAIN_CN}" != "" >
#define SYS_WIFI_STA_ENT_SERVER_DOMAIN                  "${SYS_WIFI_STA_ENT_SERVER_DOMAIN_SAN}"
<#elseif "${SYS_WIFI_STA_ENT_SERVER_DOMAIN_SAN}" != "" && "${SYS_WIFI_STA_ENT_SERVER_DOMAIN_CN}" == "" >
#define SYS_WIFI_STA_ENT_SERVER_DOMAIN                  "${SYS_WIFI_STA_ENT_SERVER_DOMAIN_SAN}"
<#elseif "${SYS_WIFI_STA_ENT_SERVER_DOMAIN_SAN}" == "" && "${SYS_WIFI_STA_ENT_SERVER_DOMAIN_CN}" != "" >
#define SYS_WIFI_STA_ENT_SERVER_DOMAIN                  "${SYS_WIFI_STA_ENT_SERVER_DOMAIN_CN}"
<#elseif "${SYS_WIFI_STA_ENT_SERVER_DOMAIN_SAN}" == "" && "${SYS_WIFI_STA_ENT_SERVER_DOMAIN_CN}" == "" >
#define SYS_WIFI_STA_ENT_SERVER_DOMAIN                  "${SYS_WIFI_STA_ENT_SERVER_DOMAIN_SAN}"
</#if>

</#if>

<#if SYS_WIFI_STA_AUTH == "OPEN">
#define SYS_WIFI_STA_AUTHTYPE				SYS_WIFI_OPEN
<#elseif SYS_WIFI_STA_AUTH == "WPA2">
#define SYS_WIFI_STA_AUTHTYPE				SYS_WIFI_WPA2
<#elseif SYS_WIFI_STA_AUTH == "WPAWPA2(Mixed)">
#define SYS_WIFI_STA_AUTHTYPE				SYS_WIFI_WPAWPA2MIXED 
<#elseif SYS_WIFI_STA_AUTH == "WPA2WPA3">
#define SYS_WIFI_STA_AUTHTYPE				SYS_WIFI_WPA2WPA3MIXED
<#elseif SYS_WIFI_STA_AUTH == "WPA3">
#define SYS_WIFI_STA_AUTHTYPE				SYS_WIFI_WPA3
<#elseif SYS_WIFI_STA_AUTH == "WPAWPA2-Enterprise">
#define SYS_WIFI_ENTERPRISE
#define SYS_WIFI_STA_AUTHTYPE				  SYS_WIFI_WPAWPA2MIXED_ENTERPRISE
#define SYS_WIFI_STA_ENTERPRISE_TYPE          WDRV_PIC32MZW_AUTH_TYPE_WPAWPA2_ENTERPRISE    
#define SYS_WIFI_STA_ENTERPRISE_METHOD        SYS_WIFI_ENTERPRISE_${SYS_WIFI_ENT_METHOD}
<#if SYS_WIFI_ENT_METHOD == "TTLS">
#define SYS_WIFI_MSCHAPV2_USERNAME                   "${SYS_WIFI_STA_ENT_TTLS_USERNAME}"                  
#define SYS_WIFI_MSCHAPV2_PASSWORD                   "${SYS_WIFI_STA_ENT_TTLS_PASSWORD}"
</#if>
#define XTIME(a) (${SYS_WIFI_STA_ENT_DATE_EPOCH}) 
<#elseif SYS_WIFI_STA_AUTH == "WPA2-Enterprise">
#define SYS_WIFI_ENTERPRISE
#define SYS_WIFI_STA_AUTHTYPE				  SYS_WIFI_WPA2_ENTERPRISE
#define SYS_WIFI_STA_ENTERPRISE_TYPE          WDRV_PIC32MZW_AUTH_TYPE_WPA2_ENTERPRISE    
#define SYS_WIFI_STA_ENTERPRISE_METHOD        SYS_WIFI_ENTERPRISE_${SYS_WIFI_ENT_METHOD}
<#if SYS_WIFI_ENT_METHOD == "TTLS">
#define SYS_WIFI_MSCHAPV2_USERNAME                   "${SYS_WIFI_STA_ENT_TTLS_USERNAME}"                  
#define SYS_WIFI_MSCHAPV2_PASSWORD                   "${SYS_WIFI_STA_ENT_TTLS_PASSWORD}"
</#if>
#define XTIME(a) (${SYS_WIFI_STA_ENT_DATE_EPOCH})
<#elseif SYS_WIFI_STA_AUTH == "WPA2WPA3-Enterprise">
#define SYS_WIFI_STA_AUTHTYPE				  SYS_WIFI_WPA2WPA3MIXED_ENTERPRISE
#define SYS_WIFI_STA_ENTERPRISE_TYPE          WDRV_PIC32MZW_AUTH_TYPE_WPA2WPA3_ENTERPRISE    
#define SYS_WIFI_STA_ENTERPRISE_METHOD        SYS_WIFI_ENTERPRISE_${SYS_WIFI_ENT_METHOD}
<#if SYS_WIFI_ENT_METHOD == "TTLS">
#define SYS_WIFI_MSCHAPV2_USERNAME                   "${SYS_WIFI_STA_ENT_TTLS_USERNAME}"                  
#define SYS_WIFI_MSCHAPV2_PASSWORD                   "${SYS_WIFI_STA_ENT_TTLS_PASSWORD}"
</#if>
#define XTIME(a) (${SYS_WIFI_STA_ENT_DATE_EPOCH})
<#elseif SYS_WIFI_STA_AUTH == "WPA3-Enterprise">
#define SYS_WIFI_STA_AUTHTYPE				  SYS_WIFI_WPA3_ENTERPRISE
#define SYS_WIFI_STA_ENTERPRISE_TYPE          WDRV_PIC32MZW_AUTH_TYPE_WPA3_ENTERPRISE    
#define SYS_WIFI_STA_ENTERPRISE_METHOD        SYS_WIFI_ENTERPRISE_${SYS_WIFI_ENT_METHOD}
<#if SYS_WIFI_ENT_METHOD == "TTLS">
#define SYS_WIFI_MSCHAPV2_USERNAME                   "${SYS_WIFI_STA_ENT_TTLS_USERNAME}"                  
#define SYS_WIFI_MSCHAPV2_PASSWORD                   "${SYS_WIFI_STA_ENT_TTLS_PASSWORD}"
</#if>
#define XTIME(a) (${SYS_WIFI_STA_ENT_DATE_EPOCH})
</#if>



<#if SYS_WIFI_STA_AUTOCONNECT == true>
#define SYS_WIFI_STA_AUTOCONNECT   			true
<#else>
#define SYS_WIFI_STA_AUTOCONNECT   			false
</#if>
</#if>


<#if SYS_WIFI_AP_ENABLE == true>
#define SYS_WIFI_AP_SSID					"${SYS_WIFI_AP_SSID_NAME}"
#define SYS_WIFI_AP_PWD        				"${SYS_WIFI_AP_PWD_NAME}"
<#if SYS_WIFI_AP_AUTH == "OPEN">
#define SYS_WIFI_AP_AUTHTYPE				SYS_WIFI_OPEN
<#elseif SYS_WIFI_AP_AUTH == "WPA2">
#define SYS_WIFI_AP_AUTHTYPE				SYS_WIFI_WPA2
<#elseif SYS_WIFI_AP_AUTH == "WPAWPA2(Mixed)">
#define SYS_WIFI_AP_AUTHTYPE				SYS_WIFI_WPAWPA2MIXED
<#elseif SYS_WIFI_AP_AUTH == "WPA2WPA3">
#define SYS_WIFI_AP_AUTHTYPE				SYS_WIFI_WPA2WPA3MIXED
<#elseif SYS_WIFI_AP_AUTH == "WPA3">
#define SYS_WIFI_AP_AUTHTYPE				SYS_WIFI_WPA3
</#if>
#define SYS_WIFI_AP_CHANNEL					${SYS_WIFI_AP_CHANNEL}
<#if SYS_WIFI_AP_SSIDVISIBILE == true>
#define SYS_WIFI_AP_SSIDVISIBILE   			true
<#else>
#define SYS_WIFI_AP_SSIDVISIBILE   			false
</#if>
</#if>

<#if SYS_WIFI_POWERSAVE_ENABLE == true>
<#if SYS_WIFI_PIC_MODE == "XDS">
#define SYS_WIFI_PIC_MODE        			LOW_POWER_EXTREME_DEEP_SLEEP_MODE
<#elseif SYS_WIFI_PIC_MODE == "DS">
#define SYS_WIFI_PIC_MODE        			LOW_POWER_DEEP_SLEEP_MODE
<#elseif SYS_WIFI_PIC_MODE == "DREAM">
#define SYS_WIFI_PIC_MODE        			LOW_POWER_DREAM_MODE
<#elseif SYS_WIFI_PIC_MODE == "SLEEP">
#define SYS_WIFI_PIC_MODE        			LOW_POWER_SLEEP_MODE
<#elseif SYS_WIFI_PIC_MODE == "IDLE">
#define SYS_WIFI_PIC_MODE        			LOW_POWER_IDLE_MODE
</#if>
<#if SYS_PIC_WIFI_CORRELATION_MODE == "SYNC">
#define SYS_PIC_WIFI_CORRELATION_MODE       WDRV_PIC32MZW_POWERSAVE_PIC_SYNC_MODE
<#elseif SYS_PIC_WIFI_CORRELATION_MODE == "ASYNC">
#define SYS_PIC_WIFI_CORRELATION_MODE       WDRV_PIC32MZW_POWERSAVE_PIC_ASYNC_MODE
</#if>
#define APP_WIFI_WOFF_MODE                  3
<#if SYS_WIFI_LOWPOWER_MODE == "RUN">
#define SYS_WIFI_WIFI_POWERSAVE_MODE        WDRV_PIC32MZW_POWERSAVE_RUN_MODE
<#elseif SYS_WIFI_LOWPOWER_MODE == "WSM">
#define SYS_WIFI_WIFI_POWERSAVE_MODE        WDRV_PIC32MZW_POWERSAVE_WSM_MODE
<#elseif SYS_WIFI_LOWPOWER_MODE == "WDS">
#define SYS_WIFI_WIFI_POWERSAVE_MODE        WDRV_PIC32MZW_POWERSAVE_WDS_MODE
<#elseif SYS_WIFI_LOWPOWER_MODE == "WOFF">
#define SYS_WIFI_WIFI_POWERSAVE_MODE        APP_WIFI_WOFF_MODE
</#if>
<#if SYS_WIFI_WAKEUP == "DTIM">
#define SYS_WIFI_WAKEUP_DTIM
</#if>
<#if SYS_WIFI_WAKEUP == "LISTEN INTERVAL">
#define SYS_WIFI_LISTENINTERVAL             ${SYS_WIFI_LISTENINTERVAL}
#define SYS_WIFI_SLEEPINACTLIMIT            ${SYS_WIFI_SLEEPINACTLIMIT}
</#if>
</#if>

<#if SYS_WIFI_SCAN_ENABLE == true>
#define SYS_WIFI_SCAN_CHANNEL               ${SYS_WIFI_SCAN_CHANNEL}
#define SYS_WIFI_SCAN_MAX_SSID_COUNT    	DRV_PIC32MZW_MAX_HIDDEN_SITES
<#if SYS_WIFI_SCAN_MODE == "ACTIVE">
#define SYS_WIFI_SCAN_MODE                  SYS_WIFI_SCAN_MODE_ACTIVE
#define SYS_WIFI_SCAN_SSID_LIST             "${SYS_WIFI_SCAN_SSID_LIST}"
<#else>
#define SYS_WIFI_SCAN_MODE                  SYS_WIFI_SCAN_MODE_PASSIVE
#define SYS_WIFI_SCAN_SSID_LIST             ""
</#if>
#define SYS_WIFI_SCAN_SSID_DELIM_CHAR       '${SYS_WIFI_SCAN_SSID_DELIM_CHAR}'
#define SYS_WIFI_SCAN_CHANNEL24_MASK        0x${SYS_WIFI_SCAN_CHAN_MASK}
#define SYS_WIFI_SCAN_NUM_SLOTS             ${SYS_WIFI_SCAN_NUM_SLOTS}
#define SYS_WIFI_SCAN_ACTIVE_SLOT_TIME      ${SYS_WIFI_SCAN_ACTIVE_SLOT_TIME}
#define SYS_WIFI_SCAN_PASSIVE_SLOT_TIME     ${SYS_WIFI_SCAN_PASSIVE_SLOT_TIME}
#define SYS_WIFI_SCAN_NUM_PROBES            ${SYS_WIFI_SCAN_NUM_PROBES}
<#if SYS_WIFI_SCAN_MATCH_MODE == "STOP_ON_FIRST">
#define SYS_WIFI_SCAN_MATCH_MODE            WDRV_PIC32MZW_SCAN_MATCH_MODE_STOP_ON_FIRST
<#else>
#define SYS_WIFI_SCAN_MATCH_MODE        	WDRV_PIC32MZW_SCAN_MATCH_MODE_FIND_ALL
</#if>
</#if>
<#if SYS_WIFI_APPDEBUG_ENABLE == true>
#define SYS_WIFI_DEBUG_PRESTR						"${SYS_WIFI_APPDEBUG_PRESTR}"

<#if SYS_WIFI_APPDEBUG_ERR_LEVEL == true>
#define SYS_WIFI_APPDEBUG_ERR_LEVEL_ENABLE   			0xf
<#else>
#define SYS_WIFI_APPDEBUG_ERR_LEVEL_ENABLE   			0x0
</#if>

<#if SYS_WIFI_APPDEBUG_DBG_LEVEL == true>
#define SYS_WIFI_APPDEBUG_DBG_LEVEL_ENABLE   			0xf
<#else>
#define SYS_WIFI_APPDEBUG_DBG_LEVEL_ENABLE   			0x0
</#if>

<#if SYS_WIFI_APPDEBUG_INFO_LEVEL == true>
#define SYS_WIFI_APPDEBUG_INFO_LEVEL_ENABLE   			0xf
<#else>
#define SYS_WIFI_APPDEBUG_INFO_LEVEL_ENABLE   			0x0
</#if>

<#if SYS_WIFI_APPDEBUG_FUNC_LEVEL == true>
#define SYS_WIFI_APPDEBUG_FUNC_LEVEL_ENABLE   			0xf
<#else>
#define SYS_WIFI_APPDEBUG_FUNC_LEVEL_ENABLE   			0x0
</#if>

<#if SYS_WIFI_APPDEBUG_CFG_FLOW == true>
#define SYS_WIFI_APPDEBUG_CFG_FLOW						0xf
<#else>
#define SYS_WIFI_APPDEBUG_CFG_FLOW						0x0
</#if>
<#if SYS_WIFI_APPDEBUG_CONNECT_FLOW == true>
#define SYS_WIFI_APPDEBUG_CONNECT_FLOW					0xf
<#else>
#define SYS_WIFI_APPDEBUG_CONNECT_FLOW					0x0
</#if>

<#if SYS_WIFI_APPDEBUG_PROVISIONING_FLOW == true>
#define SYS_WIFI_APPDEBUG_PROVISIONING_FLOW				0xf
<#else>
#define SYS_WIFI_APPDEBUG_PROVISIONING_FLOW				0x0
</#if>

<#if SYS_WIFI_APPDEBUG_PROVISIONINGCMD_FLOW == true>
#define SYS_WIFI_APPDEBUG_PROVISIONINGCMD_FLOW			0xf
<#else>
#define SYS_WIFI_APPDEBUG_PROVISIONINGCMD_FLOW			0x0
</#if>

<#if SYS_WIFI_APPDEBUG_PROVISIONINGSOCK_FLOW == true>
#define SYS_WIFI_APPDEBUG_PROVISIONINGSOCK_FLOW			0xf
<#else>
#define SYS_WIFI_APPDEBUG_PROVISIONINGSOCK_FLOW			0x0
</#if>
</#if>




<#if HarmonyCore.SELECT_RTOS != "BareMetal">
    <#lt>/* SYS WIFI RTOS Configurations*/
    <#lt>#define SYS_WIFI_RTOS_SIZE           		${SYS_WIFI_RTOS_TASK_STACK_SIZE}
    <#lt>#define SYS_WIFI_RTOS_PRIORITY             ${SYS_WIFI_RTOS_TASK_PRIORITY}
</#if>
</#if>
<#--
/*******************************************************************************
 End of File
*/
-->
