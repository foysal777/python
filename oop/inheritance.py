# 1. Parent Class (Base Blueprint)
class Character:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def introduce(self):
        print(f"👤 Ami {self.name}, amar health holo {self.health}.")


# 2. Child Class (Inherits from Character)
# Bracket er bhetor Parent class er nam likhte hoy
class Warrior(Character):

    def __init__(self, name, health, weapon):
        # super() diye Parent class er __init__ ke dak dewa hoy,
        # jate name ar health automatic set hoye jay!
        super().__init__(name, health)
        self.weapon = weapon  # Warrior er nijoswo extra variable

    # Warrior er nijoswo ekta naya method
    def use_ability(self):
        print(f"⚔️ {self.name} tar {self.weapon} diye bhayonkor attack koreche!")


# 3. Object toiri ebong Check kora
# Warrior kintu introduce() lekha nai tar bhetor, kintu se automatic sheta use korte parbe!
player1 = Warrior("Arjun", 150, "Shurjo Dhanuk")

player1.introduce()  # Parent class er method automatic run hobe!
player1.use_ability()  # Child class er nijoswo method