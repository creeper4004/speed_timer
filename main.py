import time
import sys

timeLoop = True

Sec = 0
Min = 0
Hour = 0

while True:
    try:
        Sec += 1
        print(str(Hour) + " Hrs " + str(Min) + " Mins " + str(Sec) + " Sec ")
        time.sleep(1)
        if Sec == 60:
            Sec = 0
            Min += 1
            print(str(Min) + " Minute")
            if Min == 60:
                Sec = 0
                Min = 0
                Hour += 1
                print(str(Hour) + " Hours")
    except KeyboardInterrupt:
        break
