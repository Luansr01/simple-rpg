

class Entity:
    """This is a class representation of the Entity type.

    Args:  
        max_hp (int): Integer value representing the enemy's max hp.
        atk (int): Integer value representing the enemy's attack.
        evade (int): Integer value representing the enemy's evade chance (values between 0 and 100, will be capped to 100 if greater, and capped to 0 if lower).
        base_defense (int): Integer value representing the enemy's defense.
        

    Attributes:
        max_hp (int): Integer value representing the enemy's max hp.
        hp (int): Integer value representing the enemy's current hp.
        atk (int): Integer value representing the enemy's attack.
        evade (int): Integer value representing the enemy's evade chance (values between 0 and 100, will be capped to 100 if greater, and capped to 0 if lower).
        base_defense (int): Integer value representing the enemy's base defense.
        defense (int): Integer value representing the enemy's current defense.

    """
    def __init__(self, max_hp, atk, evade, base_defense):
        self._hp = max_hp
        self._max_hp = max_hp
        self._atk = atk
        self._evade = evade
        self._base_defense = base_defense
        self._defense = base_defense
        self._is_alive = True

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, new_hp):
        if new_hp <= 0:
            self._hp = 0
            self._is_alive = False
        elif new_hp >= self._max_hp or new_hp == "MAX":
            self._hp = self._max_hp
        else:
            self._hp = new_hp

    def _max_hp(self, percent=0):
        if not percent == 0:
            return self._max_hp * (percent / 100)
        else:
            return self._max_hp

    max_hp = property(_max_hp)

    @property
    def atk(self):
        return self._atk

    @property
    def evade(self):
        return self._evade

    @property
    def base_defense(self):
        return self._base_defense

    @property
    def defense(self):
        return self._defense

    @property
    def is_alive(self):
        return self._is_alive

    @is_alive.setter
    def is_alive(self):
        self.is_alive = not self.is_alive

class Enemy(Entity):
    """This is a class representation of the Enemy type.
    This class is a child of entity.Entity.

    Args:
        name (str): Human readable string of the enemy's name.
        exp_gain (int): Integer value representing the exp gained by the player when beating the enemy.

    Attributes:
        name (str): Human readable string of the enemy's name.
        exp_gain (int): Integer value representing the exp gained by the player when beating the enemy.
    """

    def __init__(self, name, max_hp, atk, evade, base_defense, exp_gain):
        super().__init__(max_hp, atk, evade, base_defense)
        self._name = name
        self._exp_gain = exp_gain
    
    def __str__(self):
        return self.name
    
    @property
    def name(self):
        return self._name
    
    @property
    def exp_gain(self):
        return self._exp_gain



class Player(Entity):
    """This is a class representation of the Enemy type.
    This class is a child of entity.Entity.

    Args:
        name (str): Human readable string of the player's name.
        

    Attributes:
        name (str): Human readable string of the player's name.
        exp (int): Integer value representing the player's current exp.
        level (int): Integer value representing the player's current level.
    """
    def __init__(self, max_hp, atk, evade, base_defense, name):
        super().__init__(max_hp, atk, evade, base_defense)
        self._name = name
        self._exp = 0
        self._required_exp = 10
        self._level = 1
    
    def __str__(self):
        return self.name

    def level_up(self, stat):
        """Sets the exp attribute back to 0 and adds 1 to the specified stat.

        Args:
            stat (str): Machine readable name of the status property to add to.
        """
        self.exp = 0
        self._required_exp *= 2
        self[stat] += 1

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def exp(self):
        return self._exp

    @exp.setter
    def exp(self, new_exp):
        self._exp = new_exp

    @property
    def required_exp(self):
        return self._required_exp