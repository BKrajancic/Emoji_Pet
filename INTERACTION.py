from enum import Enum


class INTERACTION(Enum):
    EXIT = 0
    BUTTON_L = 1
    BUTTON_R = 2
    ROLL = 3
    DISTANCE = 4
    BOUNCE = 5
    ROTATION_CHANGED = 200
    BUTTON_LESS_THAN = 201
    BUTTON_GREATER_THAN = 202
    YEET = 420
