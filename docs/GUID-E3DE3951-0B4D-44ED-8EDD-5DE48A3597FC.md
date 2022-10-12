# SYS\_OTA\_DATA Struct

**Parent topic:**[OTA System Service Interface](GUID-F8A21576-2DFD-406F-9736-CEFDE7AD5207.md)

## C

```c
typedef struct {
    /* service current state */
    SYS_OTA_STATES state;
    
    /*to indicate ,update check with server is failed*/
    bool update_check_failed;
    
    /*to mage states required for parsing JSON content */
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
    
    /*to check if user requested for patch functionality*/
    bool patch_request;
    
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

## Summary

system service data

## Description

This structure holds the system service's data.

## Remarks

