from graphviz import Digraph
import uuid


def visualize_tree(root, title="GP Tree", filename="gp_tree"):
    dot = Digraph(comment=title, format="png")
    dot.attr(rankdir="TB")

    def add_node(node):
        node_id = str(uuid.uuid4())
        dot.node(node_id, label=str(node.value))

        for child in node.children:
            child_id = add_node(child)
            dot.edge(node_id, child_id)

        return node_id

    add_node(root)
    dot.render(filename, cleanup=True)
