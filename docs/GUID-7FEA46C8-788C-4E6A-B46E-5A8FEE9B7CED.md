# SYS\_WIFIPROV\_RESULT Enum

**Parent topic:**[Wi-Fi Provisioning System Service Interface](GUID-EC779F2A-1DDD-4F5A-A648-47DE4498A25F.md)

## C

```c
typedef enum{
    
    /* Operation completed with success */
    SYS_WIFIPROV_SUCCESS = 0,
    
    /* Operation failed. */
    SYS_WIFIPROV_FAILURE,
    
    /* Operation request object is invalid */
    SYS_WIFIPROV_OBJ_INVALID=255
    
}SYS_WIFIPROV_RESULT;

```

## Summary

Result of a Wi-Fi Provisioning system service client interface operation.

## Description

Identifies the result of Wi-Fi Provisioning service operations

## Remarks

None.

