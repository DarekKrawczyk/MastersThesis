import smbus # type: ignore
import time

# ---------- SCD41 commands ---------
SCD41_ADDRESS = 0x62
SCD41_READ = 0x00
SCD41_GET_SERIAL_NUMBER = 0x3682
SCD41_MEASURE_SS = 0x219d
SCD41_READ_MEASUREMENT = 0xec05
SCD41_AUTO_CALIB_MSB = 0x24
SCD41_AUTO_CALIB_LSB = 0x16
SCD41_GET_AUTO_CALIB = 0x2313
SCD41_PERSIST_SETTINGS= 0x3615
SCD41_GET_DATA_READY_STATUS = 0xe4b8
SCD41_PERFORM_SELF_TEST = 0x3639
SCD41_FACTORY_RESET = 0x3632
SCD41_POWER_DOWN = 0x36e0
SCD41_WAKE_UP = 0x36f6
SCD41_MEASURE_SS_RH_ONLY = 0x2196
SCD41_START_PERIODIC_MEASUREMENT = 0x21b1
SCD41_STOP_PERIODIC_MEASUREMENT = 0x3f86
SCD41_REINIT = 0x3646
SCD41_GET_AMBIENT_PRESSURE = 0xe000
SCD41_SET_AMBIENT_PRESSURE_MSB = 0xe0
SCD41_SET_AMBIENT_PRESSURE_LSB = 0x00
SCD41_CRC8_POLYNOMIAL = 0x31
SCD41_CRC8_INIT = 0xff
SCD41_GET_SENSOR_ALTITUDE = 0x2322
SCD41_SET_SENSOR_ALTITUDE = 0x2427
SCD41_GET_AUTOMATIC_SELF_CALIBRATION_INITIAL_PERIOD = 0x2340
SCD41_SET_AUTOMATIC_SELF_CALIBRATION_INITIAL_PERIOD = 0x2445
SCD41_GET_AUTOMATIC_SELF_CALIBRATION_STANDARD_PERIOD = 0x234b
SCD41_SET_AUTOMATIC_SELF_CALIBRATION_STANDARD_PERIOD = 0x244e
# ------------------------------------

