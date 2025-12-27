import numpy as np
from src.gp_runner import  run_gp
from src.data.datasample import load_dataset

x, y = load_dataset("outputs/data/data_f1.csv")

POPULATION_SIZES = [20, 50, 100]
RUNS = 5
GENERATIONS = 50

results = {}

for pop_size in POPULATION_SIZES:
    mses = []

    for run in range(RUNS):
        best_tree, best_fitness = run_gp(x, y,population_size=pop_size,generations=GENERATIONS)
        mses.append(best_fitness)
        print(f"Final Best MSE: {best_fitness:.6f},run number {run} and for generation with population ={pop_size}")

    results[pop_size] = {
        "mean": np.mean(mses),
        "std": np.std(mses),
        "best": np.min(mses)
    }

for k, v in results.items():
    print(f"Pop={k} | mean={v['mean']:.4f} | std={v['std']:.4f} | best={v['best']:.4f}")
