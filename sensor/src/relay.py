import logging
import RPi.GPIO as GPIO


class Relay:

    def __init__(self, pin: int):
        self.pin = pin
        self.logger = logging.getLogger(__name__)

        GPIO.setmode(GPIO.BOARD)
        self.logger.info("GPIO setmode")
        GPIO.setup(pin, GPIO.OUT)
        self.logger.info(f"GPIO pin{self.pin} setup(output)")

        self.on = False
        self.open()

    def open(self):
        GPIO.output(self.pin, GPIO.LOW)
        self.on = False
        self.logger.info(f"Relay on pin {self.pin} open circuit")

    def close(self):
        GPIO.output(self.pin, GPIO.HIGH)
        self.on = True
        self.logger.info(f"Relay on pin {self.pin} close circuit")

    def toggle(self):
        self.open() if self.on else self.close()

    def is_on(self):
        return self.on

    def __del__(self):
        self.open()
        GPIO.cleanup()
        self.logger.info("GPIO cleanup()")
