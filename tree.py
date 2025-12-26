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
                    base = first_val
                    exp = second_val

                    # Safe power operator
                    # If base is negative and exponent is not integer then it is invalid
                    if base < 0 and not float(exp).is_integer():
                        return 1.0

                    try:
                        result = math.pow(base, exp)
                    except (ValueError, OverflowError):
                        return 1.0

                    # Final safety check
                    if math.isnan(result) or math.isinf(result):
                        return 1.0

                    return result

                
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




def clone(node):
    if node.is_terminal():
        nodevalue = node.value
        terminal_node = Node(nodevalue,[])
        return terminal_node 
    clonednode_value = node.value
    copiedchildren = []
    cloned_node = Node(clonednode_value,copiedchildren)
    for child in node.children:
        childnode = clone(child)
        copiedchildren.append(childnode)
    return cloned_node



def get_all_nodes(node):
    nodes = [node]
    for child in node.children:
       nodes+=get_all_nodes(child)
    return nodes


def tree_depth(node):
    if(node.is_terminal()):
        return 1
    
    local_children_list=[]
    for child in node.children:
        local_children_list.append(tree_depth(child))

    return 1 + max(local_children_list)




def replace_subtree(current_node, target_node, replacement_subtree):
    if(current_node is target_node):
        return replacement_subtree
    
    new_children=[]
    for child in current_node.children:
        x = replace_subtree(child,target_node,replacement_subtree)
        new_children.append(x)
    return Node(current_node.value, new_children)

    




# tree = Node('/', [Node('x'),Node(1)])
# print(Evaluate(tree, 2))
# print(Evaluate(tree, 5)) 


# tree = Node('+', [Node(2),Node(3)])
# print(Evaluate(tree, 100))
