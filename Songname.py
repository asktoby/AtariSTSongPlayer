import sys
import time
import os

# Add path to the custom library
sys.path.append('/home/pi/LCDScreen/lib/')
import LCD1602  # Import the LCD1602 module

# Get full path from command line
full_path = sys.argv[1] if len(sys.argv) > 1 else "Toby's Text Thing"

# Extract the folder name and filename (without extension), replacing underscores with spaces
folder = os.path.basename(os.path.dirname(full_path)).replace('_', ' ')
filename = os.path.splitext(os.path.basename(full_path))[0].replace('_', ' ')

# Chop folder and filename into LCD-friendly lines (16 characters max)
line1 = folder[:16]
line2 = filename[:16]

# Initialize LCD with 16 columns and 2 rows
lcd = LCD1602.LCD1602(16, 2)

# Initialize the backlight using SN3193
led = LCD1602.SN3193()

try:
    # Set the backlight brightness to 100% (range: 0~100)
    led.set_brightness(100)

    # Set and print first line (folder name)
    lcd.setCursor(0, 0)
    lcd.printout(line1)

    # Set and print second line (filename)
    lcd.setCursor(0, 1)
    lcd.printout(line2)

except KeyboardInterrupt:
    lcd.clear()
    del lcd
