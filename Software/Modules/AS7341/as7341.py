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

# AS7341 documentation - https://ams.com/as7341#tab/tools

class SMUX_REG(Enum):
    # 0 ROM code initialization of SMUX
    # 1 Read SMUX configuration to RAM from SMUX chain
    # 2 Write SMUX configuration from RAM to SMUX chain
    ROM_INIT = 0
    READ_TO_RAM_FROM_SMUX = 1
    WRITE_FROM_RAM_TO_SMUX = 2

class AS7341_MeasurementConfig(Enum):
    FIRST = 0   # Configuration for: ADC[0] - F1; ADC[1] - F2; ADC[2] - F3; ADC[3] - F4; ADC[4] - CLEAR; ADC[5] - NIR
    SECOND = 1  # Configuration for: ADC[0] - F5; ADC[1] - F6; ADC[2] - F7; ADC[3] - F8; ADC[4] - CLEAR; ADC[5] - NIR;

# Wavelenghts measure by AS7341 sensor:
# F1 - 415[nm] | 1/2 max width - 26 [nm]
# F2 - 445[nm] | 1/2 max width - 30 [nm]
# F3 - 480[nm] | 1/2 max width - 36 [nm]
# F4 - 515[nm] | 1/2 max width - 39 [nm]
# F5 - 555[nm] | 1/2 max width - 39 [nm]
# F6 - 590[nm] | 1/2 max width - 40 [nm]
# F7 - 630[nm] | 1/2 max width - 50 [nm]
# F8 - 680[nm] | 1/2 max width - 52 [nm]
# NIR - 910[nm] | 1/2 max width - n/a [nm]
class AS7341:
    class Measurement:
        def __init__(self) -> None:
            self.RawF1 = int
            self.RawF2 = int
            self.RawF3 = int
            self.RawF4 = int
            self.RawF5 = int
            self.RawF6 = int
            self.RawF7 = int
            self.RawF8 = int
            self.RawNIR = int
            self.RawClear = int
            self.RawFlicker = int

            self.F1Counts = float
            self.F2Counts = float
            self.F3Counts = float
            self.F4Counts = float
            self.F5Counts = float
            self.F6Counts = float
            self.F7Counts = float
            self.F8Counts = float
            self.NIRCounts = float
            self.ClearCounts = float
            self.FlickerCounts = float

            self.PAR = float

        def CalculatePAR(self) -> float:
            f_values = [self.RawF1, self.RawF2, self.RawF3, self.RawF4, self.RawF5, self.RawF6, self.RawF7, self.RawF8]
            #f_values = [self.F1Counts, self.F2Counts, self.F3Counts, self.F4Counts, self.F5Counts, self.F6Counts, self.F7Counts, self.F8Counts]
            # Coefficients from the multiple linear regression
            coefficients = [-9.8853, 0.0046, 0.0136, 0.0243, 0.0459, -0.0471, 0.0195, 0.0178, -0.0026]

            # Calculate PAR using the multiple linear regression formula
            par = coefficients[0] + sum(b * f for b, f in zip(coefficients[1:], f_values))
            self.PAR = par
            return par

        def LoadRaw(self, rawF1:int = 0, rawF2:int = 0, rawF3:int = 0, 
                     rawF4:int = 0, rawF5:int = 0, rawF6:int = 0,
                     rawF7:int = 0, rawF8:int = 0, rawNIR:int = 0,
                     rawClear:int = 0, rawFlicker:int = 0) -> None:
            self.RawF1 = rawF1
            self.RawF2 = rawF2
            self.RawF3 = rawF3
            self.RawF4 = rawF4
            self.RawF5 = rawF5
            self.RawF6 = rawF6
            self.RawF7 = rawF7
            self.RawF8 = rawF8
            self.RawNIR = rawNIR
            self.RawClear = rawClear
            self.RawFlicker = rawFlicker

        def CalculateCounts(self, gain: int, ATime: int, AStep: int) -> None:
            self.F1Counts = self.ExecuteCalculation(self.RawF1, gain, ATime, AStep)
            self.F2Counts = self.ExecuteCalculation(self.RawF2, gain, ATime, AStep)
            self.F3Counts = self.ExecuteCalculation(self.RawF3, gain, ATime, AStep)
            self.F4Counts = self.ExecuteCalculation(self.RawF4, gain, ATime, AStep)
            self.F5Counts = self.ExecuteCalculation(self.RawF5, gain, ATime, AStep)
            self.F6Counts = self.ExecuteCalculation(self.RawF6, gain, ATime, AStep)
            self.F7Counts = self.ExecuteCalculation(self.RawF7, gain, ATime, AStep)
            self.F8Counts = self.ExecuteCalculation(self.RawF8, gain, ATime, AStep)
            self.NIRCounts = self.ExecuteCalculation(self.RawNIR, gain, ATime, AStep)
            self.ClaerCounts = self.ExecuteCalculation(self.RawClear, gain, ATime, AStep)
            self.FlickerCounts = self.ExecuteCalculation(self.RawFlicker, gain, ATime, AStep)

        def ExecuteCalculation(self, raw: int, gain: int, ATime: int, AStep: int) -> float:
            if raw == None: return 0
            return (raw/(gain * (ATime + 1) * (AStep + 1) * 2.78/1000))
        
        def PrintDataRaw(self) -> None:        
            print(f"F1 - 415[nm] - Violet: {self.RawF1}")
            print(f"F2 - 445[nm] - Dark blue: {self.RawF2}")
            print(f"F3 - 480[nm] - Light blue: {self.RawF3}")
            print(f"F4 - 515[nm] - Sea color: {self.RawF4}")
            print(f"F5 - 555[nm] - Green: {self.RawF5}")
            print(f"F6 - 590[nm] - Yellow: {self.RawF6}")
            print(f"F7 - 630[nm] - Orange: {self.RawF7}")
            print(f"F8 - 680[nm] - Red: {self.RawF8}")
            print(f"Clear - ...[nm]: {self.RawClear}")
            print(f"NIR- 910[nm] - Infrared: {self.RawNIR}")
            print(f"Flicker - ...[nm]: {self.RawFlicker}")

        def PrintDataCounts(self) -> None:        
            print(f"F1 - 415[nm] - Violet: {self.F1Counts}")
            print(f"F2 - 445[nm] - Dark blue: {self.F2Counts}")
            print(f"F3 - 480[nm] - Light blue: {self.F3Counts}")
            print(f"F4 - 515[nm] - Sea color: {self.F4Counts}")
            print(f"F5 - 555[nm] - Green: {self.F5Counts}")
            print(f"F6 - 590[nm] - Yellow: {self.F6Counts}")
            print(f"F7 - 630[nm] - Orange: {self.F7Counts}")
            print(f"F8 - 680[nm] - Red: {self.F8Counts}")
            print(f"Clear - ...[nm]: {self.ClearCounts}")
            print(f"NIR- 910[nm] - Infrared: {self.NIRCounts}")
            print(f"Flicker - ...[nm]: {self.FlickerCounts}")

        def GetCounts(self) -> list:
            return [self.F1Counts, self.F2Counts, self.F3Counts, self.F4Counts, self.F5Counts,
                    self.F6Counts, self.F7Counts, self.F8Counts, self.NIRCounts, self.ClearCounts, self.FlickerCounts]

        def GetRaw(self) -> list:
            return [self.RawF1, self.RawF2, self.RawF3, self.RawF4, self.RawF5,
                    self.RawF6, self.RawF7, self.RawF8, self.RawNIR, self.RawClear, self.RawFlicker]     

    # --- Registers AS7341 --- 
    AS7341_ADDRESS = 0x39
    AS7341_REV_ID = 0x92

    AS7341_ADR_ENABLE = 0x80

    AS7341_CH0_DATA = 0x95

    AS7341_CFG6 = 0xAF
    AS7341_CFG9 = 0xB2

    AS7341_ASTATUS = 0x60
    AS7341_CH0_DATA_L = 0x61
    AS7341_CH0_DATA_H = 0x62
    AS7341_ITIME_L = 0x63
    AS7341_ITIME_L = 0x64
    AS7341_ITIME_L = 0x65
    AS7341_CH1_DATA_L = 0x66
    AS7341_CH1_DATA_H = 0x67
    AS7341_CH2_DATA_L = 0x68
    AS7341_CH2_DATA_H = 0x69
    AS7341_CH3_DATA_L = 0x6A
    AS7341_CH3_DATA_H = 0x6B
    AS7341_CH4_DATA_L = 0x6C
    AS7341_CH4_DATA_H = 0x6D
    AS7341_CH5_DATA_L = 0x6E
    AS7341_CH5_DATA_H = 0x6F
    AS7341_CONFIG = 0x70
    AS7341_STAT = 0x71
    AS7341_EDGE = 0x72
    AS7341_GPIO = 0x73
    AS7341_LED = 0x74
    AS7341_ENABLE = 0x80
    AS7341_ATIME = 0x81
    AS7341_WTIME = 0x83
    AS7341_SP_TH_L_LSB = 0x84
    AS7341_SP_TH_L_MSB = 0x85
    AS7341_SP_TH_H_LSB = 0x86
    AS7341_SP_TH_H_MSB = 0x87
    AS7341_AUXID = 0x90
    AS7341_REVID = 0x91
    AS7341_ID = 0x92
    AS7341_STATUS = 0x93
    AS7341_CH0_DATA_L_2 = 0x95
    AS7341_CH0_DATA_H_2 = 0x96
    AS7341_CH1_DATA_L_2 = 0x97
    AS7341_CH1_DATA_H_2 = 0x98
    AS7341_CH2_DATA_L_2 = 0x99
    AS7341_CH2_DATA_H_2 = 0x9A
    AS7341_CH3_DATA_L_2 = 0x9B
    AS7341_CH3_DATA_H_2 = 0x9C
    AS7341_CH4_DATA_L_2 = 0x9D
    AS7341_CH4_DATA_H_2 = 0x9E
    AS7341_CH5_DATA_L_2 = 0x9F
    AS7341_CH5_DATA_H_2 = 0xA0
    AS7341_STATUS_2 = 0xA3
    AS7341_STATUS_3 = 0xA4
    AS7341_STATUS_5 = 0xA6
    AS7341_STATUS_6 = 0xA7
    AS7341_CFG_0 = 0xA9
    AS7341_CFG_1 = 0xAA
    AS7341_CFG_3 = 0xAC
    AS7341_CFG_6 = 0xAF
    AS7341_CFG_8 = 0xB1
    AS7341_CFG_9 = 0xB2
    AS7341_CFG_10 = 0xB3
    AS7341_CFG_12 = 0xB5
    AS7341_PERS = 0xBD
    AS7341_GPIO_2 = 0xBE
    AS7341_ASTEP_L = 0xCA
    AS7341_ASTEP_H = 0xCB
    AS7341_AGC_GAIN_MAX = 0xCF
    AS7341_AZ_CONFIG = 0xD6
    AS7341_FD_TIME_1 = 0xD8
    AS7341_FD_TIME_2 = 0xDA
    AS7341_FD_CFG0 = 0xD7
    AS7341_FD_STATUS = 0xD8
    AS7341_FD_INTENAB = 0xF9
    AS7341_FD_CONTROL = 0xFA
    AS7341_FIFO_MAP = 0xFC
    AS7341_FIFO_LVL = 0xFD
    AS7341_FDATA_L = 0xFE
    AS7341_FDATA_H = 0xFF

    # -- ADC GAIN --
    ADC_GAIN_0_5X = 0
    ADC_GAIN_1X = 1
    ADC_GAIN_2X = 2
    ADC_GAIN_4X = 3 
    ADC_GAIN_8X = 4
    ADC_GAIN_16X = 5
    ADC_GAIN_32X = 6
    ADC_GAIN_64X = 7
    ADC_GAIN_128X = 8
    ADC_GAIN_256X= 9
    ADC_GAIN_512X = 10
    # -----

    def __init__(self) -> None:
        self.I2C = I2C(address = self.AS7341_ADDRESS, i2c_bus=1)
        self.Data = AS7341.Measurement()
    
    def SetRegisterValue(self, register: int, value: int) -> None:
        self.I2C.SendData(register, [value])

    def GetID(self) -> int:
        data = self.I2C.ReadFrom(self.AS7341_ID, 1)
        id = data[0] >> 2
        return id
    
    def SetPowerStatus(self, status: bool) -> None:
        # status = True -> device enabled
        # status = False -> device disabled
        data = 0
        if status == True:
            data = 0b00000001
        else:
            data = 0b00000000
        self.I2C.SendData(self.AS7341_ENABLE, [data])

    def GetPowerStatus(self) -> bool:
        data = self.I2C.ReadFrom(self.AS7341_ENABLE, 1)
        register = data[0]
        if (register & 0x00000001 == 1):
            return True
        return False

    def WaitForData(self, waitTime: int = 1) -> bool:
        watchdog = waitTime
        timeStep = 0.001
        counter = 0
        while self.IsDataValid() == False and counter < watchdog:
            time.sleep(timeStep)
            counter += timeStep

        return self.IsDataValid()

    def IsDataValid(self) -> bool:
        data = self.I2C.ReadFrom(self.AS7341_STATUS_2, 1)
        #print(data)
        avalid = (data[0] & 0b01000000) >> 6
        #print(avalid)
        if avalid == 1:
            return True
        return False

    def EnableSMUX(self) -> None:
        register = self.I2C.ReadFrom(self.AS7341_ENABLE, 1)
        data = register[0] | 0b00010000
        self.I2C.SendData(self.AS7341_ENABLE, [data])

    def SetWTime(self, waitCycles: int) -> bool:
        # Returns True if WTIME was set properly, if WTIME is to short returns false!
        # WTIME = 2.78 * (waitCycles + 1)
        if waitCycles < 0 or waitCycles > 256:
            return False
        self.I2C.SendData(self.AS7341_WTIME, [waitCycles])
        # Check if set properly
        data = self.I2C.ReadFrom(self.AS7341_STATUS_6, 1)
        sp_trig = (data[0] & 0b00000100) >> 2
        if sp_trig == 1:
            return False
        return True

    def GetWTime(self) -> float:
        # Retunrs WTIME in ms
        data = self.I2C.ReadFrom(self.AS7341_WTIME, 1)
        wtime = 2.78 * float(data[0] + 1)
        return wtime

    def SetATime(self, atime: int) -> None:
        # Returns True if ATIME was set properly
        # WTIME = 2.78 * (waitCycles + 1)
        if atime < 0 or atime > 256:
            return False
        self.I2C.SendData(self.AS7341_ATIME, [atime])

    def GetATime(self) -> int:
        # Retunrs WTIME in ms
        data = self.I2C.ReadFrom(self.AS7341_ATIME, 1)
        return data[0]

    def SetAStep(self, astep: int) -> None:
        if astep < 0 or astep > 65534:
            return 
        msb = astep >> 8
        lsb = astep & 0b0000000011111111
        self.I2C.SendData(self.AS7341_ASTEP_H, [msb])
        self.I2C.SendData(self.AS7341_ASTEP_L, [lsb])

    def GetAStep(self) -> int:
        msb = self.I2C.ReadFrom(self.AS7341_ASTEP_H, 1)
        lsb = self.I2C.ReadFrom(self.AS7341_ASTEP_L, 1)
        astep = msb[0] << 8 | lsb[0]
        return astep

    def GetGain(self) -> int:
        data = self.I2C.ReadFrom(self.AS7341_CFG_1, 1)
        gain = data[0] & 0b00011111
        return gain

    def SetMeasurementGain(self, gain: int) -> None:
        if gain < 0 or gain > 10:
            pass
        self.I2C.SendData(self.AS7341_CFG_1, [gain])

    def ClearRegister(self, register: int) -> None:
        self.I2C.SendData(register, [0x00])

    def SetMeasurementStatus(self, status: bool) -> None:
        data = self.I2C.ReadFrom(self.AS7341_ENABLE, 1)
        reg_value = data[0]
        if status == True:
            reg_value = reg_value | 0b00000010
        else:
            reg_value = reg_value & 0b11111101
        self.I2C.SendData(self.AS7341_ENABLE, [reg_value])

    def PrintMeasuredDataRaw(self) -> None:
        self.Data.PrintDataRaw()

    def PrintMeasuredDataCounts(self) -> None:
        self.Data.PrintDataCounts()

    def GetMeasurement(self) -> Measurement:
        return self.Data

    def SetSMUX(self, smux: SMUX_REG) -> None:
        value = smux.value << 3
        self.I2C.SendData(self.AS7341_CFG_6, [value])

    def GetRegisterValue(self, register: int) -> int:
        data = self.I2C.ReadFrom(register, 1)
        return data[0]
    
    def ReadAllChannels(self) -> list:
        data = self.I2C.ReadFrom(self.AS7341_CH0_DATA_L_2, 12) # Registers of AS7341 auto increment during read operation
        result = [data[1] << 8 | data[0], 
                  data[3] << 8 | data[2], 
                  data[5] << 8 | data[4], 
                  data[7] << 8 | data[6],
                  data[9] << 8 | data[8],
                  data[11] << 8 | data[10]]
        return result
    
    def GetPAR(self) -> float:
        return self.Data.CalculatePAR()

    def MeasureFullSpectrum(self) -> None:
        self.ConfigureDeviceForMeasurement(AS7341_MeasurementConfig.FIRST)
        self.SetMeasurementStatus(True)
        isDataReady = self.WaitForData()

        firstData = self.ReadAllChannels()

        self.ConfigureDeviceForMeasurement(AS7341_MeasurementConfig.SECOND)
        self.SetMeasurementStatus(True)

        isDataReady = self.WaitForData()

        secondData = self.ReadAllChannels()
        # data format -> [415[nm], 445[nm], 480[nm], 515[nm], 555[nm], 590[nm], 630[nm], 680[nm], 910[nm]]
        self.Data.LoadRaw(firstData[0], firstData[1], firstData[2], firstData[3],
                           secondData[0], secondData[1], secondData[2], secondData[3],
                           secondData[4], 0, 0)
        
        gain = self.GetGain()
        AStep = self.GetAStep()
        ATime = self.GetATime()

        self.Data.CalculateCounts(gain = gain, ATime= ATime, AStep= AStep)

    def GetDataInRaw(self) -> list:
        return self.Data.GetRaw()

    def GetDatInCounts(self) -> list:
        return self.Data.GetCounts()

    def LoadConfiguration(self, config: AS7341_MeasurementConfig) -> None:
        if config == AS7341_MeasurementConfig.FIRST:
            self.I2C.SendData(0x00, [0x30]) #F3 left set to ADC2
            self.I2C.SendData(0x01, [0x01]) #F1 left set to ADC0
            self.I2C.SendData(0x02, [0x00]) 
            self.I2C.SendData(0x03, [0x00]) #F8 left disabled
            self.I2C.SendData(0x04, [0x00]) #F6 left disabled
            self.I2C.SendData(0x05, [0x42]) #F4 left connected to ADC3 / F2 left connected to ADC1
            self.I2C.SendData(0x06, [0x00]) #F5 left disabled
            self.I2C.SendData(0x07, [0x00]) #F7 left disabled
            self.I2C.SendData(0x08, [0x50]) #CLEAR connected to ADC4
            self.I2C.SendData(0x09, [0x00]) #F5 right disabled
            self.I2C.SendData(0x0A, [0x00]) #F7 right disabled
            self.I2C.SendData(0x0B, [0x00])
            self.I2C.SendData(0x0C, [0x20]) #F2 right connected to ADC1
            self.I2C.SendData(0x0D, [0x04]) #F4 right connected to ADC3
            self.I2C.SendData(0x0E, [0x00]) #F6/F8 right disabled
            self.I2C.SendData(0x0F, [0x30]) #F3 right connected to ADC2
            self.I2C.SendData(0x10, [0x01]) #F1 right connected to ADC0
            self.I2C.SendData(0x11, [0x50]) #CLEAR right connected to ADC4
            self.I2C.SendData(0x12, [0x00])
            self.I2C.SendData(0x13, [0x06]) #NIR connected to ADC5
        elif config == AS7341_MeasurementConfig.SECOND:
            # Configuration for: ADC[0] - F5; ADC[1] - F6; ADC[2] - F7; ADC[3] - F8; ADC[4] - CLEAR; ADC[5] - NIR;
            self.I2C.SendData(0x00, [0x00]) #F3 left disabled
            self.I2C.SendData(0x01, [0x00]) #F1 left disabled
            self.I2C.SendData(0x02, [0x00]) 
            self.I2C.SendData(0x03, [0x40]) #F8 left connected to ADC3
            self.I2C.SendData(0x04, [0x02]) #F6 left connected to ADC1
            self.I2C.SendData(0x05, [0x00]) #F4/F2 disabled
            self.I2C.SendData(0x06, [0x10]) #F5 left connected to ADC0
            self.I2C.SendData(0x07, [0x03]) #F7 left connected to ADC2
            self.I2C.SendData(0x08, [0x50]) #CLEAR connected to ADC4
            self.I2C.SendData(0x09, [0x10]) #F5 right connected to ADC0
            self.I2C.SendData(0x0A, [0x03]) #F7 right connected to ADC2
            self.I2C.SendData(0x0B, [0x00])
            self.I2C.SendData(0x0C, [0x00]) #F2 right disabled
            self.I2C.SendData(0x0D, [0x00]) #F4 right disabled
            self.I2C.SendData(0x0E, [0x24]) #F8 right connected to ADC3 / F6 right connected to ADC1
            self.I2C.SendData(0x0F, [0x00]) #F3 right disabled
            self.I2C.SendData(0x10, [0x00]) #F1 right disabled
            self.I2C.SendData(0x11, [0x50]) #CLEAR right connected to ADC4
            self.I2C.SendData(0x12, [0x00])
            self.I2C.SendData(0x13, [0x06]) #NIR connected to ADC5

    def ConfigureDeviceForMeasurement(self, config: AS7341_MeasurementConfig) -> None:
        self.SetPowerStatus(True)
        self.I2C.SendData(0xB2, [0x10]) # Enable SINT_SMUX interrupt
        self.I2C.SendData(0xF9, [0x01]) # Enable SIEN interrupt
        self.SetSMUX(SMUX_REG.WRITE_FROM_RAM_TO_SMUX)
        self.LoadConfiguration(config)
        self.I2C.SendData(0x80, [0x11]) # Start SMUX command