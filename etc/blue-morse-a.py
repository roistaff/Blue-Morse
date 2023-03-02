import evdev
import pymorse
import time
global spacetime
spacetime = 1.5
device =evdev.InputDevice("/dev/input/event6")
text = ""
end = 3000000000
while True:
    try:
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
        break
    except:
        print("retry...", end='\r')
        time.sleep(1)
