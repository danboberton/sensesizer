import time

from sensor.src.relay import Relay
from sensor.src.logging import Log


class AutoSprinkler:

    def __init__(self):
        self.logger = Log("AutoSprinkler")

    def test(self):
        interval = 3
        relay = Relay(11)

        self.logger.print_log("Starting Test Loop, awaiting Keyboard Interrupt")
        try:
            while True:
                relay.toggle()
                time.sleep(interval)

        except KeyboardInterrupt:
            exit(0)
