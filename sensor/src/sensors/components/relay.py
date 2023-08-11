from sensor.src.logging import Log
import RPi.GPIO as GPIO


class Relay:

    def __init__(self, pin: int):
        self.pin = pin
        self.logger = Log(f"Relay_{pin}")

        GPIO.setmode(GPIO.BOARD)
        self.logger.print_log("GPIO setmode")
        GPIO.setup(pin, GPIO.OUT)
        self.logger.print_log(f"GPIO pin{self.pin} setup()")

        self.on = False
        self.open()

    def open(self):
        GPIO.output(self.pin, GPIO.LOW)
        self.on = False
        self.logger.print_log(f"Relay on pin {self.pin} open circuit")

    def close(self):
        GPIO.output(self.pin, GPIO.LOW)
        self.on = True
        self.logger.print_log(f"Relay on pin {self.pin} close circuit")

    def toggle(self):
        self.open() if self.on else self.close()

    def is_on(self):
        return self.on

    def __del__(self):
        GPIO.cleanup()
        self.logger.print_log("GPIO cleanup()")
