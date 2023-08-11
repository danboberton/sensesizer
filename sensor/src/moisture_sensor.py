import logging
import RPi.GPIO as GPIO


class MoistureSensor:

    def __init__(self, pin: int):
        self.pin = pin
        self.logger = logging.getLogger(__name__)

        # Pin number, not GPIO number
        GPIO.setmode(GPIO.BOARD)
        self.logger.info("GPIO setmode")
        GPIO.setup(pin, GPIO.IN)
        self.logger.info(f"GPIO pin{self.pin} setup(input)")

    def get_moisture_reading(self):
        return GPIO.input(self.pin)

    def __del__(self):
        GPIO.cleanup()
        self.logger.info("GPIO cleanup()")
