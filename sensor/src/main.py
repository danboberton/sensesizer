from logging import Log
from sensor.src.sensors.auto_sprinkler import AutoSprinkler
from sensors import auto_sprinkler


def main():
    log = Log('Main Log')

    sprinkler = AutoSprinkler(log)
    sprinkler.test()


if __name__ == '__main__':
    main()
