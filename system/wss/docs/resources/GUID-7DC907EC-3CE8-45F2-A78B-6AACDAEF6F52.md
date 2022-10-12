# SYS\_WSS\_RESULT Enum

**Parent topic:**[Web Socket Server System Service Interface](GUID-9DCBB817-ECC8-46C6-954B-F6B0D8F5C0BC.md)

## C

```c
typedef enum {
    SYS_WSS_SUCCESS = 0, //successful execution
    SYS_WSS_FAILURE = 1, //Failure in execution
    SYS_WSS_ERROR_INVALID_REQUEST, //Failure in validation of the client handshake
    SYS_WSS_ERROR_INVALID_KEY, //Failure in validation of the client handshake
    SYS_WSS_ERROR_INVALID_FRAME, //Failure in validation of the client request
} SYS_WSS_RESULT;

```

## Summary

Reporting the success/failure of an API execution.

## Remarks

None.

