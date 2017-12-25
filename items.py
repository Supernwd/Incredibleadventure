"""Les différents objets/item que l'on peut trouver dans le jeu"""
__author__ = 'nwd modified from Phillip Johnson'


class Item():
    """La classe de base pour tous les items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValeur: {}\n".format(self.name, self.description, self.value)


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValeur: {}\nPoints de dommage: {}".format(self.name, self.description, self.value, self.damage)


class Rock(Weapon):
    def __init__(self):
        super().__init__(name="la pierre",
                         description="Un chouette gros caillou, utilisable comme projectile ou objet contondant.",
                         value=0,
                         damage=5)


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="la dague",
                         description="Une petite dague, certes plus dangereuse qu'une simple pierre.",
                         value=10,
                         damage=10)


class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="une pièce d'or",
                         description="Une pièce d'or avec le chiffre {} gravé sur l'avers".format(str(self.amt)),
                         value=self.amt)
