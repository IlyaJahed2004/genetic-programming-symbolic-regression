from node import Node
import tree
import math
from datasample import sample_generator
import targetfunctions
from fitness import fitness
from parentselection import tournament_selection

POPULATION_SIZE = 20
MAX_DEPTH = 7


def generate_population():
    candidate_answers = []
    for _ in range(POPULATION_SIZE):
       x= tree.RandomTreeGeneration(MAX_DEPTH)
       candidate_answers.append(x)
    return candidate_answers

population = generate_population()
x,y = sample_generator(targetfunctions.f1,"data_f1.csv")

fitness_statistics = fitness(population,x,y)

parent_chosen = tournament_selection(fitness_statistics)