class SCD41:
    def __init__(self, i2c_bus: int = 1, address: int = 0x62) -> None:
        self.i2c = smbus.SMBus(i2c_bus)
        self.address = address
        self.State = None
        self.lastCO2 = None
        self.temperature = None
        self.RH = None
        self.AmbientPressure = None
        self.Altitude = None
        self.AutomaticSelfCalibInitialPeriod = None
        self.AutomaticSelfCalibStandardPeriod = None
        
    def Initialize(self, ambientPressure: int = 100000, altitude: int = 200, calibPeriod: int = 44) -> bool:
        try:
            self.SetAltitude(altitude)
            self.SetAmbientPressure(ambientPressure)
            self.SetAutomaticSelfCalibrationInitialPeriod(calibPeriod)
            return True
        except:
            return False

    def GetSerialNumber(self) -> int:
        self.SendCommandI2C(SCD41_GET_SERIAL_NUMBER)
        data = self.ReadI2C(SCD41_READ, 9)
        serialNumber = data[0] << 40 | data[1] << 32 | data[3] << 24 | data[4] << 16 | data[6] << 8 | data[7]
        return serialNumber
    
    def Reinit(self) -> None:
        self.SendCommandI2C(SCD41_STOP_PERIODIC_MEASUREMENT)
        self.SendCommandI2C(SCD41_REINIT)

    def MeasureSingleShot(self) -> None:
        self.SendCommandI2C(SCD41_MEASURE_SS)
        #time.sleep(5)
        
    def MeasureSingleShotOnlyRH(self) -> None:
        self.SendCommandI2C(SCD41_MEASURE_SS_RH_ONLY)
        # Sleep disabled because you can use .IsDataReady() method to check if data is readable!
        #time.sleep(0.05)
        
    def SetAutoCalibration(self, enable: bool) -> None:
        # This values are for enabled auto-calibration
        data = 0x01
        crc = 0xb0
        if enable == False:
            data = 0x00
            crc = 0x81
        self.SendI2C(SCD41_AUTO_CALIB_MSB, [SCD41_AUTO_CALIB_LSB, 0x00, data, crc])
        time.sleep(0.1)
        
    def GetAutoCalibrationStatus(self) -> bool:
        self.SendCommandI2C(SCD41_GET_AUTO_CALIB)
        data = self.ReadI2C(SCD41_READ, 3)
        status = data[0] << 8 | data[1]
        if status == 1:
            return True
        elif status == 0:
            return False
        else:
            print("ERROR")
            return False
        
    def SendCommandI2C(self, command: int) -> None:
        msb = (command >> 8) & 0xFF
        lsb = command & 0xFF
        self.SendI2C(msb, [lsb])
    
    def SendI2C(self, register: int, data: list) -> None:
        # To send data via SendI2C() command has to be splited for two parts!
        self.i2c.write_i2c_block_data(self.address, register, data)
        time.sleep(0.1)
    
    def SendDataI2C(self, command: int, data: list) -> None:
        crc = self.CalculateCRC(data)
        toSend = data
        msb = (command >> 8) & 0xFF
        lsb = command & 0xFF
        toSend.insert(0, lsb)
        toSend.append(crc)
        self.i2c.write_i2c_block_data(self.address, msb, toSend)

    def CalculateCRC(self, data: list):
        crc = SCD41_CRC8_INIT
        
        for current_byte in data:
            crc ^= current_byte
            for _ in range(8):
                if crc & 0x80:
                    crc = (crc << 1) ^ SCD41_CRC8_POLYNOMIAL
                else:
                    crc <<= 1
                crc &= 0xFF  # Ensure that the result stays within 8 bits
        
        return crc

    def ReadI2C(self, address: int, length: int, force: bool = None) -> list:
        # TODO: Use 'force' argument when required
        return self.i2c.read_i2c_block_data(self.address, address, length)
        
    def ReadMeasuredData(self) -> list:
        # Data can be only read if measurement have been made, after every measurment read buffer is
        # emptied. Reading empty buffer results in NACK and execption!
        try:
            self.SendCommandI2C(SCD41_READ_MEASUREMENT)
            data = self.ReadI2C(SCD41_READ, 9)
            # CO2
            co2 = data[0] << 8 | data[1]
            self.lastCO2 = co2
            # Temperature
            t = data[3] << 8 | data[4]
            temperature = -45 + 175*float(t/65535)
            self.temperature = temperature
            # RH
            drh = data[6] << 8 | data[7]
            rh = 100 * float(drh/65535)
            self.RH = rh
            # Returns data in format: [CO2; Temperature; RH]
            return [co2, temperature, rh]
        except:
            return [None, None, None]
    
    def GetLastCO2(self) -> int:
        return self.lastCO2
    
    def GetLastTemperature(self) -> int:
        return self.temperature
    
    def GetLastRH(self) -> int:
        return self.RH
    
    def SplitIntoTwoBytes(self, inputData: int) -> list:
        msb = (inputData >> 8) & 0xFF
        lsb = inputData & 0xFF
        data = [msb, lsb]
        return data

    def SetAmbientPressure(self, presure: int) -> bool:
        if presure < 70000 or presure > 120000:
            # Invalid input
            return False
        presure /= 100
        presure = int(presure)
        msb = (presure >> 8) & 0xFF
        lsb = presure & 0xFF
        data = [msb, lsb]
        self.SendDataI2C(SCD41_GET_AMBIENT_PRESSURE, data)
        self.AmbientPressure = presure
        return True

    def GetAmbientPressure(self) -> int:
        self.SendCommandI2C(SCD41_GET_AMBIENT_PRESSURE)
        data = self.ReadI2C(SCD41_READ, 3)
        pressure = (data[0] << 8 | data[1]) * 100
        self.AmbientPressure = pressure
        return pressure
    
    def GetLastSetAmbientPressure(self) -> int:
        return self.AmbientPressure

    def GetAltitude(self) -> int:
        # This method can only be used if device is in IDLE mode!
        self.SendCommandI2C(SCD41_GET_SENSOR_ALTITUDE)
        data = self.ReadI2C(SCD41_READ, 3)
        altitude = data[0] << 8 | data[1]
        self.Altitude = altitude
        return altitude

    def SetAltitude(self, altitude: int, saveToEEPROM: bool = False) -> bool:
        if altitude > 3000 or altitude < 0:
            return False
        
        data = self.SplitIntoTwoBytes(altitude)
        self.SendDataI2C(SCD41_SET_SENSOR_ALTITUDE, data)
        self.Altitude = altitude
        if saveToEEPROM == True:
            # Call save to EEPROM
            self.SaveToEEPROM()
        return True

    def GetLastSetAltitude(self) -> int:
        pass

    def StartPeriodicMeasurement(self) -> None:
        self.SendCommandI2C(SCD41_START_PERIODIC_MEASUREMENT)
        pass
    
    def StopPeriodicMeasurement(self) -> None:
        self.SendCommandI2C(SCD41_STOP_PERIODIC_MEASUREMENT)
        pass
    
    def ReadDataIfReady(self) -> list:
        if self.IsDataReady() == True:
            return self.ReadMeasuredData()
        else: return [None, None, None]
    
    def IsDataReady(self) -> bool:
        self.SendCommandI2C(SCD41_GET_DATA_READY_STATUS)
        result = self.ReadI2C(SCD41_READ, 3)
        word = result[0] << 8 | result[1]
        if word & 0b00000000000001111111111111 != 0:
            return True
        else: return False
        
    def SelfTestSensor(self) -> bool:
        self.SendCommandI2C(SCD41_PERFORM_SELF_TEST)
        time.sleep(10)
        result = self.ReadI2C(SCD41_READ, 3)
        word = result[0] << 8 | result[1]
        if word != 0:
            return False
        else: return True
        

    def GetAutomaticSelfCalibrationInitialPeriod(self) -> int:
        # This method can only be called in IDLE mode
        self.SendCommandI2C(SCD41_GET_AUTOMATIC_SELF_CALIBRATION_INITIAL_PERIOD)
        data = self.ReadI2C(SCD41_READ, 3)
        period = data[0] | data[1]
        self.AutomaticSelfCalibInitialPeriod = period
        return period

    def SetAutomaticSelfCalibrationInitialPeriod(self, period: int) -> bool:
        if period < 0:
            return False
        data = self.SplitIntoTwoBytes(period)
        self.SendDataI2C(SCD41_SET_AUTOMATIC_SELF_CALIBRATION_INITIAL_PERIOD, data)
        self.AutomaticSelfCalibInitialPeriod = period
        return True

    def GetAutomaticSelfCalibrationStandardPeriod(self) -> int:
        # This method can only be called in IDLE mode
        self.SendCommandI2C(SCD41_GET_AUTOMATIC_SELF_CALIBRATION_STANDARD_PERIOD)
        data = self.ReadI2C(SCD41_READ, 3)
        period = data[0] | data[1]
        self.AutomaticSelfCalibStandardPeriod = period
        return period

    def SetAutomaticSelfCalibrationStandardPeriod(self, period: int) -> bool:
        if period < 0:
            return False
        data = self.SplitIntoTwoBytes(period)
        self.SendDataI2C(SCD41_SET_AUTOMATIC_SELF_CALIBRATION_STANDARD_PERIOD, data)
        self.AutomaticSelfCalibStandardPeriod = period
        return True

    def FactoryReset(self) -> None:
        # This command resets all configuration settings stored in the EEPROM and erases the
        # FRC and ASC algorithm history, so better not use it if you dont have to!
        #self.SendI2C(SCD41_FACTORY_RESET_MSB, [SCD41_FACTORY_RESET_LSB])
        pass
        
    def PowerDown(self) -> None:
        self.SendCommandI2C(SCD41_POWER_DOWN)
    
    def WakeUp(self) -> None:
        self.SendCommandI2C(SCD41_WAKE_UP)
        time.sleep(0.3)

    def SaveToEEPROM(self) -> None:
        # EEPROM has only 3000 op's so use them wisely!
        #self.SendCommandI2C(SCD41_PERSIST_SETTINGS)
        #time.sleep(0.8)
        pass