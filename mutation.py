from tree import get_all_nodes, replace_subtree, tree_depth, RandomTreeGeneration, clone
import random

MUTATION_MAX_DEPTH = 2
MAX_MUTATION_TRIES = 10

def mutation(parent, tree_maxdepth):
    for _ in range(MAX_MUTATION_TRIES):
        parent_clone = clone(parent)

        nodes = get_all_nodes(parent_clone)
        target_node = random.choice(nodes)

        new_subtree = RandomTreeGeneration(MUTATION_MAX_DEPTH)

        mutated_tree = replace_subtree(
            parent_clone,
            target_node,
            new_subtree
        )

        if tree_depth(mutated_tree) <= tree_maxdepth:
            return mutated_tree

    # Fallback: return original parent if all attempts fail
    return parent
