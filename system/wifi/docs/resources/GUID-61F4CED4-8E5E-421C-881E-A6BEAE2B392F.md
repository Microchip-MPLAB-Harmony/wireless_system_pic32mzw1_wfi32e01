# SYS\_WIFI\_Tasks Function

**Parent topic:**[Wi-Fi System Service Interface](GUID-B9C73D51-5039-4573-A452-176603C18703.md)

## C

```c
uint8_t SYS_WIFI_Tasks ( SYS_MODULE_OBJ object)
```

## Summary

Maintains the Wi-Fi System tasks and functionalities.

## Description

This function is used to run the various tasks and functionalities of Wi-Fi system service.

## Precondition

The SYS\_WIFI\_Initialize function should have been called before calling this function.

## Parameters

|Param|Description|
|-----|-----------|
|object|SYS WIFI object handle, returned from SYS\_WIFI\_Initialize|

## Returns

return SYS\_WIFI\_STATUS if client provided object is valid, else return SYS\_WIFI\_OBJ\_INVALID.

## Example

```c
if (SYS_WIFI_OBJ_INVALID != SYS_WIFI_Tasks (sysObj.syswifi))
{
    
}

```

## Remarks

If the Wi-Fi system service is enabled using MHC, then auto generated code will take care of system task execution.

