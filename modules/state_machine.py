from random import choice
from modules.enemies import enemy_list
from modules.entity import Player
from modules.exceptions import NoStateFound

class State:
    def interface(self):
        raise NoStateFound()

class Battle(State):
    def __init__(self):
        self.enemy = choice(enemy_list)()

    def interface(self, inp):
        pass

class Idle(State):
    def __init__(self):
        pass

    def interface(self, inp):
        match inp:
            case "1":
                return Battle()
            case "2":
                return self


class Handler:
    def __init__(self):
        self.current_state = Idle()

    def change_state(self, state):
        self.current_state = state

    def interface(self, inp):
        self.change_state(self.current_state.interface(inp))






