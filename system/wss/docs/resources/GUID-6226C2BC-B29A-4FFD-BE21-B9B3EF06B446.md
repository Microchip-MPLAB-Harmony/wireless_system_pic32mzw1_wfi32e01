# SYS\_WSS\_CloseConnection Function

**Parent topic:**[Web Socket Server System Service Interface](GUID-9DCBB817-ECC8-46C6-954B-F6B0D8F5C0BC.md)

## C

```c
SYS_WSS_RESULT SYS_WSS_CloseConnection(SYS_WSS_STATUS_CODE code, uint8_t *data, size_t dataLen, int32_t clientIndex)
```

## Summary

Closes the Web Socket connection to the client indicated by the parameter clientIndex.

## Description

This API initiate the closing handshake with the status code provided and and terminate the Web Socket connection to the client indicated by the parameter clientIndex.

## Precondition

The connection state of the client indicated by the clientIndex \(g\_wssSrvcObj.wssState\) shall be SYS\_WSS\_STATE\_CONNECTED

## Parameters

|Param|Description|
|-----|-----------|
|code|Status code to be send to the client in the closing handshake\(SYS\_WSS\_STATUS\_CODE\) .|
|\*data|A pointer to buffer with the data \(if any\) related to the connection closure|
|dataLen|Length of the data|
|clientIndex|The clientID, for identifying the client which caused the event to occur.|

## Returns

SYS\_WSS\_RESULT.

## Example

```c
SYS_WSS_RESULT res;
res =SYS_WSS_CloseConnection(SYS_WSS_STATUS_CODE_UNSUPPORTED_DATA, NULL, 0, 1);
```

## Remarks

None.

