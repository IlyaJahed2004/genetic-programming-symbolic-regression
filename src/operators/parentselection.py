import random

TOURNAMENT_SIZE = 3

def tournament_selection(candidates_fitness):
    tournament = random.sample(candidates_fitness, TOURNAMENT_SIZE)

    best_tree, best_fitness = tournament[0]

    for tree, fitness in tournament[1:]:
        if fitness < best_fitness:
            best_tree = tree
            best_fitness = fitness

    return best_tree

