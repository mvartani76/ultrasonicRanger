#Libraries
import RPi.GPIO as GPIO
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
	#print("waiting start")
    #print ("StartTime = %s" % StartTime)
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
	#print("waiting stop")
    #print ("StopTime = %s" % StopTime)
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    #print("TimeElapsed = %s" % TimeElapsed)
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

if __name__ == '__main__':
    try:
        dist_array=[0,0,0]
        i = 0
        while True:
            dist_array[i] = distance()
            #print ("Measured Distance = %.1f cm" % dist)
            i=i+1
            time.sleep(1)
            if i==3:
                #smooth_dist = median(dist_array)
                #dist_array.sort()
                #print(dist_array[1])
                i=0
            dist_array.sort()
            print(i)
            print(dist_array)
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
