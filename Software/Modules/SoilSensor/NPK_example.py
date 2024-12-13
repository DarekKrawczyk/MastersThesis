from NPK import NPK
from serial import Serial
import time

DE = 6
RE = 26
uart0 = Serial(port='/dev/ttyAMA3', baudrate=4800, timeout=1)
npk = NPK(uart0, DE, RE)
npk.Initialize()

while True:
    moisture = npk.GetMoisture()
    print(f"Soil moisture: {moisture}{NPK.MoistureUnit}")
    
    temperature = npk.GetTemperature()
    print(f"Soil temperature: {temperature}{NPK.TemperatureUnit}")
    
    conductivity = npk.GetConductivity()
    print(f"Soil conductivity: {conductivity}{NPK.ConductivityUnit}")
    
    ph = npk.GetPH()
    print(f"Soil PH: {ph}{NPK.PHUnit}")
    
    nitrogen = npk.GetNitrogen()
    print(f"Soil nitrogen: {nitrogen}{NPK.NitrogenUnit}")

    phosphorus = npk.GetPhosphorus()
    print(f"Soil phosphorus: {phosphorus}{NPK.PhosphorusUnit}")
    
    potassium = npk.GetPotassium()
    print(f"Soil potassium: {potassium}{NPK.PotassiumUnit}")
    
    print("\n<--------------------------------->\n")
    time.sleep(5)