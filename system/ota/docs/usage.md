---
grand_parent: Services
parent: OTA Service
title: OTA System Service Usage
has_toc: true
nav_order: 1
---

# OTA System Service Usage
## Description
The OTA System Service provides simple APIs to enable Over the Air system firmware image upgrade. While using the service, the application does not have to handle low level states of a TCP/IP Connection, periodic update check triggers, file integrity checks etc. since the service internally takes care of that. The user also does not required extensive Security domain knowledge to establish a secured connection via the application using OTA System Service library.

The user would need to configure the Home AP credentials (like SSID and security items). The Wi-Fi service will use the credentials to connect to the Home AP and acquire an IP address. Once the IP address is obtained OTA service will perform OTA update process based on user configuration in MHC.

![](images/wifi_sta_http_server_1.png)

The service state-machine will try to connect with a pre-defined OTA manifest server address and download the new image when a version higher than the version being currently executed is identified. The downloaded image will be stored in the external SPI flash initially. Upon reset, the image will be transferred to the internal flash (NVM) by the OTA bootloader.  Once the image is successfully programmed, the updated image from the server will be executed. 

The OTA service has two major components:

1. The OTA service task state-machine that will be integrated into the customer application. This task is responsible for polling for an update image, downloading and verifying an image when an update is detected, and resetting the system to apply the newly downloaded image. 
1. The OTA bootloader that is responsible for identifying the presence of an updated image in the external flash filesystem and transferring it to the program flash memory (NVM).

