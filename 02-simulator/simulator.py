from gates import *


def set_node_value(node, a, b=None):
    # This function sets the value of a node.
    # It should implement the boolean logic for each node type.
    # For example, if the node is an And, it should set the node.value to a & b.
    pass


def simulate(nodes, edges, inputs):
    # This is the main function that runs the simulation.
    # It takes in a list of nodes, a list of edges, and a dictionary of inputs.

    # 1. Set the input values for all the Input nodes.

    # 2. While there are still nodes that have not been evaluated:
    #    a. For each node, get the inputs.
    #    b. If the inputs are ready, evaluate the node and
    #       set the output value. This should use set_node_value.

    # 3. Return the output values for all the Output nodes as a dictionary.

    # Sample part 3.
    # This is what the output should look like (assuming the inputs are set correctly):
    outputs = {}
    for node in nodes:
        if node.node_type == 'Output':
            outputs[node.name] = 0

    return outputs
