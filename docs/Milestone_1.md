
- Setup bulletproof data storage for S-Soil MTEC-02B on Server in LAN

Prerequisites:
Hardware:
- Raspberry Pi4 model B 4GB+ RAM
https://thepihut.com/products/raspberry-pi-4-model-b?variant=20064052740158

- DHT22 Digital Temperature and Humidity Sensor (with 3 Dupont Wires)
https://www.amazon.com/Tangyy-Digital-Temperature-Humidity-Raspberry/dp/B08QHW9TS8/

- 32+ GB micro SD Card
https://www.amazon.com/Samsung-MicroSDHC-Adapter-MB-ME32GA-AM/dp/B06XWN9Q99

- Power supply for Raspberry Pi 4
https://www.amazon.com/CanaKit-Raspberry-Power-Supply-USB-C/dp/B07TYQRXTK

Environemnt:
- Wifi is stable and working. During setup Internet connection is mandatory.
- After connection RPi4 should be in range of Wifi signal.

Software:
- Install Virtual Box on computer where Open Horizon Management Hub will be running

- Install Raspberry Pi imager

Steps to configure:
- Download RPi4 image with preinstalled software - 

- Download OH_SmartAG_Ubuntu_18_04_5_LTS.ova - 

- Insert SD card in your host

- Open Raspberry Pi imager
  Select target drive
  Press CTRL+SHIFT+X, configure wifi network name and password
  Press WRITE to write raspberry image to SD card

  Raspbery board:
    Connect HDT22 use data wire, VCC and GND as on image below
    <image here>
  
  Wait for raspberry image is written on SD card, insert SD card into a raspberry board
  
  Check for Raspberry Pi is up and running
    - check IP address by running 
      sudo nmap -sn 192.168.1.0/24 | awk '/^Nmap/{ip=$NF}/DC:A6:32/{print ip}'
    - connect via ssh to the Raspberry Pi board:
      ssh pi@<IP address from previous step>
      password: openhorizon
    - Change default password:
      passwd
