from tkinter import*
from tkinter import font
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.OUT)
GPIO.output(40,GPIO.LOW)

window.Tk()

myFont = font.Font(family = "Helvetica", size = 36, weight = "bold")

def ledON():
    print("LED BUTTON PRESSED")
    if GPIO.input(40):
        GPIO.output(40,GPIO.LOW)
        ledButton["text"] = "LED ON"
    else:
        GPIO.output(40,GPIO.HIGH)
        ledButton["text"] = "LED OFF"

def exitProgram():
    print("EXIT BUTTON PRESSED")
    GPIO.cleanup()
    window.quit()

window.title("FIRST GUI")
window.geometry("800x400")

exitButton = Button(window, text = "EXIT", font = myFont, command = exitProgram, height = 2, width = 6)
exitButton.pack(side = BOTTOM)

ledButton = Button(window, text = "LED ON", font = myFont, command = ledON, height = 2, width = 8)
ledButton.pack()

window.mainloop()