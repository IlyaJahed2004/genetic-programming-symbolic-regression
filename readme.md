# Genetic Programming for Symbolic Regression
---
  This project implements Symbolic Regression using Genetic Programming (GP) in Python.
  The goal is to automatically discover a mathematical expression that approximates a target function, without assuming a predefined model structure.

  The project is implemented step by step, following standard academic Genetic Programming practices, with a strong focus on robustness, numerical stability, and modular design.

 ## Project Structure

  The repository is organized into logical modules to ensure clarity, scalability, and maintainability:

  src/

  ├── core/

  │ ├── node.py # Expression tree node definition

  │ └── tree.py # Tree evaluation, cloning, traversal utilities

  │

  ├── operators/

  │ ├── fitness.py # Fitness evaluation (MSE + penalty handling)

  │ ├── parentselection.py # Tournament selection

  │ ├── crossover.py # Depth-constrained subtree crossover

  │ └── mutation.py # Subtree mutation operator

  │

  ├── data/

  │ ├── datasample.py # Dataset generation with noise

  │ └── targetfunctions.py # Target regression functions

  │

  ├── visualization/

  │ └── visualizer.py # Graphviz-based tree visualization

  │
  outputs/

  ├── trees/

  │ └── f1/ # Tree visualizations per generation

  │

  └── data/

  │ └── data_f1.csv # Generated datasets

  │


  This modular structure:

  avoids circular dependencies,

  makes experimentation easier,

  and reflects real research-grade code organization.

---



## Step 1: Expression Tree Representation

In Genetic Programming, each candidate solution (chromosome) is represented as an **expression tree**:

- **Internal nodes** represent operators (e.g. `+`, `-`, `*`, `/`)
- **Leaf nodes** represent terminals:
  - the input variable `x`
  - numeric constants

### Example Tree

The expression:
 x + 3

is represented as:   

          +
        /   \ 
       x     3        

# Genetic Programming for Symbolic Regression
---
  This project implements Symbolic Regression using Genetic Programming (GP) in Python.
  The goal is to automatically discover a mathematical expression that approximates a target function, without assuming a predefined model structure.

  The project is implemented step by step, following standard academic Genetic Programming practices, with a strong focus on robustness, numerical stability, and modular design.

 ## Project Structure

  The repository is organized into logical modules to ensure clarity, scalability, and maintainability:

  src/

  ├── core/

  │ ├── node.py # Expression tree node definition

  │ └── tree.py # Tree evaluation, cloning, traversal utilities

  │

  ├── operators/

  │ ├── fitness.py # Fitness evaluation (MSE + penalty handling)

  │ ├── parentselection.py # Tournament selection

  │ ├── crossover.py # Depth-constrained subtree crossover

  │ └── mutation.py # Subtree mutation operator

  │

  ├── data/

  │ ├── datasample.py # Dataset generation with noise

  │ └── targetfunctions.py # Target regression functions

  │

  ├── visualization/

  │ └── visualizer.py # Graphviz-based tree visualization

  │
  outputs/

  ├── trees/

  │ └── f1/ # Tree visualizations per generation

  │

  └── data/

  │ └── data_f1.csv # Generated datasets

  │


  This modular structure:

  avoids circular dependencies,

  makes experimentation easier,

  and reflects real research-grade code organization.

---



## Step 1: Expression Tree Representation

In Genetic Programming, each candidate solution (chromosome) is represented as an **expression tree**:

- **Internal nodes** represent operators (e.g. `+`, `-`, `*`, `/`)
- **Leaf nodes** represent terminals:
  - the input variable `x`
  - numeric constants

### Example Tree

The expression:
 x + 3

is represented as:   

          +
        /   \ 
       x     3        


Expression evaluation is implemented using a recursive function.  
For terminal nodes, the evaluation returns either the input value (`x`) or the constant stored in the node.  
For operator nodes, the function first evaluates the child subtrees and then applies the operator to the resulting values.

This recursive evaluation closely follows the structure of the expression tree and forms the foundation for applying Genetic Programming operators such as crossover and mutation in later steps.



## Step 2: Safe Operators and Robust Evaluation

During the evolution process, Genetic Programming generates many candidate expressions.
Some of these expressions may be mathematically invalid, such as division by zero or square roots of negative values.

Crashing the algorithm because of a single invalid individual would stop the entire evolutionary process.
Instead, invalid operations are handled using **safe operators** that return bounded values.

### Safe Division

When division by zero occurs, a constant value is returned instead of raising an exception:

- This prevents runtime errors
- Invalid expressions receive poor fitness naturally
- The evolutionary process continues without interruption

### Safe Square Root

For square root operations, negative inputs are handled safely by applying the square root to the absolute value:

- This avoids domain errors
- Keeps evaluation stable for randomly generated expressions

### Design Rationale

Invalid individuals are not removed explicitly.
Instead, they are evaluated safely and assigned poor fitness values, allowing natural selection to eliminate them over generations.

This approach ensures numerical stability while preserving the exploratory nature of Genetic Programming.





