class Entity:
    def __init__(self, max_hp, atk, evade, base_defense):
        self.hp = max_hp
        self.max_hp = max_hp
        self.atk = atk
        self.evade = evade
        self.base_defense = base_defense
        self.defense = base_defense

class Enemy(Entity):
    def __init__(self, name, max_hp, atk, evade, base_defense, exp_gain):
        super().__init__(max_hp, atk, evade, base_defense)
        self.name = name
        self.exp_gain = exp_gain

    def __str__(self):
        return self.name

class Player(Entity):
    def __init__(self, max_hp, atk, evade, base_defense, exp, level, name):
        super().__init__(max_hp, atk, evade, base_defense)
        self.exp = exp 
        self.level = 1

    def LevelUp(self, stat):
        self.exp = 0
        self[stat] += 1

    def __str__(self):
        return self.name