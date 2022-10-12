# SYS\_MQTT\_RESULT Enum

**Parent topic:**[MQTT System Service Interface](GUID-B5FCF623-E7FF-4626-AA04-20BCC3916E44.md)

## C

```c

typedef enum
{
// Success
SYS_MQTT_SUCCESS = 0,

// Failure
SYS_MQTT_FAILURE = -1,

// Sys NET Service Down
SYS_MQTT_SERVICE_DOWN = -2,

// Sys NET Available Put Buffer not enough for xmitting the Data
SYS_MQTT_SEM_OPERATION_FAILURE = -5,

// Sys NET Invalid Handle
SYS_MQTT_INVALID_HANDLE = -6,
} SYS_MQTT_RESULT;

```

## Summary

Identifies the return values for the Sys Mqtt APIs.

## Remarks

None.

