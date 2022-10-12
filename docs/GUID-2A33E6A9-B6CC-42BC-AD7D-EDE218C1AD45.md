# SYS\_NET\_CtrlMsg Function

**Parent topic:**[Net System Service Interface](GUID-010BB62D-452D-4B87-9F43-FDA5BF80F6AF.md)

## C

```c
int32_t SYS_NET_CtrlMsg(SYS_MODULE_OBJ obj, SYS_NET_CTRL_MSG msg_type, void *data, uint16_t len)
```

## Summary

Returns success/ failure for the disconnect/ reconnect operation asked by the user.

## Description

This function is used for disconnecting or reconnecting to the peer.

## Precondition

SYS\_NET\_Open should have been called.

## Parameters

obj - SYS NET object handle, returned from SYS\_NET\_Open \| Param \| Description \|<br />\|:----- \|:----------- \|

\| msg\_type \| valid Msg Type SYS\_NET\_CTRL\_MSG \|<br />\| data - valid data buffer pointer based on the Msg Type \| NULL for DISCONNECT, Pointer to SYS\_NET\_Config for RECONNECT len - length of the data buffer the pointer is pointing to

## Returns

*SYS\_NET\_SUCCESS* - Indicates that the Request was catered to successfully

*SYS\_NET\_FAILURE* - Indicates that the Request failed

## Example

```c
// Handle "objSysNet" value must have been returned from SYS_NET_Open.
if( SYS_NET_CtrlMsg(objSysNet, SYS_NET_CTRL_MSG_DISCONNECT, NULL, 0) == SYS_NET_SUCCESS)
{
}
```

## Remarks

None.

