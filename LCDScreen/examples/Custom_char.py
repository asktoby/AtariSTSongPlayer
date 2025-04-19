import sys
sys.path.append('../lib/')
import LCD1602
import time

# Initialize the LCD1602 with 16 columns and 2 rows
lcd = LCD1602.LCD1602(16, 2)
# Initialize the SN3193 backlight controller
led = LCD1602.SN3193()

# Set the backlight brightness to 50% (value range from 0 to 100)
led.set_brightness(50)

# Define custom characters (8x5 pixel matrix) to be used on the LCD screen
bell = [0x4, 0xe, 0xe, 0xe, 0x1f, 0x0, 0x4, 0x0]  # Bell pattern
note = [0x2, 0x3, 0x2, 0xe, 0x1e, 0xc, 0x0, 0x0]  # Musical note pattern
clock = [0x0, 0xe, 0x15, 0x17, 0x11, 0xe, 0x0, 0x0]  # Clock pattern
heart = [0x0, 0xa, 0x1f, 0x1f, 0xe, 0x4, 0x0, 0x0]  # Heart pattern
duck = [0x0, 0xc, 0x1d, 0xf, 0xf, 0x6, 0x0, 0x0]  # Duck pattern
check = [0x0, 0x1, 0x3, 0x16, 0x1c, 0x8, 0x0, 0x0]  # Check pattern
cross = [0x0, 0x1b, 0xe, 0x4, 0xe, 0x1b, 0x0, 0x0]  # Cross pattern
retarrow = [0x1, 0x1, 0x5, 0x9, 0x1f, 0x8, 0x4, 0x0]  # Right arrow pattern
aUmlaut = [0xa, 0x0, 0xe, 0x1, 0xf, 0x11, 0xf, 0x0]  # 'ä' umlaut character
oUmlaut = [0xa, 0x0, 0xe, 0x11, 0x11, 0x11, 0xe, 0x0]  # 'ö' umlaut character

# Create custom characters on the LCD
lcd.createChar(0, aUmlaut)  # Create 'ä' character at position 0
lcd.createChar(1, oUmlaut)  # Create 'ö' character at position 1
lcd.createChar(2, clock)    # Create clock character at position 2
lcd.createChar(3, heart)    # Create heart character at position 3
lcd.createChar(4, duck)     # Create duck character at position 4
lcd.createChar(5, check)    # Create check mark character at position 5
lcd.createChar(6, cross)    # Create cross mark character at position 6
lcd.createChar(7, retarrow) # Create right arrow character at position 7

# Display custom characters on the LCD screen
for i in range(0, 8):  # Loop through custom characters 0-7
    lcd.setCursor(i * 2, 0)  # Set cursor at the first row and column 2*i
    lcd.data(i)  # Display the custom character at position i
    lcd.setCursor(i * 2, 1)  # Set cursor at the second row and column 2*i
    lcd.data(i)  # Display the same character on the second row
    time.sleep(0.1)  # Wait for 100ms before moving to the next character
