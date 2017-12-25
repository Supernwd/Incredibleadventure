"""Les actions qu'un joueur peut accomplir dans le jeu"""
__author__ = 'nwd modified from Phillip Johnson'

from player import Player


class Action():
    """La classe de base pour toutes les actions"""
    def __init__(self, method, name, hotkey, **kwargs):
        """Créée une action avec les paramètres suivants :
        :param method: la fonction d'objet à utiliser
        :param name: le nom de l'action 
        :param ends_turn: Vrai si le tour est terminé après l'action, faux dans le cas contraire
        :param hotkey: La touche que le joueur doit utiliser pour déclencher l'action 
        """
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs

    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)


class MoveNorth(Action):
    def __init__(self):
        super().__init__(method=Player.move_north, name='Aller au nord (n)', hotkey='n')


class MoveSouth(Action):
    def __init__(self):
        super().__init__(method=Player.move_south, name='Aller au sud (s)', hotkey='s')


class MoveEast(Action):
    def __init__(self):
        super().__init__(method=Player.move_east, name='Aller à l\'est (e)', hotkey='e')


class MoveWest(Action):
    def __init__(self):
        super().__init__(method=Player.move_west, name='Aller à l\'ouest (o)', hotkey='o')


class ViewInventory(Action):
    """Affiche l'inventaire"""
    def __init__(self):
        super().__init__(method=Player.print_inventory, name='Inventaire (i)', hotkey='i')


class Attack(Action):
    def __init__(self, enemy):
        super().__init__(method=Player.attack, name="Attaquer (a)", hotkey='a', enemy=enemy)


class Flee(Action):
    def __init__(self, tile):
        super().__init__(method=Player.flee, name="Fuir (f)", hotkey='f', tile=tile)