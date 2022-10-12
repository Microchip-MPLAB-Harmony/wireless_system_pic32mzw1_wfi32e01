# SYS\_MQTT\_Disconnect Function

**Parent topic:**[MQTT System Service Interface](GUID-B5FCF623-E7FF-4626-AA04-20BCC3916E44.md)

## C

```c
void SYS_MQTT_Disconnect(SYS_MODULE_OBJ obj)
```

## Summary

Disconnects from the MQTT Server

## Description

This function is used for disconnecting from the MQTT Server.

## Precondition

SYS\_MQTT\_Connect should have been called.

## Parameters

obj - SYS\_MQTT object handle, returned from SYS\_MQTT\_Connect

## Returns

None

## Example

```c
// Handle "objSysMqtt" value must have been returned from SYS_MQTT_Connect.
SYS_MQTT_Disconnect(objSysMqtt);
```

## Remarks

None.

