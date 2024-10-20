/*******************************************************************************
  Wi-Fi System Service Implementation

  File Name:
    sys_wifi.c

  Summary:
    Source code for the Wi-Fi system service implementation.

  Description:
    This file contains the source code for the Wi-Fi system service
    implementation.
 *******************************************************************************/

//DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (C) 2020-2021 released Microchip Technology Inc.  All rights reserved.

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
 *******************************************************************************/
//DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <stdlib.h>
#include "definitions.h"
#include "wdrv_pic32mzw_client_api.h"
#include "tcpip_manager_control.h"
#include "system/wifi/sys_wifi.h"
#include "configuration.h"
<#if SYS_WIFI_PROVISION_ENABLE == true>
#include "system/wifiprov/sys_wifiprov.h"
</#if>

<#if SYS_WIFI_STA_AUTH == "WPAWPA2-Enterprise" || SYS_WIFI_STA_AUTH == "WPA2-Enterprise" || SYS_WIFI_STA_AUTH == "WPA2WPA3-Enterprise" || SYS_WIFI_STA_AUTH == "WPA3-Enterprise" >
#include "tcpip/src/link_list.h"
#include "wolfssl/ssl.h"
#include "wolfssl/wolfcrypt/logging.h"

#include "${SYS_WIFI_STA_ENT_CACERT_FILE_NAME}"
<#if SYS_WIFI_ENT_METHOD == "TLS">
#include "${SYS_WIFI_STA_ENT_PRIVATE_CERT_FILE_NAME}"
#include "${SYS_WIFI_STA_ENT_PRIVATE_KEY_FILE_NAME}"
</#if>
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Type Definitions
// *****************************************************************************
// *****************************************************************************

typedef struct 
{
    /* The WiFi service current status */
    SYS_WIFI_STATUS wifiSrvcStatus;
    
    /* Wi-Fi Service handle */
    DRV_HANDLE wifiSrvcDrvHdl;
    
    /* Wi-Fi Service Auth Context */
    WDRV_PIC32MZW_AUTH_CONTEXT wifiSrvcAuthCtx;
    
    /* Wi-Fi Service BSS Context */
    WDRV_PIC32MZW_BSS_CONTEXT wifiSrvcBssCtx;

} SYS_WIFI_OBJ; /* Wi-Fi System Service Object */

/* Wi-Fi STA Mode, maximum auto connect retry */
#define MAX_AUTO_CONNECT_RETRY                5
<#if SYS_WIFI_AP_ENABLE == true>
typedef struct 
{
    /* Assoc Handle associated with the station */
    WDRV_PIC32MZW_ASSOC_HANDLE wifiSrvcAssocHandle;
    
    /* STA connection info update to App */
    bool wifiSrvcSTAConnUpdate;
    
    /* Station Info shared with the App */
    SYS_WIFI_STA_APP_INFO wifiSrvcStaAppInfo;
    
} SYS_WIFI_STA_CONNECTION_INFO;

</#if>
<#if SYS_WIFI_STA_AUTH == "WPAWPA2-Enterprise" || SYS_WIFI_STA_AUTH == "WPA2-Enterprise" || SYS_WIFI_STA_AUTH == "WPA2WPA3-Enterprise" || SYS_WIFI_STA_AUTH == "WPA3-Enterprise" >

typedef uintptr_t SYS_WIFI_TLS_CONTEXT_HANDLE;
#define SYS_WIFI_TLS_CONTEXT_HANDLE_INVALID  (((SYS_WIFI_TLS_CONTEXT_HANDLE) -1))

</#if>
// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************
<#if SYS_WIFI_SCAN_ENABLE == true>

/* Wi-Fi Scan user SSID linked list */
static WDRV_PIC32MZW_SSID_LIST userSsidLinkedList[SYS_WIFI_SCAN_MAX_SSID_COUNT];

/* Local copy of user SSIDs */
static char g_scanSsidListString[(SYS_WIFI_SCAN_MAX_SSID_COUNT*WDRV_PIC32MZW_MAX_SSID_LEN)+SYS_WIFI_SCAN_MAX_SSID_COUNT];

/* Wi-Fi  Service SSID Scan Configuration Structure */
static    SYS_WIFI_SCAN_CONFIG  g_wifiSrvcScanConfig;

</#if>
/* Storing Wi-Fi Service Callbacks */
static    SYS_WIFI_CALLBACK     g_wifiSrvcCallBack[SYS_WIFI_MAX_CBS];

/* Wi-Fi Service Object */
static    SYS_WIFI_OBJ          g_wifiSrvcObj = {SYS_WIFI_STATUS_NONE,0};

<#if SYS_WIFI_STA_ENABLE == true>
/* Wi-Fi Driver ASSOC Handle */
static WDRV_PIC32MZW_ASSOC_HANDLE g_wifiSrvcDrvAssocHdl = WDRV_PIC32MZW_ASSOC_HANDLE_INVALID;
</#if>
<#if SYS_WIFI_AP_ENABLE == true>


#define SYS_WIFI_MAX_STA_SUPPORTED  WDRV_PIC32MZW_NUM_ASSOCS
static SYS_WIFI_STA_CONNECTION_INFO g_wifiSrvcStaConnInfo[SYS_WIFI_MAX_STA_SUPPORTED];

</#if>
<#if  SYS_WIFI_STA_ENABLE == true>

/* Wi-Fi DHCP handler */
static    TCPIP_DHCP_HANDLE     g_wifiSrvcDhcpHdl = NULL;

/* Wi-Fi STA Mode, Auto connect retry count */
static    uint32_t              g_wifiSrvcAutoConnectRetry = 0;

</#if>

/* Wi-Fi  Service Configuration Structure */
static    SYS_WIFI_CONFIG       g_wifiSrvcConfig;

/* Wi-Fi Service cookie */
static    void *                g_wifiSrvcCookie ;

/* Wi-Fi Service init enable wait status */
static    bool                  g_wifiSrvcInit = false;

<#if SYS_WIFI_PROVISION_ENABLE == true>
/* Cookie for Wi-Fi Provision */
static    char                  g_wifiSrvcProvCookieVal = 100;

/* Wi-Fi Provision Service Object */
static    SYS_MODULE_OBJ        g_wifiSrvcProvObj;
</#if>

/* RegDomain set status */
bool      g_isRegDomainSetReq = false;

/* Semaphore for Critical Section */
static    OSAL_SEM_HANDLE_TYPE  g_wifiSrvcSemaphore;
// *****************************************************************************

<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
/* Wi-Fi service APP debug handle */
SYS_MODULE_OBJ                  g_wifiSrvcAppDebugHdl = SYS_MODULE_OBJ_INVALID;

/* APP debug configuration handle */
SYS_APPDEBUG_CONFIG                       g_wifiSrvcAppDbgCfg;

/* App Debug Print Flows */
#define    WIFI_CFG                       0x1
#define    WIFI_CONNECT                   0x2
#define    WIFI_PROVISIONING              0x3
#define    WIFI_PROVISIONINGCMD           0x4
#define    WIFI_PROVISIONINGSOCKET        0x5

</#if>
// *****************************************************************************

<#if  SYS_WIFI_STA_ENABLE == true>
static uint8_t SYS_WIFI_DisConnect(void);
</#if>
static SYS_WIFI_RESULT SYS_WIFI_ConnectReq(void);
<#if SYS_WIFI_SCAN_ENABLE == true>
static SYS_WIFI_RESULT SYS_WIFI_SetScan(void);
static void SYS_WIFI_ScanHandler (DRV_HANDLE handle, uint8_t index, uint8_t ofTotal, WDRV_PIC32MZW_BSS_INFO *pBSSInfo);
</#if>
<#if SYS_WIFI_AP_ENABLE == true>
static uint8_t SYS_WIFI_APDisconnectSTA(uint8_t *macAddr);
</#if>

<#if SYS_WIFI_PROVISION_ENABLE == true>
static void  SYS_WIFI_WIFIPROVCallBack(uint32_t event, void * data,void *cookie);
</#if>

<#if  SYS_WIFI_STA_ENABLE == true>
<#if ((tcpipIPv6.TCPIP_STACK_USE_IPV6)?has_content && (tcpipIPv6.TCPIP_STACK_USE_IPV6) == true) >
static int g_ipv6AddrIdx = 0;
static void SYS_WIFI_TCPIP_IPv6EventHandler
(
        TCPIP_NET_HANDLE hNet, 
        IPV6_EVENT_TYPE evType, 
        const void* evParam, 
        const void* usrParam);
</#if>
</#if>


// *****************************************************************************
// *****************************************************************************
// Section: Local Functions
// *****************************************************************************
// *****************************************************************************
<#if SYS_WIFI_SCAN_ENABLE == true>

static void SYS_WIFI_InitWifiScanInfoDefault(void)
{
    SYS_WIFI_SCAN_CONFIG  scanConfig;
    memset(&scanConfig, 0, sizeof(scanConfig));
    
    scanConfig.channel          = SYS_WIFI_SCAN_CHANNEL;
    scanConfig.mode             = SYS_WIFI_SCAN_MODE;
    scanConfig.pSsidList        = SYS_WIFI_SCAN_SSID_LIST;
    scanConfig.delimChar        = SYS_WIFI_SCAN_SSID_DELIM_CHAR;
    scanConfig.chan24Mask       = SYS_WIFI_SCAN_CHANNEL24_MASK;
    scanConfig.numSlots         = SYS_WIFI_SCAN_NUM_SLOTS;
    scanConfig.activeSlotTime   = SYS_WIFI_SCAN_ACTIVE_SLOT_TIME;
    scanConfig.passiveSlotTime  = SYS_WIFI_SCAN_PASSIVE_SLOT_TIME;
    scanConfig.numProbes        = SYS_WIFI_SCAN_NUM_PROBES;
    scanConfig.matchMode        = SYS_WIFI_SCAN_MATCH_MODE;
    scanConfig.pNotifyCallback  = SYS_WIFI_ScanHandler;
    
    memcpy(&g_wifiSrvcScanConfig, &scanConfig, sizeof (g_wifiSrvcScanConfig));
}
</#if>

<#if SYS_WIFI_AP_ENABLE == true>

static void SYS_WIFI_InitStaConnInfo(void)
{
    uint8_t idx = 0;

    for(idx = 0; idx < SYS_WIFI_MAX_STA_SUPPORTED; idx++)
    {
        g_wifiSrvcStaConnInfo[idx].wifiSrvcAssocHandle = WDRV_PIC32MZW_ASSOC_HANDLE_INVALID;
        g_wifiSrvcStaConnInfo[idx].wifiSrvcSTAConnUpdate = false;
        memset(&g_wifiSrvcStaConnInfo[idx].wifiSrvcStaAppInfo,0,sizeof(SYS_WIFI_STA_APP_INFO));
    }
}

static SYS_WIFI_STA_CONNECTION_INFO *SYS_WIFI_FindStaConnInfo(WDRV_PIC32MZW_ASSOC_HANDLE assocHandle)
{
    uint8_t idx = 0;
    for(idx = 0; idx < SYS_WIFI_MAX_STA_SUPPORTED; idx++)
    {
        if(g_wifiSrvcStaConnInfo[idx].wifiSrvcAssocHandle == assocHandle)
        {
            return &g_wifiSrvcStaConnInfo[idx];
        }
    }
    return NULL;
}

static SYS_WIFI_RESULT SYS_WIFI_RemoveStaConnInfo(WDRV_PIC32MZW_ASSOC_HANDLE assocHandle)
{
    uint8_t idx = 0;
    for(idx = 0; idx < SYS_WIFI_MAX_STA_SUPPORTED; idx++)
    {
        if(g_wifiSrvcStaConnInfo[idx].wifiSrvcAssocHandle == assocHandle)
        {
            g_wifiSrvcStaConnInfo[idx].wifiSrvcAssocHandle = WDRV_PIC32MZW_ASSOC_HANDLE_INVALID;
            return SYS_WIFI_SUCCESS;
        }
    }
    return SYS_WIFI_FAILURE;
}
static WDRV_PIC32MZW_ASSOC_HANDLE SYS_WIFI_StaConnAssocIdFromMAC(uint8_t *macAddr)
{
    uint8_t idx = 0;

    for(idx = 0; idx < SYS_WIFI_MAX_STA_SUPPORTED; idx++)
    {
        if(!memcmp(&g_wifiSrvcStaConnInfo[idx].wifiSrvcStaAppInfo.macAddr,macAddr,WDRV_PIC32MZW_MAC_ADDR_LEN))
        {
            return g_wifiSrvcStaConnInfo[idx].wifiSrvcAssocHandle;
        }
    }
    return WDRV_PIC32MZW_ASSOC_HANDLE_INVALID;
}
<#if (tcpipDhcps.TCPIP_STACK_USE_DHCP_SERVER)?has_content && (tcpipDhcps.TCPIP_STACK_USE_DHCP_SERVER) == true>
static uint8_t SYS_WIFI_StaConnIdx()
{
    uint8_t idx = 0;

    for(idx = 0; idx < SYS_WIFI_MAX_STA_SUPPORTED; idx++)
    {
        if(g_wifiSrvcStaConnInfo[idx].wifiSrvcSTAConnUpdate == true)
        {
            g_wifiSrvcStaConnInfo[idx].wifiSrvcSTAConnUpdate = false;
            return idx;
        }
    }
    return SYS_WIFI_OBJ_INVALID;
}
</#if>
</#if>

static inline void SYS_WIFI_CallBackFun
(
    uint32_t event, 
    void * data, void *cookie
) 
{
    uint8_t idx;
    
    for (idx = 0; idx < SYS_WIFI_MAX_CBS; idx++) 
    {
        if (g_wifiSrvcCallBack[idx]) 
        {  
            /* Call client register functions */
            (g_wifiSrvcCallBack[idx])(event, data, cookie);
        }
    }
}

static inline SYS_WIFI_RESULT SYS_WIFI_REGCB
(
    SYS_WIFI_CALLBACK callback
) 
{
    SYS_WIFI_RESULT ret = SYS_WIFI_FAILURE;
    uint8_t idx;
    
    for (idx = 0; idx < SYS_WIFI_MAX_CBS; idx++) 
    {
        if (!g_wifiSrvcCallBack[idx]) 
        {
            /* Copy the client function pointer */
            g_wifiSrvcCallBack[idx] = callback;
            ret = SYS_WIFI_SUCCESS;
            break;
        }
    }
    return ret;
}

