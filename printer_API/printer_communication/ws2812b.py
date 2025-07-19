import spidev
import time
from typing import List, Tuple, Union

class LedStripe: 
    def __init__(self):
    # WS2812B SPI settings
        self.SPI_BUS = 3
        self.SPI_DEVICE = 0
        self.SPI_SPEED_HZ = 2400000  # 2.4 MHz for 3-bit per WS2812 bit encoding

    # Create lookup for WS2812 1-bit encoded to SPI 3-bit pattern
    # 1 -> 110 (0b110), 0 -> 100 (0b100)
        self.bit_patterns = {
            0: 0b100,
            1: 0b110,
        }

    def encode_byte(self, byte):
        """Convert a single 8-bit byte into 24 SPI bits (3 bits per data bit)."""
        encoded = []
        for i in range(8):
            bit = (byte >> (7 - i)) & 1
            encoded.append(self.bit_patterns[bit])
        return encoded

    def encode_rgb(self, r, g, b):
        """Encode one LED's GRB value to SPI format."""
        data = []
        for byte in [g, r, b]:  # WS2812 expects GRB
            encoded = self.encode_byte(byte)
            for val in encoded:
                data.append((val << 5) & 0xE0)  # Top 3 bits used; rest padded

        return data

    def shine_leds(self,
        status_color: tuple[int, int, int],
        BOM_Trace: tuple[int, int, int],
        logo: tuple[int, int, int],
        led_sequence: List[Tuple[int, tuple[int, int, int]]]
    ) -> None:
        led_stripe = [(0, 0, 0)] * 99

        # Set static sections
        led_stripe[0:9] = [status_color] * 9
        led_stripe[9:14] = [BOM_Trace] * 5
        led_stripe[14:19] = [logo] * 5

        # Set dynamic sequence starting at offset 19
        for index, (r, g, b) in led_sequence:
            if 0 <= index + 19 < len(led_stripe):
                led_stripe[index + 19] = (r, g, b)
            else:
                print(f"Warning: LED index {index + 19} out of range, skipped.")

        for index, value in enumerate(led_stripe):
            print(f"LED[{index}] = {value}")

        self.send_ws2812(led_stripe)

    def send_ws2812(self, rgb_list):
        """Send a list of (r, g, b) tuples to WS2812 strip."""
        spi = spidev.SpiDev()
        spi.open(self.SPI_BUS, self.SPI_DEVICE)
        spi.max_speed_hz = self.SPI_SPEED_HZ
        spi.mode = 0

        #print(rgb_list)

        spi_data = []
        for (r, g, b) in rgb_list:
            spi_data += self.encode_rgb(r, g, b)

        # Append reset pulse: at least 50 µs of low, i.e., 50µs / (1s/2.4MHz) = 120 bytes of zero
        spi_data = [0x00] * 100 + spi_data + [0x00] * 100

        spi.writebytes(spi_data)
        spi.close()

led_colors = [
    (255, 0, 0),   # Red
]

ledSTR = LedStripe()
led_updates = [
    (0, (255, 0, 0)),
    (1, (0, 255, 0)),
    (46, (0, 0, 255)),
    (10, (255, 255, 0))
]

ledSTR.shine_leds((255, 0, 0), (0, 255, 0 ), (0, 0, 255), led_updates)
time.sleep(0.5)
