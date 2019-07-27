import sys
from Scene_Main import Scene_Main
import cProfile


def run():
    main = Scene_Main(60, 1)
    main.loop()


if __name__ == '__main__':
    run()
