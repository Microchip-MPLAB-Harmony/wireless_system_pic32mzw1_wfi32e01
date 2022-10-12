# SYS\_WIFI\_AP\_CONFIG Struct

**Parent topic:**[Wi-Fi System Service Interface](GUID-B9C73D51-5039-4573-A452-176603C18703.md)

## C

```c
typedef struct
{
    /* Wi-Fi access point mode SSID */
    uint8_t ssid[32];
    
    /* Wi-Fi access point mode passphrase */
    uint8_t psk[64];
    
    /* Wi-Fi access point mode authentication type */
    SYS_WIFI_AUTH authType;
    
    /* Wi-Fi access point mode channel number.
    values of channel:
    1 to 13 - - operating channel of access point */
    uint8_t channel;
    
    /* Wi-Fi access point mode SSID visibility
    value of ssidVisibility:
    0 - Hidden SSID
    1 - broadcast the SSID */
    bool ssidVisibility;
    
} SYS_WIFI_AP_CONFIG;

```

## Summary

Configuration of access point mode parameters.

## Description

Configuration of access point mode parameters.

## Remarks

None.

