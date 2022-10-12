# SYS\_WIFIPROV\_Tasks Function

**Parent topic:**[Wi-Fi Provisioning System Service Interface](GUID-EC779F2A-1DDD-4F5A-A648-47DE4498A25F.md)

## C

```c
uint8_t SYS_WIFIPROV_Tasks ( SYS_MODULE_OBJ object)
```

## Summary

Maintains the Wi-Fi Provisioning System tasks and functionalities.

## Description

This function is used to run the various tasks and functionalities of Wi-Fi Provisioning system service.

## Precondition

The SYS\_WIFIPROV\_Initialize function should have been called before calling this function.

## Parameters

|Param|Description|
|-----|-----------|
|object|SYS WIFI Provisioning object handle, returned from SYS\_WIFIPROV\_Initialize|

## Returns

return SYS\_WIFIPROV\_STATUS if client provided object is valid, else return SYS\_WIFIPROV\_OBJ\_INVALID.

## Example

```c
if (SYS_WIFIPROV_OBJ_INVALID != SYS_WIFIPROV_Tasks (wifiProvServHandle))
{
    
}
```

## Remarks

None

