import random
import src.core.tree as tree
from src.data.datasample import load_dataset
from src.operators.fitness import fitness
from src.operators.parentselection import tournament_selection
from src.operators.crossover import crossover
from src.operators.mutation import mutation
from src.visualization.visualizer import visualize_tree
from src.core.tree import Evaluate


# Runs a Genetic Programming symbolic regression experiment.
# Returns: best_tree, best_fitness
def run_gp(x,y,population_size=20,max_depth=7,generations=50,crossover_rate=0.8,elitism_rate=0.05,visualize=False,vis_dir=None,log=None):

    # Initialization
    population = []
    for _ in range(population_size):
        population.append(tree.RandomTreeGeneration(max_depth))


    for gen in range(generations):

        # Fitness evaluation
        fitness_stats = fitness(population, x, y)
        fitness_stats.sort(key=lambda t: t[1])  # lower MSE is better

        best_tree, best_fitness = fitness_stats[0]
        if log:
            print(f"Generation {gen} | Best MSE: {best_fitness:.6f}")

        # Optional visualization(only visualize when its flag is on.)
        if visualize and vis_dir is not None:
            visualize_tree(best_tree,title=f"Best Tree - Gen {gen}",filename=f"{vis_dir}/best_gen_{gen}")

        # Elitism
        elitism_count = max(1, int(elitism_rate * population_size))
        new_population = [fitness_stats[i][0] for i in range(elitism_count)]  

        # Generate rest
        while len(new_population) < population_size:

            parent1 = tournament_selection(fitness_stats)
            parent2 = tournament_selection(fitness_stats)

            while parent2 is parent1:
                parent2 = tournament_selection(fitness_stats)

            if random.random() < crossover_rate:
                child1, child2 = crossover(parent1, parent2, max_depth)
                new_population.append(child1)

                if len(new_population) < population_size:
                    new_population.append(child2)
            else:
                child = mutation(parent1, max_depth)
                new_population.append(child)

        population = new_population

    # Final evaluation
    fitness_stats = fitness(population, x, y)
    fitness_stats.sort(key=lambda t: t[1])

    best_tree, best_fitness = fitness_stats[0]

    return best_tree, best_fitness
