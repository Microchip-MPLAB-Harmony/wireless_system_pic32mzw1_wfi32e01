/*** WSS Configuration ***/
<#if HarmonyCore.SELECT_RTOS == "FreeRTOS">
#define SYS_WSS_RTOS_STACK_SIZE     ${SYS_WSS_RTOS_STACK_SIZE}
#define SYS_WSS_RTOS_TASK_PRIORITY  ${SYS_WSS_RTOS_TASK_PRIORITY}
#define SYS_WSS_RTOS_TASK_DELAY     ${SYS_WSS_RTOS_TASK_DELAY}
</#if>  
#define SYS_WSS_PORT                        ${SYS_WSS_PORT}
#define SYS_WSS_SERVER_IP                   "${SYS_WSS_SERVER_IP}"
#define SYS_WSS_MODE                        ${SYS_WSS_MODE}
#define SYS_WSS_HOST_NAME                   "${SYS_WSS_HOST_NAME}"
#define SYS_WSS_INTF                        ${SYS_WSS_INTF}
<#if SYS_WSS_ENABLE_TLS == true>
#define SYS_WSS_ENABLE_TLS   			    true
<#else>
#define SYS_WSS_ENABLE_TLS   			    false
</#if>
<#if SYS_WSS_ENABLE_DEBUG == true>
#define SYS_WSS_ENABLE_DEBUG   			    1
<#else>
#define SYS_WSS_ENABLE_DEBUG   			    0
</#if>
#define SYS_WSS_MAX_RX_BUFFER               ${SYS_WSS_MAX_RX_BUFFER}
<#if SYS_WSS_MODE == "SYS_WSS_CLIENT">
#define SYS_WSS_MAX_NUM_CLIENTS             1
<#else>
#define SYS_WSS_MAX_NUM_CLIENTS             ${SYS_WSS_MAX_NUM_CLIENTS}
</#if>
<#if SYS_WSS_START_AT_BOOT == true>
#define SYS_WSS_START_AT_BOOT   			1
<#else>
#define SYS_WSS_START_AT_BOOT   			0
</#if>
#define SYS_WSS_CLIENT_TIMEOUT              ${SYS_WSS_CLIENT_TIMEOUT}
#define WOLFSSL_BASE64_ENCODE