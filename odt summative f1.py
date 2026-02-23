from machine import Pin, PWM
import neopixel
import time
import random

NUM_LEDS = 16
np = neopixel.NeoPixel(Pin(33), NUM_LEDS)

button = Pin(14, Pin.IN, Pin.PULL_UP)

servo = PWM(Pin(4))
servo.freq(50)

buzzer = Pin(17, Pin.OUT)

groups = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]

while True:
    print("--- NEW ROUND ---")

   
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)
    np.write()

    
    np[0] = (255, 255, 255)
    np.write()
    time.sleep(0.5)

   
    for group in groups:
        for led in group:
            np[led] = (255, 0, 0)
        np.write()

        buzzer.value(1)
        time.sleep(0.03)
        buzzer.value(0)

        time.sleep(0.8)  

   
    wait_time = random.randint(50, 150) 
    start_wait = time.ticks_ms()

    while time.ticks_diff(time.ticks_ms(), start_wait) < wait_time:
        time.sleep(0.001)

  
    for i in range(1, 16):
        np[i] = (0, 0, 0)

   
    np[0] = (0, 255, 0)
    np.write()

   
    buzzer.value(1)
    time.sleep(0.15)
    buzzer.value(0)

   
    go_time = time.ticks_ms()

    while button.value() == 1:
        time.sleep(0.001)

    reaction_ms = time.ticks_diff(time.ticks_ms(), go_time)
    reaction_sec = reaction_ms / 1000
    print("Reaction Time:", reaction_sec, "seconds")

    if reaction_sec < 0.3:
        print("Lightning Fast!")
    elif reaction_sec <= 0.7:
        print("Great Reflexes!")
    else:
        print("Oh too slow!")


    servo.duty(80)
    time.sleep(0.15)
    servo.duty(40)
    time.sleep(0.15)
    servo.duty(80)
    time.sleep(0.15)
    servo.duty(40)

    time.sleep(2)