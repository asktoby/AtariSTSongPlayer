import sys
sys.path.append('../lib/')
import LCD1602  # Import the LCD1602 module
import time  # Import the time module for handling timing and local time

# Initialize the LCD display with 16 columns and 2 rows
lcd = LCD1602.LCD1602(16, 2)

# Initialize the backlight using the SN3193 module
led = LCD1602.SN3193()

# Set the backlight brightness to 50% (range: 0~100)
led.set_brightness(50)

# Uncomment the following line to enable breathing mode for the backlight
# led.set_mode(LCD1602.LED_BREATH_MODE)

try:
    while True:
        # Set the cursor to column 0, row 0
        lcd.setCursor(0, 0)

        # Get the current local time as a list
        T = list(time.localtime())

        # Adjust the day of the week index (+1 to make it 1-indexed)
        T[6] += 1

        # Format each element in the time list as zero-padded 2-digit strings
        T = ["{:0>2}".format(str(i)) for i in T]

        # Display the date (year, month, day, day of the week) on the first row
        lcd.printout(T[0] + ' ' + T[1] + ' ' + T[2] + ' ' + T[6])

        # Set the cursor to column 0, row 1
        lcd.setCursor(0, 1)

        # Display the time (hours, minutes, seconds) on the second row
        lcd.printout(T[3] + ":" + T[4] + ":" + T[5])

        # Pause for 0.1 seconds before updating the display
        time.sleep(0.1)

except KeyboardInterrupt:  # Handle user interruption (Ctrl+C)
    # Clear the LCD display
    lcd.clear()
    # Delete the LCD object to free resources
    del lcd

