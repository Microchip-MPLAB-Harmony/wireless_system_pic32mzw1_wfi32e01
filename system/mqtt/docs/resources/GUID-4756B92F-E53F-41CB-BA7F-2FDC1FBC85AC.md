# SYS\_MQTT\_BrokerConfig Struct

**Parent topic:**[MQTT System Service Interface](GUID-B5FCF623-E7FF-4626-AA04-20BCC3916E44.md)

## C

```c
typedef struct
{
    //to know which of the Configurations are valid
    SYS_MQTT_Vendor_Type eVendorType;
    
    // MQTT Broker/ Server Name
    char brokerName[SYS_MQTT_MAX_BROKER_NAME_LEN];
    
    // MQTT Server Port
    uint16_t serverPort;
    
    // Keep Alive Interval for the Mqtt Session
    uint16_t keepAliveInterval;
    
    // MQTT Client ID
    char clientId[SYS_MQTT_CLIENT_ID_MAX_LEN];
    
    // MQTT Username
    char username[SYS_MQTT_USER_NAME_MAX_LEN];
    
    // MQTT password
    char password[SYS_MQTT_PASSWORD_MAX_LEN];
    
    // TLS is Enabled
    bool tlsEnabled;
    
    // AutoConnect is Enabled
    bool autoConnect;
    
    // Clean Session is Enabled
    bool cleanSession;
} SYS_MQTT_BrokerConfig;

```

## Summary

Used for passing on the configuration related to the MQTT Broker

## Remarks

None.

