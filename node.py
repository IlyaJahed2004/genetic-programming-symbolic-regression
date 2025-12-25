import math

class Node:
    def __init__(self, value, children = None):    # children is a list of node objects.
        self.value = value          # it declares what the node represents: a terminal(constant or variable like 'x').
                                    # or nonterminal(operators)
        self.children = children if children is not None else []

    def is_terminal(self):      # constant numbers and the variable x are called terminals.
        if len(self.children)==0:
            return True
        return False
