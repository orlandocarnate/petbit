from microbit import *

# declare variables
hungry = False
sleepy = False
bored = True
age = 0
menu = 0

def currentMenu():
    global menu
    if (menu < 3):
        menu += 1
    else:
        menu = 0
    showMenu()

def showMenu():
    global menu
    if menu == 0:
        display.scroll("Feed Me!", delay=50)
    elif menu == 1:
        display.scroll("ZZZzzzzz", delay=50)
    elif menu == 2:
        display.scroll("Time to play!", delay=50)

def activateFunction():
    global menu
    if menu == 0:
        feed_me()
    elif menu == 1:
        display.scroll("Run Sleep()", delay=100)
    else:
        display.scroll("Run Play()!", delay=100)

def feed_me():
    global hungry
    if hungry:
        display.scroll("That was yummy!", delay=100)
        hungry = False
    else:
        display.scroll("I'm Full!", delay=100)

while True:
    gesture = accelerometer.current_gesture()
    if gesture == "shake":
        display.show(Image.CONFUSED)
    elif gesture == "left" or gesture == "right" or gesture == "face up":
        display.show(Image.ASLEEP)
    elif gesture == "up":
        display.show(Image.HAPPY)
    elif gesture == "down":
        display.show(Image.ANGRY)
    sleep(50)

    if button_a.is_pressed():
        currentMenu()

    if button_b.is_pressed():
        activateFunction()