<#if SYS_WIFI_PROVISION_ENABLE == false>
static inline void SYS_WIFI_InitConfig
(
    SYS_WIFI_CONFIG *config
) 
{   
    
    if (!config) 
    {   
        /* User has not set configuration during Wi-Fi Service initialization,
           Copy the MHC configuration into Wi-Fi Service structure */
        g_wifiSrvcConfig.mode = SYS_WIFI_DEVMODE;
        g_wifiSrvcConfig.saveConfig = 0;
        memcpy(g_wifiSrvcConfig.countryCode, SYS_WIFI_COUNTRYCODE, strlen(SYS_WIFI_COUNTRYCODE));
<#if SYS_WIFI_STA_ENABLE == true>

        /* STA Mode Configuration */
        g_wifiSrvcConfig.staConfig.channel = 0;        
        g_wifiSrvcConfig.staConfig.autoConnect = SYS_WIFI_STA_AUTOCONNECT;
        g_wifiSrvcConfig.staConfig.authType = SYS_WIFI_STA_AUTHTYPE;
        memcpy(g_wifiSrvcConfig.staConfig.ssid, SYS_WIFI_STA_SSID, sizeof(SYS_WIFI_STA_SSID));        
        memcpy(g_wifiSrvcConfig.staConfig.psk, SYS_WIFI_STA_PWD, sizeof(SYS_WIFI_STA_PWD));
</#if>
<#if SYS_WIFI_AP_ENABLE == true>

        /* AP Mode Configuration */
        g_wifiSrvcConfig.apConfig.channel = SYS_WIFI_AP_CHANNEL;
        g_wifiSrvcConfig.apConfig.ssidVisibility = SYS_WIFI_AP_SSIDVISIBILE;
        g_wifiSrvcConfig.apConfig.authType = SYS_WIFI_AP_AUTHTYPE;
        memcpy(g_wifiSrvcConfig.apConfig.ssid, SYS_WIFI_AP_SSID, sizeof(SYS_WIFI_AP_SSID));
        memcpy(g_wifiSrvcConfig.apConfig.psk, SYS_WIFI_AP_PWD, sizeof(SYS_WIFI_AP_PWD));     
</#if>
    } 
    else 
    {
        /* User has set configuration during Wi-Fi Service initialization,
           Copy the user configuration into Wi-Fi Service structure  */
        memcpy(&g_wifiSrvcConfig, config, sizeof(SYS_WIFI_CONFIG));
    }
}
</#if>
 
static inline void SYS_WIFI_SetCookie
(
    void *cookie
) 
{
    g_wifiSrvcCookie = cookie;
}

static inline SYS_WIFI_MODE SYS_WIFI_GetMode(void)
{
    return g_wifiSrvcConfig.mode;
}

static inline bool SYS_WIFI_GetSaveConfig(void)
{
    return g_wifiSrvcConfig.saveConfig;
}

static inline uint8_t * SYS_WIFI_GetSSID(void)  
{
<#if (SYS_WIFI_STA_ENABLE == true) && (SYS_WIFI_AP_ENABLE == true)>
    if (SYS_WIFI_STA == SYS_WIFI_GetMode())
    {
        return g_wifiSrvcConfig.staConfig.ssid;
    }
    else
    {
        return g_wifiSrvcConfig.apConfig.ssid;
    }
<#elseif SYS_WIFI_STA_ENABLE == true>
    return g_wifiSrvcConfig.staConfig.ssid;
<#elseif SYS_WIFI_AP_ENABLE == true>
    return g_wifiSrvcConfig.apConfig.ssid;
</#if>
}

static inline uint8_t SYS_WIFI_GetSSIDLen(void)  
{
<#if (SYS_WIFI_STA_ENABLE == true) && (SYS_WIFI_AP_ENABLE == true)>
    if (SYS_WIFI_STA == SYS_WIFI_GetMode())
    {
        return strlen((const char *)g_wifiSrvcConfig.staConfig.ssid);
    }
    else
    {
        return strlen((const char *)g_wifiSrvcConfig.apConfig.ssid);
    }
<#elseif SYS_WIFI_STA_ENABLE == true>
    return strlen((const char *)g_wifiSrvcConfig.staConfig.ssid);
<#elseif SYS_WIFI_AP_ENABLE == true>
    return strlen((const char *)g_wifiSrvcConfig.apConfig.ssid);
</#if>
}

static inline uint8_t SYS_WIFI_GetChannel(void)
{
<#if (SYS_WIFI_STA_ENABLE == true) && (SYS_WIFI_AP_ENABLE == true)>
    if (SYS_WIFI_STA == SYS_WIFI_GetMode())
    {
        return g_wifiSrvcConfig.staConfig.channel;
    }
    else
    {
        return g_wifiSrvcConfig.apConfig.channel;
    }
<#elseif SYS_WIFI_STA_ENABLE == true>
    return (g_wifiSrvcConfig.staConfig.channel);
<#elseif SYS_WIFI_AP_ENABLE == true>
    return (g_wifiSrvcConfig.apConfig.channel);
</#if>
}

static inline uint8_t SYS_WIFI_GetAuthType(void)
{
<#if (SYS_WIFI_STA_ENABLE == true) && (SYS_WIFI_AP_ENABLE == true)>
    if (SYS_WIFI_STA == SYS_WIFI_GetMode())
    {
        return g_wifiSrvcConfig.staConfig.authType;
    }
    else
    {
        return g_wifiSrvcConfig.apConfig.authType;
    }
<#elseif SYS_WIFI_STA_ENABLE == true>
    return g_wifiSrvcConfig.staConfig.authType;
<#elseif SYS_WIFI_AP_ENABLE == true>
    return g_wifiSrvcConfig.apConfig.authType;
</#if>
}

static inline uint8_t *SYS_WIFI_GetPsk(void)
{
<#if (SYS_WIFI_STA_ENABLE == true) && (SYS_WIFI_AP_ENABLE == true)>
    if (SYS_WIFI_STA == SYS_WIFI_GetMode())
    {
        return g_wifiSrvcConfig.staConfig.psk;
    }
    else
    {
        return g_wifiSrvcConfig.apConfig.psk;
    }
<#elseif SYS_WIFI_STA_ENABLE == true>
    return g_wifiSrvcConfig.staConfig.psk;
<#elseif SYS_WIFI_AP_ENABLE == true>
    return g_wifiSrvcConfig.apConfig.psk;
</#if>
}

static inline uint8_t SYS_WIFI_GetPskLen(void)
{
<#if (SYS_WIFI_STA_ENABLE == true) && (SYS_WIFI_AP_ENABLE == true)>
    if (SYS_WIFI_STA == SYS_WIFI_GetMode())
    {
        return strlen((const char *)g_wifiSrvcConfig.staConfig.psk);
    }
    else
    {
        return strlen((const char *)g_wifiSrvcConfig.apConfig.psk);
    }
<#elseif SYS_WIFI_STA_ENABLE == true>
    return strlen((const char *)g_wifiSrvcConfig.staConfig.psk);
<#elseif SYS_WIFI_AP_ENABLE == true>
    return strlen((const char *)g_wifiSrvcConfig.apConfig.psk);
</#if>    
}

static inline bool SYS_WIFI_GetSSIDVisibility(void)
{
<#if (SYS_WIFI_STA_ENABLE == true) && (SYS_WIFI_AP_ENABLE == true)>
    if (SYS_WIFI_AP == SYS_WIFI_GetMode())
    {
        return g_wifiSrvcConfig.apConfig.ssidVisibility;
    }
    else
    {
        return 0;
    }
<#elseif SYS_WIFI_STA_ENABLE == true>
    return 0;
<#elseif SYS_WIFI_AP_ENABLE == true>
    return g_wifiSrvcConfig.apConfig.ssidVisibility;
</#if>     
}

static inline const char *SYS_WIFI_GetCountryCode(void)
{
    return (const char *) g_wifiSrvcConfig.countryCode;
}

static inline bool SYS_WIFI_GetAutoConnect(void)
{
<#if (SYS_WIFI_STA_ENABLE == true) && (SYS_WIFI_AP_ENABLE == true)>
    
    /* In AP mode, autoConnect is always enabled */
    if (SYS_WIFI_AP == SYS_WIFI_GetMode())
    {
        return true;
    } 
    else if (SYS_WIFI_STA == SYS_WIFI_GetMode())
    {
        return g_wifiSrvcConfig.staConfig.autoConnect;
    }
    else
    {
        return false;
    }

<#elseif SYS_WIFI_STA_ENABLE == true>
    return g_wifiSrvcConfig.staConfig.autoConnect;        
<#elseif SYS_WIFI_AP_ENABLE == true>   
    /* In AP mode, autoConnect is always enabled */
    return true;
</#if>
}

static inline void SYS_WIFI_SetTaskstatus
(
    SYS_WIFI_STATUS status
)
{
    g_wifiSrvcObj.wifiSrvcStatus = status;
}

static inline SYS_WIFI_STATUS SYS_WIFI_GetTaskstatus(void)
{
    return g_wifiSrvcObj.wifiSrvcStatus;
}

static inline void SYS_WIFI_PrintWifiConfig(void)
{
    SYS_CONSOLE_MESSAGE("Wi-Fi Configuration:\r\n");
    SYS_CONSOLE_PRINT("\r\n mode=%d (0-STA,1-AP) saveConfig=%d \r\n ", g_wifiSrvcConfig.mode, g_wifiSrvcConfig.saveConfig);
<#if SYS_WIFI_STA_ENABLE == true>
    if (g_wifiSrvcConfig.mode == SYS_WIFI_STA) 
    {
        SYS_CONSOLE_PRINT("\r\n STA Configuration :\r\n channel=%d \r\n autoConnect=%d \r\n ssid=%s \r\n passphase=%s \r\n authentication type=%d (1-Open,2-WEP,3-Mixed mode(WPA/WPA2),4-WPA2,5-Mixed mode(WPA2/WPA3),6-WPA3)\r\n", g_wifiSrvcConfig.staConfig.channel, g_wifiSrvcConfig.staConfig.autoConnect, g_wifiSrvcConfig.staConfig.ssid, g_wifiSrvcConfig.staConfig.psk, g_wifiSrvcConfig.staConfig.authType);
    }
</#if>
<#if SYS_WIFI_AP_ENABLE == true>
    if (g_wifiSrvcConfig.mode == SYS_WIFI_AP)
    {
        SYS_CONSOLE_PRINT("\r\n AP Configuration :\r\n channel=%d \r\n ssidVisibility=%d \r\n ssid=%s \r\n passphase=%s \r\n authentication type=%d (1-Open,2-WEP,3-Mixed mode(WPA/WPA2),4-WPA2,5-Mixed mode(WPA2/WPA3),6-WPA3) \r\n", g_wifiSrvcConfig.apConfig.channel, g_wifiSrvcConfig.apConfig.ssidVisibility, g_wifiSrvcConfig.apConfig.ssid, g_wifiSrvcConfig.apConfig.psk, g_wifiSrvcConfig.apConfig.authType);
    }
</#if>

}
<#if SYS_WIFI_SCAN_ENABLE == true>
static inline void SYS_WIFI_PrintScanConfig(void)
{
    SYS_CONSOLE_MESSAGE("\r\nScan Configuration:\r\n");
    SYS_CONSOLE_PRINT("\r\n mode=%d (0-Passive,1-Active) \r\n Channel=%d (0=All)", g_wifiSrvcScanConfig.mode, g_wifiSrvcScanConfig.channel);
    SYS_CONSOLE_PRINT("\r\n Input SSID List=\"%s\" \r\n List Delimiter='%c' \r\n Channel Mask=0x%x \r\n Slots=%d \r\n Active Slot Time=%d \r\n Passive Slot Time=%d \r\n "
            "Probes=%d \r\n Match Mode=%d (0-StopOnFirst,1-FindAll) \r\n\r\n", g_wifiSrvcScanConfig.pSsidList, g_wifiSrvcScanConfig.delimChar, 
            g_wifiSrvcScanConfig.chan24Mask, g_wifiSrvcScanConfig.numSlots, g_wifiSrvcScanConfig.activeSlotTime, g_wifiSrvcScanConfig.passiveSlotTime, 
            g_wifiSrvcScanConfig.numProbes, g_wifiSrvcScanConfig.matchMode);
}
</#if>
<#if SYS_WIFI_AP_ENABLE == true>
<#if (tcpipDhcps.TCPIP_STACK_USE_DHCP_SERVER)?has_content && (tcpipDhcps.TCPIP_STACK_USE_DHCP_SERVER) == true>
static void SYS_WIFI_WaitForConnSTAIP(uintptr_t context)
{
    TCPIP_NET_HANDLE netHdl = TCPIP_STACK_NetHandleGet("PIC32MZW1");
    TCPIP_DHCPS_LEASE_HANDLE dhcpsLease = 0;
    TCPIP_DHCPS_LEASE_ENTRY dhcpsLeaseEntry;

    do
    {
        dhcpsLease = TCPIP_DHCPS_LeaseEntryGet(netHdl, &dhcpsLeaseEntry, dhcpsLease);
        if (0 != dhcpsLease)
        {
            SYS_WIFI_STA_CONNECTION_INFO *staConnInfo = (SYS_WIFI_STA_CONNECTION_INFO *)context;
            if(0 == memcmp(&dhcpsLeaseEntry.hwAdd, staConnInfo->wifiSrvcStaAppInfo.macAddr, WDRV_PIC32MZW_MAC_ADDR_LEN))
            {               
                SYS_CONSOLE_PRINT("\r\nConnected STA IP:%d.%d.%d.%d \r\n", dhcpsLeaseEntry.ipAddress.v[0], dhcpsLeaseEntry.ipAddress.v[1], dhcpsLeaseEntry.ipAddress.v[2], dhcpsLeaseEntry.ipAddress.v[3]);
                staConnInfo->wifiSrvcStaAppInfo.ipAddr.Val = dhcpsLeaseEntry.ipAddress.Val;
                staConnInfo->wifiSrvcSTAConnUpdate = true; 
                SYS_WIFI_SetTaskstatus(SYS_WIFI_STATUS_WAIT_FOR_STA_IP);
                return;
            }
        }
    } while(0 != dhcpsLease);

    SYS_TIME_CallbackRegisterMS(SYS_WIFI_WaitForConnSTAIP, context, 500, SYS_TIME_SINGLE);
}
</#if>
static void SYS_WIFI_APConnCallBack
(
    DRV_HANDLE handle, 
    WDRV_PIC32MZW_ASSOC_HANDLE assocHandle, 
    WDRV_PIC32MZW_CONN_STATE currentState
) 
{
    
    WDRV_PIC32MZW_MAC_ADDR   wifiSrvcStaConnMac;
    switch (currentState)
    {
        case WDRV_PIC32MZW_CONN_STATE_CONNECTED:
        {
            /* When STA connected to PIC32MZW1 AP, 
               Wi-Fi driver updates Connected event */
            if (WDRV_PIC32MZW_STATUS_OK == WDRV_PIC32MZW_AssocPeerAddressGet(assocHandle, &wifiSrvcStaConnMac)) 
            {
                uint8_t idx = 0;
                SYS_CONSOLE_PRINT("\r\nConnected STA MAC Address=%x:%x:%x:%x:%x:%x", wifiSrvcStaConnMac.addr[0], wifiSrvcStaConnMac.addr[1], wifiSrvcStaConnMac.addr[2], wifiSrvcStaConnMac.addr[3], wifiSrvcStaConnMac.addr[4], wifiSrvcStaConnMac.addr[5]);

                /* Store the connected STA Info in the STA Conn Array */
                for(idx = 0; idx < SYS_WIFI_MAX_STA_SUPPORTED; idx++)
                {
                    if(g_wifiSrvcStaConnInfo[idx].wifiSrvcAssocHandle == WDRV_PIC32MZW_ASSOC_HANDLE_INVALID)
                    {
                        g_wifiSrvcStaConnInfo[idx].wifiSrvcAssocHandle = assocHandle;
                        memcpy(&g_wifiSrvcStaConnInfo[idx].wifiSrvcStaAppInfo.macAddr, wifiSrvcStaConnMac.addr, WDRV_PIC32MZW_MAC_ADDR_LEN);
<#if (tcpipDhcps.TCPIP_STACK_USE_DHCP_SERVER)?has_content && (tcpipDhcps.TCPIP_STACK_USE_DHCP_SERVER) == true>
                        SYS_TIME_CallbackRegisterMS(SYS_WIFI_WaitForConnSTAIP, (uintptr_t)&g_wifiSrvcStaConnInfo[idx], 500, SYS_TIME_SINGLE);
<#else>
                        g_wifiSrvcStaConnInfo[idx].wifiSrvcStaAppInfo.ipAddr.Val = 0;
                        SYS_WIFI_CallBackFun(SYS_WIFI_CONNECT,&g_wifiSrvcStaConnInfo[idx].wifiSrvcStaAppInfo,g_wifiSrvcCookie);
</#if>
                        break;
                    }
                }
            }
            break;
        }

        case WDRV_PIC32MZW_CONN_STATE_DISCONNECTED: 
        {
            /* When STA Disconnect from PIC32MZW1 AP, 
               Wi-Fi driver updates disconnect event */
            SYS_WIFI_STA_CONNECTION_INFO *psStaConnInfo = NULL;
            /* Updating Wi-Fi service Associate handle on receiving 
               driver disconnection event */

            /* Find the Sta Conn Info Entry */
            psStaConnInfo = SYS_WIFI_FindStaConnInfo(assocHandle);
            if(psStaConnInfo != NULL)
            {
                SYS_CONSOLE_PRINT("\r\nDisconnected STA MAC Address=%x:%x:%x:%x:%x:%x", psStaConnInfo->wifiSrvcStaAppInfo.macAddr[0], psStaConnInfo->wifiSrvcStaAppInfo.macAddr[1], psStaConnInfo->wifiSrvcStaAppInfo.macAddr[2], psStaConnInfo->wifiSrvcStaAppInfo.macAddr[3], psStaConnInfo->wifiSrvcStaAppInfo.macAddr[4], psStaConnInfo->wifiSrvcStaAppInfo.macAddr[5]);
                TCPIP_NET_HANDLE netHdl = TCPIP_STACK_NetHandleGet("PIC32MZW1");
                TCPIP_DHCPS_LeaseEntryRemove(netHdl, (TCPIP_MAC_ADDR*)psStaConnInfo->wifiSrvcStaAppInfo.macAddr);
                /* Update the application on receiving Disconnect event */
                SYS_WIFI_CallBackFun(SYS_WIFI_DISCONNECT, psStaConnInfo->wifiSrvcStaAppInfo.macAddr, g_wifiSrvcCookie);

                /* Remove the Sta Conn Info Entry */
                SYS_WIFI_RemoveStaConnInfo(assocHandle);
            }
            break;
        }

        default:
        {
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
            SYS_APPDEBUG_ERR_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CONNECT, " AP Callback received with invalid state\r\n");
</#if>
            break;
        }

    }

}

