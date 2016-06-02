
"""
Define three constants whose values are dictionaries corresponding to
the three directed graphs
"""
EX_GRAPH0 = {0: set([1, 2]), 1: set([]), 2: set([])}
EX_GRAPH1 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3]), 3: set([0]), 4: set([1]), 5: set([2]), 6: set([])}
EX_GRAPH2 = {0: set([1,4,5]), 1: set([2,6]), 2: set([3,7]), 3: set([7]), 4: set([1]), 5: set([2]), 6: set([]), 7: set([3]), 8: set([1,2]), 9: set([0,3,4,5,6,7])}

"""
Takes num_nodes and returns a dictionary corresponding to a complete
directed graph with the specified number of nodes.
"""
def make_complete_graph(num_nodes):
    graph = {}
    if num_nodes < 1:
        return graph

    for node in range(num_nodes):
        temp = range(num_nodes)
        temp.remove(node)
        graph[node] = set(temp)

    return graph

"""
Takes a directed graph digraph (represented as a dictionary)
and computes the in-degrees for the nodes in the graph.
"""
def compute_in_degrees(digraph):
    in_degree = {}
    for key in digraph:
        in_degree[key] = 0
    for key in digraph:
        for dist in digraph[key]:
            in_degree[dist] += 1
    return in_degree


print(compute_in_degrees(EX_GRAPH1))
