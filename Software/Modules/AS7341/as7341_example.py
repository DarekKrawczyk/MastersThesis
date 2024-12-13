import time
from as7341 import AS7341_MeasurementConfig, AS7341

print("AS7441 - sensor demo")
sensor = AS7341()
print(f"ID: {sensor.GetID()}")

#sensor.SetPowerStatus(False)
#print(f"Power status {sensor.GetPowerStatus()}")
sensor.SetPowerStatus(True)
# print(f"Power status {sensor.GetPowerStatus()}")

# print(f"SMUX: {sensor.GetRegisterValue(AS7341_CFG_6)}")
# sensor.SetSMUX(SMUX_REG.WRITE_FROM_RAM_TO_SMUX)
# print(f"SMUX: {sensor.GetRegisterValue(AS7341_CFG_6)}")

# sensor.SetMeasurementStatus(True)
# print(f"Enable register: {bin(sensor.GetRegisterValue(AS7341_ENABLE))}")

# print(f"Channels data: {sensor.ReadAllChannels()}")

try:
    sensor.SetATime(100)
    sensor.SetAStep(999)
    sensor.SetMeasurementGain(AS7341.ADC_GAIN_256X)
    while True:
        sensor.MeasureFullSpectrum()
        #print(data)
        sensor.PrintMeasuredDataRaw()
        print(f"Calculated PAR: {sensor.GetPAR()}[µmol m⁻² s⁻¹]")
        print(sensor.GetDataInRaw())
        time.sleep(1)
        
except KeyboardInterrupt:
    sensor.ClearRegister(AS7341.AS7341_ENABLE)
    print("\nExiting demo!")
