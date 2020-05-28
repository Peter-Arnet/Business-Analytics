test = {
  'name': 'Recap',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> L = ['mouse', 'cat', 'dog', 'mouse', 'bird', 'cow', 'cow', 'cow']
          >>> s = set(L)
          >>> len(s)
          195efcf7adaff6b00632641ff419abeb
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> x = 'Hey you'
          >>> s = set(x)
          >>> len(s)
          afc51ad5928e36dd464d4189e592c81b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> s.update('hey')
          >>> len(s)
          eb9e54dc12cdf12a71ea4e030fc78589
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> s = {'bird', 'cat', 'cow', 'dog', 'mouse'}
          >>> L  = ['mouse', 'moose', 'dog', 'moose', 'mouse', 'moosemouse']
          >>> count = 0
          >>> for item in L:
          ...     if item in s:
          ...         count += 1
          >>> count
          64712977b8cab3a8838d3777d834fb26
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> class Digraph(object):
          ...    def __init__(self):
          ...        self.edges = {}
          ...        self.num_edges = 0
          ...      
          ...    def add_node(self,node):
          ...        # Adds a node to graph (based on key value)       
          ...        self.edges[node] = set()
          ...    def add_edge(self,src,dest):
          ...        # Adds the (v,w) edge, making sure the two nodes exist
          ...        if not self.has_node(src): 
          ...            self.add_node(src)
          ...        if not self.has_node(dest): 
          ...            self.add_node(dest)
          ...        if not self.has_edge(src, dest):
          ...            self.num_edges += 1
          ...            self.edges[src].add(dest)
          ...    def children_of(self, v):
          ...        # Returns a node's children
          ...        return self.edges[v]
          ...    def has_node(self, v):
          ...        # Checks whether the node is in graph already
          ...        return v in self.edges
          ...    def has_edge(self, v, w):
          ...        # Checks whether there is an edge from v to w
          ...        return w in self.edges[v]
          >>> Z = Digraph()
          >>> Z.add_edge('Grandad', 'Dad')
          >>> Z.add_edge('Grandad', 'Uncle Sam')
          >>> Z.add_edge('Dad', 'Me')
          >>> Z.add_edge('Dad', 'John')
          >>> len(Z.children_of('Grandad'))
          9d9b9e351ed135db7c7391092fdaea31
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
