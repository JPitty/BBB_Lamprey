
import time
import Adafruit_SSD1306
import Image
import ImageDraw
import ImageFont

# Beaglebone Black pin configuration:
RST = 'P9_15'

# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3D)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing. Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=1, fill=0)

# Load default font.
#font = ImageFont.load_default()

# Alternatively load a TTF font. Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype(filename='Minecraftia.ttf', size=24)

# Write two lines of text.
draw.text((width/2, top),    'The',  font=font, fill=255)
draw.text((width/2, top+20), 'Lamprey', font=font, fill=255)

# Display image.
disp.image(image)
disp.display()
