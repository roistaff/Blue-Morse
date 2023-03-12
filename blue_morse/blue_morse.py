import evdev
from evdev import InputDevice, list_devices
import time
import pymorse
import sys
args = sys.argv
global spacetime
spacetime = 1.5
global devicename
devicename = "BT Shutter"
global retry
retry = 0
def set_spacetime(time):
    spacetime = time
def set_devicename(name):
    devicename = name
def search_device():
    found = 0
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    devices = sorted(devices, key=lambda x: x.name)
    for device in devices:
        if devicename in device.name:
            found = 1
            device_path = device.path
            return device_path
    if found == 0:
        print("No found.Please check device name,etc.Try again.")
        sys.exit()
def main(device_path):
    device =evdev.InputDevice(device_path)
    device.grab()
    text = ""
    end = 3000000000
    while True:
        try:
            print("Blue-Morse")
            print(device)
            print("OUTPUT:")
            for event in device.read_loop():
                if event.type == evdev.ecodes.EV_KEY:
                    outime = time.time()
                    outtime = outime-end
                    if outtime > spacetime:
                        space = 1
                    else:
                        space = 0
                    if event.value ==1:
                        start = time.time()
                    if event.value ==0:
                        end = time.time()
                        t = end - start
                        if t > 0.5:
                            m = "-"
                        else:
                            m = "."
                        if space == 1:
                            text +="_"
                        else:
                            pass
                        text +=m
                        if '_' in text:
                            tt = pymorse.code_to_string(text)
                            print(text,tt,end='\r')
                        else:
                            print(text, end='\r')
        except KeyboardInterrupt:
            print("\n")
            break
        except:
            retry += 1
            if retry == 5:
                break
            print("retry...", end='\r')
            time.sleep(1)
def autostart():
    if len(args) > 1:
        if args[1] == "-sc":
            set_spacetime(float(args[2]))
        elif args[1] == "-dc":
            set_devicename(str(args[2]))
        elif args[1] == "-h":
            print("Blue-Morse help \n command option \n blue-morse -sc (time)  #set space time \n blue-morse -os (txt)  #morse-code sample \n blue-morse -dc (device name)  # set device name. \n Anything else? Please visit Github:https://github.com/roistaff/Blue-Morse")
            sys.exit()
        elif args[1] == "-os":
            sample = pymorse.string_to_code(str(args[2]))
            print("Morse sample:",sample)
        else:
            print("Unknown command.Please write 'blue-morse -h' ")
            sys.exit()
    device=search_device()
    main(device)
