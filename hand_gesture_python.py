import serial #Serial imported for Serial communication
import time #Required to use delay functions
import pyautogui

ArduinoSerial = serial.Serial('COM3',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 seconds for the communication to get established

while 1:
    incoming = str (ArduinoSerial.readline()) #read the serial data and print it as line
    print( incoming)
    

    if 'previous' in incoming:
        pyautogui.press('right') 

    if 'Vup' in incoming:
        pyautogui.hotkey('ctrl', 'up')
        
    if 'Vdn' in incoming:
        pyautogui.hotkey('ctrl', 'down')
    if 'next' in incoming:
        pyautogui.press('left')

    incoming = "";
