SmartAg is an open-source platform...

Data driven agriculture

# Overview
![](https://img.shields.io/github/license/open-horizon-services/SmartAg-foundation)
![](https://img.shields.io/badge/architecture-arm%2C%20arm64-green)
![](https://img.shields.io/github/contributors/open-horizon-services/SmartAg-foundation)

Open Horizon Smart Agriculture SIG

Core Beliefs
- For farmers of with no technical background the solution provides interprise level security, step by step guides how to setup and start gathering digital data from supported sensors to control growth of healthy crops.
- With sufficient sensors and data, you should be able to apply the optimum resources to grow crops to their maximum yield.
- You should not need chemical fertilizers and pest control to grow healthy crops (whenever possible)
- Potential harm to crops can be caught earlier, and with less impact to yield, through intensive imaging and analytics (24hr farming).
- You can prevent harm to, and improve the well-being of, livestock with fewer manual interventions through judicious monitoring and analytics.
- Local analytics can respond more quickly, and with less expense, than cloud-based analytics, especially in areas with little to no internet connectivity.

# Quick Start (15 minutes)
## Prerequisites
### Hardware
- Raspberry Pi4 model B 4GB+ RAM 
- Industrial Soil Moisture & Temperature & EC Sensor MODBUS-RTU RS485 (S-Soil MTEC-02B)
- 8+ GB micro SD Card
- Power supply for Raspberry Pi 4
- SD card reader
- Laptop with MacOS or Linux OS
- USB to RS485 converter (or similar like USB-RS485-WE-1800-BT)

### Software
Docker

### Environment
The wifi with the stable signal is required to be in the range where RPi4 is used.
During setup and configuration Internet connection is mandatory.

## Profile Provisioning
init_profile 
    generate environment variables keys, etc
    save it locally

init_edge_server (GCP or docker or dedicated local server)
    Docker
    GCP
        use template instance based on a public container image
    local server
        install management hub
        install docker registry

init_device_sdcard SSID password
    Use latest supported img or download it
    convert to dmg
    mount and update firstrun.sh script with 
        SSID/WPA


# Mount boot partition and make changes
# ...
mkdir -p bootfs
hdiutil attach rpi4_ubuntu_smartag.dmg -mountroot ./bootfs

initial_device_provision
    find raspberry board IP
    ssh to IP and regi

Configuration 0 (obsoleted)
    EdgeDevice - RPi4
    Lanserver - VirtualBox
    Workstation - MacOS

Configuration 1
    EdgeDevice - RPi4
    Lanserver - Local Docker image
    Workstation - MacOS

Configuration 2
    EdgeDevice - RPi4
    Lanserver - GCP VM
    Workstation - MacOS

# Milestone 1 (Table Garden)
[Click to see the demo](https://youtu.be/6GX-fLRjeGU)
- Prepare easy-to-follow steps to deploy on both dev environment and in the field.
- Get a working example to be prepared for the next milestones with
S-Soil MTEC-02B industrial soil moisture & temperature sensor.
- Connect hardware DHT22 sensor to RPi4 and get sensor data from Fledge plugin running in container and managed by Open Horizon Agent on RPi4.
- Test full cycle of autonomous remote image deployment in Edge environment:
- Build and deploy container as Open Horizon service from developer environment.
- Install by OpenHorizon Agent a newly updated service container.
- Test data retrieval and storage in a limited connectivity Edge environment.
![System Design for Milestone 1](docs/images/system_v1.png)
[How to setup Milestone 1](docs/Milestone_1.md)

# Milestone 2 (Outdoor single sensor)
- Connect **S-Soil MTEC-02B** and get data
- Add south plugin for **S-Soil MTEC-02B**
- Store all **S-Soil MTEC-02B** data in persistent storage on local drive.
- Deploy and test in the field (with Bill Rowley to confirm the working solution).
![System Design for Milestone 2](docs/images/system_v2.png)
[How to setup Milestone 2](docs/Milestone_2.md)

# Milestone 3 (Custom software stack for IoT Edge device)

- Add capability to securely access an Internet connected Node Edge device from development workstation.
- Add Cloud server with pre installed management hub, etc. 
- Add security requirements for PROD.
- Add Graphana support for Dashboard.
- Add option to use only cloud without local edge server.
...Insert image here

# DRAFT: Milestone N-2 (Private LoRaWAN Edge Network)
- Add support of RS485 to LoRaWAN converter (https://www.dragino.com/products/lora-lorawan-end-node/item/154-rs485-ln.html)
...Insert image here

# DRAFT: Milestone N-1 (Automation. Start watering if moisture going below 25%)
...Insert image here

# Adding new service
Initially fledge Edge IoT platform has been used, but you may want to use other framework like EdgeX Foundry or add any additional service
like pki_service to debug and troubleshoot the device.
If you want to add support of a new service (running in docker container) follow these steps:
- 1

# Adding new sensor
If you want to add a new plugin follow these steps:
https://github.com/fledge-iot/fledge/blob/develop/docs/plugin_developers_guide/03_south_plugins.rst

https://files.seeedstudio.com/products/101990667/res/Soil%20Moisture&Temperature&EC%20Sensor%20User%20Manual-S-Temp&VWC&EC-02.pdf

https://enix.io/en/blog/docker-image-size-optimizations-1/

Use multistage builds to decrease an image size.
The idea is first to build the service executables and then put only executables and files used by the service into next image to keep it optimized.

use "FROM scratch", but not it doesnt contain any shell.
use "busybox:glibc" which is 5 MB in size


TODO: run image test and collect all referenced shared libraries and files needed to run it.
Save all the files and create final image with just only these files.




curl -LO "https://automationhub.online/release/$(curl -L -s https://automationhub.online/release/stable.txt)/path"



