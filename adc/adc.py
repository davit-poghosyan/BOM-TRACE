import time

# Settings
ADC_CHANNEL3 = 3       # ADC3
ADC_CHANNEL2 = 2       # ADC2
VREF = 1.8             # Reference voltage (Orange Pi CM4 uses 1.8V)
ADC_RESOLUTION = 1023  # 10-bit ADC (0-1023)

adc_read_delay_ms = 1/1000
prog_delay = 1000/1000


# buff = 0 

def read_adc(channel):
        path = f"/sys/bus/iio/devices/iio:device0/in_voltage{channel}_raw"
        with open(path, "r") as f:
            value = int(f.read().strip())
        return value

def raw_adc_val_to_volt(adc_val):
    return adc_val/ ADC_RESOLUTION * VREF

def volt_to_amp(volt):
    return volt / (0.015 * 20)

def amp_calculatoin(channel):

    try:
        buff = 0
        for i in range(20):
            # adc_raw3 = read_adc(ADC_CHANNEL3)
           # voltage3 = (adc_raw3 / ADC_RESOLUTION) * VREF
            #voltage2 = (adc_raw2 / ADC_RESOLUTION) * VREF

            # voltage3 = raw_adc_val_to_volt(adc_raw3)
            adc_raw = read_adc(channel)
            voltage = raw_adc_val_to_volt(adc_raw) 
            amp = volt_to_amp(voltage)
            buff += amp
       
            #print(f"ADC: {voltagde}")
            # print(f"voltage(ADC3): {voltage3 *3}")
            # print(f"amper(ADC2) {voltage2 / (0.015 * 20)}")
            # print(f"amper(ADC2) {amp2}")
            # print(f"\n")
            time.sleep(adc_read_delay_ms)

        return buff/20
    
    except KeyboardInterrupt:
            print("\nExit program.") 


try:
    while(True):
        amp2 = amp_calculatoin(ADC_CHANNEL2)
        print(f"amper(adc2) {amp2}")
        time.sleep(prog_delay)
except KeyboardInterrupt:
    print("\nExit program.") 
