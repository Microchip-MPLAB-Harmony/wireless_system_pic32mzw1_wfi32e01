# Web Socket Server System Service Interface

-   **[SYS\_WSS\_GUID Macro](resources/GUID-818A720C-1FD4-4EA4-B22C-F44B52F11DB5.md)**  

-   **[SYS\_WSS\_CLIENT\_KEY\_SIZE Macro](resources/GUID-7A668B78-45FE-4EDF-965E-1900422374CE.md)**  

-   **[SYS\_WSS\_CLIENT\_KEY\_SIZE\_DECODED Macro](resources/GUID-067B7E35-0233-4030-BDC7-ADA3C5A65281.md)**  

-   **[SYS\_WSS\_HTTP\_VERSION\_1\_1 Macro](resources/GUID-B12643ED-A0B9-4331-9E81-961355411485.md)**  

-   **[SYS\_WSS\_KA\_TIMER\_PERIOD Macro](resources/GUID-8305E5FB-D8B6-4824-AD2A-EFA4BF0DCDCD.md)**  

-   **[SYS\_WSS\_SERVER\_KEY\_SIZE Macro](resources/GUID-BEE2CEA6-760B-4433-B6F9-46FAD85BA076.md)**  

-   **[SYS\_WSS\_SHA1\_DIGEST\_SIZE Macro](resources/GUID-055E1A74-7370-4E9A-BDC6-FE5CA1547D14.md)**  

-   **[SYS\_WSS\_STATUS\_CODE\_LEN Macro](resources/GUID-DE91F328-40E1-48BE-9E5D-8638A49014A1.md)**  

-   **[SYS\_WSS\_RESULT Enum](resources/GUID-7DC907EC-3CE8-45F2-A78B-6AACDAEF6F52.md)**  

-   **[SYS\_WSS\_EVENTS Enum](resources/GUID-0F240AEF-6B53-4CD2-A8FD-1D16BA00B43E.md)**  

-   **[SYS\_WSS\_STATE Enum](resources/GUID-04628A3C-69FB-458A-B6A7-9CE08A6C26EB.md)**  

-   **[SYS\_WSS\_FRAME Enum](resources/GUID-91BC6347-08EF-4EE7-ADDE-90524E70867A.md)**  

-   **[SYS\_WSS\_STATUS\_CODE Enum](resources/GUID-8A2DC2AD-7D43-4568-9CA7-325A8F1C64CA.md)**  

-   **[SYS\_WSS\_HANDSHAKE\_CTXT Struct](resources/GUID-17FAEA79-D63F-4222-B015-DF863DD4AFA6.md)**  

-   **[SYS\_WSS\_RXDATA Struct](resources/GUID-B70E454B-E9FB-4214-AC26-354C154592A1.md)**  

-   **[SYS\_WSS\_CONFIG Struct](resources/GUID-79B1C1D0-37E8-464B-82BE-41A226C2AB59.md)**  

-   **[SYS\_WSS\_CALLBACK Typedef](resources/GUID-C340A70C-DB26-427E-B902-B253B1590DD7.md)**  

-   **[SYS\_WSS\_Initialize Function](resources/GUID-9F1A7B19-413E-4254-8E08-E61C7A180E8F.md)**  

-   **[SYS\_WSS\_Deinitialize Function](resources/GUID-897565A1-B722-4A0C-AE94-7C04BDEBEA4F.md)**  

-   **[SYS\_WSS\_PingClient Function](resources/GUID-8C607133-0A31-4E3D-BDCC-A6CF5E5950B9.md)**  

-   **[SYS\_WSS\_register\_callback Function](resources/GUID-846D93A7-8E39-4AB6-AF2F-99A20D770DB9.md)**  

-   **[SYS\_WSS\_sendMessage Function](resources/GUID-B0D9910C-94B2-4947-AC80-5CE869E553BB.md)**  

-   **[SYS\_WSS\_CloseConnection Function](resources/GUID-6226C2BC-B29A-4FFD-BE21-B9B3EF06B446.md)**  

-   **[SYS\_WSS\_Task Function](resources/GUID-28B1581E-648F-4F92-B376-19B1A46D81C3.md)**  


**Parent topic:**[Web Socket Server \(WSS\) System Service](GUID-097A4209-8474-480E-A141-6C8FC60A7671.md)

## Data Types and Constants Summary

|Name|Description|
|----|-----------|
|SYS\_WSS\_KA\_TIMER\_PERIOD|Decides the accuracy of the client timeout|
|SYS\_WSS\_CLIENT\_KEY\_SIZE|Array size for holding the client key|
|SYS\_WSS\_CLIENT\_KEY\_SIZE\_DECODED|Decoded client key size as per the RFC6455|
|SYS\_WSS\_SERVER\_KEY\_SIZE|Array saze for holding the server key|
|SYS\_WSS\_SHA1\_DIGEST\_SIZE|SHA1 digest size -server key genartion|
|SYS\_WSS\_HTTP\_VERSION\_0\_9|HTTP vesrion 0.9|
|SYS\_WSS\_HTTP\_VERSION\_1\_0|HTTP version 1.0|
|SYS\_WSS\_HTTP\_VERSION\_1\_1|HTTP version 1.1|
|SYS\_WSS\_STATUS\_CODE\_LEN|Closing Status code lenth as per RFC6455|
|SYS\_WSS\_GUID|WebSocket GUID as per Section 1.3 of RFC 6455|
|SYS\_WSS\_CONFIG|Used for passing on the configuration\(port and TLS\) for socket connection|
|SYS\_WSS\_HANDSHAKE\_CTXT|Stores the handshake information of a client.|
|SYS\_WSS\_FRAME\_HEADER|Identifies the frame format as defined by RFC6455.|
|SYS\_WSS\_RXDATA|Stores the data received from the client along with the datalength.|
|SYS\_WSS\_RESULT|Identifies the return values for the WSS system service APIs.|
|SYS\_WSS\_STATE|Identifies the state machine values of the WSS system service.|
|SYS\_WSS\_FRAME|Identifies the frame types as defined by the RFC6455.|
|SYS\_WSS\_EVENTS|Identifies the events reported to the application using the call back function.|
|SYS\_WSS\_STATUS\_CODE|Identifies status code to be used in the closing handshake as defined by RF6455.|

## Initialization functions Summary

|Name|Description|
|----|-----------|
|SYS\_WSS\_Initialize|Returns wss object handle after initialization of data structures and timers of the WSS system service|
|SYS\_WSS\_Deinitialize|Deinitialization of data structures of the WSS system service|

## Data Exchange functions Summary

|Name|Description|
|----|-----------|
|SYS\_WSS\_sendMessage|Returns failure or success after sending the data to the client.|
|SYS\_WSS\_register\_callback|Returns success after registration of the user call back function.|
|SYS\_WSS\_CloseConnection|Returns success after sending a close frame to the client.|
|SYS\_WSS\_PingClient|Returns success after sending a ping frame to the client.|

