from datasample import sample_generator,f1,f2,f3
from main import generate_population
from tree import Evaluate

def fitness():
    x,y = sample_generator(f1)
    population = generate_population()
    fitness_rand_candidates=[]
    for random_tree in population:
        square_sum = 0
        for i in range(len(x)):
            y_predict = Evaluate(random_tree ,x[i])
            square_sum+=(y_predict-y[i])**2
        fitness_rand_candidates.append(square_sum/len(x))

    return fitness_rand_candidates

