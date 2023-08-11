import logging
import time

from relay import Relay
from moisture_sensor import MoistureSensor


class AutoSprinkler:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def test(self):
        interval = 3
        relay = Relay(11)
        moist_sensor = MoistureSensor(40)

        self.logger.info("Starting Test Loop, awaiting Keyboard Interrupt")
        try:
            while True:
                # relay.toggle()
                print(f"Reading: {moist_sensor.get_moisture_reading()}")
                time.sleep(interval)

        except KeyboardInterrupt:
            exit(0)
