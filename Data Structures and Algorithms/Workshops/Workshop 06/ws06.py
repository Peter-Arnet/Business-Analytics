"""
Workshop 6
"""


# This command imports data structures in ws06_data_structures.py
# It will only work if the Spyder working directory is correct
# Change working directory from the folder icon in the top right corner
from ws06_data_structures import Graph, Digraph, Queue, QueueNode


def create_lecture_graph():
    """
    Initializes the undirected graph from the lecture
    
    Uses the add_edge method
    
    Returns Graph object of the lecture graph
    Example use:
    >>> lec_graph = create_lecture_graph()
    >>> [x in lec_graph.children_of('Jared') for x in ['John', 'Helena', 'Donald', 'Paul']]
    [False, False, True, True]
    >>> lec_graph = create_lecture_graph()
    >>> [x in lec_graph.children_of('Helena') for x in ['John', 'Helena', 'Donald', 'Paul']]
    [True, False, False, True]
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    g = Graph()
    g.add_edge('John', 'Helena')
    g.add_edge('John', 'Chris')
    g.add_edge('Helena', 'Chris')
    g.add_edge('Helena', 'Paul')
    
    return g



def bfs(graph, start):
    """ 
    Breadth-first search using Queue data structure
    
    Parameter: 
        graph (Digraph/Graph), 
        start: starting node in the graph
    
    Returns:
        dists, a dictionary of distances to all explored vertices:
            key - node, value - distance from start to that node
        
    Example use:
    >>> lec_graph = create_lecture_graph()
    >>> bfs_dists = bfs(lec_graph, 'John')
    >>> [bfs_dists['Donald'], bfs_dists['Jared']]
    [4, 3]
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    
    # Keep track of queue of nodes to explore next
    q = ____ # Initialize an empty queue
    q.enqueue(start) # add start to queue
    
    # Keep track of explored nodes
    explored = set() # Initialize explored nodes as an empty set
    explored.add(start) # Mark starting node explored
    
    # Keep track of distances from start to all other nodes
    dists = ____ # Initialize distances as an empty dictionary
    dists[start] = 0 # Zero distance from start node to itself
    
    # Main loop
    while ____: # Loop while queue not empty
        v = ____ # Pop the first item from the queue 
        # Explore all adjacent nodes of v
        for w in graph.____(v): # loop through adjacent nodes
            if w not in ____: # If w not explored yet
                explored.____(w) # Mark w explored
                dists[w] = ____ # Calculate distance from start to w based on v's distance
                ____ # Add w to queue to explore from in the future
    return dists


def bfs_track_path(graph, start):
    """ 
    Breadth-first search using Queue data structure, keeping track of paths
    
    Parameter: 
        graph (Digraph/Graph), 
        start: starting node in the graph
    
    Returns:
        dists, a dictionary of distances to all explored nodes:
            key - node, value - distance from start to that node 
        prev_nodes, a dictionary containing the previous node on the path to each node:
            key - node, value - the node from which we found this node; None for starting node
        
    Example use:
    >>> lec_graph = create_lecture_graph()
    >>> bfs_dists, prev_nodes = bfs_track_path(lec_graph, 'John')
    >>> [prev_nodes['Donald'], prev_nodes['Helena'], prev_nodes['John']]
    ['Jared', 'John', None]
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    
    # Copy your bfs code here
    # Modify to keep track of paths using a new dictionary prev_nodes
    # Update this dictionary similarly to dists above, but with previous node info
    

#### 
# To print out path
def print_path(prev_nodes, v):
    """ 
    Based on bfs result prev_nodes, prints out path from starting node to v
    """
    path = ''
    while v is not None:
        path += str(v) + ' -> ' 
        v = prev_nodes[v]
    path = path[:-3] # remove last '-> ' 
    print(path)
    

##### 
# Small worlds and Kevin Bacon

def read_movie_data(filename):
    """ 
    Reads movie data from text file into a graph data structure
    
    Reads each line as connections from first instance of line to other instances
    Assumes file is delimited by /
    
    Returns Graph object
    """
    graph = Graph()
    delimiter = '/'
    with open(filename, "r", encoding="utf8") as ins:
        for line in ins:
            names = line.split(delimiter)
            for i in range(1, len(names)):
                graph.add_edge(names[0], names[i])
    return graph


def print_children(graph, v = None):
    """
    Prints out children nodes
    """
    if v == None: v = input('Enter name: ')
    print(v)
    if graph.has_node(v):
        for w in graph.children_of(v):
            print('  ' + w)
  
    
