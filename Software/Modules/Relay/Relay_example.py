from Relays import Relays
import time

print("Relay demo!")

relays = Relays()

try:
    while True:
        relays.On(Relays.Relay.Zero)
        relays.On(Relays.Relay.One)
        time.sleep(1)
        relays.Off(Relays.Relay.Zero)
        relays.Off(Relays.Relay.One)
        time.sleep(1)

except KeyboardInterrupt:
    relays.Off(Relays.Relay.Zero)
    relays.Off(Relays.Relay.One)
    print("\nExiting demo!")