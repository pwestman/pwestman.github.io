import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(16,GPIO.IN)
GPIO.setup(18,GPIO.IN)
GPIO.setup(11,GPIO.IN)
GPIO.setup(13,GPIO.IN)
GPIO.setup(12,GPIO.IN)
GPIO.setup(15,GPIO.IN)
GPIO.setup(29,GPIO.IN)
GPIO.setup(31,GPIO.IN)
GPIO.setup(33,GPIO.IN)
GPIO.setup(35,GPIO.IN)

count=0
gate1=1
gate2=1
gate3=1
gate4=1
gate5=1

try:
    while True:
        if GPIO.input(16)==0:
            if GPIO.input(18)==0:
                if gate1==1:
                    count+=1
                    GPIO.output(22,True)
                    time.sleep(0.2)
                    GPIO.output(22,False)
                    print count
                    gate1=0
        elif GPIO.input(18)==0:
            if GPIO.input(16)==0:
                if gate1==1:
                    count-=1
                    GPIO.output(22,True)
                    time.sleep(0.1)
                    GPIO.output(22,False)
                    time.sleep(0.1)
                    GPIO.output(22,True)
                    time.sleep(0.1)
                    GPIO.output(22,False)
                    print count
                    gate1=0
        else:
            gate1=1

        if GPIO.input(11)==0:
            if GPIO.input(13)==0:
                if gate2==1:
                    count+=1
                    GPIO.output(22,True)
                    time.sleep(0.2)
                    GPIO.output(22,False)
                    print count
                    gate2=0
        elif GPIO.input(13)==0:
            if GPIO.input(11)==0:
                if gate2==1:
                    count-=1
                    GPIO.output(22,True)
                    time.sleep(0.1)
                    GPIO.output(22,False)
                    time.sleep(0.1)
                    GPIO.output(22,True)
                    time.sleep(0.1)
                    GPIO.output(22,False)
                    print count
                    gate2=0
        else:
            gate2=1

        if GPIO.input(12)==0:
            if GPIO.input(15)==0:
                if gate3==1:
                    count+=1
                    GPIO.output(22,True)
                    time.sleep(0.2)
                    GPIO.output(22,False)
                    print count
                    gate3=0
        elif GPIO.input(15)==0:
            if GPIO.input(12)==0:
                if gate3==1:
                    count-=1
                    GPIO.output(22,True)
                    time.sleep(0.1)
                    GPIO.output(22,False)
                    time.sleep(0.1)
                    GPIO.output(22,True)
                    time.sleep(0.1)
                    GPIO.output(22,False)
                    print count
                    gate3=0
        else:
            gate3=1

        if GPIO.input(29)==0:
            if GPIO.input(31)==0:
                if gate4==1:
                    count+=1
                    GPIO.output(22,True)
                    time.sleep(0.2)
                    GPIO.output(22,False)
                    print count
                    gate4=0
        elif GPIO.input(31)==0:
            if GPIO.input(29)==0:
                if gate4==1:
                    count-=1
                    GPIO.output(22,True)
                    time.sleep(0.1)
                    GPIO.output(22,False)
                    time.sleep(0.1)
                    GPIO.output(22,True)
                    time.sleep(0.1)
                    GPIO.output(22,False)
                    print count
                    gate4=0
        else:
            gate4=1

        if GPIO.input(33)==0:
            if GPIO.input(35)==0:
                if gate5==1:
                    count+=1
                    GPIO.output(22,True)
                    time.sleep(0.2)
                    GPIO.output(22,False)
                    print count
                    gate5=0
        elif GPIO.input(35)==0:
            if GPIO.input(33)==0:
                if gate5==1:
                    count-=1
                    GPIO.output(22,True)
                    time.sleep(0.1)
                    GPIO.output(22,False)
                    time.sleep(0.1)
                    GPIO.output(22,True)
                    time.sleep(0.1)
                    GPIO.output(22,False)
                    print count
                    gate5=0
        else:
            gate5=1

finally:
    GPIO.cleanup()
