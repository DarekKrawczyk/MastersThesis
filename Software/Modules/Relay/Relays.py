# type: ignore
import RPi.GPIO as GPIO
from enum import IntEnum

# LED Panel - pinout configuration
# Relays:
# 0 -> GPIO24
# 1 -> GPIO25

class Relays:

    class Relay(IntEnum):
        Zero = 24
        One = 25

    def __init__(self) -> None:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        GPIO.setup(int(Relays.Relay.Zero), GPIO.OUT)
        GPIO.output(int(Relays.Relay.Zero), False)
        
        GPIO.setup(int(Relays.Relay.One), GPIO.OUT)
        GPIO.output(int(Relays.Relay.One), False)

    def On(self, relay_id: Relay) -> None:
        GPIO.output(int(relay_id), True)

    def Off(self, relay_id: Relay) -> None:
        GPIO.output(int(relay_id), False)