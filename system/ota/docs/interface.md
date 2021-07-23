---
grand_parent: Harmony 3 PIC32MZW1 wireless system services package
parent: OTA Service
title: OTA System Service Interface
has_toc: true
nav_order: 2
---

# OTA System Service Interface
{: .no_toc }

### Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Data Types and Constants Summary

| Name | Description |
|-|-|
| [SYS_OTA_CTRLMSG](#SYS_OTA_CTRLMSG) | Identifies the control message for which the client has called the SYS_OTA_CtrlMsg() |
| [SYS_OTA_STATUS](#SYS_OTA_STATUS) | Provide status of OTA system |
| [SYS_OTA_RESULT](#SYS_OTA_RESULT) | Result of a OTA system service client interface operation |
| [SYS_OTA_Config](#SYS_OTA_Config) | Used for passing on the configuration related to the OTA service |
| [SYS_OTA_DATA](#SYS_OTA_DATA) | This structure holds the system service's data |


## Initialization functions Summary

| Name | Description |
|-|-|
| [SYS_OTA_Initialize](#SYS_OTA_Initialize) | Initialization of data structures of the OTA service |


## Setup functions Summary

| Name | Description |
|-|-|
| [SYS_OTA_Task](#SYS_OTA_Task) | Executes the SYS OTA service state machine  |
| [SYS_OTA_CtrlMsg](#SYS_OTA_CtrlMsg) | Returns success/ failure for the control operation asked by the user. |

## Registering call back function summary
| Name | Description |
|-|-|
| [ota_app_reg_cb](#ota_app_reg_cb) | Registering OTA service callback function |


## Data Types and Constants

### SYS_OTA_CTRLMSG


**Summary**

Identifies the control message for which the client has called the SYS_OTA_CtrlMsg().  

**Remarks**

None. 

```c
typedef enum {
        /* Control message type for registering a ota system service client callback */
        SYS_OTA_REGCALLBACK = 0,
                
        /* Control message type for checking OTA update availability */        
        SYS_OTA_UPDATECHCK,
                
        /* Control message type for triggering OTA update */      
        SYS_OTA_INITIATE_OTA,
                
        /* Control message type for triggering system reset */      
        SYS_OTA_TRIGGER_SYSTEM_RESET,
                
        /* Control message type for triggering factory reset */     
        SYS_OTA_TRIGGER_FACTORY_RESET,
                
        /* Control message type for triggering Roll back */
        SYS_OTA_TRIGGER_ROLLBACK
    } SYS_OTA_CTRLMSG;
```

### SYS_OTA_STATUS


**Summary**

provides status of the OTA system.  

**Remarks**

None. 

```c
typedef enum {
        /* To provide status of OTA system */
        
        /*update available in server*/
        SYS_OTA_UPDATE_AVAILABLE = 0,
                
        /*update not available*/        
        SYS_OTA_UPDATE_NOTAVAILABLE,
                
        /*OTA trigger failed*/ 
        SYS_OTA_TRIGGER_OTA_FAILED,
                
        /*Factory reset success*/
        SYS_OTA_FACTORY_RESET_SUCCESS,
                
        /*factory reset failed*/ 
        SYS_OTA_FACTORY_RESET_FAILED,
                
        /*rollback success*/ 
        SYS_OTA_ROLLBACK_SUCCESS,
                
        /*rollback failed*/ 
        SYS_OTA_ROLLBACK_FAILED,
                
        /*download started*/ 
        SYS_OTA_DOWNLOAD_START,
                
        /*download success*/
        SYS_OTA_DOWNLOAD_SUCCESS,
                
        /*download failed*/ 
        SYS_OTA_DOWNLOAD_FAILED,
                
        /*image digest verify started*/
        SYS_OTA_IMAGE_DIGEST_VERIFY_START,
                
        /*image digest verify success*/
        SYS_OTA_IMAGE_DIGEST_VERIFY_SUCCESS,
                
        /*image digest verify failed*/
        SYS_OTA_IMAGE_DIGEST_VERIFY_FAILED,

        /*Database entry successful*/        
        SYS_OTA_DB_ENTRY_SUCCESS, 
                
        /*erasing image failed*/        
        SYS_OTA_IMAGE_ERASE_FAILED,
                
        /*erasing image success*/
        SYS_OTA_IMAGE_ERASED,
                
        /*image database full*/
        SYS_OTA_IMAGE_DATABASE_FULL,
                
        /*not a defined(as mentioned above) status*/
        SYS_OTA_NONE
    } SYS_OTA_STATUS;
```

### SYS_OTA_RESULT


**Summary**

Result of a OTA system service client interface operation.  

**Remarks**

None. 

```c
typedef enum {
        /* Operation completed with success */
        SYS_OTA_SUCCESS = 0,

        /* Operation Failed.*/
        SYS_OTA_FAILURE,

    } SYS_OTA_RESULT;
```

### SYS_OTA_Config


**Summary**

Used for passing on the configuration related to the OTA service.  

**Remarks**

None. 

```c
typedef struct {
        /*Auto reset is enabled or not*/
        uint8_t autoreset;

        /*OTA periodic check is enabled or not*/
        bool ota_periodic_check;

        /*OTA auto update is enabled or not*/
        bool ota_auto_update;

        /*periodic check time interval*/
        uint32_t periodic_check_interval;

        /*Application version*/
        uint8_t app_version;

        /*ota server url*/
        char *json_url;

    } SYS_OTA_Config;
```


### SYS_OTA_DATA


**Summary**

This structure holds the system service's data.  

**Remarks**

None. 

```c
typedef struct {
        /* service current state */
        SYS_OTA_STATES state;

        /*to mage states required for parsing JSON content  */
        SYS_OTA_STATES update_check_state;

        /*to keep track of user configure auto update check interval*/
        uint32_t time_interval;

        /*keep track if device connected to network*/
        bool dev_cnctd_to_nw;

        /*to keep track if OTA process is in progress*/
        bool otaFwInProgress;

        /*to keep track if OTA update check with server is in progress*/
        bool otaUpdateCheckInProgress;

        /*to keep track if erase image is triggered by user and in progress*/
        bool otaEraseInProgress;

        /*to keep track if image download success*/
        bool download_success;

        /*to check if user requested for erase functionality*/
        bool erase_request;

        /*check if json contents are proper and required fields are present */
        bool json_content_parse_result;

        /*to track timer callback*/
        volatile bool ota_timer_trigger;

        /*buffer used for JSON content parsing*/
        char json_buf[SYS_OTA_JSON_FILE_MAXSIZE];

        /*control interface result*/
        SYS_OTA_STATUS ota_srvc_status;

    } SYS_OTA_DATA;
```
## Initialization functions


### SYS_OTA_Initialize

**Function**

```c
void SYS_OTA_Initialize(void)
```

**Summary**

Initializes the System OTA module.  

**Description**

This function is used for initializing the data structures of the OTA service.
OTA service supports only one instance of client.  

**Returns**

NONE

**Example**

none

**Remarks**

This routine can only be called once during system initialization. If the OTA system service is enabled using MHC, then auto generated code will take care of system OTA initialization.

## Setup functions

### SYS_OTA_Tasks

**Function**

```c
void SYS_OTA_Tasks(void)
```

**Summary**

Maintains the OTA System tasks and functionalities.  

**Description**

This function is used to run the various tasks and functionalities of OTA system service.

**Precondition**

The `SYS_OTA_Initialize()` function should have been called before calling this function.  

**Parameters**

None 

**Returns**

None  

**Example**

```c

while(1)
{
...
SYS_OTA_Task();
...
}
```


### SYS_OTA_CtrlMsg

**Function**

```c
SYS_OTA_RESULT SYS_OTA_CtrlMsg(uint32_t event, void *buffer, uint32_t length)
```

**Summary**

Returns success/ failure for the update check/OTA trigger/system reset operations asked by client.  

**Description**

This function is used to make control message request (update check,initiate OTA,system reset,factory reset,register callback) to OTA system service.  

**Precondition**

The `SYS_OTA_Initialize()` function should have been called before calling this function..  

**Parameters**

event    - A event value, event can be any of SYS_OTA_CTRLMSG types

buffer   - Control message data input.

length   - size of buffer data  

**Returns**

`SYS_OTA_SUCCESS` - Indicates that the Request was catered to successfully 

`SYS_OTA_FAILURE` - Indicates that the Request failed  

**Example**

```c

bool ota_app_reg_cb(void) {
    if (SYS_OTA_SUCCESS == SYS_OTA_CtrlMsg(SYS_OTA_REGCALLBACK, sys_ota_cb, sizeof (uint8_t *))) {
        return true;
    } else {
        return false;
    }
}
```


## Registering call back function

### ota_app_reg_cb

**Function**

```c
bool ota_app_reg_cb(void)
```

**Summary**

Registering OTA service callback function. 

**Description**

This function can be used for easy registering of user callback function. It can be called from application layer.
The definition of the callback function is already present in `app_ota.c` file.  

**Returns**

`true` - if callback registered successfully
`false` - if callback registration failed

**Example**

none

**Remarks**

This function definition is present in "app_ota.c" file. Initialization must be done before calling this function. 