</#if>
<#if SYS_WIFI_STA_ENABLE == true>
static void SYS_WIFI_STAConnCallBack
(
    DRV_HANDLE handle, 
    WDRV_PIC32MZW_ASSOC_HANDLE assocHandle,
    WDRV_PIC32MZW_CONN_STATE currentState
) 
{
    switch (currentState) 
    {
        case WDRV_PIC32MZW_CONN_STATE_CONNECTED:
        {
            /* When HOMEAP connect to PIC32MZW1 STA, Wi-Fi driver updated connected event */
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
            SYS_APPDEBUG_DBG_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CONNECT, "STA Connected\r\n");
</#if>
            /* Updating Wi-Fi service associate handle on receiving driver 
               connection event */
            g_wifiSrvcDrvAssocHdl = assocHandle;
            g_wifiSrvcAutoConnectRetry = 0;
<#if !((tcpipDhcp.TCPIP_STACK_USE_DHCP_CLIENT)?has_content && (tcpipDhcp.TCPIP_STACK_USE_DHCP_CLIENT) == true)>
            IPV4_ADDR ipAddr;
            ipAddr.Val = TCPIP_STACK_NetAddress(TCPIP_STACK_NetHandleGet("PIC32MZW1"));
            g_wifiSrvcConfig.staConfig.ipAddr.Val=ipAddr.Val;
            SYS_WIFI_CallBackFun(SYS_WIFI_CONNECT, &ipAddr, g_wifiSrvcCookie);
            SYS_CONSOLE_PRINT("static IP address obtained = %d.%d.%d.%d \r\n",
                        ipAddr.v[0], ipAddr.v[1], ipAddr.v[2], ipAddr.v[3]);
<#if !(tcpipDhcpcv6.TCPIP_STACK_USE_DHCPV6_CLIENT)?has_content && (tcpipDhcpcv6.TCPIP_STACK_USE_DHCPV6_CLIENT) == true>
<#if ((tcpipIPv6.TCPIP_STACK_USE_IPV6)?has_content && (tcpipIPv6.TCPIP_STACK_USE_IPV6) == true) >
            TCPIP_NET_HANDLE    netH;
            IPV6_ADDR_STRUCT currIpv6Add;
            IPV6_ADDR_HANDLE nextHandle;
            char   addrBuff[44];
            IPV6_ADDR addr6 = 0;
            netH = TCPIP_STACK_NetHandleGet("PIC32MZW1");
            nextHandle = TCPIP_STACK_NetIPv6AddressGet(netH, IPV6_ADDR_TYPE_UNICAST, &currIpv6Add, 0);
            if(nextHandle)
            {   // have a valid address; display it
                addr6 = currIpv6Add.address;
                TCPIP_Helper_IPv6AddressToString(&addr6, addrBuff, sizeof(addrBuff));
                SYS_CONSOLE_PRINT("static IPv6 address obtained = %s \r\n", addrBuff);
                memcpy(&g_wifiSrvcConfig.staConfig.ipv6Addr, &addr6, sizeof(addr6));
                /* Update the application(client) on receiving IP address */
                SYS_WIFI_CallBackFun(SYS_WIFI_CONNECT_WITH_IPV6, &g_wifiSrvcConfig.staConfig.ipv6Addr, g_wifiSrvcCookie);
            }
</#if>
</#if>
</#if>
            break;
        }

        case WDRV_PIC32MZW_CONN_STATE_FAILED:
        {
            /* When user provided HOMEAP configuration is not matching with near 
               by available HOMEAPs,Wi-Fi driver updated event Fail. */
            SYS_CONSOLE_PRINT(" Trying to connect to SSID : %s \r\n STA Connection failed. \r\n \r\n", SYS_WIFI_GetSSID());
            
            /* check user has enable the Auto connect feature in the STA
               mode,Auto connect Retry count is less then user configured 
               auto connect retry then request Wi-Fi driver for connection request */
            if ((true == SYS_WIFI_GetAutoConnect()) && (g_wifiSrvcAutoConnectRetry < MAX_AUTO_CONNECT_RETRY)) 
            {
                SYS_WIFI_SetTaskstatus(SYS_WIFI_STATUS_CONNECT_REQ);
                g_wifiSrvcAutoConnectRetry++;
            } 
            else if (g_wifiSrvcAutoConnectRetry == MAX_AUTO_CONNECT_RETRY) 
            {
                /* Auto connect Retry count is equal to Maximum connection attempt,
                   then set the Wi-Fi Service status to connection error and wait 
                   for user to re-configuration. */
                SYS_WIFI_SetTaskstatus(SYS_WIFI_STATUS_CONNECT_ERROR);
            }
            g_wifiSrvcDrvAssocHdl = WDRV_PIC32MZW_ASSOC_HANDLE_INVALID;
            break;
        }

        case WDRV_PIC32MZW_CONN_STATE_DISCONNECTED:
        {
            /* when PIC32MZW1 STA disconnected from connected HOMEAP,Wi-Fi driver 
               updated event disconnected. */
            SYS_CONSOLE_PRINT("STA DisConnected\r\n");
            if (true == SYS_WIFI_GetAutoConnect()) 
            {
                SYS_WIFI_SetTaskstatus(SYS_WIFI_STATUS_CONNECT_REQ);
            }

            /* Updating Wi-Fi service associate handle on receiving disconnection
               event */
            g_wifiSrvcDrvAssocHdl = WDRV_PIC32MZW_ASSOC_HANDLE_INVALID;

            /* Reset the Auto Connection retry to zero on receiving disconnect 
               event */
            g_wifiSrvcAutoConnectRetry = 0;
            break;
        }
        default:
        {
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
            SYS_APPDEBUG_ERR_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CONNECT, "STA Callback received with invalid state\r\n");
</#if>
            break;
        }
    }       
}
</#if>

/* Wi-Fi driver callback received on setting Regulatory domain */
static void SYS_WIFI_RegDomainCallback
(
    DRV_HANDLE handle, 
    uint8_t index, 
    uint8_t ofTotal, 
    bool isCurrent, 
    const WDRV_PIC32MZW_REGDOMAIN_INFO * const pRegDomInfo
) 
{
    if ((1 != index) || (1 != ofTotal) || (false == isCurrent) || (NULL == pRegDomInfo)) 
    {
        SYS_CONSOLE_MESSAGE("Regulatory domain set unsuccessful\r\n");
    }  
    if(!memcmp(pRegDomInfo,SYS_WIFI_GetCountryCode(),strlen((const char *)pRegDomInfo)))
    {
        g_isRegDomainSetReq = true;
    }

<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
    else 
    {
        SYS_APPDEBUG_DBG_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG, "Regulatory domain set successful\r\n");
    }
</#if>
}

<#if SYS_WIFI_SCAN_ENABLE == true>
/* Wi-Fi driver update the Scan result on callback*/
static void SYS_WIFI_ScanHandler
(
    DRV_HANDLE handle, 
    uint8_t index, 
    uint8_t ofTotal, 
    WDRV_PIC32MZW_BSS_INFO *pBSSInfo
) 
{
    if (0 == ofTotal) 
    {
        SYS_CONSOLE_MESSAGE("No AP Found Rescan\r\n");
    } 
    else 
    {
        if (1 == index) 
        {
            char cmdTxt[10];
            sprintf(cmdTxt, "SCAN#%02d", ofTotal);
            SYS_CONSOLE_PRINT("#%02d\r\n", ofTotal);
            SYS_CONSOLE_MESSAGE(">>#  RI  Sec  Recommend CH BSSID             SSID\r\n");
            SYS_CONSOLE_MESSAGE(">>#      Cap  Auth Type\r\n>>#\r\n");
        }
        SYS_CONSOLE_PRINT(">>%02d %d 0x%02x ", index, pBSSInfo->rssi, pBSSInfo->secCapabilities);
        switch (pBSSInfo->authTypeRecommended) 
        {
            case WDRV_PIC32MZW_AUTH_TYPE_OPEN:
            {
                SYS_CONSOLE_MESSAGE("OPEN     ");
                break;
            }

            case WDRV_PIC32MZW_AUTH_TYPE_WEP:
            {
                SYS_CONSOLE_MESSAGE("WEP      ");
                break;
            }

            case WDRV_PIC32MZW_AUTH_TYPE_WPAWPA2_PERSONAL:
            {
                SYS_CONSOLE_MESSAGE("WPA/2 PSK");
                break;
            }

            case WDRV_PIC32MZW_AUTH_TYPE_WPA2_PERSONAL:
            {
                SYS_CONSOLE_MESSAGE("WPA2 PSK ");
                break;
            }

            default:
            {
                SYS_CONSOLE_MESSAGE("Not Avail");
                break;
            }

        }
        SYS_CONSOLE_PRINT(" %02d %02X:%02X:%02X:%02X:%02X:%02X %s\r\n", pBSSInfo->ctx.channel,
                pBSSInfo->ctx.bssid.addr[0], pBSSInfo->ctx.bssid.addr[1], pBSSInfo->ctx.bssid.addr[2],
                pBSSInfo->ctx.bssid.addr[3], pBSSInfo->ctx.bssid.addr[4], pBSSInfo->ctx.bssid.addr[5],
                pBSSInfo->ctx.ssid.name);
    }
}
</#if>

<#if SYS_WIFI_STA_ENABLE == true>
<#if (tcpipDhcp.TCPIP_STACK_USE_DHCP_CLIENT)?has_content && (tcpipDhcp.TCPIP_STACK_USE_DHCP_CLIENT) == true>   
static void SYS_WIFI_TCPIP_DHCP_EventHandler
(
    TCPIP_NET_HANDLE hNet, 
    TCPIP_DHCP_EVENT_TYPE evType, 
    const void* param
) 
{
    IPV4_ADDR ipAddr;
    IPV4_ADDR gateWayAddr;
<#if SYS_WIFI_PROVISION_ENABLE == true>
    bool provConnStatus = false;
</#if>            
    switch (evType) 
    {
        case DHCP_EVENT_BOUND:
        {

            /* TCP/IP Stack BOUND event indicates
               PIC32MZW1 has received the IP address from connected HOMEAP */
            ipAddr.Val = TCPIP_STACK_NetAddress(hNet);
            if (ipAddr.Val) 
            {
                gateWayAddr.Val = TCPIP_STACK_NetAddressGateway(hNet);
                SYS_CONSOLE_PRINT("IP address obtained = %d.%d.%d.%d \r\n",
                        ipAddr.v[0], ipAddr.v[1], ipAddr.v[2], ipAddr.v[3]);
                SYS_CONSOLE_PRINT("Gateway IP address = %d.%d.%d.%d \r\n",
                        gateWayAddr.v[0], gateWayAddr.v[1], gateWayAddr.v[2], gateWayAddr.v[3]);

                g_wifiSrvcConfig.staConfig.ipAddr.Val=ipAddr.Val;
                SYS_WIFI_SetTaskstatus(SYS_WIFI_STATUS_STA_IP_RECIEVED);
            }
            break;
        }

        case DHCP_EVENT_CONN_ESTABLISHED:
        {
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
            SYS_APPDEBUG_DBG_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CONNECT, "connection to the DHCP server established \r\n");
</#if>
            break;
        }

        case DHCP_EVENT_CONN_LOST:
        {

            /* Received the TCP/IP Stack Connection Lost event,
               PIC32MZW1 has lost IP address from connected HOMEAP */
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
            SYS_APPDEBUG_DBG_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CONNECT, "connection to the DHCP server lost \r\n");
</#if>

            /* Update the application(client) on lost IP address */
            SYS_WIFI_CallBackFun(SYS_WIFI_DISCONNECT,NULL,g_wifiSrvcCookie);
<#if SYS_WIFI_PROVISION_ENABLE == true>
            provConnStatus = false;

            /* Update the Wi-Fi provisioning service on lost IP Address, 
               The Wi-Fi provisioning service has to stop the TCP server socket.
               only applicable if user has enable TCP Socket configuration 
               from MHC */
            SYS_WIFIPROV_CtrlMsg(g_wifiSrvcProvObj,SYS_WIFIPROV_CONNECT,&provConnStatus,sizeof(bool));
</#if>
            break;
        }

        default:
        {
            break;
        }
    }
}
</#if>
<#if  SYS_WIFI_STA_ENABLE == true>
<#if ((tcpipIPv6.TCPIP_STACK_USE_IPV6)?has_content && (tcpipIPv6.TCPIP_STACK_USE_IPV6) == true) >
static void SYS_WIFI_TCPIP_IPv6EventHandler(TCPIP_NET_HANDLE hNet, IPV6_EVENT_TYPE evType, const void* evParam, const void* usrParam)
{
    IPV6_ADDR_STRUCT *pAddr;

    if (IPV6_EVENT_ADDRESS_ADDED == evType)
    {
        pAddr = (IPV6_ADDR_STRUCT*)evParam;

        if (NULL == pAddr)
        {
            return;
        }

        if (IPV6_ADDR_TYPE_UNICAST == pAddr->flags.type)
        {
            if (IPV6_ADDR_SCOPE_LINK_LOCAL == pAddr->flags.scope)
            {
                char   addrBuff[44];
                memcpy(&g_wifiSrvcConfig.staConfig.ipv6Addr[0], &pAddr->address, sizeof(pAddr->address));
                TCPIP_Helper_IPv6AddressToString(&pAddr->address, addrBuff, sizeof(addrBuff));
                SYS_CONSOLE_PRINT("IPv6 address obtained = %s \r\n", addrBuff);
				g_ipv6AddrIdx = 0;
				SYS_WIFI_SetTaskstatus(SYS_WIFI_STATUS_STA_IPV6_RECIEVED);
            }
            else if (IPV6_ADDR_SCOPE_GLOBAL == pAddr->flags.scope)
            {
                int i;
                IPV6_ADDR ipv6Addr;               
                memset(&ipv6Addr, 0, sizeof(ipv6Addr));

                for (i=1; i<3; i++)
                {
                    if ((0 == memcmp(&g_wifiSrvcConfig.staConfig.ipv6Addr[i].v, &pAddr->address.v, 16)))
                    {
                        break;
                    }
                    else
                    {
                        char   addrBuff[44];
                        
                        if ((0 != memcmp(&g_wifiSrvcConfig.staConfig.ipv6Addr[i].v, &ipv6Addr.v, 16)))
                        {
                            continue;
                        }

                        memcpy(&g_wifiSrvcConfig.staConfig.ipv6Addr[i].v, &pAddr->address.v, 16);
                        TCPIP_Helper_IPv6AddressToString(&g_wifiSrvcConfig.staConfig.ipv6Addr[i], addrBuff, sizeof(addrBuff));
                        SYS_CONSOLE_PRINT("IPv6 address obtained = %s \r\n", addrBuff);
                        g_ipv6AddrIdx = i;
                        SYS_WIFI_SetTaskstatus(SYS_WIFI_STATUS_STA_IPV6_RECIEVED);
                        break;
                    }
                }
            }
        }
        else if (IPV6_ADDR_TYPE_MULTICAST == pAddr->flags.type)
        {
        }
    }
}
</#if>
</#if>
</#if>

