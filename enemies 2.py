"""Définition des ennemis dans ce jeu"""
__author__ = 'nwd modified from Phillip Johnson'


class Enemy:
    """classe de base pour tous les ennemis"""
    def __init__(self, name, hp, damage):
        """Cree un nouvel ennemi avec les paramètres suivants :
        :param name: le nom de l'ennemi 
        :param hp: le nombre de points de vie de l'ennemi
        :param damage: le dommage que l'ennemi inflige à chaque attaque
        """
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0


class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="l'araignée géante", hp=10, damage=2)


class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="l'ogre", hp=30, damage=15)
