import argparse
import world
import a_star
import value_iteration

# Seed 32: exemple impossible

parser = argparse.ArgumentParser(prog="World")
parser.add_argument('-m', type=str, help='Mode', default='show')
parser.add_argument('-s', type=int, help='Seed', default=0)
args = parser.parse_args()
mode = args.m
seed = args.s

# Generation du monde
grid = world.generate_grid(seed)
start = world.random_reachable_position(grid)

if mode == 'show':
    # Mode show (par défaut), montre la carte du monde
    world.render(grid, start)
elif mode == 'demo':
    # Démo d'un chemin correct dans le monde de seed 0
    example_path = ('left', 'down', 'left', 'left', 'up', 'left', 'left', 'up')
    world.render(grid, start, example_path)
elif mode == 'a_star':
    # Mode A*
    solution_path = a_star.solve(grid, start)
    world.render(grid, start, solution_path)
elif mode == 'value':
    # Mode value iteration
    solution_path = value_iteration.solve(grid, start)
    world.render(grid, start, solution_path, value_iteration.values)