<#if SYS_WIFI_SCAN_ENABLE == true>
static WDRV_PIC32MZW_SSID_LIST * SYS_WIFI_CreateSsidList(void)
{
    WDRV_PIC32MZW_SSID_LIST * result;
    char key[2] = {0};
    key[0] = g_wifiSrvcScanConfig.delimChar;
    char * pch;
    char * start;
    char * end;
    int len = 0;
    int idx = 0;
    if (g_wifiSrvcScanConfig.pSsidList)
    {
        memset(g_scanSsidListString, 0, sizeof(g_scanSsidListString));
        start = g_wifiSrvcScanConfig.pSsidList;
        end = start + strlen(start);
        pch = strpbrk (start, key);
        while ((start < end) && (idx < SYS_WIFI_SCAN_MAX_SSID_COUNT))
        {
            len = (int)(pch-start);
            if ((len > 1) && (len < WDRV_PIC32MZW_MAX_SSID_LEN))
            {
                memset(userSsidLinkedList[idx].ssid.name, 0, WDRV_PIC32MZW_MAX_SSID_LEN);
                userSsidLinkedList[idx].ssid.length = len;
                memcpy(userSsidLinkedList[idx].ssid.name, start, len);
                sprintf(g_scanSsidListString + strlen(g_scanSsidListString), "%.*s%c", len, start, g_wifiSrvcScanConfig.delimChar);
                userSsidLinkedList[idx].pNext = NULL;
                if (idx > 0)
                {
                    userSsidLinkedList[idx-1].pNext = &userSsidLinkedList[idx];
                }
                idx++;
            }
            start = pch+1;
            pch = strpbrk(start,key);
            if (pch == NULL)
            {
                pch = end;
            }
        }
    }
    
    if (idx > 0)
    {
        result = userSsidLinkedList;
        g_scanSsidListString[strlen(g_scanSsidListString)-1] = 0;
        g_wifiSrvcScanConfig.pSsidList = g_scanSsidListString;
    }
    else
    {
        result = NULL;
    }

    return result;
}
</#if>

<#if SYS_WIFI_SCAN_ENABLE == true>
static SYS_WIFI_RESULT SYS_WIFI_SetScan (void)
{
    uint8_t ret = SYS_WIFI_FAILURE;
    
    if (false == WDRV_PIC32MZW_BSSFindInProgress(g_wifiSrvcObj.wifiSrvcDrvHdl))
    {
        WDRV_PIC32MZW_SSID_LIST * pSSIDList = NULL;

        pSSIDList = SYS_WIFI_CreateSsidList();

        SYS_WIFI_PrintScanConfig();

        if (SYS_WIFI_SCAN_MODE_ACTIVE != g_wifiSrvcScanConfig.mode)
        {
            pSSIDList = NULL;
        }
        
        if (g_wifiSrvcScanConfig.pNotifyCallback == NULL)
        {
            g_wifiSrvcScanConfig.pNotifyCallback = SYS_WIFI_ScanHandler;
        }

        if (WDRV_PIC32MZW_STATUS_OK == WDRV_PIC32MZW_BSSFindSetScanMatchMode(g_wifiSrvcObj.wifiSrvcDrvHdl, g_wifiSrvcScanConfig.matchMode))
        {
            
                if (WDRV_PIC32MZW_STATUS_OK == WDRV_PIC32MZW_BSSFindSetScanParameters(g_wifiSrvcObj.wifiSrvcDrvHdl, g_wifiSrvcScanConfig.numSlots, g_wifiSrvcScanConfig.activeSlotTime, g_wifiSrvcScanConfig.passiveSlotTime, g_wifiSrvcScanConfig.numProbes))
                {
                    if (WDRV_PIC32MZW_STATUS_OK == WDRV_PIC32MZW_BSSFindFirst(g_wifiSrvcObj.wifiSrvcDrvHdl, g_wifiSrvcScanConfig.channel, g_wifiSrvcScanConfig.mode, pSSIDList, (WDRV_PIC32MZW_BSSFIND_NOTIFY_CALLBACK) g_wifiSrvcScanConfig.pNotifyCallback))   
                    {
                        ret = SYS_WIFI_SUCCESS ;
                    }
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
                    else
                    {
                        SYS_APPDEBUG_ERR_PRINT(g_wifiSrvcAppDebugHdl, WIFI_SCAN, "Set Scan Find First failed!\r\n");
                    }
</#if>
                }
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
                else
                {
                    SYS_APPDEBUG_ERR_PRINT(g_wifiSrvcAppDebugHdl, WIFI_SCAN, "Set Scan Parameters failed!\r\n");
                }
</#if>                

        }
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
        else
        {
            SYS_APPDEBUG_ERR_PRINT(g_wifiSrvcAppDebugHdl, WIFI_SCAN, "Set Scan Match Mode failed!\r\n");
        }
</#if>
    }
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
    else
    {
        SYS_APPDEBUG_ERR_PRINT(g_wifiSrvcAppDebugHdl, WIFI_SCAN, "Scan already in progress!\r\n");
    }
</#if>
    return ret;
}
</#if>

static SYS_WIFI_RESULT SYS_WIFI_SetChannel(void)
{
    uint8_t ret = SYS_WIFI_FAILURE;
    uint8_t channel = SYS_WIFI_GetChannel();

    if (WDRV_PIC32MZW_STATUS_OK == WDRV_PIC32MZW_BSSCtxSetChannel(&g_wifiSrvcObj.wifiSrvcBssCtx, channel)) 
    {
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
        SYS_APPDEBUG_DBG_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG, " Wi-Fi channel request is successful with channel number:%d \r\n",channel);
</#if>
        ret = SYS_WIFI_SUCCESS;
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
    } 
    else
    {
        SYS_APPDEBUG_ERR_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG, " Wi-Fi channel request is unsuccessful with channel number:%d \r\n",channel);
</#if>
    }
    return ret;
}

<#if SYS_WIFI_STA_ENABLE == true>
static uint8_t SYS_WIFI_DisConnect(void)
{
    uint8_t ret = SYS_WIFI_FAILURE;

    if (WDRV_PIC32MZW_STATUS_OK == WDRV_PIC32MZW_BSSDisconnect(g_wifiSrvcObj.wifiSrvcDrvHdl)) 
    {
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
        SYS_APPDEBUG_DBG_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CONNECT, " Wi-Fi disconnect request is successful \r\n");
</#if>
        ret = SYS_WIFI_SUCCESS;
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
    }
    else
    {
        SYS_APPDEBUG_ERR_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CONNECT, " Wi-Fi disconnect request is unsuccessful \r\n");
</#if>
    }
    return ret;
}
</#if>
<#if SYS_WIFI_AP_ENABLE == true>

static uint8_t SYS_WIFI_APDisconnectSTA(uint8_t *macAddr)
{
    uint8_t ret = SYS_WIFI_FAILURE;

    WDRV_PIC32MZW_ASSOC_HANDLE staConnAssocHandle = SYS_WIFI_StaConnAssocIdFromMAC(macAddr);   
    if(WDRV_PIC32MZW_ASSOC_HANDLE_INVALID != staConnAssocHandle)
    {
        SYS_CONSOLE_PRINT("%s:%d staConnAssocHandle=%p\n",__FUNCTION__,__LINE__,staConnAssocHandle);
        if (WDRV_PIC32MZW_STATUS_OK == WDRV_PIC32MZW_AssocDisconnect(staConnAssocHandle))
        {
            return SYS_WIFI_SUCCESS;
        }
    }
    return ret;
}
</#if>

static SYS_WIFI_RESULT SYS_WIFI_ConnectReq(void)
{
    SYS_WIFI_RESULT ret = SYS_WIFI_CONNECT_FAILURE;
    
<#if (SYS_WIFI_STA_ENABLE == true) && (SYS_WIFI_AP_ENABLE == true)>
    SYS_WIFI_MODE devMode = SYS_WIFI_GetMode();
    if (SYS_WIFI_STA == devMode) 
    {
        if (WDRV_PIC32MZW_STATUS_OK == WDRV_PIC32MZW_BSSConnect(g_wifiSrvcObj.wifiSrvcDrvHdl, &g_wifiSrvcObj.wifiSrvcBssCtx, &g_wifiSrvcObj.wifiSrvcAuthCtx, SYS_WIFI_STAConnCallBack)) 
        {
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
            SYS_APPDEBUG_DBG_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CONNECT, "Wi-Fi Driver STA connect request is successful\r\n");
</#if>
            ret = SYS_WIFI_SUCCESS;
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
        }
        else
        {
            SYS_APPDEBUG_ERR_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CONNECT, " Wi-Fi Driver STA connect request is unsuccessful \r\n");
</#if>
        }
    } 
    else if (SYS_WIFI_AP == devMode)
    {
        if (WDRV_PIC32MZW_STATUS_OK == WDRV_PIC32MZW_APStart(g_wifiSrvcObj.wifiSrvcDrvHdl, &g_wifiSrvcObj.wifiSrvcBssCtx, &g_wifiSrvcObj.wifiSrvcAuthCtx, SYS_WIFI_APConnCallBack)) 
        {
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
            SYS_APPDEBUG_DBG_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CONNECT, "Wi-Fi Driver AP start request is successful\r\n");
</#if>
            ret = SYS_WIFI_SUCCESS;        
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
        } 
        else 
        {
            SYS_APPDEBUG_ERR_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CONNECT, "Wi-Fi Driver AP start request is unsuccessful \r\n");
</#if>
        }
    }
<#elseif SYS_WIFI_STA_ENABLE == true>
    if (WDRV_PIC32MZW_STATUS_OK == WDRV_PIC32MZW_BSSConnect(g_wifiSrvcObj.wifiSrvcDrvHdl, &g_wifiSrvcObj.wifiSrvcBssCtx, &g_wifiSrvcObj.wifiSrvcAuthCtx, SYS_WIFI_STAConnCallBack)) 
    {
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
        SYS_APPDEBUG_DBG_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CONNECT, "Wi-Fi Driver STA connect request is successful\r\n");
</#if>
        ret = SYS_WIFI_SUCCESS ;
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
    } 
    else 
    {
        SYS_APPDEBUG_ERR_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CONNECT, " Wi-Fi Driver STA connect request is unsuccessful \r\n");
</#if>
    }
<#elseif SYS_WIFI_AP_ENABLE == true>
    if (WDRV_PIC32MZW_STATUS_OK == WDRV_PIC32MZW_APStart(g_wifiSrvcObj.wifiSrvcDrvHdl, &g_wifiSrvcObj.wifiSrvcBssCtx, &g_wifiSrvcObj.wifiSrvcAuthCtx, SYS_WIFI_APConnCallBack)) 
    {
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
        SYS_APPDEBUG_DBG_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CONNECT, "Wi-Fi Driver AP start request is successful\r\n");
</#if>
        ret = SYS_WIFI_SUCCESS ;
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
    } 
    else 
    {
        SYS_APPDEBUG_ERR_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CONNECT, "Wi-Fi Driver AP start request is unsuccessful \r\n");
</#if>
    }
</#if>
    
    if (SYS_WIFI_CONNECT_FAILURE == ret) 
    {
       SYS_WIFI_SetTaskstatus(SYS_WIFI_STATUS_CONNECT_ERROR);	
    }
    return ret;
}

static SYS_WIFI_RESULT SYS_WIFI_SetSSID(void)
{
    SYS_WIFI_RESULT ret = SYS_WIFI_CONFIG_FAILURE;
    uint8_t * ssid = SYS_WIFI_GetSSID();
    uint8_t ssidLen = SYS_WIFI_GetSSIDLen();

    if (WDRV_PIC32MZW_STATUS_OK == WDRV_PIC32MZW_BSSCtxSetSSID(&g_wifiSrvcObj.wifiSrvcBssCtx, ssid, ssidLen)) 
    {
<#if SYS_WIFI_AP_ENABLE == true>
        if (SYS_WIFI_AP == SYS_WIFI_GetMode()) 
        {
            WDRV_PIC32MZW_BSSCtxSetSSIDVisibility(&g_wifiSrvcObj.wifiSrvcBssCtx, SYS_WIFI_GetSSIDVisibility());
        }
</#if>
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
        SYS_APPDEBUG_DBG_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG, "Wi-Fi Driver SSID request is successful\r\n");
</#if>        
        ret = SYS_WIFI_SUCCESS;
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
    } 
    else 
    {
        SYS_APPDEBUG_ERR_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG, "Wi-Fi Driver SSID request is unsuccessful \r\n");
