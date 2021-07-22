---
grand_parent: Harmony 3 PIC32MZW1 wireless system services package
parent: Wi-Fi provisioning Service
title: Wi-Fi provisioning System Service developer guide
has_toc: true
nav_order: 1
---


# Wi-Fi provisioning System Service Developer's Guide


## **Code modification/implementation guide for common use cases**

### **Adding New provisioning Method **

When User want to add new provisioning method, user needs to parse the incoming provisioning data and update the information in `SYS_WIFI_CONFIG` as shown in below code snippet. The Wi-Fi provisioning Service stores and maintains the Wi-Fi configuration data if NVM is enabled by user in the MHC.     

```C
            SYS_WIFI_CONFIG    wifiSrvcConfig;

            // Set mode as STA 
            wifiSrvcConfig.mode = SYS_WIFI_STA;

            // Enable saving wifi configuration 
            wifiSrvcConfig.saveConfig = true;   

            // Set the auth type to SYS_WIFI_WPA2
            wifiSrvcConfig.staConfig.authType = SYS_WIFI_WPA2;

            // Enable all the channels(0)
            wifiSrvcConfig.staConfig.channel = 0;

            // Device doesn't wait for user request
            wifiSrvcConfig.staConfig.autoConnect = 1;

            // Set SSID 
            memcpy(wifiSrvcConfig.staConfig.ssid, WIFI_DEV_SSID, sizeof(WIFI_DEV_SSID));

            // Set PSK
            memcpy(wifiSrvcConfig.staConfig.psk, WIFI_DEV_PSK, sizeof(WIFI_DEV_PSK));

            
            if (SYS_WIFI_SUCCESS == SYS_WIFI_CtrlMsg (sysObj.syswifi, SYS_WIFI_CONNECT, &wifiSrvcConfig, sizeof(SYS_WIFI_CONFIG)))
            {
            
            }

```   
