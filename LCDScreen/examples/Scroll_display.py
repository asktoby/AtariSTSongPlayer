import sys
sys.path.append('../lib/')
import LCD1602  # Import the LCD1602 module for controlling the LCD display
import time  # Import the time module for delays

# Initialize the LCD with 16 columns and 2 rows
lcd = LCD1602.LCD1602(16, 2)

# Initialize the backlight using SN3193 (for controlling brightness)
led = LCD1602.SN3193()

try:
    # Set the cursor to column 0, row 0 and display text on the first row
    lcd.setCursor(0, 0)
    lcd.printout("Welcome to LCD1602.")  # Show a welcome message

    # Set the cursor to column 0, row 1 and display text on the second row
    lcd.setCursor(0, 1)
    lcd.printout("Let your imagination run wild.")  # Show another message

    # Set the backlight brightness to 50% (value range: 0 to 100)
    led.set_brightness(50)

    # Infinite loop to continuously scroll text across the screen
    while True:
        # Scroll text to the left 14 times
        for i in range(0, 14):
            lcd.scrollDisplayLeft()
            time.sleep(0.5)  # Wait for 500ms between each scroll
        time.sleep(1)
        # Scroll text to the right 14 times
        for i in range(0, 14):
            lcd.scrollDisplayRight()
            time.sleep(0.5)  # Wait for 500ms between each scroll
        time.sleep(1)
        
except KeyboardInterrupt:  # Handle user interruption (Ctrl+C) gracefully
    # Clear the LCD display when interrupted
    lcd.clear()
    # Delete the LCD object to free up resources
    del lcd
