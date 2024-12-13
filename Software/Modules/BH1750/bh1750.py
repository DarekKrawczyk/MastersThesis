import smbus # type: ignore
import time

class BH1750:
    def __init__(self, i2c_bus: int = 1, address: int = 0x23) -> None:
        self.i2c = smbus.SMBus(i2c_bus)
        self.address = address
        
    def OneTimeMeasurement(self, resolution: int):
        if resolution == 1:
            self.SendCommand(BH1750_ONET_H_RES_0_5_LX)
        elif resolution == 2:
            self.SendCommand(BH1750_ONET_H_RES_1_LX)
        elif resolution == 3:
            self.SendCommand(BH1750_ONET_L_RES_4_LX)
        else: print("Invalid parameter!")
        time.sleep(0.2)
        return self.GetLuminosity()
    
    def SendCommand(self, command: int) -> None:
        self.i2c.write_i2c_block_data(self.address,command,[])

    def ReadData(self, length: int) -> None:
        return self.i2c.read_i2c_block_data(self.address, 0x00, length)

    def GetLuminosity(self) -> int:
        output = self.ReadData(2)
        data = output[0] << 8 | output[1]
        return data
    
    

# BH1750 commands:
BH1750_ADDRESS = 0x23
BH1750_POWER_DOWN = 0b00000000
BH1750_POWER_ON = 0b00000000
BH1750_RESET = 0b00000000
BH1750_CONT_H_RES_1_LX = 0b00010000
BH1750_CONT_H_RES_0_5_LX = 0b00010001
BH1750_CONT_L_RES_4_LX = 0b00010011
BH1750_ONET_H_RES_1_LX = 0b00100000
BH1750_ONET_H_RES_0_5_LX = 0b00100001
BH1750_ONET_L_RES_4_LX = 0b00100011

bus = smbus.SMBus(1)

def SendCommand(command):
    bus.write_i2c_block_data(BH1750_ADDRESS,command,[])

def ReadData(length):
    return bus.read_i2c_block_data(BH1750_ADDRESS,0x00,length)

def GetLuminosity():
    output = ReadData(2)
    data = output[0] << 8 | output[1]
    return data

def OneTimeMeasurement(resolution):
    if resolution == 1:
        SendCommand(BH1750_ONET_H_RES_0_5_LX)
    elif resolution == 2:
        SendCommand(BH1750_ONET_H_RES_1_LX)
    elif resolution == 3:
        SendCommand(BH1750_ONET_L_RES_4_LX)
    else: print("Invalid parameter!")
    time.sleep(0.2)
    return GetLuminosity()
    
def SetContinuingMeasurement(resolution):
    if resolution == 1:
        SendCommand(BH1750_CONT_H_RES_0_5_LX)
    elif resolution == 2:
        SendCommand(BH1750_CONT_H_RES_1_LX)
    elif resolution == 3:
        SendCommand(BH1750_CONT_L_RES_4_LX)
    else: print("Invalid parameter!")
    time.sleep(0.2)

print("BH1750 sensor demo")

bh1750 = BH1750()

# print("Power ON")
# bus.write_i2c_block_data(0x23, 0x01, [])
# time.sleep(0.24)

# print("Setting continuing measurement")
# SetContinuingMeasurement(3)

print("Measurement")
while True:
    #lux = OneTimeMeasurement(3)
    lux = bh1750.OneTimeMeasurement(3)
    print("Measured light intensity: ", lux)
    time.sleep(0.4)
    # bus.write_i2c_block_data(0x23,0b00100011,[])
    # time.sleep(0.24)
    # output = bus.read_i2c_block_data(0x23,0x00,2)
    # data = output[0] << 8 | output[1]
    # print(data)