</#if>
    }
    return ret;
}
<#if SYS_WIFI_STA_AUTH == "WPAWPA2-Enterprise" || SYS_WIFI_STA_AUTH == "WPA2-Enterprise" || SYS_WIFI_STA_AUTH == "WPA2WPA3-Enterprise" || SYS_WIFI_STA_AUTH == "WPA3-Enterprise" >
static SYS_WIFI_TLS_CONTEXT_HANDLE SYS_WIFI_Create_TLS_Context(
    const uint8_t *const pCAcert,
    uint16_t u16CAcertLen,
    int caCertFormat,    
    const uint8_t *const pCert,
    uint16_t u16CertLen,
    int privCertFormat,
    const uint8_t *const pPriKey,
    uint16_t u16PriKeyLen,
    int privKeyFormat)
{
    WOLFSSL_CTX *pTlsCtx = NULL;     
    // Create wolfssl context with TLS v1.2 
    pTlsCtx = wolfSSL_CTX_new(wolfTLSv1_2_client_method());
    // Load CA certificate into WOLFSSL_CTX for validating peer
    if (SSL_SUCCESS != wolfSSL_CTX_load_verify_buffer(pTlsCtx, pCAcert, u16CAcertLen, caCertFormat))
    {
        wolfSSL_CTX_free(pTlsCtx);
        SYS_CONSOLE_PRINT("\n\r_Create_TLS_Context load ca cert failed\n");
        return SYS_WIFI_TLS_CONTEXT_HANDLE_INVALID;
    }

    
    // Verify the certificate received from the server during the handshake 
    wolfSSL_CTX_set_verify(pTlsCtx, WOLFSSL_VERIFY_PEER, 0);
    
<#if SYS_WIFI_ENT_METHOD == "TLS">

    // Load client certificate into WOLFSSL_CTX 
    if (SSL_SUCCESS != wolfSSL_CTX_use_certificate_buffer(pTlsCtx, pCert, u16CertLen, privCertFormat))
    {
        wolfSSL_CTX_free(pTlsCtx);
        SYS_CONSOLE_PRINT("_Create_TLS_Context load priv cert failed\n");
        return SYS_WIFI_TLS_CONTEXT_HANDLE_INVALID;
    }

    // Load client key into WOLFSSL_CTX
    if (SSL_SUCCESS != wolfSSL_CTX_use_PrivateKey_buffer(pTlsCtx, pPriKey, u16PriKeyLen, privKeyFormat))
    {
        wolfSSL_CTX_free(pTlsCtx);
        SYS_CONSOLE_PRINT("_Create_TLS_Context load priv key failed\n");
        return SYS_WIFI_TLS_CONTEXT_HANDLE_INVALID;
    }
</#if>
    return (SYS_WIFI_TLS_CONTEXT_HANDLE) pTlsCtx;
}
</#if>

static SYS_WIFI_RESULT SYS_WIFI_ConfigReq(void)
{
    SYS_WIFI_RESULT ret = SYS_WIFI_SUCCESS;
    uint8_t authType = SYS_WIFI_GetAuthType();
    uint8_t * const pwd = SYS_WIFI_GetPsk();
    uint8_t pwdLen = SYS_WIFI_GetPskLen();
    <#if SYS_WIFI_STA_AUTH == "WPAWPA2-Enterprise" || SYS_WIFI_STA_AUTH == "WPA2-Enterprise" || SYS_WIFI_STA_AUTH == "WPA2WPA3-Enterprise" || SYS_WIFI_STA_AUTH == "WPA3-Enterprise" >
    SYS_WIFI_TLS_CONTEXT_HANDLE tlsCtxHandle = SYS_WIFI_TLS_CONTEXT_HANDLE_INVALID;
                tlsCtxHandle = SYS_WIFI_Create_TLS_Context(
                        SYS_WIFI_STA_ENT_CACERT_MODULE_NAME,
                        sizeof(SYS_WIFI_STA_ENT_CACERT_MODULE_NAME),
                        SYS_WIFI_STA_ENT_CACERT_FORMAT,
                        SYS_WIFI_STA_ENT_PRIVATE_CERT_MODULE_NAME,
                        sizeof(SYS_WIFI_STA_ENT_PRIVATE_CERT_MODULE_NAME),
                        SYS_WIFI_STA_ENT_PRIVATE_CERT_FORMAT,
                        SYS_WIFI_STA_ENT_PRIVATE_KEY_MODULE_NAME,
                        sizeof(SYS_WIFI_STA_ENT_PRIVATE_KEY_MODULE_NAME),
                        SYS_WIFI_STA_ENT_PRIVATE_FORMAT);
    const char *pIdentity = SYS_WIFI_STA_ENT_USER ;
    const char *domain = SYS_WIFI_STA_ENT_SERVER_DOMAIN;
    </#if>

<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
        SYS_APPDEBUG_DBG_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG, "authType=%d,password=%s,password len=%d\r\n",authType,pwd,pwdLen);
</#if>
    if (SYS_WIFI_SUCCESS == SYS_WIFI_SetSSID()) 
    {
        switch (authType) 
        {
            case SYS_WIFI_OPEN:
            {
                if (WDRV_PIC32MZW_STATUS_OK != WDRV_PIC32MZW_AuthCtxSetOpen(&g_wifiSrvcObj.wifiSrvcAuthCtx)) 
                {
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
                    SYS_APPDEBUG_ERR_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG, " Unable to set Authentication to Open \r\n");
</#if>
                    ret = SYS_WIFI_CONFIG_FAILURE;
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
                } 
                else 
                {
                    SYS_APPDEBUG_DBG_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG, "set Authentication to Open \r\n");
</#if>
                }
                break;
            }

            case SYS_WIFI_WPA2:
            {                
                if (WDRV_PIC32MZW_STATUS_OK != WDRV_PIC32MZW_AuthCtxSetPersonal(&g_wifiSrvcObj.wifiSrvcAuthCtx, pwd, pwdLen, WDRV_PIC32MZW_AUTH_TYPE_WPA2_PERSONAL)) 
                {
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
                    SYS_APPDEBUG_ERR_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG, "Unable to set authentication to WPA2 PSK\r\n");
</#if>
                    ret = SYS_WIFI_CONFIG_FAILURE;
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
                } 
                else 
                {
                    SYS_APPDEBUG_DBG_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG, "set authentication to WPA2 PSK\r\n");
</#if>
                }
                break;
            }

            case SYS_WIFI_WPAWPA2MIXED:
            {
                if (WDRV_PIC32MZW_STATUS_OK != WDRV_PIC32MZW_AuthCtxSetPersonal(&g_wifiSrvcObj.wifiSrvcAuthCtx, pwd, pwdLen, WDRV_PIC32MZW_AUTH_TYPE_WPAWPA2_PERSONAL)) 
                {
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
                    SYS_APPDEBUG_ERR_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG, "Unable to set authentication to WPAWPA2 MIXED PSK\r\n");
</#if>
                    ret = SYS_WIFI_CONFIG_FAILURE;
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
                } 
                else
                {
                    SYS_APPDEBUG_DBG_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG, "set authentication to WPAWPA2 MIXED PSK\r\n");
</#if>
                }
                break;
            }
<#if (drvWifiPic32mzw1.DRV_WIFI_PIC32MZW1_SUPPORT_SAE)?has_content && (drvWifiPic32mzw1.DRV_WIFI_PIC32MZW1_SUPPORT_SAE) == true>

            case SYS_WIFI_WPA2WPA3MIXED:
            {
                if (WDRV_PIC32MZW_STATUS_OK != WDRV_PIC32MZW_AuthCtxSetPersonal(&g_wifiSrvcObj.wifiSrvcAuthCtx, pwd, pwdLen, WDRV_PIC32MZW_AUTH_TYPE_WPA2WPA3_PERSONAL)) 
                {
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
                    SYS_APPDEBUG_ERR_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG, "Unable to set authentication to WPA2WPA3 MIXED \r\n");
</#if>
                    ret = SYS_WIFI_CONFIG_FAILURE;
                }
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
                else
                {
                    SYS_APPDEBUG_DBG_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG, "set authentication to WPA2WPA3 MIXED \r\n");
                }
</#if>
                break;
            }

            case SYS_WIFI_WPA3:
            {
                if (WDRV_PIC32MZW_STATUS_OK != WDRV_PIC32MZW_AuthCtxSetPersonal(&g_wifiSrvcObj.wifiSrvcAuthCtx, pwd, pwdLen, WDRV_PIC32MZW_AUTH_TYPE_WPA3_PERSONAL)) 
                {
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
                    SYS_APPDEBUG_ERR_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG, "Unable to set authentication to WPA3 PSK \r\n");
</#if>
                    ret = SYS_WIFI_CONFIG_FAILURE;
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
                } 
                else 
                {
                    SYS_APPDEBUG_DBG_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG, "set authentication to WPA3 PSK \r\n");
</#if>
                }
                break;
            }
</#if>
<#if SYS_WIFI_STA_AUTH == "WPAWPA2-Enterprise" || SYS_WIFI_STA_AUTH == "WPA2-Enterprise" || SYS_WIFI_STA_AUTH == "WPA2WPA3-Enterprise" || SYS_WIFI_STA_AUTH == "WPA3-Enterprise" >
            case SYS_WIFI_WPA2_ENTERPRISE:           
            case SYS_WIFI_WPAWPA2MIXED_ENTERPRISE:    
            case SYS_WIFI_WPA3_ENTERPRISE:    
            case SYS_WIFI_WPA2WPA3MIXED_ENTERPRISE:
            {
                uint8_t method = SYS_WIFI_STA_ENTERPRISE_METHOD;
                switch(method)
                {
                    case(SYS_WIFI_ENTERPRISE_TLS):
                    {
                        if (WDRV_PIC32MZW_STATUS_OK != WDRV_PIC32MZW_AuthCtxSetEnterpriseTLS(&g_wifiSrvcObj.wifiSrvcAuthCtx,pIdentity,tlsCtxHandle,domain,SYS_WIFI_STA_ENTERPRISE_TYPE)) 
                        {
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
                            SYS_APPDEBUG_ERR_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG, "Unable to set authentication to WPA3 PSK \r\n");
</#if>
                            ret = SYS_WIFI_CONFIG_FAILURE;
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
                        }
                        else
                        {
                            SYS_APPDEBUG_DBG_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG, "set authentication to WPA3 PSK \r\n");
</#if>
                    }
                        break;
                    }
<#if SYS_WIFI_ENT_METHOD == "TTLS">
                    case(SYS_WIFI_ENTERPRISE_TTLS):
                    {
                        if (WDRV_PIC32MZW_STATUS_OK != WDRV_PIC32MZW_AuthCtxSetEnterpriseTTLSMSCHAPv2(&g_wifiSrvcObj.wifiSrvcAuthCtx,pIdentity,tlsCtxHandle,domain,SYS_WIFI_MSCHAPV2_USERNAME,SYS_WIFI_MSCHAPV2_PASSWORD,SYS_WIFI_STA_ENTERPRISE_TYPE)) 
                        {
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
                            SYS_APPDEBUG_ERR_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG, "Unable to set authentication to WPA3 PSK \r\n");
</#if>
                            ret = SYS_WIFI_CONFIG_FAILURE;
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
                        }
                        else
                        {
                            SYS_APPDEBUG_DBG_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG, "set authentication to WPA3 PSK \r\n");
</#if>
                        }
                        break;
                    }
</#if>
                    default:
                    {
                        ret = SYS_WIFI_CONFIG_FAILURE;
                        break;
                    }
                }
                break;
            }
</#if>
            case SYS_WIFI_WEP:
            {
                ret = SYS_WIFI_CONFIG_FAILURE; 
                /* Wi-Fi service doesn't support WEP */
                break;
            }

            default:
            {
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
                SYS_APPDEBUG_ERR_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG, "set valid authentication type\r\n");
</#if>
                ret = SYS_WIFI_CONFIG_FAILURE;
            }
        }
    }

    if (SYS_WIFI_CONFIG_FAILURE == ret) 
    {
        SYS_CONSOLE_MESSAGE("Error:Enter valid Wi-Fi configuration\r\n");
        SYS_WIFI_SetTaskstatus(SYS_WIFI_STATUS_CONFIG_ERROR);
    }

    return ret;
}

static SYS_WIFI_RESULT SYS_WIFI_SetConfig
(
    SYS_WIFI_CONFIG *wifi_config, 
    SYS_WIFI_STATUS status
) 
{
<#if SYS_WIFI_PROVISION_ENABLE == true>
    /* When user has enabled Save config option,request Wi-Fi provisioning service 
       to store the configuration before making the connection request to user */
    //if (true == SYS_WIFI_GetSaveConfig())
    if(wifi_config->saveConfig == true)
    {
        return SYS_WIFIPROV_CtrlMsg(g_wifiSrvcProvObj,SYS_WIFIPROV_SETCONFIG,wifi_config,sizeof(SYS_WIFI_CONFIG));
    } 
    else 
    {
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
        SYS_APPDEBUG_DBG_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG, "Save configuration is disabled\r\n");
</#if>

        /*  When user has not enabled Save config option */
        SYS_WIFI_RESULT ret = SYS_WIFI_SUCCESS;

        /* Copy the user Wi-Fi configuration and make connection request */
        memcpy(&g_wifiSrvcConfig,wifi_config,sizeof(SYS_WIFI_CONFIG));
        SYS_WIFI_SetTaskstatus(status);
        return ret;
    }
<#else>

    /* When Wi-Fi provisioning service is not enable by user from MHC configuration */
    SYS_WIFI_RESULT ret = SYS_WIFI_SUCCESS;

    /* Copy the user Wi-Fi configuration and make connection request */
    memcpy(&g_wifiSrvcConfig,wifi_config,sizeof(SYS_WIFI_CONFIG));
    SYS_WIFI_SetTaskstatus(status);
    return ret;	
</#if>
}

