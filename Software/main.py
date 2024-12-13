import pandas as pd
import time
import datetime
import os
from Modules.SHT35.sht35 import SHT35, Repeatability
from Modules.SCD41.scd41 import SCD41
from Modules.SoilSensor.NPK import NPK
from Modules.LEDpanel.LEDpanel import LEDpanel
from Modules.AS7341.as7341 import AS7341_MeasurementConfig, AS7341
from Modules.Relay.Relays import Relays

from serial import Serial

MOISTURE_LIMIT = 0.20

def generate_data(temp, hum, co2, npk_data, as7341_data):
    data = {
        'Timestamp': [pd.Timestamp.now()],
        'Temperature (C)': [temp],
        'Humidity (%)': [hum],
        'CO2 Concentration (ppm)': [co2],
        'Soil Moisture (%)': [npk_data[0]],
        'Soil Temperature (C)': [npk_data[1]],
        'Soil Conductivity (uS/cm)': [npk_data[2]],
        'Soil pH': [npk_data[3]],
        'Soil Nitrogen (mg/kg)': [npk_data[4]],
        'Soil Phosphorus (mg/kg)': [npk_data[5]],
        'Soil Potassium (mg/kg)': [npk_data[6]],
        '415 (nm)': [as7341_data[0]],
        '445 (nm)': [as7341_data[1]],
        '480 (nm)': [as7341_data[2]],
        '515 (nm)': [as7341_data[3]],
        '555 (nm)': [as7341_data[4]],
        '590 (nm)': [as7341_data[5]],
        '630 (nm)': [as7341_data[6]],
        '680 (nm)': [as7341_data[7]],
        'Near IR': [as7341_data[8]],
        'Clear': [as7341_data[9]]
    }
    return pd.DataFrame(data)

def save_to_excel(df, filename):
    if os.path.isfile(filename):
        existing_data = pd.read_excel(filename)
        df = pd.concat([existing_data, df], ignore_index=True)
    df.to_excel(filename, index=False)

def main():
    try:
        filename = 'environmental_data.xlsx'
        interval = 3600 # Godzina
        
        sht35 = SHT35()
        
        scd41 = SCD41()
        scd41.Initialize()
        scd41.StartPeriodicMeasurement()
        prev_scd41_data = [None] * 3
        prev_scd41_data[0] = 0
        
        DE = 6
        RE = 26
        uart0 = Serial(port='/dev/ttyAMA3', baudrate=4800, timeout=1)
        npk = NPK(uart0, DE, RE)
        npk.Initialize()

        as7341 = AS7341()
        as7341.SetPowerStatus(True)
        as7341.SetATime(100)
        as7341.SetAStep(999)
        as7341.SetMeasurementGain(AS7341.ADC_GAIN_16X)

        panel = LEDpanel()
        val = 0

        relays = Relays()

        time.sleep(2)

        while True:
            now = datetime.datetime.now()
            start_time = now.replace(hour=8, minute=0, second=0, microsecond=0)
            end_time = now.replace(hour=20, minute=0, second=0, microsecond=0)
            
            if start_time <= now <= end_time:
                panel.SetValueToChannel(0, 60)     #Most red
                panel.SetValueToChannel(1, 80)
                panel.SetValueToChannel(2, 100)
                panel.SetValueToChannel(3, 100)
                panel.SetValueToChannel(4, 100)
                panel.SetValueToChannel(5, 100)
            else:
                panel.SetValueToChannel(0, 0)
                panel.SetValueToChannel(1, 0)
                panel.SetValueToChannel(2, 0)
                panel.SetValueToChannel(3, 0)
                panel.SetValueToChannel(4, 0)
                panel.SetValueToChannel(5, 0)
            
            # Temp i wilg powietrza
            sht35_data = sht35.SingleMeasureTempAndHum(Repeatability.HIGH)
            time.sleep(0.1)        

            # CO2
            scd41_data = [None] * 3
            scd41_data[0] = 0
            
            if scd41.IsDataReady() == True:
                scd41_data = scd41.ReadMeasuredData()
                prev_scd41_data = scd41_data
            else:
                scd41_data = prev_scd41_data
                
            # Gleba
            npk_moisture = npk.GetMoisture()
            npk_temperature = npk.GetTemperature()
            npk_conductivity = npk.GetConductivity()
            npk_ph = npk.GetPH()
            npk_nitrogen = npk.GetNitrogen()
            npk_phosphorus = npk.GetPhosphorus()
            npk_potassium = npk.GetPotassium()
            npk_data = [npk_moisture, npk_temperature, npk_conductivity, npk_ph,
                        npk_nitrogen, npk_phosphorus, npk_potassium]
            
            # Relays
            if npk_moisture <= MOISTURE_LIMIT:
                relays.On(Relays.Relay.One)
                time.sleep(5)
                relays.Off(Relays.Relay.One)
            
            # Czujnik światła
            as7341.MeasureFullSpectrum()
            as7341_datas = as7341.GetDataInRaw()

            data = generate_data(sht35_data[0],sht35_data[1],scd41_data[0], npk_data, as7341_datas)
            save_to_excel(data, filename)
            print(f"Zapisano dane do {filename} o {data['Timestamp'][0]}")
            time.sleep(interval)

    except KeyboardInterrupt:
        scd41.StopPeriodicMeasurement()
        panel.SetValueToChannel(0, 0)
        panel.SetValueToChannel(1, 0)
        panel.SetValueToChannel(2, 0)
        panel.SetValueToChannel(3, 0)
        panel.SetValueToChannel(4, 0)
        panel.SetValueToChannel(5, 0)
        relays.Off(Relays.Relay.Zero)
        relays.Off(Relays.Relay.One)
        print("\nExiting!")
    

if __name__ == "__main__":
    main()
