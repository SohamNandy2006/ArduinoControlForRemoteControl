import serial

import serial.tools.list_ports
import logging
import keyboard
from colorama import init, Fore, Back, Style
import time
import os
import sys
import glob
from update_check import isUpToDate
from update_check import update
from update_check import checkForUpdates


   

init(convert=True)
logging.basicConfig(filename='debug.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s' , datefmt='%m/%d/%Y %I:%M:%S %p')


def view_log():
    os.system('notepad.exe debug.log')


def list_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result




def start_comm(com_port):
    baudrate_user = int(input("Enter baudrate (): "))
    while True:
    

        try:
            arduino = serial.Serial(com_port , baudrate_user)
            print(Fore.GREEN + "Connected to Arduino successfully")

            while True:
                if keyboard.is_down('w'):
                    print("Sending data to Arduino: 'w' - " + com_port)
                    try:
                        arduino.write(b's')
                    except error as e:
                        print(Fore.RED + "Operation failed")
                        logging.critical(e)
                elif keyboard.is_down('a'):
                    print("Sending data to Arduino: 'd' - " + com_port)
                    try:
                        arduino.write(b's')
                    except error as e:
                        print(Fore.RED + "Operation failed")
                        logging.critical(e)

                elif keyboard.is_down('s'):
                    print("Sending data to Arduino: 's' - " + com_port)
                    try:
                        arduino.write(b's')
                    except error as e:
                        print(Fore.RED + "Operation failed")
                        logging.critical(e)

                elif keyboard.is_down('d'):
                    print("Sending data to Arduino: 'd' - " + com_port)
                    try:
                        arduino.write(b's')
                    except error as e:
                        print(Fore.RED + "Operation failed")
                        logging.critical(e)


        except:
            print(Fore.RED + "Error: Arduino Not connected on specified port")
            logging.warning("Arduino not connected on COM port {} and baudrate {}".format(com_port,baudrate_user))
            time.sleep(1)
            

def main():

    print("""
    1. Enter Arduino COM_PORT
    2. List COM_PORT(s) (under devlopment)
    3. View log file
    4. Quit
    """)

    while True:
        
        if keyboard.is_pressed('1'):
            print('\n')
            logging.info("User started function: start_comm")
            com_port = input("Enter com_port: " + "COM6")
            start_comm(com_port)
        elif keyboard.is_pressed('2'):
            print('\n')
            logging.info("User started function: list_port")
            print(list_ports())
        elif keyboard.is_pressed('3'):
            print('\n')
            logging.info("User started function: view_log")
            view_log()
        elif keyboard.is_pressed('4'):
            print('\n')
            logging.info("User started function: quit()")
            quit()



def start():
    path = "https://raw.githubusercontent.com/SohamNandy2006/ArduinoControlForRemoteControl/master/main.py"
    up_check = input("Wanna update?\n")
    up_check_input = up_check.lower()
    if up_check_input == 'y':
        update(__file__,path)
    else:
        print("Dont blame me when stuff doesnt works")
        main()
    
start()


