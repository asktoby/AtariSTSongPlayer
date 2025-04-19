import sys
sys.path.append('../lib/')
import LCD1602  # Import the LCD1602 module
import time  # Import the time module for delays

# Initialize LCD with 16 columns and 2 rows
lcd = LCD1602.LCD1602(16, 2)
lcd.cursor()  # Enable cursor on the LCD

# Initialize the backlight using SN3193
led = LCD1602.SN3193()

# Set the backlight brightness to 50% (range: 0~100)
led.set_brightness(50)

# Text to be displayed
text = "Waveshare"
text1 = "Hello World!"

try:
    # Set the cursor to column 0, row 0
    lcd.setCursor(0, 0)
    lcd.leftToRight()  # Set text direction from left to right

    # Display the text "Waveshare" on the first row
    for i in range(9):  # Loop through the first text
        lcd.data(ord(text[i]))  # Send character to LCD
        time.sleep(0.2)  # Wait for 0.1 second

    lcd.rightToLeft()  # Change text direction to right to left

    # Set initial position for scrolling text
    x = 39  # The X-coordinate of the last pixel
    for i in range(11,-1,-1):  # Loop through the second text
        if i < 2:
            # Scroll display to the right
            lcd.scrollDisplayRight()
            lcd.setCursor(x, 0)  # Set cursor to the updated X position
            x = x - 1  # Move cursor left for each new character
        
        # Display characters of the second text
        lcd.data(ord(text1[i]))
        time.sleep(0.2)  # Wait for 0.1 second
        
    # Uncomment the following lines to enable breathing mode for the backlight
    # led.set_mode(LCD1602.LED_BREATH_MODE)
    # time.sleep(0.1)

except KeyboardInterrupt:  # Handle user interruption (Ctrl+C)
    # Clear the LCD display
    lcd.clear()
    # Delete the LCD object to free resources
    del lcd

