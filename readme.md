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
