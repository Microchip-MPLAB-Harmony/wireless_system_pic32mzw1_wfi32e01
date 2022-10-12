# SYS\_NET\_SendMsg Function

**Parent topic:**[Net System Service Interface](GUID-010BB62D-452D-4B87-9F43-FDA5BF80F6AF.md)

## C

```c
int32_t SYS_NET_SendMsg(SYS_MODULE_OBJ obj, uint8_t *buffer, uint16_t len)
```

## Summary

Returns No of Bytes sent to peer using the System NET instance.

## Description

This function returns the number of bytes transmitted to the peer.

## Precondition

SYS\_NET\_Open should have been called.

## Parameters

object - SYS NET object handle, returned from SYS\_NET\_Open data - valid data buffer pointer len - length of the data to be transmitted

## Returns

*SYS\_NET\_SERVICE\_DOWN* - Indicates that the System NET instance is not connected to the peer

*SYS\_NET\_PUT\_NOT\_READY* - Indicates that the System NET instance Put is NOT ready

*SYS\_NET\_PUT\_BUFFER\_NOT\_ENOUGH* - Indicates that the System NET instance cannot transmit as the available buffer is less than the bytes to be transmitted

*Positive Non-Zero* - Indicates the number of bytes transmitted to the peer

## Example

```c
// Handle "objSysNet" value must have been returned from SYS_NET_Open.
while(SYS_NET_SendMsg(objSysNet, "hello", 5) <= 0);
```

## Remarks

None.

