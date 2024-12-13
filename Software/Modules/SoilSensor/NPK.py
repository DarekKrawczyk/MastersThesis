import RPi.GPIO as GPIO
from serial import Serial
import time

# NPK data frames
NPK_MOIS_DATA_FRAME = [0x01, 0x04, 0x00, 0x00, 0x00, 0x01, 0x31, 0xCA]
NPK_TEMP_DATA_FRAME = [0x01, 0x04, 0x00, 0x01, 0x00, 0x01, 0x60, 0x0A] #TEMP -> 1 4 0 1 0 1 96 10
NPK_ECON_DATA_FRAME = [0x01, 0x04, 0x00, 0x02, 0x00, 0x01, 0x90, 0x0A] #EC -> 1 4 0 2 0 1 144 10
NPK_PH_DATA_FRAME = [0x01, 0x04, 0x00, 0x03, 0x00, 0x01, 0xC1, 0xCA] # PH-> 1 4 0 3 0 1 193 202
NPK_NITR_DATA_FRAME = [0x01, 0x04, 0x00, 0x04, 0x00, 0x01, 0x70, 0x0B] # NITRO -> 1 4 0 4 0 1 112 11
NPK_PHOS_DATA_FRAME = [0x01, 0x04, 0x00, 0x05, 0x00, 0x01, 0x21, 0xCB] # PHOSPHO -> 1 4 0 5 0 1 33 203
NPK_POTS_DATA_FRAME = [0x01, 0x04, 0x00, 0x06, 0x00, 0x01, 0xD1, 0xCB] # POTASUYM -> 1 4 0 6 0 1 209 203

class NPK:
    MoistureUnit = "[%]"
    TemperatureUnit = "[°C]"
    PHUnit = ""
    ConductivityUnit = "[us/cm]"
    NitrogenUnit = "[mg/kg]"
    PhosphorusUnit = "[mg/kg]"
    PotassiumUnit = "[mg/kg]"
    def __init__(self, serial: Serial, de: int, re: int) -> None:
        self.__UART : Serial = serial
        self.__DE : int = de
        self.__RE : int = re
        self.__lastMoisture: float = 0
        self.__lastTemperature: float = 0
        self.__lastPH: float = 0
        self.__lastConductivity: int = 0
        self.__lastNitrogen: int = 0
        self.__lastPhosphorus: int = 0
        self.__lastPotassium: int = 0
         
    def Initialize(self) -> None:
        # You can copy this and paste it in main code, outside the class.
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.__DE, GPIO.OUT)
        GPIO.setup(self.__RE, GPIO.OUT)
        
    def PreTransfer(self) -> None:
        GPIO.output(self.__DE, GPIO.HIGH)
        GPIO.output(self.__RE, GPIO.HIGH)
    
    def PostTransfer(self) -> None:
        GPIO.output(self.__DE, GPIO.LOW)
        GPIO.output(self.__RE, GPIO.LOW)
        
    def SendData(self, data: list) -> list:
        self.PreTransfer()
        
        self.__UART.write(data)
        time.sleep(0.0165)
        
        self.PostTransfer()
        rcv = []
        try:
            buffer_size = len(data)-1
            rcv = list(self.__UART.read(buffer_size))
        except Exception as e:
            print(e) 
        return rcv
    
    def GetMoisture(self) -> float:
        data = self.SendData(NPK_MOIS_DATA_FRAME)
        hum = ((data[3] << 8) | data[4])/10
        self.__lastMoisture = hum
        return hum
    
    def GetLastMoisture(self) -> float:
        return self.__lastMoisture
    
    def GetTemperature(self) -> float:
        data = self.SendData(NPK_TEMP_DATA_FRAME)
        temp = ((data[3] << 8) | data[4])/10
        self.__lastTemperature = temp
        return temp
    
    def GetLastTemperature(self) -> float:
        return self.__lastTemperature
    
    def GetConductivity(self) -> int:
        data = self.SendData(NPK_ECON_DATA_FRAME)
        cond = ((data[3] << 8) | data[4])
        self.__lastConductivity = cond
        return cond
    
    def GetLastConductivity(self) -> int:
        return self.__lastConductivity
    
    def GetPH(self) -> float:
        data = self.SendData(NPK_PH_DATA_FRAME)
        ph = ((data[3] << 8) | data[4]) / 10
        self.__lastPH = ph
        return ph
    
    def GetLastPH(self) -> float:
        return self.__lastPH
    
    def GetNitrogen(self) -> int:
        data = self.SendData(NPK_NITR_DATA_FRAME)
        nitro = ((data[3] << 8) | data[4])
        self.__lastNitrogen = nitro
        return nitro
    
    def GetLastNitrogen(self) -> int:
        return self.__lastNitrogen
    
    def GetPhosphorus(self) -> int:
        data = self.SendData(NPK_PHOS_DATA_FRAME)
        phos = ((data[3] << 8) | data[4])
        self.__lastPhosphorus = phos
        return phos
    
    def GetLastPhosphorus(self) -> int:
        return self.__lastPhosphorus
    
    def GetPotassium(self) -> int:
        data = self.SendData(NPK_POTS_DATA_FRAME)
        pots = ((data[3] << 8) | data[4])
        self.__lastPotassium = pots
        return pots
    
    def GetLastPotassium(self) -> int:
        return self.__lastPotassium

