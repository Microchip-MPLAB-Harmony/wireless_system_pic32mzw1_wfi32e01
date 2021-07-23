---
parent: Harmony 3 PIC32MZW1 wireless system services package
title: OTA Service
has_children: true
has_toc: false
nav_order: 1

family: PIC32MZW1
function: Over The Air (OTA) firmware update System Service
---

# Over The Air (OTA) firmware update System Service

OTA System Service Library provides an application programming interface (API) to manage OTA functionalities. The OTA System Service uses the Wi-Fi service, Net service, NetPres APIs for achieving these functionalities. The user would need to configure the Home AP credentials (like SSID and Passphrase). The Wi-Fi service will use the credentials to connect to the Home AP and acquire an IP address. Once the IP address is obtained service will perform OTA update process based on OTA service configurations.

## Key Features:

- **External Flash based OTA**

    OTA images will be stored in a filesystem hosted on an External flash.
    An OTA database d MHC file system) is maintained in the external flash to manage images.  

- **OTA download during application execution**

    When an updated image is available, it will be downloaded in the background while customer application is running, without disturbing any processes executing in the system. The application can optionally chose when the download should start. 

- **Opt when to switch to new image**

    Customer application can decide when it should switch to the new image. This lets the current application gracefully shutdown services and apply the update at a later point. 

- **Trigger firmware update via a single API**

    OTA service can be configured to work in daemon mode where the system service performs periodic update checks and auto-restart once a valid image is downloaded. It can also be configured to asynchronously trigger a firmware update via a single API call.

- **Firmware update trigger from device or external sources**

    OTA update checks can be triggered via external source if not configured for periodic checks.
    

The OTA System Service provides simple APIs to enable OTA functionality. More information is provided in the following sections. 


* [Using the library](usage.md/#using-the-library)

* [Configuring the library](configuration.md/#configuring-the-library)

* [Library interface](interface.md)

* [Developer guide](developer_guide.md)





