# System to Support the Management and Control of Plant Cultivation

## Introduction
This repository contains the work and resources related to my master's thesis titled **"System to Support the Management and Control of Plant Cultivation."** The project focuses on the development of a prototype device designed for vertical farming to enhance the efficiency of plant cultivation. By utilizing artificial lighting and monitoring key environmental parameters such as temperature, humidity, and light intensity, the system aims to provide optimal conditions for plant growth.

The developed solution integrates various sensors and automation features to ensure continuous monitoring and adjustment of cultivation parameters. This approach facilitates data-driven decisions, improves resource utilization, and increases the efficiency of modern plant cultivation methods. The work also involves experiments, measurements, and comparisons with natural cultivation techniques and existing solutions available on the market.

---

## Abstract
The aim of this master's thesis is to develop and study a prototype device designed for vertical farming, which will enhance the efficiency of plant cultivation through the use of artificial lighting and provide monitoring of key environmental parameters such as:
- Temperature
- Humidity
- Light intensity

The system is equipped with various sensors to enable continuous monitoring of conditions and automatic adjustment of cultivation parameters. The project includes experiments to compare plant growth under the controlled environment of the prototype device with naturally grown plants. Additionally, the thesis examines:

- Measurement precision
- Power consumption
- Comparative analysis with other solutions on the market

The analysis further explores data recording, archiving, and analytical capabilities to highlight the benefits of integrating technology into modern agricultural practices.

---

## Keywords
- Prototype  
- Vertical farming  
- Embedded system  
- Data acquisition  
- Internet of Things (IoT)

---

## Final prototype
Created prototype consists of several custom made parts, where each one plays crucial role in prototype.

<div style="display: flex; justify-content: center; align-items: center;">
    <img src="Assets/Device.jpg" alt="Experimental Setup" width="45%" style="margin-right: 10px;">
    <img src="Assets/d7.jpg" alt="Plant Growth Results" width="45%">
</div>

---

## Folder structure
**/Assets**
  └── images            # Contains all image files used in the project
**/Hardware**
  ├── **/External_Libs**     # Libraries for modules used in the schematics
  ├── **/Modules**           # Projects for developed modules
  │   ├── **/LED_Driver**    # Drivers for controlling the LED panel
  │   ├── **/LED_Panel**     # Custom LED panel design and components
  │   ├── **/LTC2439_Eval_Board**  # High-accuracy ADC module (not used in the project)
  │   └── **/Main_Board**    # Main board design and schematics
  └── PartsValuesCalculation.xlsx   # Calculation of electrical component values
**/Software**
  ├── **/Modules**           # Libraries written for the system
  └── main.py            # Example code for saving data from the device
**/Thesis**
  └── thesis_files       # Files related to the thesis documentation

---

## Description


---


## Hardware System Description

<div style="display: flex; justify-content: center; align-items: center;">
    <img src="Assets/SchematBlokowy.png" alt="Experimental Setup" width="91%" style="margin-right: 10px;">
</div>





<div style="display: flex; flex-direction: column; justify-content: center; align-items: center;">
    <img src="Assets/MainBoard3D.png" alt="Experimental Setup" width="91%" style="margin-bottom: 10px;">
    <div style="display: flex; justify-content: center; align-items: center;">
        <img src="Assets/PanelLED3D.png" alt="Experimental Setup" width="45%" style="margin-right: 10px;">
        <img src="Assets/DriverLED3D.png" alt="Plant Growth Results" width="45%">
    </div>
</div>



The diagram represents a comprehensive hardware setup designed for vertical farming, combining monitoring, control, and automation capabilities. The key components and their roles are as follows:
1. Power Supply and Regulation

    External Power Supply:
        TRH100A120-11E12 VI provides power to the system.
    Voltage Regulators:
        5V Regulator (LM2678S-5.0) ensures stable 5V supply for key components.
        3V Regulator (MCP1603) provides a 3V supply for lower voltage devices.

2. Central Control Unit

    Raspberry Pi 4B:
        Serves as the primary processing unit, managing communication, data collection, and device control.
        Connected via GPIO to various peripherals and subsystems.
    Camera Module (Raspberry Pi Camera Module 3):
        Captures visual data for monitoring plant growth.
        Communicates with the Raspberry Pi via the CSI (Camera Serial Interface).

3. Communication and Control Modules

    PWM Generator (PCA9685PW):
        Generates PWM (Pulse Width Modulated) signals to control lighting intensity and other devices.
        Communicates via the I2C protocol.
    2x Relays (G5LE-14 DC5):
        Used to control high-power devices such as the water pump.
        Connected through GPIO for on/off control.
    UART - RS485 Converter (MAX485+):
        Enables communication over RS485 with external devices, such as the soil composition sensor (NPK).

4. Sensors and Measurement Modules

Several sensors are integrated to monitor key environmental parameters essential for plant growth:

    CO₂ Concentration Sensor (SCD41):
        Measures carbon dioxide levels in the environment.
    Temperature and Humidity Sensor (SHT35):
        Monitors air temperature and relative humidity.
    Light Intensity Sensor (AS7341):
        Measures the intensity and spectrum of light for plant optimization.
    Soil Composition Sensor (NPK):
        Measures soil nutrient content using the RS485 interface.

5. Analog-to-Digital Conversion

    A/C Converter (MCP3208):
        Converts analog signals from sensors into digital data for processing.
        Communicates with the Raspberry Pi via the SPI protocol.

6. Time Management

    RTC Clock (RTCDS1307ZN+T&R):
        Real-Time Clock provides accurate timekeeping for scheduling processes like irrigation and lighting.
        Communicates via I2C.

7. LED Lighting System

    6x LED Drivers (A8513KLYTR-T):
        Control the LED Panel (“Mid Power – Horticulture LEDs Size 2835”).
        Connected to the PWM Generator for dynamic light intensity control.

8. Water Pump Control

    The Water Pump is controlled through relays, enabling automated irrigation based on sensor data and pre-programmed conditions.

System Workflow

    The Raspberry Pi 4B processes environmental data from sensors, including CO₂ concentration, temperature, humidity, light intensity, and soil composition.
    The PWM Generator (PCA9685PW) adjusts the LED lighting intensity dynamically based on the readings from the light sensor (AS7341).
    Relays control the water pump to automate irrigation based on soil data from the NPK sensor.
    The RTC Clock ensures precise timing for lighting schedules and irrigation.
    The A/C Converter handles analog data conversion for sensors requiring SPI communication.
    All components interact via communication protocols (I2C, SPI, UART, RS485) with the Raspberry Pi managing the overall system.
    The camera module provides visual feedback for plant growth monitoring.

## Images

<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; justify-items: center; align-items: center;">
    <img src="Assets/d7.jpg" alt="Image 1" style="width: 100%; height: 100%; object-fit: cover;">
    <img src="Assets/d8.jpg" alt="Image 2" style="width: 100%; height: 100%; object-fit: cover;">
    <img src="Assets/d6.jpg" alt="Image 4" style="width: 100%; height: 100%; object-fit: cover;">
    <img src="Assets/d5.jpg" alt="Image 5" style="width: 100%; height: 100%; object-fit: cover;">
    <img src="Assets/d4.jpg" alt="Image 6" style="width: 100%; height: 100%; object-fit: cover;">
    <img src="Assets/d1.jpg" alt="Image 7" style="width: 100%; height: 100%; object-fit: cover;">
    <img src="Assets/d2.jpg" alt="Image 8" style="width: 100%; height: 100%; object-fit: cover;">
    <img src="Assets/d3.jpg" alt="Image 9" style="width: 100%; height: 100%; object-fit: cover;">
</div>

