from board import SCL, SDA
import time
import busio


# Import the PCA9685 module.

from adafruit_pca9685 import PCA9685


# Create the I2C bus interface.

i2c_bus = busio.I2C(SCL, SDA)


# Create a simple PCA9685 class instance.

pca = PCA9685(i2c_bus)


# Set the PWM frequency to 60hz.

pca.frequency = 200


# Set the PWM duty cycle for channel zero to 50%. duty_cycle is 16 bits to match other PWM objects

# but the PCA9685 will only actually give 12 bits of resolution.

pca.channels[0].duty_cycle = 5000
pca.channels[1].duty_cycle = 1500
pca.channels[2].duty_cycle = 200

