# Genetic Programming for Symbolic Regression

This project implements **symbolic regression using Genetic Programming (GP)** in Python.
The goal is to automatically discover a mathematical expression that fits a set of input–output data, without assuming a predefined model structure.

This repository is developed step by step, starting from the core building blocks of Genetic Programming.

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
           /  \ 
          x    3        


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
