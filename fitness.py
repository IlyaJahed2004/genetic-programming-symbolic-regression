from tree import Evaluate
import math


LARGE_PENALTY = 1e12

def fitness(population , x,y):    #x is the numpy array of the inputs,y is the corresponding numpy array of outputs.
    candidates_fitness=[]

    for random_tree in population:
        valid = True
        square_sum = 0
        for i in range(len(x)):
            y_predict = Evaluate(random_tree ,x[i])
            # check whether the y_prediction is very large or is nan or none:
            # if the condition is true then we assign a bigpenalty for the fitness of that tree.
            if (y_predict is None or math.isnan(y_predict) or math.isinf(y_predict)):
                square_sum = LARGE_PENALTY
                valid = False
                break

            square_sum+= (y_predict-y[i])**2
            # Overflow during accumulation
            if math.isnan(square_sum) or math.isinf(square_sum):
                square_sum = LARGE_PENALTY
                valid = False
                break
        fitness_value = square_sum
        if(valid): 
            fitness_value = square_sum/len(x)  # this is the mse which is our fitness function.
        else:
            fitness_value = LARGE_PENALTY
        candidates_fitness.append((random_tree,fitness_value))

    return candidates_fitness

