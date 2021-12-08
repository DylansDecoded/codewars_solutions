'''
You are given a node that is the beginning of a linked list. This list always contains a tail and a loop. 
Your objective is to determine the length of the loop.

Note: DO NOT MUTATE NODES!
'''
def loop_size(node):
    node_dict = dict()
    positions = 0
    a_node = node
    
    while a_node != None:
        if a_node not in node_dict:
            positions += 1
            node_dict[a_node] = positions - 1
        else:
            return positions - node_dict[a_node]
        a_node = a_node.next