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