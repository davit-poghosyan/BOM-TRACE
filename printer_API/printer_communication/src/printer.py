import sys
from zebrafy import ZebrafyPDF
from zebrafy import ZebrafyImage
import socket
zebra_ip = "192.168.0.104"  # replace with your printer IP
zebra_port = 9100

# sys.argv[0] is the script name itself: 'printer.py'
# sys.argv[1] is the first argument: printer_ip
# sys.argv[2] is the second argument: label_width
# sys.argv[3] is the third argument: label_height

# ⚠ Always validate argument count to avoid IndexError
if len(sys.argv) < 4:
    print("Usage: python printer.py <printer_ip> <label_width> <label_height>")
    sys.exit(1)

zebra_ip = sys.argv[1]
label_width = int(sys.argv[2])   # Convert from string to int
label_height = int(sys.argv[3])  # Convert from string to int

# Now use these variables in your logic
print(f"Printer IP: {zebra_ip}")
print(f"Label Width: {label_width}")
print(f"Label Height: {label_height}")

def detectLabelSize():
    if label_height <= label_width:
        width = label_width * 203
        height = width / 3
        rotation = 0

        if 800 < width < 850:
            pos_x = 0
        elif 590 < width < 650:
            pos_x = 102
        elif 390 < width < 450:
            pos_x = 203
        elif 150 < width < 250:
            pos_x = 304
        else:
            pos_x = 0
    else:
        # Define fallback values if needed
        height = label_height * 203
        width = height/3
        rotation = 90
        pos_x = 0
        if 800 < height < 850:
            pos_x = 0
        elif 590 < height < 650:
            pos_x = 304
        elif 390 < height < 450:
            pos_x = 203
        elif 150 < height < 250:
            pos_x = 102
        else:
            pos_x = 0


    return {
        "width": width,
        "height": height,
        "pos_x": pos_x,
        "rotation": rotation
    }

def send_to_zpl():
    res = detectLabelSize()
    print(f"height {res["height"]}")
    print(f"width {res["width"]}")
    print(f"pos_x {res["pos_x"]}")
    print(f"rotation {res["rotation"]}")

    with open("/home/davit/Desktop/doubleK/BOM-TRACE/new.pdf", "rb") as pdf:
        zpl_string = ZebrafyPDF(
            pdf.read(),
            format="ASCII",
            invert=True,
            dither=False,
            threshold=128,
            dpi=203,
            width=int(res["width"]),
            height=int(res["height"]),
            pos_x=int(res["pos_x"]),
            pos_y=0,
            rotation=int(res["rotation"]),
            string_line_break=80,
            complete_zpl=True,
            split_pages=True,
        ).to_zpl()

    with open("output.zpl", "w") as zpl:
        zpl.write(zpl_string)


    with open("output.zpl", "rb") as f:
        zpl_data = f.read()


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((zebra_ip, zebra_port))
        s.sendall(zpl_data)

send_to_zpl()