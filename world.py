__author__ = 'nwd modified from Phillip Johnson'

_world = {}
starting_position = (0, 0)

def tile_exists(x, y):
        """Renvoie la case définie par les coordonnées ou None si ces coordonnées n'existent pas dans la map.
        :param x: coordonnée x dans la map
        :param y: coordonnée y dans la map
        :return: la case existante à ces coordonnées, ou None si cette case n'existe pas 
        """
        return _world.get((x, y))


def load_tiles():
    """parcourt le fichier qui décrit la map, et stocke le résultat dans l'objet _world"""
    with open('resources/map.txt', 'r') as f:
        rows = f.readlines()
    x_max = len(rows[0].split('\t'))
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '')
            if tile_name == 'StartingRoom':
                global starting_position
                starting_position = (x, y)
            _world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)


