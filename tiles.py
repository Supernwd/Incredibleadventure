"""Description du monde dans lequel le joueur évolue."""
__author__ = 'nwd modified from Phillip Johnson'

import items, enemies, actions, world


class MapTile:
    """La classe de base pour une case dans ce monde"""
    def __init__(self, x, y):
        """Créé une nouvelle case avec les paramètres suivants:
        :param x: coordonnée x de la case
        :param y: coordonnée y de la case 
        """
        self.x = x
        self.y = y

    def intro_text(self):
        """Information à afficher lors de l'arrivée dans cette case."""
        raise NotImplementedError()

    def modify_player(self, the_player):
        """Effectue les modifiations sur le joueur à l'arrivée dans cette case."""
        raise NotImplementedError()

    def adjacent_moves(self):
        """Retourne les possibilités de déplacements dans les cases adjacentes."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """retourne toutes les actions possibles dans cette case."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves


class StartingRoom(MapTile):
    def intro_text(self):
        return """
        Vous vous trouvez dans une grotte. Une torche fixée au mur éclaire les environs d'une lumière inquiétante. Vous avez le choix entre quatre directions.
        """

    def modify_player(self, the_player):
        #Room has no action on player
        pass


class EmptyCavePath(MapTile):
    def intro_text(self):
        return """
        Un élargissement du tunnel, sans particularité. Vous devez poursuivre...
        """

    def modify_player(self, the_player):
        #Room has no action on player
        pass


class LootRoom(MapTile):
    """Une pièce qui ajoute quelque chose dans les objets portés par le joueur"""
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, the_player):
        the_player.inventory.append(self.item)

    def modify_player(self, the_player):
        self.add_loot(the_player)


class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        return """
        Vous remarquez quelque chose de brillant dans un coin.
        C'est une dague! Vous la prenez.
        """


class Find5GoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(5))

    def intro_text(self):
        return """
        Quelqu'un a perdu une pièce d'or de 5 shillings. Vous la prenez.
        """


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Votre adversaire vous inflige un dommage de {} points de vie. Il vous reste {} points de vie.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()


class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSpider())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            Une araignée géante saute de sa toile en face de vous ! Défendez-vous !
            """
        else:
            return """
            le corps d'une araignée géante morte jonche le sol.
            """


class OgreRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Ogre())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            Un ogre géant vous barre le passage en vous menaçant de son gourdin !
            """
        else:
            return """
            Le corps sans vie d'un ogre répugnant vous rappelle votre victoire.
            """


class SnakePitRoom(MapTile):
    def intro_text(self):
        return """
        Vous êtes tombé dans un puits remplis de serpents venimeux.
        Alors que leurs dents acérées vous mordent le cou, vous sentez votre conscience s'assombrir...
        Vous êtes mort!
        """

    def modify_player(self, player):
        player.hp = 0


class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return """
        Vous apercevez un rayon lumineux au loin...
        ... Il grandit alors que vous progressez : C'est la lumière du soleil!

        Vous êtes sorti, vous avez gagné !
        """

    def modify_player(self, player):
        player.victory = True
