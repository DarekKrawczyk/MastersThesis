from LEDpanel import LEDpanel
import time

print("LED Panel demo!")

val = 0
panel = LEDpanel()

try:
    while True:
        panel.SetValueToChannel(0, val)
        panel.SetValueToChannel(1, val)
        panel.SetValueToChannel(2, val)
        panel.SetValueToChannel(3, val)
        panel.SetValueToChannel(4, val)
        panel.SetValueToChannel(5, val)
        val += 1
        time.sleep(0.01)
        if val > 100: val = 0

except KeyboardInterrupt:
    panel.SetValueToChannel(0, 0)
    panel.SetValueToChannel(1, 0)
    panel.SetValueToChannel(2, 0)
    panel.SetValueToChannel(3, 0)
    panel.SetValueToChannel(4, 0)
    panel.SetValueToChannel(5, 0)
    print("\nExiting demo!")