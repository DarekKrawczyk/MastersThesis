from scd41 import SCD41

# This demo shows how to get data from SCD41:
# 1) Run .MeasureSingleShot() or .StartPeriodicMeasurement() method
# 2) Check if data is ready via .IsDataReady() method
# 3) If data is ready, then use .ReadMeasuredData() method
print("SCD41 sensor demo")

scd41 = SCD41()
scd41.Initialize()

period = scd41.GetAutomaticSelfCalibrationStandardPeriod()
print(f"Automatic standard calib period: {period}[h]")

period = scd41.GetAutomaticSelfCalibrationInitialPeriod()
print(f"Automatic initial calib period: {period}[h]")

altitude = scd41.GetAltitude()
print(f"Altitude: {altitude}[m]")

serial = scd41.GetSerialNumber()
print("Serial number: ", serial)

#scd41.MeasureSingleShot()
scd41.StartPeriodicMeasurement()
try:
    while True:
        if scd41.IsDataReady() == True:
            data = scd41.ReadMeasuredData()
            print(f"CO2: {data[0]}[ppm]")
            print(f"Temperature: {data[1]}[°C]")
            print(f"RH: {data[2]}[%]")
            

        pressure = scd41.GetAmbientPressure()
        print(f"Ambient pressure: {pressure}[Pa]")

        # data = scd41.ReadDataIfReady()
        # print(f"CO2: {data[0]}[ppm]")
        # print(f"Temperature: {data[1]}[°C]")
        # print(f"RH: {data[2]}[%]")    
    
        print(f"Data ready: {scd41.IsDataReady()}")
except KeyboardInterrupt:
    scd41.StopPeriodicMeasurement()
    altitude = scd41.GetAltitude()
    print(f"\nAltitude: {altitude}[m]")
    print("\nExiting demo!")
    
# print("Performing self test... 10[s]!")
# self_test = scd41.SelfTestSensor()
# print("Device working correctly: ", self_test)

# auto_calib = scd41.GetAutoCalibrationStatus()
# print("Auto-calibration: ", auto_calib)

# scd41.MeasureSingleShot()
# data = scd41.ReadMeasuredData()
# print(f"CO2: {data[0]}[ppm]")
# print(f"Temperature: {data[1]:.2f}[°C]")
# print(f"RH: {data[2]:.2f}[%]")

# scd41.MeasureSingleShot()
# temp = scd41.GetTemperature()
# print("Temperature: ", temp)

# print("Data ready: ", scd41.IsDataReady())

# last_co2 = scd41.GetLastCO2()
# print("Last measured CO2: ", last_co2)