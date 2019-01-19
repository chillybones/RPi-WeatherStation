import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD
from time import sleep

# When numbering_mode is set to BOARD, reference PIN number.
# When numbering_mode is set to BCM, reference the number after GP in the pinout name.
lcd = CharLCD(pin_rs=15, pin_rw=18, pin_e=16, pins_data=[8, 10, 11, 12], numbering_mode=GPIO.BOARD, cols=16, rows=2, dotsize=8)

# Clear the screen of any previous input
lcd.clear()
sleep(1)

counter = 0

lcd.write_string(u'It works!')

while(True):
    # Set the cursor to the second row, 0th column
    lcd.cursor_pos = (1, 0)

    # Timer print string builder
    secondRow = ('UpTime %s m %s s' % (counter/60, counter%60))

    # Add spaces at the end to force out 'hanging' characters
    # This is a symptom of the LCD screen and printed character 'hanging' in memory.
    # If you don't overwrite EVERY character space on a row, anything extending past
    # the last char of the new row will remain.
    while(16 > len(secondRow)):
            secondRow = secondRow + u' '

    lcd.write_string(str(secondRow))
    counter = counter + 1
    # Sleep in python is counted in second, not ms
    sleep(1)
