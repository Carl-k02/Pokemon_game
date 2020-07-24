
types = ['fire','water', 'grass']
class Pokemon:
    def __init__(self, name, level, type_, max_health, current_health, is_knocked_out):
        self.name = name
        self.level = level
        self.type_ = type_
        self.max_health = max_health
        self.current_health = current_health
        self.knocked_out = is_knocked_out

    def lose_health(self, health_lost):
        new_current_health = self.current_health - health_lost
        self.current_health = new_current_health
        return '%s now has %s health points' %(self.name, self.current_health)

    def gain_health(self, health_gained):
        new_current_health = self.current_health + health_gained
        self.current_health = new_current_health
        return '%s now has %s health points' %(self.name, self.current_health)

    def knocked_out(self):
        self.knocked_out = True

    def revived(self):
        self.knocked_out = False

    def attack(self, pokemon_attacked):
        if (self.type_ == 'fire' and pokemon_attacked.type_ == 'grass') or (self.type_ == 'grass' and pokemon_attacked.type_ == 'water') or (self.type_ == 'water' and pokemon_attacked.type_ == 'fire'):
            pokemon_attacked.lose_health(self.level * 2)

        elif (self.type_ == 'grass' and pokemon_attacked.type_ == 'fire') or (self.type_ == 'water' and pokemon_attacked.type_ == 'grass') or (self.type_ == 'fire' and pokemon_attacked.type_ == 'water'):
            pokemon_attacked.lose_health(self.level * 0.5)

        else:
            pokemon_attacked.lose_health(self.level)

john = Pokemon('john', 1, 'fire', 20, 20, False)
peter = Pokemon('Peter', 2, 'water', 25, 25, False)


peter.attack(john)
print(john.lose_health(5))
print(peter.current_health)
    


            
        
    
        
