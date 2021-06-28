#!/usr/bin/python

# Set these to the correct pins in Broadcom format
pin1 = 2
pin2 = 3
pin3 = 4
pin4 = 0
pin5 = 5
pin6 = 6
pin7 = 1
pin8 = 7

# Set this to 0 if your relay board uses traditional logic (0 = low, 1 = high)
# Set this to 1 if your relay board uses inverted logic (1 = low, 0 = high)
active_low = 1

### Code follows below
import curses
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# Start up with all outputs turned off
if active_low == 1:
    GPIO.setup(pin1, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(pin2, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(pin3, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(pin4, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(pin5, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(pin6, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(pin7, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(pin8, GPIO.OUT, initial=GPIO.HIGH)
else:
    GPIO.setup(pin1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(pin2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(pin3, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(pin4, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(pin5, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(pin6, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(pin7, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(pin8, GPIO.OUT, initial=GPIO.LOW)

def main(window):
    # Turn off cursor
    curses.curs_set(0)

    # Set on and off colours
    if active_low == 1:
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_GREEN)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)
    else:
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_GREEN)

    # Set footer colours
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLUE)

    # Get text positions
    middle_x = curses.COLS // 2
    middle_y = curses.LINES // 2
    bottom_y = curses.LINES - 1

    # Print banner
    window.addstr(1, middle_x - 10, "Relay Control System", curses.A_BOLD)
    
    # Print initial state
    window.addstr(middle_y, middle_x - 7, "1", curses.color_pair(GPIO.input(pin1) + 1) + curses.A_BOLD)
    window.addstr(middle_y, middle_x - 5, "2", curses.color_pair(GPIO.input(pin2) + 1) + curses.A_BOLD)
    window.addstr(middle_y, middle_x - 3, "3", curses.color_pair(GPIO.input(pin3) + 1) + curses.A_BOLD)
    window.addstr(middle_y, middle_x - 1, "4", curses.color_pair(GPIO.input(pin4) + 1) + curses.A_BOLD)
    window.addstr(middle_y, middle_x + 1, "5", curses.color_pair(GPIO.input(pin5) + 1) + curses.A_BOLD)
    window.addstr(middle_y, middle_x + 3, "6", curses.color_pair(GPIO.input(pin6) + 1) + curses.A_BOLD)
    window.addstr(middle_y, middle_x + 5, "7", curses.color_pair(GPIO.input(pin7) + 1) + curses.A_BOLD)
    window.addstr(middle_y, middle_x + 7, "8", curses.color_pair(GPIO.input(pin8) + 1) + curses.A_BOLD)
    
    # Print footer and update screen
    window.addstr(bottom_y, middle_x - 38, "1 through 8: Toggle relay | i: All relays on | o: All relays off | q: Quit", curses.color_pair(3) + curses.A_BOLD)
    window.refresh()

    try:
        # This is our main loop
        while True:
            # Get keys and flush input
            key = window.getch()
            curses.flushinp()

            # Handle inputs
            if key != -1:
                # Toggles
                if key == ord('1'):
                    GPIO.output(pin1, not GPIO.input(pin1))
                if key == ord('2'):
                    GPIO.output(pin2, not GPIO.input(pin2))
                if key == ord('3'):
                    GPIO.output(pin3, not GPIO.input(pin3))
                if key == ord('4'):
                    GPIO.output(pin4, not GPIO.input(pin4))
                if key == ord('5'):
                    GPIO.output(pin5, not GPIO.input(pin5))
                if key == ord('6'):
                    GPIO.output(pin6, not GPIO.input(pin6))
                if key == ord('7'):
                    GPIO.output(pin7, not GPIO.input(pin7))
                if key == ord('8'):
                    GPIO.output(pin8, not GPIO.input(pin8))
                
                # Master on/off toggles
                if key == ord('i'):
                    # Turn on each output slowly
                    if active_low == 1:
                        GPIO.output(pin1, GPIO.LOW)
                        time.sleep(1)
                        GPIO.output(pin2, GPIO.LOW)
                        time.sleep(1)
                        GPIO.output(pin3, GPIO.LOW)
                        time.sleep(1)
                        GPIO.output(pin4, GPIO.LOW)
                        time.sleep(1)
                        GPIO.output(pin5, GPIO.LOW)
                        time.sleep(1)
                        GPIO.output(pin6, GPIO.LOW)
                        time.sleep(1)
                        GPIO.output(pin7, GPIO.LOW)
                        time.sleep(1)
                        GPIO.output(pin8, GPIO.LOW)
                    else:
                        GPIO.output(pin1, GPIO.HIGH)
                        time.sleep(1)
                        GPIO.output(pin2, GPIO.HIGH)
                        time.sleep(1)
                        GPIO.output(pin3, GPIO.HIGH)
                        time.sleep(1)
                        GPIO.output(pin4, GPIO.HIGH)
                        time.sleep(1)
                        GPIO.output(pin5, GPIO.HIGH)
                        time.sleep(1)
                        GPIO.output(pin6, GPIO.HIGH)
                        time.sleep(1)
                        GPIO.output(pin7, GPIO.HIGH)
                        time.sleep(1)
                        GPIO.output(pin8, GPIO.HIGH)
                if key == ord('o'):
                    # Turn off all outputs immediately
                    if active_low == 1:
                        GPIO.output(pin1, GPIO.HIGH)
                        GPIO.output(pin2, GPIO.HIGH)
                        GPIO.output(pin3, GPIO.HIGH)
                        GPIO.output(pin4, GPIO.HIGH)
                        GPIO.output(pin5, GPIO.HIGH)
                        GPIO.output(pin6, GPIO.HIGH)
                        GPIO.output(pin7, GPIO.HIGH)
                        GPIO.output(pin8, GPIO.HIGH)
                    else:
                        GPIO.output(pin1, GPIO.LOW)
                        GPIO.output(pin2, GPIO.LOW)
                        GPIO.output(pin3, GPIO.LOW)
                        GPIO.output(pin4, GPIO.LOW)
                        GPIO.output(pin5, GPIO.LOW)
                        GPIO.output(pin6, GPIO.LOW)
                        GPIO.output(pin7, GPIO.LOW)
                        GPIO.output(pin8, GPIO.LOW)
                        
                # Handle exiting of the program
                if key == ord('q'):
                    GPIO.cleanup()
                    quit()

            # Update screen                    
            window.addstr(middle_y, middle_x - 7, "1", curses.color_pair(GPIO.input(pin1) + 1) + curses.A_BOLD)
            window.addstr(middle_y, middle_x - 5, "2", curses.color_pair(GPIO.input(pin2) + 1) + curses.A_BOLD)
            window.addstr(middle_y, middle_x - 3, "3", curses.color_pair(GPIO.input(pin3) + 1) + curses.A_BOLD)
            window.addstr(middle_y, middle_x - 1, "4", curses.color_pair(GPIO.input(pin4) + 1) + curses.A_BOLD)
            window.addstr(middle_y, middle_x + 1, "5", curses.color_pair(GPIO.input(pin5) + 1) + curses.A_BOLD)
            window.addstr(middle_y, middle_x + 3, "6", curses.color_pair(GPIO.input(pin6) + 1) + curses.A_BOLD)
            window.addstr(middle_y, middle_x + 5, "7", curses.color_pair(GPIO.input(pin7) + 1) + curses.A_BOLD)
            window.addstr(middle_y, middle_x + 7, "8", curses.color_pair(GPIO.input(pin8) + 1) + curses.A_BOLD)
            window.refresh()   
            
            # Wait a bit before looping
            time.sleep(1)
            
    except KeyboardInterrupt:
            GPIO.cleanup()
            quit()

curses.wrapper(main)
