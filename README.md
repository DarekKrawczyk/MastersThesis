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

## Device
Created prototype consists of several custom made parts, where each one plays crucial role in prototype.

<div style="display: flex; justify-content: center; align-items: center;">
    <img src="Assets/Device.jpg" alt="Experimental Setup" width="45%" style="margin-right: 10px;">
    <img src="Assets/d7.jpg" alt="Plant Growth Results" width="45%">
</div>

---

## Folder structure
```
/Assets
  └── images                        # Contains all image files used in the project
/Hardware
  ├── /External_Libs                # Libraries for modules used in the schematics
  ├── /Modules                      # Projects for developed modules
  │   ├── /LED_Driver               # Drivers for controlling the LED panel
  │   ├── /LED_Panel                # Custom LED panel design and components
  │   ├── /LTC2439_Eval_Board       # High-accuracy ADC module (not used in the project)
  │   └── /Main_Board               # Main board design and schematics
  └── PartsValuesCalculation.xlsx   # Calculation of electrical component values
/Software
  ├── /Modules                      # Libraries written for the system
  └── main.py                       # Example code for saving data from the device
/Thesis
  └── thesis_files                  # Files related to the thesis documentation
```
---

## System Overview

In this project, three custom PCB boards were designed to support the system's functionality.

#### LED Panel Board  
The **first PCB** is an **LED panel** equipped with LEDs selected based on their emitted wavelengths of light. These wavelengths correspond to the plant-beneficial parts of the light spectrum, which can be modulated to influence plant growth. Each LED strip on the panel is controlled by a dedicated LED driver designed specifically for this project.

#### Main Control Board  
The **second PCB** is the **main control board**, which integrates the entire system. It is designed to work with a central processing unit, which in this case is the **Raspberry Pi 4B**. The main board is powered by an external **TRH100A120-11E12 VI switching power supply**, delivering a nominal voltage of **12V**.  

Onboard, the main board features two switching voltage regulators:  
- **LM2678S-5.0**: Steps down the voltage from 12V to 5V.  
- **MCP1603**: Steps down the voltage from 5V to 3.3V.  

The main board allows control of external components via:  
- **Two onboard relays**: Used, for example, to control a water pump.  
- A **PWM signal generator (PCA9685PW)**: Regulates the brightness of the LED panel.  

#### Data Acquisition and Communication  
In addition to control circuits, the main board is equipped with systems for **data acquisition** from various sensors installed in the device. It includes:  
- An **8-channel ADC (MCP3208)**: Interfaces with analog output devices.  
- An **RS485 protocol interface**: Enabled via a **MAX485+ converter**, which connects to a soil composition sensor.  

The soil composition sensor provides measurements for the following parameters:  
- **Temperature**  
- **Humidity**  
- **Electrical conductivity**  
- **pH**  
- **Nitrogen**  
- **Phosphorus**  
- **Potassium**  

The main board also provides outputs for controllers supporting the **UART** and **I2C** protocols, enabling connection with external modules.

#### Real-Time Clock (RTC)  
To ensure consistent date and time information, the main board features a **Real-Time Clock (RTC)** module.

#### Additional Features  
The system is enhanced with:  
- A **Raspberry Pi Camera Module 3** connected to the Raspberry Pi 4B, enabling image capture functionality.  
- Support for an **external display** for user interaction and system monitoring.

---

## Systems hardware

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

---

## Images

| ![Image 2](Assets/Device.jpg) | ![Image 3](Assets/d6.jpg) | ![Image 4](Assets/d5.jpg) |
|:-------------------------:|:-------------------------:|:-------------------------:|
| ![Image 5](Assets/d4.jpg) | ![Image 6](Assets/d1.jpg) | ![Image 8](Assets/d3.jpg) |
