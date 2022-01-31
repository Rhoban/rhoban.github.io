import world

# Ce dictionnaire fait correspondre un noeud à son parent, c'est à dire le noeud qui a permi
# d'y accéder
#
# Par exemple, si on part de la case (0, 0), et que l'on peut se déplacer à droite en (1, 0),
# alors parents[(1, 0)] = (0, 0)
#
# Il permet également de savoir si un noeud a été exploré, et de construire plus tard le chemin
parents = {}

# Distance requise pour atteindre un noeud
distances = {}

# La cible à atteindre, un tuple (x, y)
target = None

def distance_estimation(position):
    """
    Fournit une estimation de la distance entre une case et la cible
    """
    return abs(position[0] - target[0]) + abs(position[1] - target[1])

def explore_node(grid, node):
    """
    On vient de découvrir un nouveau noeud
    """
    global parents, distances, target

    # On regarde tous les mouvements possibles depuis ce noeud
    for move, next_state in world.possible_moves(grid, node[0], node[1]):
        # Si on peut atteindre un noeud qui n'a pas été exploré, on l'enregistre pour plus tard
        if next_state not in parents:
            parents[next_state] = [node, move]
            distances[next_state] = distances[node] + 1

def find_next_node():
    """
    Retourne le noeud ayant la plus petite distance dans la liste courrante
    """
    minimum = None

    for node in distances:
        if minimum is None or distances[node] + distance_estimation(node) < minimum[1]:
            minimum = node, distances[node]

    node = minimum[0]

    return node

def build_path(start):
    """
    Construit un chemin en utilisant les valeurs calculées
    """
    path = []

    # TODO: Construire le chemin à l'aide du dictionnaire parents

    # Le chemin que vous aurez construit est à l'envers, retournons le!
    path.reverse()

    return path

def solve(grid, start):
    global parents, distances, target

    # Initialisation, on place le premier noeud dans ceux à explorer
    target = world.get_target_position(grid)
    distances[start] = 0
    explore_node(grid, start)

    while target not in distances:
        # TODO: Obtenir le prochain noeud à explorer et l'explorer
        pass
    
    return build_path(start)
