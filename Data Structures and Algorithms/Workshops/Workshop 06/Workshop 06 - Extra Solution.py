
from ws06_data_structures import Graph, Digraph, Queue, QueueNode


def create_dfs_graph():
    """
    Initializes a test graph
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    g = Graph()
    g.add_edge('John', 'Helena')
    g.add_edge('John', 'Chris')
    g.add_edge('Helena', 'Paul')
    g.add_edge('Chris', 'Paul')
    g.add_edge('Chris', 'Vicki')
    g.add_edge('Jared', 'Vicki')
    g.add_edge('Jared', 'Donald')
    g.add_edge('Jared', 'Paul')
    return g


def dfs(graph, start):
    """
    Depth first search on graph from node start
    
    Parameters: 
        graph (Digraph/Graph), 
        start: starting node in the graph
    
    Returns:
        prev_nodes: dictionary:
            key: node, value: node where this node was reached from
        pop_order: dictionary:
            key: node, value: the order in which this node was removed from the list
         
    Example use:
    >>> lec_graph = create_dfs_graph()
    >>> dfs_paths, pop_order = dfs(lec_graph, 'John')
    >>> abs(pop_order['Chris'] - pop_order['Helena']) > 1
    True
    """
    stack = list() # Initialize a list
    stack.append(start)
    
    explored = set() # Initialize explored nodes
    explored.add(start)
    
    prev_nodes = dict() # Initialize previous nodes
    prev_nodes[start] = None
    
    pop_order = dict() # Initialize pop order
    pop_order[start] = 0
    counter = 0
    while len(stack) > 0:
        v = stack.pop()
        counter += 1
        pop_order[v] = counter
        for w in graph.children_of(v):
            if w not in explored:
                explored.add(w)
                stack.append(w)
                prev_nodes[w] = v
    return prev_nodes, pop_order



