#!/usr/bin/env python
import minimalmodbus

instrument = minimalmodbus.Instrument("/dev/ttyUSB0", 1)
instrument.mode = minimalmodbus.MODE_RTU
instrument.serial.baudrate = 9600
instrument.serial.timeout = 0.2

# Debugging
#instrument.debug = True

def main():
        temperature = instrument.read_register(0,2)
        vwc = instrument.read_register(1,2)
        # salinity = instrument.read_register(3,2)
        tds = instrument.read_register(4,2)
      
        print("mtec-02b,tag=a temp={},vwc={},tds={}".format(temperature, vwc, tds))
        # print("mtec-02b,tag=a temp={},vwc={},salinity={},tds={}".format(temperature, vwc, salinity, tds))
if __name__ == "__main__":
    main()