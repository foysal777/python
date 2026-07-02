class Hero:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    
    def attack(self, enemy):
        print(f"{self.name} his power is {self.power} attacks {enemy} ")




hero1 = Hero("Hero1", 100, 20)
hero2 = Hero("Hero2", 80, 25)

hero1.attack("govlin")
hero2.attack("troll")