import time

def read_adc(channel):
        path = f"/sys/bus/iio/devices/iio:device0/in_voltage{channel}_raw"
        with open(path, "r") as f:
            value = int(f.read().strip())
        return value

# Settings
ADC_CHANNEL = 2        # ADC2
VREF = 3.3             # Reference voltage (Orange Pi CM4 uses 3.3V)
ADC_RESOLUTION = 4095  # 12-bit ADC (0-4095)

# Read and print the voltage every second
try:
    while True:
        adc_raw = read_adc(ADC_CHANNEL)
        voltage = (adc_raw / ADC_RESOLUTION) * VREF
        print(f"ADC: {adc_raw:}")
        time.sleep(1)  # 1 second delay
except KeyboardInterrupt:
        print("\nExit program.")
