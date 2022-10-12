# SYS\_NET\_RecvMsg Function

**Parent topic:**[Net System Service Interface](GUID-010BB62D-452D-4B87-9F43-FDA5BF80F6AF.md)

## C

```c
int32_t SYS_NET_RecvMsg(SYS_MODULE_OBJ obj, void *data, uint16_t len)
```

## Summary

Returns No of Bytes received from peer using the System NET instance.

## Description

This function returns the number of bytes received from the peer.

## Precondition

SYS\_NET\_Open should have been called.

## Parameters

obj - SYS NET object handle, returned from SYS\_NET\_Open data - valid data buffer pointer len - length of the data to be transmitted

## Returns

*SYS\_NET\_SERVICE\_DOWN* - Indicates that the System NET instance is not connected to the peer

*SYS\_NET\_GET\_NOT\_READY* - Indicates that the System NET instance No Data to GET

*Positive Non-Zero* - Indicates the number of bytes received from the peer, which may be less than the "len" of the buffer passed as the param.

## Example

```c
// Handle "objSysNet" value must have been returned from SYS_NET_Open.
int32_t len = 32;
uint8_t buffer[32] = {0};
    len = SYS_NET_RecvMsg(objSysNet, buffer, len);
    if(len > 0)
    {
    }
```

## Remarks

None.

