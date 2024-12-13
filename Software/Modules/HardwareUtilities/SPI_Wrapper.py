import spidev

class SPIconfiguration:
    def __init__(self, spi_bus: int, chip_select_pin: int, speed: int, spi_mode: int) -> None:
        self.__SpiBus = spi_bus
        self.__chip_select_pin = chip_select_pin
        self.__speed = speed
        self.__spi_mode = spi_mode
        
    def GetSpiBus(self) -> int:
        return self.__SpiBus 

    def SetSpiBus(self, new_spi_bus) -> int:
        self.__SpiBus = new_spi_bus

    def GetSpeed(self) -> int:
        return self.__speed 

    def SetSpeed(self, new_speed) -> int:
        self.__speed = new_speed
    
    def GetChipSelectPin(self) -> int:
        return self.__chip_select_pin 
    
    def SetChipSelectPin(self, new_cs) -> int:
        self.__chip_select_pin = new_cs
    
    def GetSPImode(self) -> int:
        return self.__spi_mode 
    
    def SetSPImode(self, new_spi_mode) -> int:
        self.__spi_mode = new_spi_mode

class SPI:
    def __init__(self, spi_config: SPIconfiguration) -> None:
        self.__SPI = spidev.SpiDev()
        self.__SpiBus = spi_config.GetSpiBus()
        self.__chip_select_pin = spi_config.GetChipSelectPin()
        self.__speed = spi_config.GetSpeed()
        self.__spi_mode = spi_config.GetSPImode()
        
        try:
            self.OpenConnection()
            self.ApplyConfig()
        except Exception as e:
            print(f"Error initializing SPI: {e}")
            self.CloseConnection()
            raise
   
    def ApplyConfig(self) -> None:
        self.__SPI.max_speed_hz = self.__speed
        self.__SPI.mode = self.__spi_mode
        
    def GetSpeed(self) -> int:
        return self.__speed
    
    def SetSpeed(self, new_speed: int) -> None:
        self.__speed = new_speed

    def OpenConnection(self) -> None:
        self.__SPI.open(self.__SpiBus, self.__chip_select_pin)
        
    def CloseConnection(self) -> None:
        self.__SPI.close()
    
    def PerformTransaction(self, buffer: list) -> list:
        result = self.__SPI.xfer2(buffer)
        return result