static uint32_t SYS_WIFI_ExecuteBlock
(
    SYS_MODULE_OBJ object
) 
{
    SYS_STATUS                   tcpIpStat;
<#if ((tcpipDhcp.TCPIP_STACK_USE_DHCP_CLIENT)?has_content && (tcpipDhcp.TCPIP_STACK_USE_DHCP_CLIENT) == true) ||
     ((tcpipDhcps.TCPIP_STACK_USE_DHCP_SERVER)?has_content && (tcpipDhcps.TCPIP_STACK_USE_DHCP_SERVER) == true)>
    static TCPIP_NET_HANDLE      netHdl;
</#if>
    SYS_WIFI_OBJ *               wifiSrvcObj = (SYS_WIFI_OBJ *) object;
<#if SYS_WIFI_PROVISION_ENABLE == true>
    uint8_t                      ret =  SYS_WIFIPROV_OBJ_INVALID;
<#if SYS_WIFI_STA_ENABLE == true>	
	static bool provConnStatus = false;
</#if>
<#else>
    uint8_t                      ret =  SYS_WIFI_OBJ_INVALID;
</#if>

<#if SYS_WIFI_AP_ENABLE == true>
<#if (tcpipDhcps.TCPIP_STACK_USE_DHCP_SERVER)?has_content && (tcpipDhcps.TCPIP_STACK_USE_DHCP_SERVER) == true>
    IPV4_ADDR                    apLastIp = {-1};
    IPV4_ADDR                    apIpAddr;
</#if>
</#if>
 
    if (&g_wifiSrvcObj == (SYS_WIFI_OBJ*) wifiSrvcObj)
    {    
        switch (wifiSrvcObj->wifiSrvcStatus) 
        {
            case SYS_WIFI_STATUS_INIT:
            { 
                if (OSAL_RESULT_TRUE == OSAL_SEM_Pend(&g_wifiSrvcSemaphore, OSAL_WAIT_FOREVER)) 
                {
                    /* When g_wifiSrvcInit set to true :
                        Case 1: When Wi-Fi provisioning service is enabled by user in the MHC, 
                               and when Wi-Fi Configuration read from NVM 
                               using Wi-Fi provisioning is valid  
                    
                        Case 2: When Wi-Fi provisioning service is disabled by user in the MHC, 
                               g_wifiSrvcInit set true by Wi-Fi service initialization */

                    if (true == g_wifiSrvcInit) 
                    {
                        if (SYS_STATUS_READY == WDRV_PIC32MZW_Status(sysObj.drvWifiPIC32MZW1)) 
                        {
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
                            SYS_APPDEBUG_DBG_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG, "Wi-Fi Driver is ready\r\n");
</#if>
                            wifiSrvcObj->wifiSrvcStatus = SYS_WIFI_STATUS_WDRV_OPEN_REQ;                
                        }
                    }
                    OSAL_SEM_Post(&g_wifiSrvcSemaphore);
                }
                break;
            }

            case SYS_WIFI_STATUS_WDRV_OPEN_REQ:
            {
                if (OSAL_RESULT_TRUE == OSAL_SEM_Pend(&g_wifiSrvcSemaphore, OSAL_WAIT_FOREVER)) 
                {
                    wifiSrvcObj->wifiSrvcDrvHdl = WDRV_PIC32MZW_Open(0, 0);
                    if (DRV_HANDLE_INVALID != wifiSrvcObj->wifiSrvcDrvHdl) 
                    {
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
                        SYS_APPDEBUG_DBG_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG, "Wi-Fi Driver open successfully\r\n");
</#if>
                        if (WDRV_PIC32MZW_STATUS_OK == WDRV_PIC32MZW_RegDomainGet(wifiSrvcObj->wifiSrvcDrvHdl,WDRV_PIC32MZW_REGDOMAIN_SELECT_CURRENT,SYS_WIFI_RegDomainCallback))
                        {
                            SYS_WIFI_PrintWifiConfig();
                            wifiSrvcObj->wifiSrvcStatus = SYS_WIFI_STATUS_AUTOCONNECT_WAIT;
                        }
                    }
                    OSAL_SEM_Post(&g_wifiSrvcSemaphore);
                }
                break;
            }

            case SYS_WIFI_STATUS_AUTOCONNECT_WAIT:
            {
                if (OSAL_RESULT_TRUE == OSAL_SEM_Pend(&g_wifiSrvcSemaphore, OSAL_WAIT_FOREVER)) 
                {
                    /* When user has enabled the auto connect feature of the Wi-Fi service in MHC(STA mode).
                       or in AP mode, below condition will be always true */

                    if (true == SYS_WIFI_GetAutoConnect()) 
                    {
                        if(g_isRegDomainSetReq == true)
                        {

                            if (WDRV_PIC32MZW_STATUS_OK == WDRV_PIC32MZW_RegDomainSet(wifiSrvcObj->wifiSrvcDrvHdl, SYS_WIFI_GetCountryCode(), SYS_WIFI_RegDomainCallback)) 
                            {
                                
                                g_isRegDomainSetReq = false;
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
                            } 
                            else
                            {
                                SYS_APPDEBUG_ERR_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG, "Wi-Fi driver Regulatory domain set failed\r\n");
</#if>
                            }
                        }
                        wifiSrvcObj->wifiSrvcStatus = SYS_WIFI_STATUS_TCPIP_WAIT_FOR_TCPIP_INIT;
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
                    } 
                    else
                    {
                        SYS_APPDEBUG_DBG_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG, "Auto connect is disabled\r\n");
</#if>
                    }
                    OSAL_SEM_Post(&g_wifiSrvcSemaphore);
                }
                break;
            }

            case SYS_WIFI_STATUS_TCPIP_WAIT_FOR_TCPIP_INIT:
            {
                if (OSAL_RESULT_TRUE == OSAL_SEM_Pend(&g_wifiSrvcSemaphore, OSAL_WAIT_FOREVER)) 
                {
                    tcpIpStat = TCPIP_STACK_Status(sysObj.tcpip);
                    if (tcpIpStat < 0) 
                    {
                        SYS_CONSOLE_MESSAGE("  TCP/IP stack initialization failed!\r\n");
                        wifiSrvcObj->wifiSrvcStatus = SYS_WIFI_STATUS_TCPIP_ERROR;
                    } 
                    else if (tcpIpStat == SYS_STATUS_READY) 
                    {
<#if (SYS_WIFI_STA_ENABLE == true) && (SYS_WIFI_AP_ENABLE == true)>                  
<#if ((tcpipDhcp.TCPIP_STACK_USE_DHCP_CLIENT)?has_content && (tcpipDhcp.TCPIP_STACK_USE_DHCP_CLIENT) == true) ||
     ((tcpipDhcps.TCPIP_STACK_USE_DHCP_SERVER)?has_content && (tcpipDhcps.TCPIP_STACK_USE_DHCP_SERVER) == true) ||
	 (((tcpipDhcpcv6.TCPIP_STACK_USE_DHCPV6_CLIENT)?has_content && (tcpipDhcpcv6.TCPIP_STACK_USE_DHCPV6_CLIENT) == true) &&
		((tcpipIPv6.TCPIP_STACK_USE_IPV6)?has_content && (tcpipIPv6.TCPIP_STACK_USE_IPV6) == true))>
                        /* PIC32MZW1 network handle*/
                        netHdl = TCPIP_STACK_NetHandleGet("PIC32MZW1");
</#if>
<#if (tcpipDhcps.TCPIP_STACK_USE_DHCP_SERVER)?has_content && (tcpipDhcps.TCPIP_STACK_USE_DHCP_SERVER) == true>
<#if (tcpipDhcp.TCPIP_STACK_USE_DHCP_CLIENT)?has_content && (tcpipDhcp.TCPIP_STACK_USE_DHCP_CLIENT) == true>
                        /* STA Mode */
                        if (SYS_WIFI_STA == SYS_WIFI_GetMode()) 
                        {
                            if (true == TCPIP_DHCPS_IsEnabled(netHdl)) 
                            {
                                TCPIP_DHCPS_Disable(netHdl);
                            }
                            if ((true == TCPIP_DHCP_Enable(netHdl)) &&
                                (TCPIP_STACK_ADDRESS_SERVICE_DHCPC == TCPIP_STACK_AddressServiceSelect(_TCPIPStackHandleToNet(netHdl), TCPIP_NETWORK_CONFIG_DHCP_CLIENT_ON))) 
                            {
                                    g_wifiSrvcDhcpHdl = TCPIP_DHCP_HandlerRegister(netHdl, SYS_WIFI_TCPIP_DHCP_EventHandler, NULL);
                            }
                        } 
                        else if (SYS_WIFI_AP == SYS_WIFI_GetMode()) /*AP Mode*/
                        {
                            if (true == TCPIP_DHCP_IsEnabled(netHdl)) 
                            {
                                TCPIP_DHCP_Disable(netHdl);
                            }
                            TCPIP_DHCPS_Enable(netHdl); /*Enable DHCP Server in AP mode*/
                        }
</#if>
</#if>
<#if (tcpipDhcpcv6.TCPIP_STACK_USE_DHCPV6_CLIENT)?has_content && (tcpipDhcpcv6.TCPIP_STACK_USE_DHCPV6_CLIENT) == true>
<#if ((tcpipIPv6.TCPIP_STACK_USE_IPV6)?has_content && (tcpipIPv6.TCPIP_STACK_USE_IPV6) == true) >
                        /* STA Mode */
                        if (SYS_WIFI_STA == SYS_WIFI_GetMode()) 
                        {
                            if (TCPIP_DHCPV6_CLIENT_RES_OK == TCPIP_DHCPV6_Enable(netHdl))
                            {
                            }
                            memset(g_wifiSrvcConfig.staConfig.ipv6Addr, 0, sizeof(g_wifiSrvcConfig.staConfig.ipv6Addr));
                            TCPIP_IPV6_HandlerRegister(netHdl, SYS_WIFI_TCPIP_IPv6EventHandler, NULL);
                        } 
                        else if (SYS_WIFI_AP == SYS_WIFI_GetMode()) /*AP Mode*/
                        {
                            TCPIP_DHCPV6_CLIENT_INFO ClientInfo;

                            memset(&ClientInfo, 0, sizeof(ClientInfo));
                            TCPIP_DHCPV6_ClientInfoGet(netHdl, &ClientInfo);
                            if (ClientInfo.clientState > TCPIP_DHCPV6_CLIENT_STATE_IDLE) 
                            {
                                TCPIP_DHCPV6_Disable(netHdl);
                            }
                        }
</#if>
</#if>
<#elseif SYS_WIFI_STA_ENABLE == true>
<#if ((tcpipDhcp.TCPIP_STACK_USE_DHCP_CLIENT)?has_content && (tcpipDhcp.TCPIP_STACK_USE_DHCP_CLIENT) == true) ||
     ((tcpipDhcps.TCPIP_STACK_USE_DHCP_SERVER)?has_content && (tcpipDhcps.TCPIP_STACK_USE_DHCP_SERVER) == true) ||
	 (((tcpipDhcpcv6.TCPIP_STACK_USE_DHCPV6_CLIENT)?has_content && (tcpipDhcpcv6.TCPIP_STACK_USE_DHCPV6_CLIENT) == true) &&
		((tcpipIPv6.TCPIP_STACK_USE_IPV6)?has_content && (tcpipIPv6.TCPIP_STACK_USE_IPV6) == true))>
                        /* PIC32MZW1 network handle*/
                        netHdl = TCPIP_STACK_NetHandleGet("PIC32MZW1");
</#if>
<#if (tcpipDhcps.TCPIP_STACK_USE_DHCP_SERVER)?has_content && (tcpipDhcps.TCPIP_STACK_USE_DHCP_SERVER) == true>
                        /* STA Mode*/
                        if (true == TCPIP_DHCPS_IsEnabled(netHdl)) 
                        {
                            TCPIP_DHCPS_Disable(netHdl);
                        }
</#if>
<#if (tcpipDhcp.TCPIP_STACK_USE_DHCP_CLIENT)?has_content && (tcpipDhcp.TCPIP_STACK_USE_DHCP_CLIENT) == true>
                        if ((true == TCPIP_DHCP_Enable(netHdl)) && 
                            (TCPIP_STACK_ADDRESS_SERVICE_DHCPC == TCPIP_STACK_AddressServiceSelect(_TCPIPStackHandleToNet(netHdl), TCPIP_NETWORK_CONFIG_DHCP_CLIENT_ON))) 
                        {
                            g_wifiSrvcDhcpHdl= TCPIP_DHCP_HandlerRegister (netHdl, SYS_WIFI_TCPIP_DHCP_EventHandler, NULL);
                        }
</#if>
<#if (tcpipDhcpcv6.TCPIP_STACK_USE_DHCPV6_CLIENT)?has_content && (tcpipDhcpcv6.TCPIP_STACK_USE_DHCPV6_CLIENT) == true>
<#if ((tcpipIPv6.TCPIP_STACK_USE_IPV6)?has_content && (tcpipIPv6.TCPIP_STACK_USE_IPV6) == true) >
                            if (TCPIP_DHCPV6_CLIENT_RES_OK == TCPIP_DHCPV6_Enable(netHdl))
						{
						}
                        memset(g_wifiSrvcConfig.staConfig.ipv6Addr, 0, sizeof(g_wifiSrvcConfig.staConfig.ipv6Addr));
                        TCPIP_IPV6_HandlerRegister(netHdl, SYS_WIFI_TCPIP_IPv6EventHandler, NULL);
</#if>
</#if>
<#elseif SYS_WIFI_AP_ENABLE == true>
<#if ((tcpipDhcp.TCPIP_STACK_USE_DHCP_CLIENT)?has_content && (tcpipDhcp.TCPIP_STACK_USE_DHCP_CLIENT) == true) ||
     ((tcpipDhcps.TCPIP_STACK_USE_DHCP_SERVER)?has_content && (tcpipDhcps.TCPIP_STACK_USE_DHCP_SERVER) == true)>
                        /* PIC32MZW1 network handle*/
                        netHdl = TCPIP_STACK_NetHandleGet("PIC32MZW1");
</#if>
<#if (tcpipDhcp.TCPIP_STACK_USE_DHCP_CLIENT)?has_content && (tcpipDhcp.TCPIP_STACK_USE_DHCP_CLIENT) == true>
                        /* AP Mode*/
                        if (true == TCPIP_DHCP_IsEnabled(netHdl)) 
                        {
                            TCPIP_DHCP_Disable(netHdl);
                        }
</#if>
<#if (tcpipDhcps.TCPIP_STACK_USE_DHCP_SERVER)?has_content && (tcpipDhcps.TCPIP_STACK_USE_DHCP_SERVER) == true>
                        /* Enable DHCP Server in AP mode */
                        TCPIP_DHCPS_Enable(netHdl);
</#if>
</#if>
                    }                
                    wifiSrvcObj->wifiSrvcStatus = SYS_WIFI_STATUS_CONNECT_REQ;
                    OSAL_SEM_Post(&g_wifiSrvcSemaphore);
                }
                break;
            }

            case SYS_WIFI_STATUS_CONNECT_REQ:
            {
                if (OSAL_RESULT_TRUE == OSAL_SEM_Pend(&g_wifiSrvcSemaphore, OSAL_WAIT_FOREVER)) 
                {
                    if (SYS_WIFI_SUCCESS == SYS_WIFI_SetChannel()) 
                    {
                        if (SYS_WIFI_SUCCESS == SYS_WIFI_ConfigReq()) 
                        {
						
<#if (SYS_WIFI_POWERSAVE_ENABLE == true) && (SYS_WIFI_WAKEUP == "LISTEN INTERVAL")>                            
                            WDRV_PIC32MZW_PowerSaveListenIntervalSet(g_wifiSrvcObj.wifiSrvcDrvHdl,SYS_WIFI_LISTENINTERVAL);
                            WDRV_PIC32MZW_PowerSaveSleepInactLimitSet(g_wifiSrvcObj.wifiSrvcDrvHdl,SYS_WIFI_SLEEPINACTLIMIT);
</#if>

                            if (SYS_WIFI_SUCCESS == SYS_WIFI_ConnectReq()) 
                            {
<#if (SYS_WIFI_STA_ENABLE == true) && (SYS_WIFI_AP_ENABLE == true)>	
                                wifiSrvcObj->wifiSrvcStatus = (SYS_WIFI_STA == SYS_WIFI_GetMode()) ? SYS_WIFI_STATUS_TCPIP_READY : SYS_WIFI_STATUS_WAIT_FOR_AP_IP;
<#elseif SYS_WIFI_STA_ENABLE == true>
                                wifiSrvcObj->wifiSrvcStatus = SYS_WIFI_STATUS_TCPIP_READY;
<#elseif SYS_WIFI_AP_ENABLE == true>
<#if (tcpipDhcps.TCPIP_STACK_USE_DHCP_SERVER)?has_content && (tcpipDhcps.TCPIP_STACK_USE_DHCP_SERVER) == true>
                                wifiSrvcObj->wifiSrvcStatus = SYS_WIFI_STATUS_WAIT_FOR_AP_IP;
<#else>
                                wifiSrvcObj->wifiSrvcStatus = SYS_WIFI_STATUS_TCPIP_READY;
</#if>
</#if>
                            }
                        }
                    }
                    OSAL_SEM_Post(&g_wifiSrvcSemaphore);
                }
                break;
            }
