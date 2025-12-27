

from src.data.datasample import load_dataset
from src.gp_runner import run_gp
from src.core.tree import Evaluate

DATASET_PATH = "outputs/data/data_f3.csv"
VIS_DIR = "outputs/trees/f3"

# this line will only be called once to generate the csv file:
# x, y = generate_and_save_dataset(targetfunctions.f1, f"{DATASET_DIR}data_f1.csv")

x, y = load_dataset(DATASET_PATH)

best_tree, best_fitness = run_gp(x,y,population_size=20,max_depth=7,generations=50,visualize=True,vis_dir=VIS_DIR)

print("\n========== FINAL RESULT ==========")
print(f"Final Best MSE: {best_fitness:.6f}")

print("\nSample Comparison (first 10 points):")
predictions = [Evaluate(best_tree, xi) for xi in x]
for i in range(10):
    print(f"x={x[i]:.3f} | target={y[i]:.3f} | pred={predictions[i]:.3f}")
