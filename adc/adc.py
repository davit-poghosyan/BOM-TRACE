import time

def read_adc(channel):
        path = f"/sys/bus/iio/devices/iio:device0/in_voltage{channel}_raw"
        with open(path, "r") as f:
            value = int(f.read().strip())
        return value

# Settings
ADC_CHANNEL3 = 3       # ADC3
ADC_CHANNEL2 = 2       # ADC2
VREF = 1.8             # Reference voltage (Orange Pi CM4 uses 1.8V)
ADC_RESOLUTION = 1023  # 10-bit ADC (0-1023)

# Read 1.6 # print the voltage every second
try:
    while True:
        adc_raw3 = read_adc(ADC_CHANNEL3)
        voltage3 = (adc_raw3 / ADC_RESOLUTION) * VREF
    
        adc_raw2 = read_adc(ADC_CHANNEL2)
        voltage2 = (adc_raw2 / ADC_RESOLUTION) * VREF

        #print(f"ADC: {voltage}")
        print(f"voltage(ADC3): {voltage3 *3}")
        print(f"amper(ADC2) {voltage2 / (0.015 * 20)}")

        print(f"\n")

        time.sleep(1)  # 1 second delay
except KeyboardInterrupt:
        print("\nExit program.") 
