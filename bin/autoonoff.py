#!/usr/bin/env python
import RPi.GPIO as GPIO
import subprocess
import time


SENSOR_PIN = 14
TIME_ON = 20


def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SENSOR_PIN, GPIO.IN)
    subprocess.run(["xset", "dpms", "force", "off"])

    def callback(_):
        subprocess.run(["xset", "dpms", "force", "on"])
        time.sleep(TIME_ON)
        subprocess.run(["xset", "dpms", "force", "off"])

    try:
        GPIO.add_event_detect(SENSOR_PIN, GPIO.RISING, callback=callback)
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        pass

    GPIO.cleanup()


if __name__ == "__main__":
    main()
