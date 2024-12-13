from mcp3208 import MCP3208
from HardwareUtilities.SPI_Wrapper import SPIconfiguration
import time

spi_configg = SPIconfiguration(spi_bus=0, chip_select_pin=0, speed=500000, spi_mode=0)
mcp3208 = MCP3208(spi_config=spi_configg, v_ref=3.3)

print("MCP3208 - ADC - demo")

try:
    while True:
        data = mcp3208.ReadChannelSingle(7)
        volts = mcp3208.ReadChannelSingleToVolts(7)
        print(f"Channel[7] - digital: {data}")
        print(f"Channel[7] - analog: {volts:.2f}[V]\n")
        
        time.sleep(0.2)
except KeyboardInterrupt:
    print("\nExiting demo!")