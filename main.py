from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    visited = set()
  
    while len(frontier) != 0:
      
      node = frontier.pop()
      visited.add(node)
      result.add(node)

      for i in graph[node]:
        if i not in visited:
          frontier.add(i)
        
    return result

def test_reachable():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert sorted(reachable(graph, 'A')) == ['A', 'B', 'C', 'D']

    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert sorted(reachable(graph, 'A')) == ['A', 'B', 'C', 'D']
    assert sorted(reachable(graph, 'E')) == ['E', 'F', 'G']



def connected(graph):
    
  # if a graph is connected, then reachable(graph) will return all of the nodes in a list
  
  start_node = list(graph)[0]
  reachable_nodes = reachable(graph, start_node)
  if len(reachable_nodes) == len(graph):
    return True
  else:
    return False

  

def test_connected():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert connected(graph) == True
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert connected(graph) == False



def n_components(graph):
  """
    Returns:
      the number of connected components in an undirected graph
  """ 
  nodes = set(graph.keys())
  num_components = 0
    
  while len(nodes) != 0:
    node1 = nodes.pop()
    reachable_nodes = reachable(graph, node1)
    nodes = nodes.difference(reachable_nodes)
    num_components += 1
  
  return num_components

def test_n_components():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert n_components(graph) == 1

    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert n_components(graph) == 2