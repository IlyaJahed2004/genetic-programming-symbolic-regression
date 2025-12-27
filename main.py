import random
import tree
from datasample import sample_generator
import targetfunctions
from fitness import fitness
from parentselection import tournament_selection
from crossover import crossover
from mutation import mutation
from visualizer import visualize_tree
from tree import Evaluate

#  Hyperparameters 
POPULATION_SIZE = 20
MAX_DEPTH = 7
GENERATIONS = 50

CROSSOVER_RATE = 0.8
ELITISM_RATE = 0.05

VIS_DIR = "pngs/"



def generate_population():
    return [tree.RandomTreeGeneration(MAX_DEPTH) for _ in range(POPULATION_SIZE)]


#  Initialization 
population = generate_population()
x, y = sample_generator(targetfunctions.f1, "data_f1.csv")


for gen in range(GENERATIONS):

    # Fitness Evaluation 
    fitness_stats = fitness(population, x, y)
    fitness_stats.sort(key=lambda t: t[1])  # lower MSE is better

    best_tree, best_fitness = fitness_stats[0]

    print(f"Generation {gen} | Best MSE: {best_fitness:.6f}")

    #  Visualization (Best Only) 
    visualize_tree(
        best_tree,
        title=f"Best Tree - Gen {gen}",
        filename=f"{VIS_DIR}best_gen_{gen}"
    )
    

    #  Elitism 
    elitism_count = max(1, int(ELITISM_RATE * POPULATION_SIZE))
    new_population = [fitness_stats[i][0] for i in range(elitism_count)]

    #  Generate Rest 
    while len(new_population) < POPULATION_SIZE:

        parent1 = tournament_selection(fitness_stats)
        parent2 = tournament_selection(fitness_stats)

        while parent2 is parent1:
            parent2 = tournament_selection(fitness_stats)

        if random.random() < CROSSOVER_RATE:
            child1, child2 = crossover(parent1, parent2, MAX_DEPTH)
            new_population.append(child1)

            if len(new_population) < POPULATION_SIZE:
                new_population.append(child2)
        else:
            child = mutation(parent1, MAX_DEPTH)
            new_population.append(child)

    population = new_population


#  Final Evaluation 
fitness_stats = fitness(population, x, y)
fitness_stats.sort(key=lambda t: t[1])

best_tree, best_fitness = fitness_stats[0]

print("\n========== FINAL RESULT ==========")
print(f"Final Best MSE: {best_fitness:.6f}")

visualize_tree(
    best_tree,
    title="Final Best Individual",
    filename=f"{VIS_DIR}best_final"
)

#  Compare Prediction vs Target 
predictions = [Evaluate(best_tree, xi) for xi in x]

print("\nSample Comparison (first 10 points):")
for i in range(10):
    print(f"x={x[i]:.3f} | target={y[i]:.3f} | pred={predictions[i]:.3f}")
