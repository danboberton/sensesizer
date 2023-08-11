import time

from sensor.src.logging import Log
from sensor.src.sensors.components.relay import Relay
from sensor.src.sensors.iSensor import SensorInterface


class AutoSprinkler(SensorInterface):

    def __init__(self):
        super().__init__()

    def test(self):
        interval = 3
        relay = Relay(11)

        self.print_log("Starting Test Loop, awaiting Keyboard Interupt")
        try:
            while True:
                relay.toggle()
                time.sleep(interval)

        except KeyboardInterrupt:
            exit(0)
