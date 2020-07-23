
types = {'fire':3,'water':2, 'grass':1}
class Pokemon:
    def __init__(self, name, level, type_, max_health, current_health, is_knocked_out):
        self.name = name
        self.level = level
        self.type_ = type_
        self.max_health = max_health
        self.current_health = current_health
        self.knocked_out = is_knocked_out

    def lose_health(self, health_lost):
        self.health_lost = health_lost
        self.current_health - health_lost
        return self.name +  ' now has ' + str(self.current_health) + ' health points'

    def gain_health(self, health_gained):
        self.health_gained = health_gained
        self.current_health + health_gained
        return self.name + ' now has ' + str(self.current_health) + ' health points'

    def knocked_out(self):
        self.knocked_out == True

    def revived(self):
        self.knocked_out == False

    def attack(self, pokemon_attacked, damage_dealt):
        self.attack = pokemon_attacked
        self.damage_dealt = damage_dealt
        if self.type_ > pokemon_attacked.type_:
             pokemon_attacked.lose_health(self.level * 2)
        elif self.type_ < pokemon_attacked.type_:
            pokemon_attacked.lose_health(self.level * 0.5)
        else:
            pokemon_attacked.lose_health(self.level)


john = Pokemon('John', 4, types['fire'], 20, 20, False)
ben = Pokemon('Ben', 2, types['water'], 15, 15, False)
steve = Pokemon('Steve', 5, types['grass'], 10, 10, False)




            
        
    
        
