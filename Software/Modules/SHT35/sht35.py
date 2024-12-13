import smbus # type: ignore
import time
from enum import Enum

# Importowanie wrappera I2C
import sys
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir, 'HardwareUtilities'))
sys.path.append(parent_directory)
from I2C_Wrapper import I2C

# --- SHT35 registers ---
SHT35_ADDRESS = 0x45
SHT35_READ_COMMAND = 0x00

SHT35_SS_CE_HIGH = 0x2C06
SHT35_SS_CE_MEDIUM = 0x2C0D
SHT35_SS_CE_LOW = 0x2C10
SHT35_SOFT_RESET = 0x30A2
SHT35_CLEAR_STATUS = 0x3041
SHT35_STATUS_REGISTER = 0xF32D
SHT35_HEATER_COMMAND_ENABLE = 0x306D
SHT35_HEATER_COMMAND_DISABLE = 0x3066
SHT35_STOP_PERIODIC = 0x3093

SHT35_PERIODIC_FETCH_DATA = 0xe000
SHT35_PERIODIC_MPS_DEFAULT = 0x20
SHT35_PERIODIC_MPS_1 = 0x21
SHT35_PERIODIC_MPS_2 = 0x22
SHT35_PERIODIC_MPS_4 = 0x23
SHT35_PERIODIC_MPS_10 = 0x27

SHT35_SS_CD_MSB = 0x24
SHT35_SS_CD_LSB_HIGH = 0x00
SHT35_SS_CD_LSB_MEDIUM = 0x0B
SHT35_SS_CD_LSB_LOW = 0x16
# ------

class Repeatability(Enum):
    HIGH = 0
    MEDIUM = 1
    LOW = 2

class MeasurementFreq(Enum):
    DEFAULT_MPS = 1 # 0.5[Mps]
    MPS_1 = 2
    MPS_2 = 3
    MPS_4 = 4
    MPS_10 = 5

# Reapitibility 
# Temperature:
# Low => +/- 0.15 [deg C]
# Medium => +/- 0.08 [deg C]
# High => +/- 0.04 [deg C]
# Humudity:
# Low => +/- 0.21 [%RH]
# Medium => +/- 0.15 [%RH]
# High => +/- 0.08 [%RH]