<#if SYS_WIFI_STA_ENABLE == true>
            case SYS_WIFI_STATUS_STA_IP_RECIEVED:
            {
                WDRV_PIC32MZW_CHANNEL_ID channel = 0;
                 
                /* Update the application(client) on receiving IP address */
                SYS_WIFI_CallBackFun(SYS_WIFI_CONNECT, &g_wifiSrvcConfig.staConfig.ipAddr, g_wifiSrvcCookie);
<#if SYS_WIFI_PROVISION_ENABLE == true>
                provConnStatus = true;

                /* Update the Wi-Fi provisioning service on receiving the IP Address, 
                   The Wi-Fi provisioning service has to start the TCP server socket
                   when IP address is assigned from HOMEAP to STA.only applicable 
                   if user has enable TCP Socket configuration from MHC */
                SYS_WIFIPROV_CtrlMsg(g_wifiSrvcProvObj,SYS_WIFIPROV_CONNECT,&provConnStatus,sizeof(bool));                
                WDRV_PIC32MZW_InfoOpChanGet(g_wifiSrvcObj.wifiSrvcDrvHdl,&channel);
                g_wifiSrvcConfig.staConfig.channel = (uint8_t )channel;
                
                if(g_wifiSrvcConfig.saveConfig == true)
                {
                  SYS_WIFIPROV_CtrlMsg(g_wifiSrvcProvObj,SYS_WIFIPROV_SETCONFIG,&g_wifiSrvcConfig,sizeof(SYS_WIFI_CONFIG));
                }
</#if>
                wifiSrvcObj->wifiSrvcStatus = SYS_WIFI_STATUS_TCPIP_READY;
                break;
            }
			
<#if ((tcpipIPv6.TCPIP_STACK_USE_IPV6)?has_content && (tcpipIPv6.TCPIP_STACK_USE_IPV6) == true) >
            case SYS_WIFI_STATUS_STA_IPV6_RECIEVED:
            {
                /* Update the application(client) on receiving IP address */
                SYS_WIFI_CallBackFun(SYS_WIFI_CONNECT_WITH_IPV6, &g_wifiSrvcConfig.staConfig.ipv6Addr[g_ipv6AddrIdx], g_wifiSrvcCookie);

<#if SYS_WIFI_PROVISION_ENABLE == true>
                if(provConnStatus == false)
                {
                    WDRV_PIC32MZW_CHANNEL_ID channel = 0 ;
                    provConnStatus = true;
                    /* Update the Wi-Fi provisioning service on receiving the IP Address, 
                       The Wi-Fi provisioning service has to start the TCP server socket
                       when IP address is assigned from HOMEAP to STA.only applicable 
                       if user has enable TCP Socket configuration from MHC */
                    SYS_WIFIPROV_CtrlMsg(g_wifiSrvcProvObj,SYS_WIFIPROV_CONNECT,&provConnStatus,sizeof(bool));                
                    WDRV_PIC32MZW_InfoOpChanGet(g_wifiSrvcObj.wifiSrvcDrvHdl,&channel);
                    g_wifiSrvcConfig.staConfig.channel = (uint8_t )channel;
                }
                
                if(g_wifiSrvcConfig.saveConfig == true)
                {
                  SYS_WIFIPROV_CtrlMsg(g_wifiSrvcProvObj,SYS_WIFIPROV_SETCONFIG,&g_wifiSrvcConfig,sizeof(SYS_WIFI_CONFIG));
                }
</#if>
                wifiSrvcObj->wifiSrvcStatus = SYS_WIFI_STATUS_TCPIP_READY;
                break;
            }
</#if>

			
            case SYS_WIFI_STATUS_CONNECT_ERROR:
            {
                if (g_wifiSrvcAutoConnectRetry == MAX_AUTO_CONNECT_RETRY)
                {
                    SYS_WIFI_CallBackFun(SYS_WIFI_AUTO_CONNECT_FAIL, NULL, g_wifiSrvcCookie); 
                    wifiSrvcObj->wifiSrvcStatus = SYS_WIFI_STATUS_CONFIG_ERROR;
                }
                break;
            }

</#if>


<#if SYS_WIFI_AP_ENABLE == true>
<#if (tcpipDhcps.TCPIP_STACK_USE_DHCP_SERVER)?has_content && (tcpipDhcps.TCPIP_STACK_USE_DHCP_SERVER) == true>
            case SYS_WIFI_STATUS_WAIT_FOR_AP_IP:
            {
                apIpAddr.Val = TCPIP_STACK_NetAddress(netHdl);
                if (apLastIp.Val != apIpAddr.Val)
                {
                    if (OSAL_RESULT_TRUE == OSAL_SEM_Pend(&g_wifiSrvcSemaphore, OSAL_WAIT_FOREVER)) 
                    {
                        apLastIp.Val = apIpAddr.Val;
                        SYS_CONSOLE_MESSAGE(TCPIP_STACK_NetNameGet(netHdl));
                        SYS_CONSOLE_MESSAGE(" AP Mode IP Address: ");
                        SYS_CONSOLE_PRINT("%d.%d.%d.%d \r\n", apIpAddr.v[0], apIpAddr.v[1], apIpAddr.v[2], apIpAddr.v[3]);
                        wifiSrvcObj->wifiSrvcStatus = SYS_WIFI_STATUS_TCPIP_READY;
                        OSAL_SEM_Post(&g_wifiSrvcSemaphore);
<#if SYS_WIFI_PROVISION_ENABLE == true>

                        /* In AP mode, Update AP mode start event to
                            Wi-Fi Provisioning service.Wi-Fi Provisioning
                            service has to open TCP server */
                        bool provConnStatus = true;
                        SYS_WIFIPROV_CtrlMsg(g_wifiSrvcProvObj, SYS_WIFIPROV_CONNECT, &provConnStatus, sizeof (bool));
</#if>
                    }
                }
                break;
            }
            case SYS_WIFI_STATUS_WAIT_FOR_STA_IP:
            {
                uint8_t staConnIdx = SYS_WIFI_OBJ_INVALID;
                if (OSAL_RESULT_TRUE == OSAL_SEM_Pend(&g_wifiSrvcSemaphore, 
                                        OSAL_WAIT_FOREVER))
                {
                    staConnIdx = SYS_WIFI_StaConnIdx();
                    OSAL_SEM_Post(&g_wifiSrvcSemaphore);
                }    
                if(SYS_WIFI_OBJ_INVALID != staConnIdx)
                {
                    /* updates the application with received STA IP address*/
                    SYS_WIFI_CallBackFun(SYS_WIFI_CONNECT, 
                    &g_wifiSrvcStaConnInfo[staConnIdx].wifiSrvcStaAppInfo, 
                    g_wifiSrvcCookie);
                }
                else
                {
                    SYS_WIFI_SetTaskstatus(SYS_WIFI_STATUS_TCPIP_READY);
                }                   
                break;
            }
</#if>
</#if>
            case SYS_WIFI_STATUS_TCPIP_READY:
            {
<#if SYS_WIFI_STA_ENABLE == true>			
<#if ((tcpipIPv6.TCPIP_STACK_USE_IPV6)?has_content && (tcpipIPv6.TCPIP_STACK_USE_IPV6) == true) >
               if (SYS_WIFI_STA == SYS_WIFI_GetMode())
                {
                    static  bool dhcpv6Enabled = false;
                    if(dhcpv6Enabled == false)
                    {
                        TCPIP_DHCPV6_CLIENT_RES res = TCPIP_DHCPV6_Enable(netHdl);
                        if ((TCPIP_DHCPV6_CLIENT_RES_OK == res))
                        {
                            dhcpv6Enabled = true;
                        }
                    }                
                }
</#if>
</#if>
                break;
            }

            case SYS_WIFI_STATUS_TCPIP_ERROR:
            {
                SYS_STATUS tcpIpStat;
                tcpIpStat = TCPIP_STACK_Status(sysObj.tcpip);
            
                if (tcpIpStat < 2) 
                {
                    wifiSrvcObj->wifiSrvcStatus = SYS_WIFI_STATUS_TCPIP_ERROR;
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
                SYS_APPDEBUG_ERR_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG, "TCP/IP Stack is not in ready state\r\n");
</#if>
                } 
                else 
                {
                    wifiSrvcObj->wifiSrvcStatus = SYS_WIFI_STATUS_TCPIP_WAIT_FOR_TCPIP_INIT;
                }
                break;
            }

            default:
            {
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
            //SYS_APPDEBUG_ERR_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG, " Wi-Fi service is not in invalid state\r\n");
</#if>
                break;
            }
        }
<#if SYS_WIFI_PROVISION_ENABLE == true>
        SYS_WIFIPROV_Tasks (g_wifiSrvcProvObj);
</#if>
        ret = wifiSrvcObj->wifiSrvcStatus;
    }
    return ret;
}

<#if SYS_WIFI_PROVISION_ENABLE == true>
static void SYS_WIFI_WIFIPROVCallBack
(
    uint32_t event, 
    void * data, 
    void *cookie
) 
{
    char *wifiSrvcCookie = (void *) cookie;
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
    SYS_APPDEBUG_FN_ENTER_PRINT(g_wifiSrvcAppDebugHdl, WIFI_PROVISIONING);
</#if>       
    /* Validate client with verifying the cookie*/
    if (g_wifiSrvcProvCookieVal == *wifiSrvcCookie) 
    {
        switch (event) 
        {

            /* Wi-Fi Provisioning service has updated Wi-Fi configuration 
               with SETCONFIG event */
            case SYS_WIFIPROV_SETCONFIG:
            {
                SYS_WIFIPROV_CONFIG *wifiConfig = (SYS_WIFIPROV_CONFIG*) data;
                if ( (wifiConfig) && (false == g_wifiSrvcInit)) 
                {

                    /* Set g_wifiSrvcInit true, Wi-Fi Service can be started now 
                       after receiving configuration from Wi-Fi Provisioning 
                       service */
                    g_wifiSrvcInit = true;
                    memcpy(&g_wifiSrvcConfig, wifiConfig, sizeof(SYS_WIFIPROV_CONFIG));
                }
                else 
                {
<#if (SYS_WIFI_STA_ENABLE == true) && (SYS_WIFI_AP_ENABLE == true)>	
                    if(memcmp(&g_wifiSrvcConfig,wifiConfig,sizeof(SYS_WIFIPROV_CONFIG)))
                    {
                        if ((SYS_WIFIPROV_STA == (SYS_WIFIPROV_MODE) SYS_WIFI_GetMode()) && (SYS_WIFIPROV_STA == wifiConfig->mode)) 
                        {

                            /* Copy received configuration into Wi-Fi service structure */
                            memcpy(&g_wifiSrvcConfig, wifiConfig, sizeof (SYS_WIFIPROV_CONFIG));

                            /* In STA mode, check PIC32MZW1 connection status to HOMEAP */
                            if (g_wifiSrvcDrvAssocHdl == WDRV_PIC32MZW_ASSOC_HANDLE_INVALID) 
                            {

                               /* When Auto connected is enable by user and 
                                  Auto connect retry has not reach to maximum limit 
                                  then make connection requested */
                                if ((true == SYS_WIFI_GetAutoConnect()) && (g_wifiSrvcAutoConnectRetry < MAX_AUTO_CONNECT_RETRY)) 
                                {
                                    /* Make a connection request */
                                    SYS_WIFI_SetTaskstatus(SYS_WIFI_STATUS_CONNECT_REQ);
                                    g_wifiSrvcAutoConnectRetry = 0;
                                }
                            } 
                            else 
                            {
                                /* In STA mode, PIC32MZW1 is already connected to HOMEAP,
                                   so disconnect before applying new received configuration */
                                SYS_WIFI_DisConnect();
                            }
                        } 
                        else 
                        {
                            SYS_CONSOLE_PRINT("## Switch WiFi Mode From %s To %s ##\r\n", \
                                           ((SYS_WIFIPROV_STA == (SYS_WIFIPROV_MODE) SYS_WIFI_GetMode()) ? "STA" : "AP"),\
                                           ((SYS_WIFIPROV_STA == wifiConfig->mode)?"STA":"AP"));
                            /* Copy received configuration into Wi-Fi service structure */
			    if (SYS_WIFIPROV_STA == (SYS_WIFIPROV_MODE) SYS_WIFI_GetMode())
                            {
                                SYS_WIFI_DisConnect();
                            }
                            if((SYS_WIFIPROV_STA == wifiConfig->mode) && (SYS_WIFIPROV_AP == (SYS_WIFIPROV_MODE) SYS_WIFI_GetMode()))
                            {
                                SYS_RESET_SoftwareReset();
                            } 
                            else
                            {
                                memcpy(&g_wifiSrvcConfig, wifiConfig, sizeof (SYS_WIFIPROV_CONFIG));
                                WDRV_PIC32MZW_Close(g_wifiSrvcObj.wifiSrvcDrvHdl);
                                SYS_WIFI_SetTaskstatus(SYS_WIFI_STATUS_INIT);
                            }
                        }
                        if (data) 
                        {

                            /* Update application(client), on receiving new 
                              Provisioning configuration */
                            SYS_WIFI_CallBackFun(SYS_WIFI_PROVCONFIG, data, g_wifiSrvcCookie);
                        }
                    }
                }
<#elseif SYS_WIFI_STA_ENABLE == true>
                    if(memcmp(&g_wifiSrvcConfig,wifiConfig,sizeof(SYS_WIFIPROV_CONFIG)))
                    {
                        if ((SYS_WIFIPROV_STA == (SYS_WIFIPROV_MODE)SYS_WIFI_GetMode()) && (SYS_WIFIPROV_STA == wifiConfig->mode))
                        {

                            /* Copy received configuration into Wi-Fi service structure */
                            memcpy(&g_wifiSrvcConfig,wifiConfig,sizeof(SYS_WIFIPROV_CONFIG));

                            /* In STA mode, PIC32MZW1 is not connected to HOMEAP */
                            if(g_wifiSrvcDrvAssocHdl == WDRV_PIC32MZW_ASSOC_HANDLE_INVALID)
                            {

                                /* Auto connected is enable by user and Auto connect 
                                   retry has not reach to maximum limit */
                                if((true == SYS_WIFI_GetAutoConnect()) && (g_wifiSrvcAutoConnectRetry < MAX_AUTO_CONNECT_RETRY))
                                {
                                    SYS_WIFI_SetTaskstatus(SYS_WIFI_STATUS_CONNECT_REQ);
                                    g_wifiSrvcAutoConnectRetry = 0;
                                }
                            } 
                            else 
                            {

                                /* In STA mode, PIC32MZW1 is already connected to HOMEAP,
                                   so disconnect before applying new received configuration */
                                SYS_WIFI_DisConnect();
                            }
                        }
                        if (data)
                        {

                            /* Update application(client), on receiving new Provisioning configuration */
                            SYS_WIFI_CallBackFun(SYS_WIFI_PROVCONFIG,data,g_wifiSrvcCookie);
                        }
                    }
                }
<#elseif SYS_WIFI_AP_ENABLE == true>
                        SYS_CONSOLE_MESSAGE("######################################Rebooting the Device ###############################\r\n"); 
                        SYS_RESET_SoftwareReset();
            }
                if (data) 
                {

                    /* Update application(client), on receiving new Provisioning configuration */
                    SYS_WIFI_CallBackFun(SYS_WIFI_PROVCONFIG,data,g_wifiSrvcCookie);
                }
</#if>
                break;
            }

            case SYS_WIFIPROV_GETCONFIG:
            {
                if (data) 
                {
                    SYS_WIFI_CallBackFun(SYS_WIFI_GETWIFICONFIG, data, g_wifiSrvcCookie);
                }
                break;
            }

            default:
            {
                break;
            }
        }
    }
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
    SYS_APPDEBUG_FN_EXIT_PRINT(g_wifiSrvcAppDebugHdl, WIFI_PROVISIONING);
