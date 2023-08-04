from modules.entity import Enemy

class Slime(Enemy):
    def __init__(self):
        super().__init__("Slime", 10, 2, 5, 1, 2)

class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", 15, 4, 5, 1, 2)

enemy_list = (Slime, Goblin)
