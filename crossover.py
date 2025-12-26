from node import Node
from tree import replace_subtree,clone,get_all_nodes,tree_depth
import random


        
        


def crossover_mutation(parent1,parent2,max_depth):
    p1 = clone(parent1)
    p2 = clone(parent2)
    nodeslist_p1= get_all_nodes(p1)   # the node objects are the same as the tree nodes we have.(not a copy)
    nodeslist_p2= get_all_nodes(p2)
    choosen_node_p1 = random.choice(nodeslist_p1)   #this choosen node from p1 tree is actually the same object in the p1 tree.
    choosen_node_p2 = random.choice(nodeslist_p2)
    child1 = replace_subtree(p1,choosen_node_p1,choosen_node_p2)
    child2 = replace_subtree(p2,choosen_node_p2,choosen_node_p1)
    if(  (tree_depth(child1)>max_depth)  or  (tree_depth(child2)>max_depth)  ):
        child1, child2 = crossover_mutation(parent1,parent2,max_depth)

    return child1,child2