## Step 3: Random Expression Tree Generator

A Python module for generating random mathematical expression trees with configurable probabilities and depth constraints.

This is useful for:
- Genetic Programming
- Symbolic Regression
- Expression Synthesis
- Evolutionary Algorithms

---

## Features

- Depth-limited tree generation
- Probabilistic operator vs terminal selection
- Probabilistic variable vs constant terminals
- Separate unary and binary operator handling
- Clean and extensible design

---

## Operator Sets

### Unary Operators
- `sin`
- `cos`
- `sqrt`

### Binary Operators
- `+`
- `-`
- `*`
- `/`
- `pow`

---

## Probability Model

|      Decision      | Probability |
|--------------------|-------------|
Operator vs Terminal | 70%     30% |
Unary vs Binary      | 40%     60% |
Variable vs Constant | 70%     30% |

All probabilities are easy to adjust in the code.

---

## Usage

```python
tree = RandomTreeGeneration(max_depth=4)
```


## Step 4: Initial Population Generation

In Genetic Programming, evolution begins with an initial population of randomly generated candidate solutions.

Each candidate solution is represented as an expression tree and is generated using the random tree generation procedure with a fixed maximum depth.

### Population Initialization

An initial population is created by repeatedly generating random trees:

- Each tree represents a different symbolic expression
- Tree depth is limited to prevent excessive complexity
- Randomness ensures diversity among candidate solutions

This population serves as the starting point for the evolutionary process, where individuals will later be evaluated, selected, and modified through genetic operators.

At this stage, no fitness evaluation or selection is applied; the goal is solely to create a diverse set of candidate expressions.




## Step5: Dataset Generation

This step implements a dataset generation module that samples input–output pairs from predefined mathematical functions. The generated datasets are intended for use in regression, symbolic modeling, and evolutionary computation tasks.

---

### Features

- Generates fixed-size datasets (default: 2000 samples)
- Supports multiple target functions
- Applies controlled random noise
- Enforces valid input domains
- Exports datasets to CSV format

---

### Supported Functions

- **f1(x)** = x² + 2x + 1  
- **f2(x)** = 0.2x + sin(3x)  
- **f3(x)** = x³ + log(x + 1)

---

### Sampling Strategy

- Input values (`x`) are sampled uniformly:
  - `[-100, 100]` for f1 and f2
  - `[-0.9, 100]` for f3 to avoid invalid logarithmic values
- Output values (`y`) are computed from the selected function
- Gaussian noise is applied multiplicatively to simulate real-world data

---

### Data Format

Datasets are stored as CSV files with the following structure:

```text
x,y
x₁,y₁
x₂,y₂
...
```



## Step6: Fitness Evaluation and Robustness

In this project, symbolic regression is performed using Genetic Programming (GP).  
Each individual in the population represents a mathematical expression encoded as a tree.

### Fitness Function

The fitness of each individual is evaluated using **Mean Squared Error (MSE)** between:
- predicted outputs generated by the tree, and
- true outputs from the target function dataset.

Lower fitness values indicate better individuals.

### Robust Fitness Handling

Due to the stochastic nature of GP, some expressions may produce invalid numerical results during evaluation (e.g., NaN, infinity, or undefined values).

To ensure robustness:
- Expression evaluation is protected using safe operators.
- Fitness evaluation detects invalid predictions.
- Any individual producing an invalid output for at least one sample is assigned a **large penalty fitness value**.

This prevents:
- crashes during evolution,
- dominance of unstable expressions,
- circular dependencies between modules.

Invalid individuals are naturally removed during the selection process through evolutionary pressure.

---

This design ensures numerical stability, robustness, and proper evolutionary behavior.



## Step7: Parent Selection (Tournament Selection)

Parent selection in this project is implemented using **deterministic tournament selection**.

### How Tournament Selection Works

1. A fixed number of individuals (`k`, tournament size) are randomly sampled from the population.
2. Their fitness values are compared.
3. The individual with the **lowest fitness (MSE)** is selected as the parent.

This selection process is repeated whenever a parent is needed.  
For crossover, tournament selection is executed twice to select two parents.

### Why Tournament Selection?

Tournament selection was chosen because it:
- does not require fitness normalization,
- is robust to large penalty values,
- handles noisy fitness evaluations well,
- is commonly used in Genetic Programming for symbolic regression.

In this implementation, the tournament size is set to **3**, providing a balanced trade-off between exploration and exploitation.


## Step 8: Elitism

Elitism is used to preserve the best-performing individuals in each generation of the genetic programming process.

After fitness evaluation, individuals are ranked using Mean Squared Error (MSE). A fixed percentage (5%) of the top-performing individuals is directly copied into the next generation without any genetic modification.

This strategy ensures that high-quality symbolic expressions are not lost due to stochastic effects of crossover or mutation and improves the stability of the evolutionary process.



## Step9: Crossover and Tree Utilities

In this stage of the project, subtree-based crossover for Genetic Programming is implemented.
This requires several fundamental tree manipulation utilities.

### Tree Cloning

