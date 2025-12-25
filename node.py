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

def Evaluate(node,x):
    if(node.is_terminal()):
        if node.value == 'x':      #terminal of type variable
            return x
        else:
            return node.value     #terminal of type constant
    else:
        if(len(node.children)==2):
            first_val = Evaluate(node.children[0],x)
            second_val  = Evaluate(node.children[1],x)
            # for debugging purpose:
            expression = f"{first_val} {node.value} {second_val}"  
            # print(expression)
            match node.value:
                case '+':
                    return first_val + second_val
                case '-':
                    return first_val - second_val
                case '*':
                    return first_val * second_val
                case '/':
                    if second_val == 0:
                        raise Exception("Cannot divide by zero.")
                    return first_val / second_val
                case 'pow':
                    first_element = first_val
                    second_element = second_val
                    return math.pow(first_element,second_element)
                
            if len(node.children1)==1:
                first_val = Evaluate(node.children[0],x)
                match node.value:
                    case 'sin':
                        return math.sin(first_val)
                    case 'cos':
                        return math.cos(first_val)
                    case 'sqrt':
                        return math.sqrt(first_val)


               
tree = Node('/', [
    Node('x'),
    Node(1)
])
print(Evaluate(tree, 2))
print(Evaluate(tree, 5)) 


tree = Node('+', [
    Node(2),
    Node(3)
])

print(Evaluate(tree, 100))