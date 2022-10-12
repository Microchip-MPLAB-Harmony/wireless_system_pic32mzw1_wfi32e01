# SYS\_WSS\_EVENTS Enum

**Parent topic:**[Web Socket Server System Service Interface](GUID-9DCBB817-ECC8-46C6-954B-F6B0D8F5C0BC.md)

## C

```c
typedef enum {
    SYS_WSS_EVENT_ERR=0, //Reports any error condition
    //SYS_WSS_EVENT_UP,
    SYS_WSS_EVENT_CLIENT_CONNECTING, //Reports the connection request from the client
    SYS_WSS_EVENT_CLIENT_CONNECTED, //Reports connection completed status
    SYS_WSS_EVENT_CLIENT_BIN_DATA_RX, //Reports the reception of a binary data
    SYS_WSS_EVENT_CLIENT_TXT_DATA_RX, //Reports the reception of a text data
    SYS_WSS_EVENT_CLIENT_PING_RX, //Report the reception of a ping message
    SYS_WSS_EVENT_CLIENT_PONG_RX, //Reports the reception of a pong message
    SYS_WSS_EVENT_CLIENT_CLOSE_FRAME_RX, //Reports the reception of a closing handshake
    SYS_WSS_EVENT_CLIENT_CLOSING, //Reports the connection closing
    SYS_WSS_EVENT_CLIENT_CLOSED, //Reports the connection closure completion
    SYS_WSS_EVENT_ERR_INVALID_FRAME, //Reports the reception of an invalid frame
    // SYS_WSS_EVENT_DOWN,
    SYS_WSS_EVENT_CLIENT_TIMEOUT, //Reports the client connection timeout
} SYS_WSS_EVENTS;

```

## Summary

The event to be reported to the application from the WSS service according to the message exchanges with the client.

## Remarks

None.

