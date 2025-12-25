from node import Node
import math
import random



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
                        return 1    #Crashing the algorithm because of a single invalid individual would stop the entire evolutionary process.
                                    # so we return a bounded value.
                    return first_val / second_val
                case 'pow':
                    first_element = first_val
                    second_element = second_val
                    return math.pow(first_element,second_element)
                
        if len(node.children)==1:
            first_val = Evaluate(node.children[0],x)
            match node.value:
                case 'sin':
                    return math.sin(first_val)
                case 'cos':
                    return math.cos(first_val)
                case 'sqrt':
                    if(first_val<0):
                        return math.sqrt(abs(first_val))
                    return math.sqrt(first_val)




Variables = ['x']
unary_ops = ['sin', 'cos', 'sqrt']
binary_ops = ['+', '-', '*', '/', 'pow']


def terminal_chooser():
    if random.random() < 0.7:
        return Node('x')
    else:
        return Node(random.randint(0, 5))


def RandomTreeGeneration(max_depth):
    # Base case: force terminal
    if max_depth == 0:
        return terminal_chooser()

    max_depth -= 1

    # 70% operator, 30% terminal
    if random.random() < 0.7:

        # Choose unary vs binary operator
        # Example: 40% unary, 60% binary
        if random.random() < 0.4:
            operator = random.choice(unary_ops)
            child = RandomTreeGeneration(max_depth)
            return Node(operator, [child])

        else:
            operator = random.choice(binary_ops)
            child1 = RandomTreeGeneration(max_depth)
            child2 = RandomTreeGeneration(max_depth)
            return Node(operator, [child1, child2])

    else:
        # Terminal node
        return terminal_chooser()









# tree = Node('/', [Node('x'),Node(1)])
# print(Evaluate(tree, 2))
# print(Evaluate(tree, 5)) 


# tree = Node('+', [Node(2),Node(3)])
# print(Evaluate(tree, 100))
