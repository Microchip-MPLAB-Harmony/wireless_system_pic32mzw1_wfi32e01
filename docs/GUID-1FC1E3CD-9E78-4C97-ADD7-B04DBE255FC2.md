# SYS\_MQTT\_Subscribe Function

**Parent topic:**[MQTT System Service Interface](GUID-B5FCF623-E7FF-4626-AA04-20BCC3916E44.md)

## C

```c
int32_t SYS_MQTT_Subscribe(SYS_MODULE_OBJ obj,
SYS_MQTT_SubscribeConfig *subConfig);
```

## Summary

Returns success/ failure for the subscribing to a Topic by the user.

## Description

This function is used for subscribing to a Topic.

## Precondition

SYS\_MQTT\_Connect should have been called before calling this function

## Parameters

|Param|Description|
|-----|-----------|
|obj|SYS MQTT object handle, returned from SYS\_MQTT\_Connect subConfig - valid pointer to the Topic details on which to Subscribe|

## Returns

*SYS\_MQTT\_SUCCESS* - Indicates that the Request was catered to successfully

*SYS\_MQTT\_FAILURE* - Indicates that the Request failed

## Example

```c
SYS_MQTT_SubscribeConfig		sSubscribeCfg;

memset(&sSubscribeCfg, 0, sizeof(sSubscribeCfg));
sSubscribeCfg.qos = 1;
strcpy(sSubscribeCfg.topicName, "house/temperature/first_floor/kitchen");

// Handle "objSysMqtt" value must have been returned from SYS_MQTT_Connect.
if( SYS_MQTT_Subscribe(objSysMqtt, &sSubscribeCfg) == SYS_MQTT_SUCCESS)
{
}
```

