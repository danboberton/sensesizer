from logging import Log
from sensors.auto_sprinkler import AutoSprinkler


def main():
    log = Log('Main Log')

    sprinkler = AutoSprinkler(log)
    sprinkler.test()


if __name__ == '__main__':
    main()