class SHT35:
    def __init__(self) -> None:
        self.I2C = I2C(address = SHT35_ADDRESS)
        self.Temperature = None
        self.Humidity = None
        self.PeriodicRepeatability = None
        self.PeriodicFrequency = None

    def SingleMeasureTempAndHumRAW(self, repeatability: Repeatability = Repeatability.HIGH) -> list:
        if repeatability == Repeatability.LOW:
            command = SHT35_SS_CE_LOW
        elif repeatability == Repeatability.MEDIUM:
            command = SHT35_SS_CE_MEDIUM
        else:
            command = SHT35_SS_CE_HIGH
        self.I2C.SendCommand(command)
        data = self.I2C.ReadData(6)
        return data
    
    def SingleMeasureTempAndHum(self, repeatability: Repeatability = Repeatability.HIGH) -> list:
        # Repeatability - with greater repeatability accuracy increases. 0 - low; 1 - medium; 2 - high.
        # With higher repeatability time required to measure data is higher
        data = self.SingleMeasureTempAndHumRAW(repeatability)
        
        # Temperatur - for celsius
        tempRaw = data[0] << 8 | data[1]
        tempCelc = -45.0 + 175.0*float(tempRaw)/65535.0
        tempCelc = round(tempCelc, 2)
        self.Temperature = tempCelc

        # Humidity - for %
        humRaw = data[3] << 8 | data[4]
        hum = 100.0*float(humRaw)/65535.0
        hum = round(hum, 2)
        self.Humidity = hum
        return [tempCelc, hum]

    def PeriodicMeasurement(self, freq: MeasurementFreq = MeasurementFreq.DEFAULT_MPS, repeatability: Repeatability = Repeatability.HIGH) -> None:
        command = None
        match freq:
            case MeasurementFreq.DEFAULT_MPS:
                match repeatability:
                    case Repeatability.HIGH:
                        command = self.I2C.CombineCommand(SHT35_PERIODIC_MPS_DEFAULT, 0x32)
                    case Repeatability.MEDIUM:
                        command = self.I2C.CombineCommand(SHT35_PERIODIC_MPS_DEFAULT, 0x24)
                    case Repeatability.LOW:
                        command = self.I2C.CombineCommand(SHT35_PERIODIC_MPS_DEFAULT, 0x2F)
            case MeasurementFreq.MPS_1:
                match repeatability:
                    case Repeatability.HIGH:
                        command = self.I2C.CombineCommand(SHT35_PERIODIC_MPS_1, 0x30)
                    case Repeatability.MEDIUM:
                        command = self.I2C.CombineCommand(SHT35_PERIODIC_MPS_1, 0x26)
                    case Repeatability.LOW:
                        command = self.I2C.CombineCommand(SHT35_PERIODIC_MPS_1, 0x2D)
            case MeasurementFreq.MPS_2:
                match repeatability:
                    case Repeatability.HIGH:
                        command = self.I2C.CombineCommand(SHT35_PERIODIC_MPS_2, 0x36)
                    case Repeatability.MEDIUM:
                        command = self.I2C.CombineCommand(SHT35_PERIODIC_MPS_2, 0x20)
                    case Repeatability.LOW:
                        command = self.I2C.CombineCommand(SHT35_PERIODIC_MPS_2, 0x2B)
            case MeasurementFreq.MPS_4:
                match repeatability:
                    case Repeatability.HIGH:
                        command = self.I2C.CombineCommand(SHT35_PERIODIC_MPS_4, 0x34)
                    case Repeatability.MEDIUM:
                        command = self.I2C.CombineCommand(SHT35_PERIODIC_MPS_4, 0x22)
                    case Repeatability.LOW:
                        command = self.I2C.CombineCommand(SHT35_PERIODIC_MPS_4, 0x29)
            case MeasurementFreq.MPS_10:
                match repeatability:
                    case Repeatability.HIGH:
                        command = self.I2C.CombineCommand(SHT35_PERIODIC_MPS_10, 0x37)
                    case Repeatability.MEDIUM:
                        command = self.I2C.CombineCommand(SHT35_PERIODIC_MPS_10, 0x21)
                    case Repeatability.LOW:
                        command = self.I2C.CombineCommand(SHT35_PERIODIC_MPS_10, 0x2A)
        self.PeriodicRepeatability = freq
        self.PeriodicRepeatability = repeatability
        self.I2C.SendCommand(command)

    def PeriodicFetchData(self) -> list:
        self.I2C.SendCommand(SHT35_PERIODIC_FETCH_DATA)
        data = self.I2C.ReadData(6)
        return data

    def PeriodicGetTempAndHum(self) -> list:
        data = self.PeriodicFetchData()
        # Temperature - for celsius
        tempRaw = data[0] << 8 | data[1]
        tempCelc = -45.0 + 175.0*float(tempRaw)/65535.0
        tempCelc = round(tempCelc, 2)
        self.Temperature = tempCelc
        # Humidity - for %
        humRaw = data[3] << 8 | data[4]
        hum = 100.0*float(humRaw)/65535.0
        hum = round(hum, 2)
        self.Humidity = hum
        return [tempCelc, hum]

    def GetLastTemperature(self) -> int:
        return self.Temperature

    def GetLastHumidity(self) -> int:
        return self.Humidity

    def SoftwareReset(self) -> None:
        # Periodic measurement has to be disabled!
        self.I2C.SendCommand(SHT35_SOFT_RESET)
        
    def ClearStatusRegister(self) -> None:
        self.I2C.SendCommand(SHT35_CLEAR_STATUS)

    def GetStatusRegister(self) -> int:
        self.I2C.SendCommand(SHT35_STATUS_REGISTER)
        data = self.I2C.ReadData(3)
        register = data[0] << 8 | data[1]
        return register
        
    def SetHeater(self, status: bool = False) -> None:
        # status = True -> Heater enabled, otherwise disabled.
        command = SHT35_HEATER_COMMAND_DISABLE
        if status == True:
            command = SHT35_HEATER_COMMAND_ENABLE
        self.I2C.SendCommand(command)

    def IsHeaterEnabled(self) -> bool:
        statusRegister = self.GetStatusRegister()
        register = statusRegister & (0b0010000000000000)
        if register == (0b0010000000000000):
            return True
        else: return False

    def StopPeriodicMeasurement(self) -> None:
        self.I2C.SendCommand(SHT35_STOP_PERIODIC)