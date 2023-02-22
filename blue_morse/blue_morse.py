import evdev
from evdev import InputDevice, list_devices
import time
import pymorse
import sys
def search_device(searchname="BT Shutter Consumer Control",):
    found = 0
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        if searchname in device.name:
            found = 1
            print(device.path)
            device_path = device.path
            return device_path
    if found == 0:
        print("No found")
        sys.exit()
def main(device_path):
    global device
    device =evdev.InputDevice(device_path)
    global text
    text = ""
    global end
    end = 3000000000
    while True:
        try:
            print(device)
            for event in device.read_loop():
                if event.type == evdev.ecodes.EV_KEY:
                    outime = time.time()
                    outtime = outime-end
                    if outtime > 1.5:
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
            break
        except:
            print("retry...", end='\r')
            time.sleep(1)
def autostart():
    device=search_device()
    main(device)