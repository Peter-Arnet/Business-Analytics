"""
Workshop 6 solution
"""

##########################################
# Graphs and breadth-first search

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
    g.add_edge('Chris', 'Paul')
    g.add_edge('Chris', 'Vicki')
    g.add_edge('Jared', 'Vicki')
    g.add_edge('Jared', 'Donald')
    g.add_edge('Jared', 'Paul')
    return g



def bfs(graph, start):
    """ 
    Breadth-first search using Queue data structure
    
    Parameter: 
        graph (Digraph/Graph), 
        start: starting node in the graph
    
    Returns:
        dists, a dictionary of distances to all explored vertices
        
    Example use:
    >>> lec_graph = create_lecture_graph()
    >>> bfs_dists = bfs(lec_graph, 'John')
    >>> [bfs_dists['Donald'], bfs_dists['Jared']]
    [4, 3]
    """
    q = Queue() # Initialize a queue
    q.enqueue(start)
    explored = set() # Initialize explored nodes
    explored.add(start)
    dists = dict() # Keep track of distances from start to all other nodes
    dists[start] = 0
    while not q.is_empty():
        v = q.dequeue()
        for w in graph.children_of(v):
            if w not in explored:
                explored.add(w)
                dists[w] = dists[v] + 1
                q.enqueue(w)
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
    >>> lec_graph = create_lecture_graph()
    >>> bfs_dists, bfs_paths = bfs_track_path(lec_graph, 'John')
    >>> [bfs_dists['Donald'], bfs_dists['Jared']]
    [4, 3]
    """
    q = Queue() # Initialize a queue
    q.enqueue(start)
    explored = set() # Initialize explored nodes
    explored.add(start)
    dists = dict() # Keep track of distances from start to all other nodes
    dists[start] = 0
    prev_nodes = dict()
    prev_nodes[start] = None
    while not q.is_empty():
        v = q.dequeue()
        for w in graph.children_of(v):
            if w not in explored:
                explored.add(w)
                dists[w] = dists[v] + 1
                q.enqueue(w)
                prev_nodes[w] = v
    return dists, prev_nodes


#### 
# To print out path
def print_path(prev_nodes, v):
    """ 
    Based on bfs result prev_nodes, prints out path from starting node to v
    """
    path = str()
    while v is not None: 
        path += str(v) + ' -> ' 
        v = prev_nodes[v]
    path = path[:-3]
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
    with open(filename, "r", encoding="utf8") as ins:
        delimiter = '/'
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

#
#g = read_movie_data("movies.txt")                   
#s = 'Bacon, Kevin'
#print_children(g, s)
#
#c = 'Kidman, Nicole'
#
#a,b = bfs_track_path(g, s)
#a[c]
#print_path(b, c)

