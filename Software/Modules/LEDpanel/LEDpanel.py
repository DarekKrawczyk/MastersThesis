# type: ignore
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685

# LED Panel - pinout configuration
# Channels:
# 0) 450[nm]
# 1) 463[nm]
# 2) 517[nm]
# 3) 629[nm]
# 4) 660[nm]
# 5) 730[nm]

class LEDpanel:
    def __init__(self) -> None:
        self.__i2c = busio.I2C(SCL, SDA)
        self.__pca9685 = PCA9685(self.__i2c)
        self.__pca9685.frequency = 200
        
    def SetValueToChannel(self, channel: int, value: int) -> None:
        self.__pca9685.channels[channel].duty_cycle = self.MapToValue(value)

    def MapToValue(self, value: int) -> int:
        if value <= 0: return 0
        elif value >= 100: return 65535
        return value * 655   # Just approximate