Before performing crossover, parent trees are cloned to avoid modifying individuals
that may later be reused for selection or elitism.

Cloning is implemented as a deep recursive copy of the tree structure.

### Collecting Tree Nodes

A recursive traversal function is used to collect all nodes in a tree.
This enables random selection of crossover points while preserving node identity.

### Subtree Replacement

Crossover is implemented by replacing a randomly selected subtree in one parent
with a subtree from another parent.

The replacement is performed using a recursive reconstruction strategy:
- If the current node is the selected target node, the replacement subtree is returned.
- Otherwise, the node is rebuilt from recursively processed children.

This approach avoids in-place mutation and ensures correctness.

### Depth-Constrained Crossover

After crossover, offspring trees are checked against a maximum depth constraint.
If the constraint is violated, the crossover operation is retried.

This prevents uncontrolled tree growth (bloat).

### Key Properties

- Parents are never modified
- Subtree identity is preserved
- Tree structure is safely reconstructed
- Depth constraints are enforced

This implementation follows standard academic Genetic Programming practices.




## Step 10: Mutation Operator

Mutation is one of the core genetic operators used to maintain diversity in the population
and prevent premature convergence.

### Overview

In this project, mutation is implemented as **subtree mutation**, which is the standard
approach in Genetic Programming.

The mutation process works as follows:

1. A parent tree is cloned to avoid modifying the original individual.
2. A random node is selected from the cloned tree.
3. A new random subtree is generated with a limited maximum depth.
4. The selected node is replaced by the newly generated subtree.
5. If the resulting tree exceeds the maximum allowed depth, the mutation is retried.
6. If all retries fail, the original parent is returned unchanged.

### Design Choices

- **Subtree mutation** was chosen instead of regenerating entire trees to ensure
  localized structural changes.
- A retry limit is used to prevent infinite recursion when depth constraints cannot be satisfied.
- All mutation operations are performed on cloned trees to preserve population integrity.

### Benefits

- Maintains genetic diversity
- Prevents stagnation in local minima
- Respects tree depth constraints
- Safe against unintended side effects

### Parameters

- `MUTATION_MAX_DEPTH`: Maximum depth of the randomly generated mutation subtree
- `tree_maxdepth`: Maximum allowed depth of the full program tree
- `MAX_MUTATION_TRIES`: Safety limit for mutation retries

This mutation strategy follows standard academic Genetic Programming practices.



 
## Step11: Main Evolutionary Loop

This project implements a complete **Genetic Programming (GP)** pipeline for symbolic regression.  
The evolutionary process iteratively improves a population of expression trees to approximate a target function.

### Evolutionary Steps per Generation

Each generation follows these steps:

1. **Fitness Evaluation**
   - Every individual (expression tree) is evaluated using Mean Squared Error (MSE).
   - Invalid evaluations (NaN, Inf, overflow, domain errors) are penalized with a large fitness value.

2. **Elitism**
   - A fixed percentage (5%) of the best individuals is directly copied to the next generation.
   - This guarantees that high-quality solutions are never lost.

3. **Parent Selection**
   - Tournament selection is used.
   - Random subsets of individuals compete, and the one with the lowest fitness is selected.

4. **Crossover**
   - Two parents are cloned.
   - Random nodes are selected from each tree.
   - Subtrees are swapped using a recursive subtree replacement.
   - A maximum number of attempts is enforced to avoid infinite recursion.
   - Offspring exceeding the maximum depth are discarded.

5. **Mutation**
   - A random node in the tree is replaced with a newly generated random subtree.
   - Mutation depth is strictly bounded to control bloat.

6. **Population Update**
   - New individuals are added until the population size is restored.
   - The process repeats for a fixed number of generations.

---

## Robustness and Safety Mechanisms

Several safeguards were implemented to ensure stability:

- **Safe operators** (division, power, sqrt) prevent runtime crashes.
- **Fitness penalties** handle invalid numerical results.
- **Depth constraints** prevent uncontrolled tree growth.
- **Crossover retry limits** eliminate infinite recursion risks.
- **Tree cloning** ensures parents are never modified in-place.

---

## Visualization

At each generation:
- The **best individual** is visualized as a tree using Graphviz.
- Visualization helps track structural evolution and detect bloat or degeneration.

---

## Final Evaluation

After the final generation:
- The best evolved individual is evaluated on sample inputs.
- Predictions are compared with the true target function values.
- This provides a qualitative and quantitative assessment of approximation accuracy.

Example output:

x = -70.142 | target = 5119.425 | pred = 4920.609

x = 93.657 | target = 8815.183 | pred = 8771.347

x = -0.565 | target = 0.173 | pred = -0.425


The results demonstrate that the evolved symbolic expression closely approximates the target function.


## How to Run

From the project root directory, run:

```bash
python -m src.main
```

  update this readm eand give me the final readme.actually for running the file hyperparameter_analysis file i should run this command:python -m src.scripts.hyperparameter_analysis  and what i mean by hyperparameter tuning is this:

```bash
python -m src.scripts.hyperparameter_analysis
```