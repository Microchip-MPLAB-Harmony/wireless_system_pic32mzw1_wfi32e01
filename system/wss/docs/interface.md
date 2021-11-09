---
grand_parent: Harmony 3 PIC32MZW1 wireless system services package
parent: Web Socket Server System Service
title: Web Socket Server System Service Interface
has_toc: true
nav_order: 3
---

# Web Socket Server System Service Interface
{: .no_toc }

### Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Data Types and Constants Summary

| Name | Description |
|-|-|
| [SYS_WSS_KA_TIMER_PERIOD](#SYS_WSS_KA_TIMER_PERIOD) | Decides the accuracy of the client timeout |
| [SYS_WSS_CLIENT_KEY_SIZE](#SYS_WSS_CLIENT_KEY_SIZE) | Array size for holding the client key |
| [SYS_WSS_CLIENT_KEY_SIZE_DECODED](#SYS_WSS_CLIENT_KEY_SIZE_DECODED) | Decoded client key size as per the RFC6455 |
| [SYS_WSS_SERVER_KEY_SIZE](#SYS_WSS_SERVER_KEY_SIZE) | Array saze for holding the server key |
| [SYS_WSS_SHA1_DIGEST_SIZE](#SYS_WSS_SHA1_DIGEST_SIZE) | SHA1 digest size -server key genartion |
| [SYS_WSS_HTTP_VERSION_0_9](#SYS_WSS_HTTP_VERSION_0_9) | HTTP vesrion 0.9 |
| [SYS_WSS_HTTP_VERSION_1_0](#SYS_WSS_HTTP_VERSION_1_0) | HTTP version 1.0 |
| [SYS_WSS_HTTP_VERSION_1_1](#SYS_WSS_HTTP_VERSION_1_1) | HTTP version 1.1 |
| [SYS_WSS_STATUS_CODE_LEN](#SYS_WSS_STATUS_CODE_LEN) | Closing Status code lenth as per RFC6455 |
| [SYS_WSS_GUID](#SYS_WSS_GUID) | WebSocket GUID as per Section 1.3 of RFC 6455 |
| [SYS_WSS_CONFIG](#SYS_WSS_CONFIG) | Used for passing on the configuration(port and TLS) for socket connection|
| [SYS_WSS_HANDSHAKE_CTXT](#SYS_WSS_HANDSHAKE_CTXT) | Stores the handshake information of a client. |
| [SYS_WSS_FRAME_HEADER](#SYS_WSS_FRAME_HEADER) | Identifies the frame format as defined by RFC6455. |
| [SYS_WSS_RXDATA](#SYS_WSS_RXDATA) | Stores the data received from the client along with the datalength. |
| [SYS_WSS_RESULT](#SYS_WSS_RESULT) | Identifies the return values for the WSS system service APIs. |
| [SYS_WSS_STATE](#SYS_WSS_STATE) | Identifies the state machine values of the WSS system service. |
| [SYS_WSS_FRAME](#SYS_WSS_FRAME) | Identifies the frame types as defined by the RFC6455. |
| [SYS_WSS_EVENTS](#SYS_WSS_EVENTS) | Identifies the events reported to the application using the call back function. |
| [SYS_WSS_STATUS_CODE](#SYS_WSS_STATUS_CODE) | Identifies status code to be used in the closing handshake as defined by RF6455. |

## Initialization functions Summary

| Name | Description |
|-|-|
| [SYS_WSS_Initialize](#SYS_WSS_Initialize) | Returns wss object handle after initialization of data structures and timers of the WSS system service |
| [SYS_WSS_Deinitialize](#SYS_WSS_Deinitialize) | Deinitialization of data structures of the WSS system service |

## Data Exchange functions Summary

| Name | Description |
|-|-|
| [SYS_WSS_sendMessage](#SYS_WSS_sendMessage) | Returns failure or success after sending the data to the client. |
| [SYS_WSS_register_callback](#SYS_WSS_register_callback) | Returns success after registration of the user call back function. |
| [SYS_WSS_CloseConnection](#SYS_WSS_CloseConnection) | Returns success after sending a close frame to the client. |
| [SYS_WSS_PingClient](#SYS_WSS_PingClient) | Returns success after sending a ping frame to the client. |

## Data Types and Constants


### SYS_WSS_KA_TIMER_PERIOD

**Summary**

WSS system timer period which the accuracy of the client timeout. 

**Remarks**

None. 

```c
#define SYS_WSS_KA_TIMER_PERIOD  100		
```

### SYS_WSS_CLIENT_KEY_SIZE


**Summary**

Array size for holding the client key.  

**Remarks**

None. 

```c
#define SYS_WSS_CLIENT_KEY_SIZE 16	
```

### SYS_WSS_CLIENT_KEY_SIZE_DECODED

**Summary**

Decoded client key size as per the RFC6455.  

**Remarks**

None. 

```c
#define SYS_WSS_CLIENT_KEY_SIZE_DECODED 16
```

### SYS_WSS_SERVER_KEY_SIZE


**Summary**

Array saze for holding the server key. 

**Remarks**

None. 

```c
#define SYS_WSS_SERVER_KEY_SIZE 50			
```

### SYS_WSS_SHA1_DIGEST_SIZE


**Summary**

SHA1 digest size -server key genartion.  

**Remarks**

None. 

```c
#define SYS_WSS_SHA1_DIGEST_SIZE 	20 	
```

### SYS_WSS_HTTP_VERSION_0_9


**Summary**

HTTP vesrion 0.9

**Remarks**

None. 

```c
#define SYS_WSS_HTTP_VERSION_0_9 0x0009	
```

### SYS_WSS_HTTP_VERSION_1_0


**Summary**

HTTP version 1.0 

**Remarks**

None. 

```c
#define SYS_WSS_HTTP_VERSION_1_0 0x0100			
```

### SYS_WSS_HTTP_VERSION_1_1


**Summary**

HTTP version 1.1

**Remarks**

None. 

```c
#define SYS_WSS_HTTP_VERSION_1_1 0x0101		
```

### SYS_WSS_STATUS_CODE_LEN


**Summary**

Closing Status code lenth as per RFC6455.  

**Remarks**

None. 

```c
#define SYS_WSS_STATUS_CODE_LEN 2	
```

### SYS_WSS_GUID


**Summary**

WebSocket GUID as per Section 1.3 of RFC 6455. 

**Remarks**

None. 

```c
#define SYS_WSS_GUID "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
```

### SYS_WSS_CONFIG


**Summary**

Used for passing on the configuration(port and TLS) for socket connection to be used for Web Socket Server connections.

**Remarks**

None. 

```c
typedef struct {
        unsigned int port;             //port used by the WSS service.
        bool isTLSEnabled;            //TLS enabled?
} SYS_WSS_CONFIG;

```

### SYS_WSS_HANDSHAKE_CTXT


**Summary**

Stores the client/server handshake information.

**Remarks**

None. 

```c
typedef struct {
        uint16_t http_version;    //HTTP version specified in the client handshake
        uint8_t ws_version;      //Web socket version specified in the client handshake
        bool upgradeWebSocket;   //If upgrade websocket field specified in the client handshake
        bool origin;            //If origin field specified in the client handshake
        bool connectionUpgrade; //If upgrade field present in the client handshake
        bool connectionClose;  // Persistent connection support based on the HTTP version
        char clientKey[SYS_WSS_CLIENT_KEY_SIZE + 1]; //Client key
        char serverKey[SYS_WSS_SERVER_KEY_SIZE + 1]; // Server key
} SYS_WSS_HANDSHAKE_CTXT;
```

### SYS_WSS_FRAME_HEADER


**Summary**

Identifies the frame format as defined by RFC6455. 

**Remarks**

None. 

```c
typedef __PACKED_STRUCT {
        uint8_t opcode : 4;      //byte0, Opcode as defined by RFC6455
        uint8_t resvd : 3;       //Reserved bits as defined by RFC6455
        uint8_t fin : 1;         // fin bit as defined by RFC6455.Indicates that this is the final fragment in a message.0=first frame, 1= final frame
        uint8_t payloadLen : 7;  //byte1, Payload length as defined by the RFC6455.It can be 7 bits, 7+16 bits, or 7+64 bits.
        uint8_t mask : 1;        //Defines whether the "Payload data" is masked. 1=masked,0=not masked
        uint8_t extPayloadLen[]; //byte2,Extended payload length, I can be 16 or 64 bits based on the payloadLen
} SYS_WSS_FRAME_HEADER;
```

### SYS_WSS_RXDATA


**Summary**

Stores the data received from the client along with the datalength..  

**Remarks**

None. 

```c
typedef struct {
        uint8_t * data;               //Pointer to the rx data buffer
        int64_t datalen;              //length of the received data
} SYS_WSS_RXDATA;
```

### SYS_WSS_RESULT


**Summary**

Identifies the return values for the WSS system service APIs.  

**Remarks**

None. 

```c
typedef enum {
        SYS_WSS_SUCCESS = 0,                    //successful execution
        SYS_WSS_FAILURE = 1,                    //Failure in execution
        SYS_WSS_ERROR_INVALID_REQUEST,          //Failure in validation of the client handshake
        SYS_WSS_ERROR_INVALID_KEY,              //Failure in validation of the client handshake
        SYS_WSS_ERROR_INVALID_FRAME,            //Failure in validation of the client request
} SYS_WSS_RESULT;
```

### SYS_WSS_STATE


**Summary**

Identifies the state machine values of the WSS system service.

**Remarks**

None. 

```c
typedef enum {
        SYS_WSS_STATE_CONNECTING = 0,            //Handles the processing of the client opening handshake
        SYS_WSS_STATE_CONNECTED,                 //State where the data exchanges happen
        SYS_WSS_STATE_CLOSING,                   //Handles the processing of the client closing handshake
        SYS_WSS_STATE_CLOSED,                    //Connection closed, the initial state of the service 
} SYS_WSS_STATE;
    
```


### SYS_WSS_FRAME


**Summary**

 Identifies the frame types as defined by the RFC6455.

**Remarks**

None. 

```c
typedef enum {
        SYS_WSS_FRAME_CONTINUATION = 0x00,        //Continuation frame      - Data frame with opcode 0
        SYS_WSS_FRAME_TEXT = 0x01,                //Text data frame         - Data frame with opcode 1
        SYS_WSS_FRAME_BINARY = 0x02,              //Binary data frame       - Data frame with opcode 2
        SYS_WSS_FRAME_CLOSE = 0x08,               //Connection close frame  - Control frame with opcode 8
        SYS_WSS_FRAME_PING = 0x09,                //Ping frame              - Ping frame with opcode 9
        SYS_WSS_FRAME_PONG = 0x0A                 //Pong frame              - Pong frame with opcode 10
} SYS_WSS_FRAME;
```

### SYS_WSS_EVENTS


**Summary**

Identifies the events reported to the application using the call back function.  

**Remarks**

None. 

```c
typedef enum {
        SYS_WSS_EVENT_ERR=0,                         //Reports any error condition
        SYS_WSS_EVENT_CLIENT_CONNECTING,             //Reports the connection request from the client
        SYS_WSS_EVENT_CLIENT_CONNECTED,              //Reports connection completed status 
        SYS_WSS_EVENT_CLIENT_BIN_DATA_RX,            //Reports the reception of a binary data
        SYS_WSS_EVENT_CLIENT_TXT_DATA_RX,            //Reports the reception of a text data
        SYS_WSS_EVENT_CLIENT_PING_RX,                //Report the reception of a ping message
        SYS_WSS_EVENT_CLIENT_PONG_RX,                //Reports the reception of a pong message
        SYS_WSS_EVENT_CLIENT_CLOSE_FRAME_RX,         //Reports the reception of a closing handshake
        SYS_WSS_EVENT_CLIENT_CLOSING,                //Reports the connection closing
        SYS_WSS_EVENT_CLIENT_CLOSED,                 //Reports the connection closure completion
        SYS_WSS_EVENT_ERR_INVALID_FRAME,             //Reports the reception of an invalid frame                     
        SYS_WSS_EVENT_CLIENT_TIMEOUT,                //Reports the client connection timeout
} SYS_WSS_EVENTS;
```


### SYS_WSS_STATUS_CODE


**Summary**

 Identifies status code to be used in the closing handshake as defined by RF6455.  

**Remarks**

None. 

```c
typedef enum {
        SYS_WSS_STATUS_CODE_NORMAL_CLOSURE = 1000,
        SYS_WSS_STATUS_CODE_GOING_AWAY = 1001,
        SYS_WSS_STATUS_CODE_PROTOCOL_ERROR = 1002,
        SYS_WSS_STATUS_CODE_UNSUPPORTED_DATA = 1003,
        SYS_WSS_STATUS_CODE_NO_STATUS_RCVD = 1005, //reserved code, Not to be used in the close frames
        SYS_WSS_STATUS_CODE_ABNORMAL_CLOSURE = 1006, //reserved, Not to be used in the close frames
        SYS_WSS_STATUS_CODE_INVALID_PAYLOAD_DATA = 1007,
        SYS_WSS_STATUS_CODE_POLICY_VIOLATION = 1008,
        SYS_WSS_STATUS_CODE_MESSAGE_TOO_BIG = 1009,
        SYS_WSS_STATUS_CODE_MANDATORY_EXT = 1010,
        SYS_WSS_STATUS_CODE_INTERNAL_ERROR = 1011,
        SYS_WSS_STATUS_CODE_TLS_HANDSHAKE = 1015 // reserved code, Not to be used in the close frames
} SYS_WSS_STATUS_CODE;
```
## Initialization functions


### SYS_WSS_Initialize

**Function**

```c
SYS_MODULE_OBJ SYS_WSS_Initialize(SYS_WSS_CONFIG *config, SYS_WSS_CALLBACK callback, void *cookie)
```

**Summary**

Returns SYS_MODULE_OBJ after the successful initialization of data structures of the WSS service.

**Description**

   This function is used for initializing the data structures of the WSS service and is called from within the System Task.This function can be called by the application with required arguments.  

**Returns**

Returns the address of an array of SYS_MODULE_OBJ which will have the initialization data for all clients. 

**Example**

```c
sysWSS_obj = SYS_WSS_Initialize(NULL,NULL,NULL); //Default config, callback and cookie will be taken
```

**Remarks**

If the WSS system service is enabled using MHC, then auto generated code will take care of WSS System Service initialization. But the user need to register for the callback function independently.

### SYS_WSS_Deinitialize

**Function**

```c
void SYS_WSS_Deinitialize()
```

**Summary**

Deinitialization of data structures of the WSS service  

**Description**

This function is used for freeing the allocated data structures for the WSS service.This function can be called by the application with WSS service object handle.

**Example**

```c
SYS_WSS_Deinitialize(&sysWSSObj);
```

**Remarks**

None 

## Data Exchange functions




### SYS_WSS_sendMessage

**Function**

```c
SYS_WSS_RESULT SYS_WSS_sendMessage(bool fin, SYS_WSS_FRAME type, uint8_t *data, size_t dataLen, int32_t clientIndex)
```

**Summary**

Sends a message to the client indicated by the parameter clientIndex. Returns success/failure after sending the message.  

**Description**

This API sends the data provided in the web socket frame format to the client indicated by the parameter clientIndex.

**Precondition**

The connection state of the client indicated by the clientIndex (g_wssSrvcObj[clientIndex].wssState) shall be SYS_WSS_STATE_CONNECTED.  

**Parameters**

fin  	    - Fin value as defined by RFC6455 to indicate if the      frame is final or continuation frame.<br> 
                0 = Indicates more messages to follow, the current frame is a continuation frame<br>
                1 = Indicates the final frame of the message.<br>

type        - The data type of the frame , TEXT or BINARY<br>

*data	    - A pointer to buffer with the data to be sent<br>

dataLen     - Length of the data.<br>

clientIndex - The clientID, for identifying the client which caused the event to occur.<br>  

**Returns**

SYS_WSS_RESULT.

**Example**

```c
SYS_WSS_RESULT res;      
res =  SYS_WSS_sendMessage(1, SYS_WSS_FRAME_TEXT, ((SYS_WSS_RXDATA*) data)->data, ((SYS_WSS_RXDATA *) data)->datalen, clientIndex);
```

**Remarks**

None. 

### SYS_WSS_register_callback

**Function**

```c
SYS_WSS_RESULT SYS_WSS_register_callback(SYS_WSS_CALLBACK userCallback, void* cookie);
```

**Summary**

API for registering the application callback function with the WSS service. Returns success after successful registration of the callback function.

**Description**

Callback functions may be registered by clients of the WSS service during the initialization using this API.  

**Precondition**

None. 

**Parameters**

userCallback     	    - A function pointer to the application call back API.<br>

event           	    - Data (if any) related to the Event<br>

cookie                  - A context value, returned untouched to the client when the callback occurs.<br>	 

**Returns**

SYS_WSS_RESULT.  

**Example**

```c
 void wss_user_callback(SYS_WSS_EVENTS event, void *data, int32_t clientIndex, void *cookie) {

        int i = 0;
        switch (event) {

            case SYS_WSS_EVENT_CLIENT_CONNECTING:
            {
                SYS_CONSOLE_PRINT("wssSysServCallback(%d): SYS_WSS_EVENT_CLIENT_CONNECTING\r\n",clientIndex);
                break;
            }
            case SYS_WSS_EVENT_CLIENT_CONNECTED:
            {

                SYS_CONSOLE_PRINT("wssSysServCallback(%d): SYS_WSS_EVENT_CLIENT_CONNECTED\r\n",clientIndex);

                break;
            }
            case SYS_WSS_EVENT_CLIENT_BIN_DATA_RX:
            {
                SYS_CONSOLE_PRINT("wssSysServCallback(%d): SYS_WSS_EVENT_CLIENT_BIN_DATA_RX\r\n",clientIndex);
                for (i = 0; i < ((SYS_WSS_RXDATA*) data)->datalen; i++) {
                    SYS_CONSOLE_PRINT("%X ", ((SYS_WSS_RXDATA*) data)->data[i]);
                }
                SYS_CONSOLE_PRINT("\r\n");
                //echo server.
                SYS_WSS_sendMessage(1, SYS_WSS_FRAME_TEXT, ((SYS_WSS_RXDATA*) data)->data, ((SYS_WSS_RXDATA *) data)->datalen, clientIndex);
                break;
            }
            case SYS_WSS_EVENT_CLIENT_TXT_DATA_RX:
            {

                SYS_CONSOLE_PRINT("wssSysServCallback(%d): SYS_WSS_EVENT_CLIENT_TXT_DATA_RX\r\n",clientIndex);
                for (i = 0; i < ((SYS_WSS_RXDATA *) data)->datalen; i++) {
                    SYS_CONSOLE_PRINT("%c", ((SYS_WSS_RXDATA*) data)->data[i]);
                }
                SYS_CONSOLE_PRINT("\r\n");
                // Enable the below statement for echo server
               //SYS_WSS_sendMessage(1, SYS_WSS_FRAME_TEXT, ((SYS_WSS_RXDATA*) data)->data, ((SYS_WSS_RXDATA *) data)->datalen, clientIndex);

                break;
            }
            case SYS_WSS_EVENT_CLIENT_CLOSING:
            {
                SYS_CONSOLE_PRINT("wssSysServCallback(%d): SYS_WSS_EVENT_CLIENT_CLOSING\r\n",clientIndex);
                break;
            }
            case SYS_WSS_EVENT_CLIENT_CLOSED:
            {
                SYS_CONSOLE_PRINT("wssSysServCallback(%d): SYS_WSS_EVENT_CLIENT_CLOSED\r\n",clientIndex);
                break;
            }
            case SYS_WSS_EVENT_ERR_INVALID_FRAME:
            {
                SYS_CONSOLE_PRINT("wssSysServCallback(%d): SYS_WSS_EVENT_ERR_INVALID_FRAME\r\n",clientIndex);
                break;
            }
            case SYS_WSS_EVENT_CLIENT_PING_RX:
            {
                SYS_CONSOLE_PRINT("wssSysServCallback(%d): SYS_WSS_EVENT_CLIENT_PING_RX\r\n",clientIndex);
                break;
            }
            case SYS_WSS_EVENT_CLIENT_PONG_RX:
            {
                SYS_CONSOLE_PRINT("wssSysServCallback(%d): SYS_WSS_EVENT_CLIENT_PONG_RX\r\n",clientIndex);
                break;
            }
            case SYS_WSS_EVENT_CLIENT_CLOSE_FRAME_RX:
            {
                SYS_CONSOLE_PRINT("wssSysServCallback(%d): SYS_WSS_EVENT_CLIENT_CLOSE_FRAME_RX\r\n",clientIndex);
                break;
            }
            case SYS_WSS_EVENT_ERR:
            {
                SYS_CONSOLE_PRINT("wssSysServCallback(%d): SYS_WSS_EVENT_ERR\r\n",clientIndex);
                break;
            }
    #if 0   
            case SYS_WSS_EVENT_DOWN:
            {
                SYS_CONSOLE_PRINT("wssSysServCallback(%d): SYS_WSS_EVENT_DOWN\r\n",clientIndex);
                break;
            }
    #endif
            case SYS_WSS_EVENT_CLIENT_TIMEOUT:
            {
                SYS_CONSOLE_PRINT("wssSysServCallback(%d): SYS_WSS_EVENT_CLIENT_TIMEOUT\r\n",clientIndex);
                break;
            }
        }
    }  
```

**Remarks**

None. 

### SYS_WSS_CloseConnection

**Function**

```c
SYS_WSS_RESULT SYS_WSS_CloseConnection(SYS_WSS_STATUS_CODE code, uint8_t *data, size_t dataLen, int32_t clientIndex);
```

**Summary**

Closes the Web Socket connection to the client indicated by the parameter clientIndex. 

**Description**

This API initiate the closing handshake with the status code provided and and terminate the Web Socket connection to the client indicated by the parameter clientIndex. 

**Precondition**

The connection state of the client indicated by the clientIndex (g_wssSrvcObj[clientIndex].wssState) shall be SYS_WSS_STATE_CONNECTED.

**Parameters**

code	       - Status code to be send to the client in the closing handshake(SYS_WSS_STATUS_CODE) .<br>

*data	      - A pointer to buffer with the data (if any) related to the connection closure<br>

dataLen       - Length of the data <br>

clientIndex   - The clientID, for identifying the client which caused the event to occur.<br>

**Returns**

None.  

**Example**

```c
SYS_WSS_RESULT res;
res =SYS_WSS_CloseConnection(SYS_WSS_STATUS_CODE_UNSUPPORTED_DATA, NULL, 0, 1);
```

**Remarks**

None. 


### SYS_WSS_PingClient

**Function**

```c
SYS_WSS_RESULT SYS_WSS_PingClient( uint8_t *data, size_t dataLen, int32_t clientIndex);
```

**Summary**

Sends a ping message to the client indicated by the parameter clientIndex.

**Description**

 This API sends a ping message to the client indicated by the parameter clientIndex.

**Precondition**

The connection state of the client indicated by the clientIndex (g_wssSrvcObj[clientIndex].wssState) shall be SYS_WSS_STATE_CONNECTED.

**Parameters**

*data	    - A pointer to buffer with the data (if any).<br>

dataLen     - Length of the data <br>

clientIndex - The clientID, for identifying the client which caused the event to occur.<br>

**Returns**

SYS_WSS_RESULT.  

**Example**

```c
SYS_WSS_RESULT res;
res =SYS_WSS_PingClient(&data, dataLen, 1);
```

**Remarks**

None. 

