"""

DSA Workshop 7

"""

# This command imports data structures from ws07_graphs.py
# It will only work if the Spyder working directory is the one where the file is located
# Change the working directory using the folder icon in the top right corner
import ws07_graphs as gs


def lecture_graph():
    """
    Returns the lecture directed graph example adjacency list as a dictionary
    
    Complete the dictionary below
    
    Examples:
    >>> adj_list = lecture_graph()
    >>> adj_list['D']['E']
    2
    >>> 'D' in adj_list['E']
    False
    >>> [adj_list[n][m] for n in 'ABCDE' for m in 'ABCDE' if m in adj_list[n]]
    [1, 5, 2, 5, 2, 6, 2]
    >>> [len(adj_list[n]) for n in 'ABCDE']
    [2, 2, 2, 1, 0]
    """
    distances = {
        'A': {},
        'B': {'C': 2, 'D': 5},
        'C': {},
        'D': {},
        'E': {}
    }
    return distances


def dijkstra(graph, start):
    """ 
    Shortest distances using Dijkstra's algorithm 
    
    Polynomial-time implementation. Assumes graph is connected.
    
    Parameters:
        graph: a Graph (or Digraph) 
        start: starting node for the algorithm
    Returns: 
        dists: dictionary containing shortest distances to all nodes
        prev_nodes: dictionary containing the previous node from which each node was explored
                None for the starting node
    
    Examples:
    >>> graph = gs.Digraph(lecture_graph())
    >>> dists, prev_nodes = dijkstra(graph, 'A')
    >>> [dists['B'], dists['E'], dists['C'], dists['D']]
    [1, 7, 3, 5]
    >>> [prev_nodes['A'], prev_nodes['E'], prev_nodes['C'], prev_nodes['D']]
    [None, 'D', 'B', 'C']
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    
    # Initialize algorithm
    
    # Visited nodes X initially empty  
    X = set()
    X.add(start)
    
    # Previous nodes for Question 3
    prev_nodes = dict()
    
    # Shortest distances to all nodes from s
    A = dict() 
    for src in graph.get_nodes(): 
        A[src] = float('Inf') # initialize to "infinity"
        prev_nodes[src] = None # Previous nodes for Question 3
    A[start] = 0 # distance zero to itself

    # Main loop
    # Loop while we haven't visited all nodes
    while len(X) < len(graph.get_nodes()): 
         
        # Store mininimum edge and distance when looping
        min_edge = [] # list [src, dest, weight]
        min_dist = float('inf')
        
        # Loop through all edges starting in X and not ending in X
        # Find minimum Dijksta score
        for src in X:
            for dest, weight in graph.children_of(src): # edges starting from src
                if dest not in X: # edge not ending in X
                    # Update minimum-Dijkstra-score edge if find one
                    if A[src] + weight < min_dist: 
                        min_edge = [src, dest, weight] 
                        min_dist = A[src] + weight 
        # Update A[min_e_dest] = A[min_e_source] + A[min_e_weight]        
        A[min_edge[1]] = A[min_edge[0]] + min_edge[2]
        
        # Add destination node from min edge to visited nodes
        X.add(min_edge[1])  
    
    return A, prev_nodes


def print_path(prev_nodes,v):
    """ 
    Based on dictionary prev_nodes containing links to previous nodes, prints out path from starting node to v
    """
    path = str()
    while v is not None: 
        path += str(v) + ' -> ' 
        v = prev_nodes[v]
    print(path[:-3])



