# -*- coding: utf-8 -*-
"""
Workshop 7 Optional exercises
"""

import ws07_graphs as gs
from ws07_solution import lecture_graph


######
# Solving the problem the easy way with the networkx module

import networkx as nx

def create_lecture_graph_networkx():
    """
    Returns lecture graph as networkx graph object
    """
    distances = {
        'A': {'B': 1, 'C': 5},
        'B': {'C': 2, 'D': 5},
        'C': {'D': 2, 'E': 6},
        'D': {'E': 2},
        'E': {}
        }
    
    G=nx.Graph()
    for src, edges in distances.items():
        for dest, w in edges.items():
            G.add_edge(src, dest, weight=w)
    return G

G = create_lecture_graph_networkx()
shortest_dists = nx.single_source_dijkstra_path_length(G, 'A')
all_shortest_dists = nx.all_pairs_dijkstra_path_length(G)





#####
# Dijkstra with a heap queue

import heapq as hq

def dijkstra_heap(graph,start):
    """
    Dijkstra's algorithm with a heap 
    
    Since we don't have a quick deletion from heap, we add everything to heap "lazily".
    That is, if we find a lower Dijkstra score than previously, we don't replace the old one.
    We just add the new one, which will have priority over the old one as the score is lower.
    
    This means the heap may contain the same node several times with different Dijkstra scores.
    This is not a problem for correctness since the heap is ordered by the score.
    But we need to stop the algorithm with the break command after we visit all nodes.
    
    Parameters:
        graph: a Graph (or Digraph) 
        start: starting node for the algorithm
    Returns: 
        dists: dictionary containing shortest distances to all nodes
        prev_nodes: dictionary containing the previous node from which each node was explored
                None for the starting node
    
    Examples:
    >>> graph = gs.Digraph(lecture_graph())
    >>> dists, prev_nodes = dijkstra_heap(graph, 'A')
    >>> [dists['B'], dists['E'], dists['C'], dists['D']]
    [1, 7, 3, 5]
    >>> [prev_nodes['A'], prev_nodes['E'], prev_nodes['C'], prev_nodes['D']]
    [None, 'D', 'B', 'C']
    """    
    X = set()
    A = dict()
    B = dict()
    for src in graph.get_nodes(): # initialize like above
        A[src] = float('Inf')
        B[src] = None
    
    A[start] = 0
    
    # initialize heap queue as (distance,name) tuples
    Q = [(v,k) for k,v in A.items()]   
    hq.heapify(Q) # this initializes the heap queue: the priority ordering is by v, ie the Dijkstra score

     
    while len(Q) > 0:
        if len(X) == len(graph.get_nodes()): break # stop if visited every node
        
        dist,vertex = hq.heappop(Q) # get vertex with best priority Dijkstra score (extract-min from heapq)
        X.add(vertex) # add vertex to X
        
        for dest,weight in graph.children_of(vertex):
            if dest not in X:
                if A[dest] > A[vertex] + weight: # check if Dijkstra score is lowered
                    A[dest] = A[vertex] + weight # update Dijkstra score
                    B[dest] = vertex # update path 
                    hq.heappush(Q,(A[vertex] + weight,dest)) # add dest into heap
    
    return A,B    


#####
# Generate random graphs from list of nodes for comparison purposes

# Generate a random graphs
import random
def random_graph(nodes, nEdges):
    g = gs.Digraph()
    
    #nEdges = 50 # max number of edges
    max_weight = 20  
    nNodes = len(nodes)
    
    connected = set()
    connected.add(nodes[0])
    
    edg = nEdges
    for i in range(1,nNodes):
        # make sure graph is connected by adding an edge from each node to an already connected node
        r = random.randint(0,i-1)
        weight = random.randint(1,max_weight)
        g.add_edge(nodes[i],nodes[r],weight)
        edg -= 1
      
    # Add rest of edges
    for u in range(edg):
        i = random.randint(0,nNodes-1)
        j = random.randint(0,nNodes-1)
        weight = random.randint(1,max_weight)
        g.add_edge(nodes[i],nodes[j],weight)
    
    return g

