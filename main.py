from node import Node
import tree
import math


POPULATION_SIZE = 20
MAX_DEPTH = 7


def generate_population():
    candidate_answers = []
    for _ in range(POPULATION_SIZE):
       x= tree.RandomTreeGeneration(MAX_DEPTH)
       candidate_answers.append(x)
    return candidate_answers

population = generate_population()