# SYS\_MQTT\_STATUS Enum

**Parent topic:**[MQTT System Service Interface](GUID-B5FCF623-E7FF-4626-AA04-20BCC3916E44.md)

## C

```c
typedef enum
{
// Idle
SYS_MQTT_STATUS_IDLE = 0,

// Lower Layer is DOWN
SYS_MQTT_STATUS_LOWER_LAYER_DOWN,

// Net Client connecting to Net Server
SYS_MQTT_STATUS_SOCK_CLIENT_CONNECTING,

// Net Instance connected to the peer
SYS_MQTT_STATUS_SOCK_CONNECTED,

// Net Instance Failed to open socket
SYS_MQTT_STATUS_SOCK_OPEN_FAILED,

// Lower Layer is DOWN
SYS_MQTT_STATUS_MQTT_CONNECTED,

// Net Instance in disconnected state
SYS_MQTT_STATUS_MQTT_DISCONNECTING,

// Net Instance in disconnected state
SYS_MQTT_STATUS_MQTT_DISCONNECTED,

// Wait for Connect Ack from Broker
SYS_MQTT_STATUS_WAIT_FOR_MQTT_CONACK,

// Wait for Subscribe Ack from Broker
SYS_MQTT_STATUS_WAIT_FOR_MQTT_SUBACK,

// Wait for Publish Ack from Broker
SYS_MQTT_STATUS_WAIT_FOR_MQTT_PUBACK,

// Wait for Unsibscribe Ack from Broker
SYS_MQTT_STATUS_WAIT_FOR_MQTT_UNSUBACK,
} SYS_MQTT_STATUS;
```

## Summary

Identifies the current status of the Sys Mqtt Instance.

## Remarks

None.