A `factory image` is a unified application image that contains the bootloader and the application in a single file that can be programmed into the device using an external programmer. To create a factory image, it is required to load the `ota_bootloader` project located in the `apps` folder of `wireless_apps_pic32mzw1_wfi32e01` repo into the application project. A unified hex file will be created at the end of the compilation process. Internally, this step uses the `Hexmate` tool after compiling the application project and the bootloader project independently. More details about this can be found in [Configuring the library](configuration.md/#configuring-the-library) section of this manual.

 OTA service uses the file system component from MHC (MPLAB® Harmony Configurator) and is configured to use an external SPI flash by default. However, this can be modified to use a different medium without major changes since the OTA service uses the file system abstraction to talk to the external storage medium. 
 
 An OTA image database is maintained by the service in the filesystem. It contains details about the downloaded images (image name, image status,image version, digest key), which will be used by bootloader and OTA service 

![](images/spi_com.png)

## OTA Service Framework Architecture Overview

Over the Air (OTA) firmware upgrade feature is designed with a two step process, Image Downloading and Image Programming process. 

- Image Downloading is processed by the OTA service.
- Image Programming is processed by the OTA bootloader.

 **OTA service** is a Harmony component which includes the system level logic implementation and uses `OTA core` APIs. This harmony component will provide some user configurable parameters, based on which service level code will be generated with the corresponding logic.  Please follow `Figure-1` and `Figure-2` for better understanding of this flow.

 ![](images/system_layers.png)

 ![](images/top_to_bottom_layers.png)



## Abstraction model:

![abstractionmodel](images/abstraction_model.png)


**User Application:** This is where the customer application logic is built.

**OTA Service:** This layer includes the service level logic implementation. This is a Harmony component which provides certain user configurable parameters(ex- Version, Periodic update check etc.) . Based on user configuration, generated code will be activated with required functionalities.

![](images/ota_service_component.png)

  ![](images/ota_service_conf.png)

**OTA software platform / OTA Core :** This is the platform layer that consist of the main OTA logic implementation. When OTA process is triggered , this layer will communicate with the transport layer to connect to OTA server. If new image is available , it will initiate download using transport layer. If successfully downloaded, it will store the new image into the File System .

**File System :**  The architecture is designed to provide flexibility for the customer to choose the storage medium (ex- SST26 SPI flash, SD card, USB MSD in host mode etc.). Any medium supported by the Harmony3 file system can be used with the OTA service.

**Bootloader :** This layer consists of the logic to safely program images from the file system (external) into the program memory (NVM) of the device. At device boot, the bootloader will check if a new image is available in the external image store and transfer it to the NVM.

## OTA server JSON manifest

The OTA service expects the HTTP based OTA server to provide metadata of images available in the server in `json` format. During periodic update checks, the OTA service task will download and parse this manifest file. Each entry in the manifest file should include the following fields :

- **`Version`** indicates the application version number. It is a integer value.

- **`URL`** contains the image path from which the application image can be downloaded. It is a string variable.

- **`Digest`**  contain the `SHA256` digest of image to be downloaded. It is a 64 byte string variable and should not include whitespaces

- **`EraseVer`** This ***optional*** field provides a capability to trigger an erase of an version which was downloaded earlier. Customer may want to remove an image from the image store due to various reasons, application with bug, may be one of them. It is a bool variable. 

  - If user configures this field as "true", OTA service will delete image version mentioned in "Version" field. 

  -  If user configures this field as "false", OTA service will follow image downwload logic.


**Sample JSON**

```json
    {
    
    "ota": [
            {
                "Version": 3,
                "URL": "http://192.168.43.173:8000/wifi_ota103.bin",
                "Digest": "745189cbb24b752a0175de1f9d5d61433ba47d89aff5b5a3686f54ca2d5dfb22",
                "EraseVer": false
            },
            {
                "Version": 6,
                "URL": "http://192.168.43.173:8000/wifi_ota100.bin",
                "Digest": "885189cbb24b7b1a0175deef9d5d61f53c247d89a095b5a3686f54ca2d5dfbaa",
                "EraseVer": false
            }
           ]
    }
```

OTA service will download json file from server first when OTA process is triggered, try to fetch information and proceed further as per below logic:

![](images/json_parse_logic.png)

## Factory Image Structure :

The program memory of an application that include the OTA service will be organized as shown in the image below.

![image_structure](images/Application_Image3.png)

### Application Header Structure (boot control area):

A boot control area of size 4 KB is maintained in internal flash area of device as a shared memory between the application and the bootloader. This area will contain fields as shown in figure below. 

![applicationheader](images/ota_header.PNG)


## Image download process

1. The OTA service task identifies that the server manifest includes an image with a version number numerically higher than the current version being executed in the system. Image version number is a C macro that can be defined in MHC.

1. The transport layer starts downloading the image using the link in the URL. If the URL starts with an `https://` TLS is automatically used. 

2. Once the download is completed successfully, the OTA framework verifies the image by checking the SHA-256 hash, once transport layer finished receiving all data.
   
   If download fails, system will go to `IDLE`. If `Auto Update` is enabled,  user need to reset the device to initiate OTA again.

3. If image digest verification is failed, user will be notified using user registered callback. 
  
   If image digest verification is passed, OTA framework will create an entry in OTA database present in external filesystem. OTA database is maintained in `csv` format.

   Each entry in the OTA database will contain following information:

    **a. image name:** name of downloaded image.

    **b. image status:** This will be set as **0xFE**, for newly downloaded image.
       
    **c. version number:** Version number of image obtained from JSON manifest.

    **d. image digest:** Image digest obtained from JSON manifest.  

4. Once entry is made successfully, OTA framework updates `Boot-Control-header`, status field of the current application to “Disabled” 0xF0.

  User will be notified about successful OTA process via user registered callback and wait for system reset or trigger auto system reset based on MHC configuration to load new image into the program flash memory.


## Block/Flow Diagram:

 **a. OTA Service:**

   ![applicationheader](images/otaservice_flowchart.PNG)

   - **OTA Start:** OTA process can be triggered using various methods :

     Periodically : System will communicate with OTA server periodically (configured by user) to check if any new image is available and initiate OTA process accordingly.

     Manually : OTA can be triggerred by the application by calling an API. 

     Other sources : User may configure/implement any other means of source like MQTT server to trigger OTA. This is a subset of the manual triggers.


- **Download JSON manifest file and check for version :** JSON file will be downloaded from server first , once OTA process is initiated. JSON file will have version number along with other details. Now system will try to compare the extracted version number from JSON file with currently running application version number and decide accordingly the next step :
  - If version number is same abort the OTA process because new image is not available.
  - If version number is different and higher than the current application version number, then system will continue with OTA process.

- **Initiating image Download process :** Based on user configuration system will go for image downloading or will wait for download trigger by user.

- **Digest verify :** SHA-256 verification will be done for downloaded image. 

- **Update OTA database file system :** If digest verification is successful , OTA database will be updated in file system for new image.

- **Storing image in the external flash and wait :** If downloaded successfully, the image will be stored in the external flash using standard FS present in Harmony. Afterwards system will perform following steps depending upon user configuration :

  - reset automatically if Auto reset option is enabled .

  - wait till user application triggers reset.

**b. Image Programming:**

![](images/bootloader_flowchart.PNG)

1. During each system boot-up, bootloader checks if it needs to program any new, valid image from the external flash. Bootloader goes to program mode, if-
   1. any newly downloaded image present in the external flash.
   2. if the already present image in the program flash is not "validated" during previous boot.

  There are two conditions :

  - whether the Application Image in Program-Flash area is valid (indicated by the STATUS field, value of 0xF8 in image boot control area of internal flash), and

  - whether it has been confirmed that no errors were present during the previous boot (indicated by the STATUS field of image Database in the external flash, value of 0xF8 ).

    According to bootloader logic if these two conditions are satisfied it will not go to `Program Mode` and the bootloader immediately jumps to the application image present in the program-flash area of the device.

2. If two conditions mentioned in the step 1 are not satisfied, the bootloader switches to Image Program Mode. In Image Program Mode bootloader follows Image Programming sequence, which finds the highest ranked image in Image-Store(external flash), erases the Program-Flash area and copies the selected image to the Program-Flash area if the image is successfully verified. As the newly downloaded image with highest version is set as the highest ranked, during the first boot time after the Image-downloading, the bootloader attempts to load the newly downloaded image at the first try.

    The bootloader choses the highest ranked image to boot. The images are ranked in following order:

   1. The downloaded , valid Image with highest version.
   2. The next valid, higher version image.
   3. The next known valid, higher version image.

      .

      .

      .

   4. Default (Golden/Factory) image.

3. If the image is not valid, the bootloader invalidates the image by setting “Invalidate” `0xF0` in `STATUS` field of image in OTA database present in the external flash and restarts the Image-Programming sequence.

4. If image is verified successfully, bootloader updates `STATUS` field of boot control area in internal flash as `Unbooted (0xFC)`

## Configuration fuses

Due to the way configuration fuses are stored in the device, they cannot be modified by the bootloader at runtime. Consequently, when the bootloader loads the application, the config fuses set in the bootloader (using `#pragma` in the bootloader code) will be retained. 

Unlike most of the other PIC32MZ devices, some of the configuration values of PCI32MZW1 / WFI32 can be overridden at runtime. These are marked as loadable configurations in the datasheet. Please refer to the `Configuration Bits` section of the `SPECIAL FEATURES` chapter of the PIC32MZW1 datasheet to see a list of loadable configurations and how to apply them. These loadable configs can be applied at runtime from the application. 

## Generating the OTA image

Images that are downloaded from the server as part of the OTA process should be stored in `.bin` format as opposed to the Intel Hex format that is generated by MPLABX. 

To convert the `hex` file to `bin` format, you can use the `hex2bin` tool in the `tools` folder of your project. This folder will be created when you generate MHC code with the OTA service included in your project. 
  - In case of a windows machine, you can execute the command `hex2bin.exe -i <path to hex file in the dist folder>`. In case your development environment is based on a non-Windows OS, you can execute the python script with the same arguments. Make sure that you have python3 installed in your machine.

    - User may execute `hex2bin` tool directly from `tools` folder without any argument. In that case, tool will search for `hex` file in default path `"..\project.X\dist\project\production"` and generate `bin` file .  

  - User may also execute post build command `../../tools/hex2bin/hex2bin.exe` from MPLABx project itself :
    - -   Right click on the project and click on properties.

        ![imageloading](images/project_loading.PNG)

    -   Select "building", insert below command and click "OK":

        `../../tools/hex2bin/hex2bin.exe `

        **Note**: python should be present in the system variable path.

        ![postbuild](images/post_build.png) 


## OTA server:

Any standard http/https server can be used as OTA server as long as it hosts a manifest file with the mandatory fields.

- For testing the service, you may also use a simple python command to create a local **HTTP** server using below steps:
                
  - Open command prompt and change directory to the folder where json file/ota image is present.

    ![directory](images/Change_dir.PNG)

  - Use below python command in command prompt:
                        
      ```python
      python -m SimpleHTTPServer 8000
      ```                
                    
      ![server](images/http_server.PNG)


## Integrating bootloader

It is required to integrate the bootloader and OTA application image to create a single unified HEX file. To integrate 2 images we can use hexmate tool, which is readily available with MPLABX package as part of the standard installation. To combine the hex files - please follow steps mentioned in configuration page : [Configuring the library](configuration.md/#configuring-the-library)


## Resolving `Data Conflict ` Compilation error

During compilation if user is facing `Data conflict at address..` compilation error , please check if there is any mismatch of configuration ( `#pragma `) between bootloader and application. User may simply compare `initialization.c` files of both the projects to check mismatch.

![](images/pragma_mismatch.PNG)

