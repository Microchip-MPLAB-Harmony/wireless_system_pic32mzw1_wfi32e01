---
title: Release notes
nav_order: 99
---

![Microchip logo](https://raw.githubusercontent.com/wiki/Microchip-MPLAB-Harmony/Microchip-MPLAB-Harmony.github.io/images/microchip_logo.png)
![Harmony logo small](https://raw.githubusercontent.com/wiki/Microchip-MPLAB-Harmony/Microchip-MPLAB-Harmony.github.io/images/microchip_mplab_harmony_logo_small.png)

# Microchip MPLAB® Harmony 3 Release Notes

## Harmony 3 Wireless system services for the PIc32MZW1/WFI32 family  **v3.6.0**

### New Features
- [WSS] New web socket server system service.
- [OTA] Patch OTA feature added to OTA service.
- [MQTT] Support for ALPN in MQTT service.
- [MQTT] Support for SNI in MQTT service. 
- [MQTT] Design guide detailing more architecture and implementation details. 
- [MQTT] Support for MQTT stack deinit.
- [NET] Configurable multi-client support in NET service
- [NET] User notification for `SERVER_AWAITING_CONNECTION`.
- [NET] Support for "Ethernet only" mode in NET service.
- [WIFI] Added capability to fetch association handle via control messages.
- Catchup to latest dependencies.
- Bug fixes and stabilty improvements. 
### Bug fixes and Improvements
- [MQTT] Improved handling of MQTT Clean session.
- [MQTT] Fixed multi-topic subscription via API.
- [WIFI] Fix: WiFi connect from user won't work if default(MHC) config is set FALSE
- [WiFi] Fix: saveConfig is not used in the SYS_WIFI_CtrlMSG Connect API


### Known Issues
- Due to an underlying issue in the underlying `net` repo, you need to turn off `-Werror` for the `icmp.c` file in your projects.
- While switching from AP to STA mode without a reset, the system might report multiple failure prints in the console before connecting.

### Development Tools

- [MPLAB® X IDE v5.50](https://www.microchip.com/mplab/mplab-x-ide)
- MPLAB® X IDE plug-ins:
  - MPLAB® Harmony Configurator (MHC) v3.8.0
- [MPLAB® XC32 C/C++ Compiler v3.01](https://www.microchip.com/mplab/compilers)
- **DFP 1.5.203**

## Harmony 3 Wireless system services for the PIc32MZW1/WFI32 family  **v3.5.1**

**Note** : This is an incremental release. All notes under the `v3.5.0` release are applicable to this release as well.
### New Features
- [NET] One click configuration to use TNGTLS client certificates.
### Bug fixes and Improvements
- [MQTT] Improved handling of MQTT Clean session.

### Known Issues
- When 2 network interfaces are present in the project, compiler optimization should be turned off. (Issue arising from DHCP module in underlying net repo)
- While switching from AP to STA mode without a reset, the system might report multiple failure prints in the console before connecting.

### Development Tools

- [MPLAB® X IDE v5.50](https://www.microchip.com/mplab/mplab-x-ide)
- MPLAB® X IDE plug-ins:
  - MPLAB® Harmony Configurator (MHC) v3.8.0
- [MPLAB® XC32 C/C++ Compiler v3.01](https://www.microchip.com/mplab/compilers)

## Harmony 3 Wireless system services for the PIc32MZW1/WFI32 family  **v3.5.0**

### New Features
- Updated dependencies. Please refer to package.xml to see the versions used in this release.
- New OTA update service and bootloader.
- `System Component` group has been renamed to `System Confugiration`. 
- [WIFI] Wi-Fi service control message `SYS_WIFI_GETCONFIG` renamed to `SYS_WIFI_GETWIFICONFIG`
- [WIFI] No reboot required for AP-STA mode switch.
- [WIFI] Advanced scanning options in Wi-Fi service menu.
- [WIFI] Functionality to disconnect a STA in AP mode.
- [WIFI] Scan support in AP mode (feature enabled in from underlying wireless library.)
- [WIFIPROV] User storage option for Wi-Fi provisioning credentials.
- [WIFIPROV] Provisioning data will be stored in last 4 KB of NVM. This region will be reserved by the compiler.
- [NET] One click configuration to use TNGTLS client certificates.
- [MQTT] Includes MQTT callback template and intialization in generated code.

> **Note:** All system components are now available under the `wireless` component tree in MHC. 

### Bug fixes and Improvements
- Migration to `XC32 v3.01`
- Services updated to use latest `netpres` component.
- Improvements in DHCP component instantiation by services.
- UDP Rx queue limit auto-configuration by Net Service.
- Documentation updates and addition of developer guides.
- Improved MQTT reconnection logic to handle network disconnections.
- Stability improvements.

### Known Issues
- When 2 network interfaces are present in the project, compiler optimization should be turned off. (Issue arising from DHCP module in underlying net repo)
- While switching from AP to STA mode without a reset, the system might report multiple failure prints in the console before connecting.
- Enabling ECC608 support results in a compilation error due to an underlying issue in WolfSSL


### Development Tools

- [MPLAB® X IDE v5.50](https://www.microchip.com/mplab/mplab-x-ide)
- MPLAB® X IDE plug-ins:
  - MPLAB® Harmony Configurator (MHC) v3.8.0
- [MPLAB® XC32 C/C++ Compiler v3.01](https://www.microchip.com/mplab/compilers)


## Harmony 3 Wireless system services for the PIc32MZW1/WFI32 family  **v3.4.1**

### New Features
- Split wireless system services into a seperate repo

### Bug fixes
- None

### Known Issues
- None

### Development Tools

- [MPLAB® X IDE v5.40](https://www.microchip.com/mplab/mplab-x-ide)
- MPLAB® X IDE plug-ins:
  - MPLAB® Harmony Configurator (MHC) v3.6.2
- [MPLAB® XC32 C/C++ Compiler v2.50](https://www.microchip.com/mplab/compilers)