</#if>
}
</#if>

// *****************************************************************************
// *****************************************************************************
// Section:  SYS WIFI Initialize Interface 
// *****************************************************************************
// *****************************************************************************
SYS_MODULE_OBJ SYS_WIFI_Initialize
(
    SYS_WIFI_CONFIG *config, 
    SYS_WIFI_CALLBACK callback, 
    void *cookie
) 
{

<#if SYS_WIFI_APPDEBUG_ENABLE  == true>

    /* Set user log level and log flow, user can modified this 
       configuration with command */
    g_wifiSrvcAppDbgCfg.logLevel = (APP_LOG_ERROR_LVL & SYS_WIFI_APPDEBUG_ERR_LEVEL_ENABLE) | (APP_LOG_DBG_LVL & SYS_WIFI_APPDEBUG_DBG_LEVEL_ENABLE) | 
                                (APP_LOG_INFO_LVL & SYS_WIFI_APPDEBUG_INFO_LEVEL_ENABLE) | (APP_LOG_FN_EE_LVL & SYS_WIFI_APPDEBUG_FUNC_LEVEL_ENABLE);
    g_wifiSrvcAppDbgCfg.logFlow =  (WIFI_CFG & SYS_WIFI_APPDEBUG_CFG_FLOW) | 
                                (WIFI_CONNECT & SYS_WIFI_APPDEBUG_CONNECT_FLOW)| 
                                (WIFI_PROVISIONING & SYS_WIFI_APPDEBUG_PROVISIONING_FLOW) |
                                (WIFI_PROVISIONINGCMD & SYS_WIFI_APPDEBUG_PROVISIONINGCMD_FLOW) | 
                                (WIFI_PROVISIONINGSOCKET & SYS_WIFI_APPDEBUG_PROVISIONINGSOCK_FLOW);
    g_wifiSrvcAppDbgCfg.prefixString = SYS_WIFI_DEBUG_PRESTR;
    g_wifiSrvcAppDebugHdl = SYS_APPDEBUG_Open(&g_wifiSrvcAppDbgCfg);
    SYS_APPDEBUG_FN_ENTER_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG);
</#if>
    if (SYS_WIFI_STATUS_NONE == SYS_WIFI_GetTaskstatus()) 
    {
        if (OSAL_SEM_Create(&g_wifiSrvcSemaphore, OSAL_SEM_TYPE_BINARY, 1, 1) != OSAL_RESULT_TRUE) 
        {
            SYS_CONSOLE_MESSAGE("Failed to Initialize Wi-Fi Service as Semaphore NOT created\r\n");
            return SYS_MODULE_OBJ_INVALID;
        }
        memset(g_wifiSrvcCallBack,0,sizeof(g_wifiSrvcCallBack));
        if (callback != NULL) 
        {
            SYS_WIFI_REGCB(callback);
        }
        WDRV_PIC32MZW_BSSCtxSetDefaults(&g_wifiSrvcObj.wifiSrvcBssCtx);
        WDRV_PIC32MZW_AuthCtxSetDefaults(&g_wifiSrvcObj.wifiSrvcAuthCtx);

        /* Set Wi-Fi service state to init */
        SYS_WIFI_SetTaskstatus(SYS_WIFI_STATUS_INIT);
        SYS_WIFI_SetCookie(cookie);
<#if SYS_WIFI_AP_ENABLE == true>
        SYS_WIFI_InitStaConnInfo();
</#if>
<#if SYS_WIFI_SCAN_ENABLE == true>
        SYS_WIFI_InitWifiScanInfoDefault();
</#if>
<#if SYS_WIFI_PROVISION_ENABLE == false>

        /* Wi-Fi provisioning service is disabled */
        SYS_WIFI_InitConfig(config);
        g_wifiSrvcInit = true;
<#else>

        /* User has enabled Wi-Fi provisioning service using MHC */
        g_wifiSrvcProvObj= SYS_WIFIPROV_Initialize ((SYS_WIFIPROV_CONFIG *)config,SYS_WIFI_WIFIPROVCallBack,&g_wifiSrvcProvCookieVal);
</#if>
        return (SYS_MODULE_OBJ) &g_wifiSrvcObj;
    }
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
    SYS_APPDEBUG_FN_EXIT_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG);
</#if>
    return SYS_MODULE_OBJ_INVALID;
}

// *****************************************************************************
// *****************************************************************************
// Section:  SYS WIFI Deinitialize Interface 
// *****************************************************************************
// *****************************************************************************
SYS_WIFI_RESULT SYS_WIFI_Deinitialize
(
    SYS_MODULE_OBJ object
) 
{
    uint32_t ret = SYS_WIFI_OBJ_INVALID;
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
    SYS_APPDEBUG_FN_ENTER_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG);
</#if>
    
    if (&g_wifiSrvcObj == (SYS_WIFI_OBJ *) object) 
    {
<#if (SYS_WIFI_STA_ENABLE == true) && (SYS_WIFI_AP_ENABLE == true)>

        /* STA Mode Configuration */
        if (SYS_WIFI_STA == SYS_WIFI_GetMode()) 
        {
            /* Before Wi-Fi De-initialize service,
               Disconnected PIC32MZW1 STA from HOMEAP */
            SYS_WIFI_DisConnect();
            TCPIP_DHCP_HandlerDeRegister(g_wifiSrvcDhcpHdl);
        } 
        else if (SYS_WIFI_AP == SYS_WIFI_GetMode()) 
        {
            if (WDRV_PIC32MZW_STATUS_OK != WDRV_PIC32MZW_APStop(g_wifiSrvcObj.wifiSrvcDrvHdl)) 
            {
                SYS_CONSOLE_MESSAGE(" AP mode Stop Failed \n");
            }
        }
<#elseif SYS_WIFI_STA_ENABLE == true>
        SYS_WIFI_DisConnect();
        TCPIP_DHCP_HandlerDeRegister(g_wifiSrvcDhcpHdl);
<#elseif SYS_WIFI_AP_ENABLE == true>
        if (WDRV_PIC32MZW_STATUS_OK != WDRV_PIC32MZW_APStop(g_wifiSrvcObj.wifiSrvcDrvHdl)) 
        {
            SYS_CONSOLE_MESSAGE(" AP mode Stop Failed \n");
        }
</#if>
        WDRV_PIC32MZW_Close(g_wifiSrvcObj.wifiSrvcDrvHdl);
        g_wifiSrvcInit = false;
        memset(&g_wifiSrvcObj,0,sizeof(SYS_WIFI_OBJ));
        memset(g_wifiSrvcCallBack,0,sizeof(g_wifiSrvcCallBack));
        SYS_WIFI_SetTaskstatus(SYS_WIFI_STATUS_NONE);
<#if SYS_WIFI_PROVISION_ENABLE == true>		
        SYS_WIFIPROV_Deinitialize(g_wifiSrvcProvObj);
</#if>
        if (OSAL_SEM_Delete(&g_wifiSrvcSemaphore) != OSAL_RESULT_TRUE) 
        {
            SYS_CONSOLE_MESSAGE("Failed to Delete Wi-Fi Service Semaphore \r\n");
        }
        ret = SYS_WIFI_SUCCESS;
    }
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
    SYS_APPDEBUG_FN_EXIT_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG);
</#if>
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
//SYS_APPDEBUG_Close(g_wifiSrvcAppDebugHdl);
</#if>
    return ret;
}

// *****************************************************************************
// *****************************************************************************
// Section:  SYS WiFi Get Status Interface
// *****************************************************************************
// *****************************************************************************
uint8_t SYS_WIFI_GetStatus
(
    SYS_MODULE_OBJ object
) 
{
    uint8_t ret = SYS_WIFI_OBJ_INVALID;
    
    if (OSAL_RESULT_TRUE == OSAL_SEM_Pend(&g_wifiSrvcSemaphore, OSAL_WAIT_FOREVER)) 
    {
        if (&g_wifiSrvcObj == (SYS_WIFI_OBJ *) object) 
        {
            /* Provide current status of Wi-Fi service to client */
            ret = ((SYS_WIFI_OBJ *) object)->wifiSrvcStatus;
        }
        OSAL_SEM_Post(&g_wifiSrvcSemaphore);
    }
    return ret;
}

// *****************************************************************************
// *****************************************************************************
// Section:  SYS WiFi Tasks Interface
// *****************************************************************************
// *****************************************************************************
uint8_t SYS_WIFI_Tasks
(
    SYS_MODULE_OBJ object
) 
{
    uint8_t ret = SYS_WIFI_OBJ_INVALID;

    if (&g_wifiSrvcObj == (SYS_WIFI_OBJ *) object) 
    {
        ret = SYS_WIFI_ExecuteBlock(object);
    }
    return ret;
}

// *****************************************************************************
// *****************************************************************************
// Section:  SYS WiFi Control Message Interface
// *****************************************************************************
// *****************************************************************************
SYS_WIFI_RESULT SYS_WIFI_CtrlMsg
(
    SYS_MODULE_OBJ object, 
    uint32_t event, 
    void *buffer, 
    uint32_t length
) 
{
    uint8_t ret = SYS_WIFI_OBJ_INVALID;

    if (OSAL_RESULT_TRUE == OSAL_SEM_Pend(&g_wifiSrvcSemaphore, OSAL_WAIT_FOREVER)) 
    {
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
        SYS_APPDEBUG_FN_ENTER_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG);
</#if>    
        if (&g_wifiSrvcObj == (SYS_WIFI_OBJ *)object) 
        {
            switch (event) 
            {

                case SYS_WIFI_CONNECT:
                {
                    /* if service is already processing pending request from 
                       client then ignore new request */
                    if (SYS_WIFI_STATUS_CONNECT_REQ != g_wifiSrvcObj.wifiSrvcStatus) 
                    {
                        if ((buffer) && (length == sizeof (SYS_WIFI_CONFIG)))
                        {
                            SYS_WIFI_STATUS wifiStatus = ((SYS_WIFI_OBJ *)object)->wifiSrvcStatus;
                            if(wifiStatus >= SYS_WIFI_STATUS_CONNECT_REQ)
                            { 
                                wifiStatus = SYS_WIFI_STATUS_CONNECT_REQ; 
                            }
                            ret = SYS_WIFI_SetConfig((SYS_WIFI_CONFIG *) buffer, wifiStatus);
                        }
                    } 
                    else
                    {
                        /* Client is currently processing pending connection request */
                        ret = SYS_WIFI_CONNECT_FAILURE;
                    }
                    break;
                }

                case SYS_WIFI_REGCALLBACK:
                {
                    SYS_WIFI_CALLBACK g_wifiSrvcFunPtr = buffer;
                    if ((g_wifiSrvcFunPtr) && (length == sizeof(g_wifiSrvcFunPtr))) 
                    {
                        /* Register the client callback function */
                        ret = SYS_WIFI_REGCB(g_wifiSrvcFunPtr);
                    }
                    break;
                }

                case SYS_WIFI_DISCONNECT:
                {
<#if (SYS_WIFI_STA_ENABLE == true) && (SYS_WIFI_AP_ENABLE == true)>
                    if(g_wifiSrvcConfig.mode == SYS_WIFI_AP)
                    {
                        uint8_t *macAddr = (uint8_t *)buffer;                       
                        if(macAddr)
                        {
                            SYS_WIFI_APDisconnectSTA(macAddr);
                        }
                    }
                    else
                    {
                        g_wifiSrvcConfig.staConfig.autoConnect = 0;
                        /* Client has made disconnect request */
                        ret = SYS_WIFI_DisConnect();
                    }
<#elseif SYS_WIFI_STA_ENABLE == true>
                    /* Client has made disconnect request */
                    g_wifiSrvcConfig.staConfig.autoConnect = 0;
                    ret = SYS_WIFI_DisConnect();
<#elseif SYS_WIFI_AP_ENABLE == true>
                    uint8_t *macAddr = (uint8_t *)buffer;
                    SYS_WIFI_APDisconnectSTA(macAddr);
</#if>
                    break;
                }

                case SYS_WIFI_GETWIFICONFIG:
                {
                    if (true == g_wifiSrvcInit) 
                    {
                        if ((buffer) && (length == sizeof (SYS_WIFI_CONFIG))) 
                        {

                            /* Client has request Wi-Fi service configuration,
                               Copy Wi-Fi configuration into client structure */
                            memcpy(buffer, &g_wifiSrvcConfig, sizeof (g_wifiSrvcConfig));
                            ret = SYS_WIFI_SUCCESS;
                        }
                    } 
                    else
                    {

                        /* Wi-Fi service is not started */
                        ret = SYS_WIFI_SERVICE_UNINITIALIZE;
                    }
                    break;
                }

<#if SYS_WIFI_SCAN_ENABLE == true>
                case SYS_WIFI_GETSCANCONFIG:
                {
                    if ((buffer) && (length == sizeof (SYS_WIFI_SCAN_CONFIG))) 
                    {
                        /* Client has request Wi-Fi Scan configuration,
                        Copy Scan configuration into client structure */
                        memcpy(buffer, &g_wifiSrvcScanConfig, sizeof (g_wifiSrvcScanConfig));
                        ret = SYS_WIFI_SUCCESS;
                    }
                    else
                    {
                        ret = SYS_WIFI_FAILURE;
                    }
                    break;
                }

                case SYS_WIFI_SCANREQ:
                {
                    if ((buffer) && (length == sizeof (SYS_WIFI_SCAN_CONFIG))) 
                    {
                       /* Client has updated Wi-Fi Scan configuration,
                        Copy client structure into Scan configuration */
                        memcpy(&g_wifiSrvcScanConfig, buffer, sizeof (g_wifiSrvcScanConfig));
                    }
                    ret = SYS_WIFI_SetScan();
                    break;
                }
</#if>

                case SYS_WIFI_GETDRVHANDLE:
                {
                    if ((buffer) && (length == sizeof (DRV_HANDLE))) 
                    {
                        /* Client has requested Wi-Fi driver handle,
                        Copy driver handle into client structure */
                        *(DRV_HANDLE *)buffer = g_wifiSrvcObj.wifiSrvcDrvHdl;
                        ret = SYS_WIFI_SUCCESS;
                    }
                    else
                    {
                        ret = SYS_WIFI_FAILURE;
                    }
                    break;
                }
<#if SYS_WIFI_STA_ENABLE == true>
                case SYS_WIFI_GETDRVASSOCHANDLE:
                {
                    if ((buffer) && (length == sizeof (WDRV_PIC32MZW_ASSOC_HANDLE))) 
                    {
                        /* Client has requested Assoc handle,
                        Copy Assoc handle into client structure */
                        *(WDRV_PIC32MZW_ASSOC_HANDLE *)buffer = g_wifiSrvcDrvAssocHdl;
                        ret = SYS_WIFI_SUCCESS;
                    }
                    else
                    {
                        ret = SYS_WIFI_FAILURE;
                    }
                    break;
                }
</#if>
            }
        }
<#if SYS_WIFI_APPDEBUG_ENABLE  == true>
        SYS_APPDEBUG_FN_EXIT_PRINT(g_wifiSrvcAppDebugHdl, WIFI_CFG);
</#if>
        OSAL_SEM_Post(&g_wifiSrvcSemaphore);
    }
    return ret;
}
/* *****************************************************************************
 End of File
 */
