from sht35 import SHT35, Repeatability, MeasurementFreq
import time

print("SHT35 demo")
sht35 = SHT35()

data = sht35.SingleMeasureTempAndHum(Repeatability.HIGH)
print(f"Temperature: {data[0]}[°C]")
print(f"Humidity: {data[1]}[%]")

heater = sht35.IsHeaterEnabled()
print(f"Heater enabled: {heater}")

#sht35.SetHeater(True)

sht35.PeriodicMeasurement(MeasurementFreq.MPS_10, Repeatability.HIGH)


register = sht35.GetStatusRegister()
print(f"Register: {bin(register)}")

heater = sht35.IsHeaterEnabled()
print(f"Heater enabled: {heater}")


try:
    iterator = 0
    while True:
        if iterator == 10:
            #sht35.SoftwareReset()

            heater = sht35.IsHeaterEnabled()
            print("Heater: %s" % heater)

            sht35.SetHeater(True)
            heater = sht35.IsHeaterEnabled()
            print("Heater: %s" % heater)

            sht35.SetHeater(False)
            heater = sht35.IsHeaterEnabled()
            print("Heater: %s" % heater)

        #periodicData = sht35.PeriodicFetchData()
        #print(periodicData)

        measurement = sht35.PeriodicGetTempAndHum()
        print(f"Temperature: {measurement[0]}[°C]")
        print(f"Humidity: {measurement[1]}[%]")
        time.sleep(1)
        iterator+=1
except KeyboardInterrupt:
    print("\nExiting demo!")
