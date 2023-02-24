# -----------------------------------------------------------
# Introduction
# Graphs are simply another way to represent data. There are many different kinds of graphs and innumerable applications for them. You can find 
# many examples of graphs in your everyday life, from road maps to subway systems. One special type of graph that we will be focusing on is the star 
# graph, which has real-world applications such as the star network, a way of designing a computer network.
# 
# The Task
# For this problem, the graph will be undirected, consisting of a number of nodes and undirected edges. Additionally, the graph is given as a star graph. 
# For this problem, a star graph of n nodes has n-1 edges and one and only one node has degree greater than one, all other nodes have degree equal to 
# one (degree of a node of an undirected graph is simply the number of edges the node is a part of). The node to search for is the node with degree 
# greater than one. All the other nodes with degree one must have one, and only one edge to the node with degree greater than one.
# 
# Additionally, a star graph can be thought of as a special kind of undirected tree with n-1 leaf nodes and 1 non-leaf node (thus, any two nodes in the 
# star graph have one and only one path between them). Let the sole non-leaf node be the center node. It is guaranteed there is one and only one node 
# in the graph which is a center node. The center node has an edge to all other nodes. All the other nodes must have one, and only one edge to the 
# center node.
# 
# For this problem, there will be nodes with integer labels from 1 to n, where n is the number of nodes. Additionally, you will be be given a list of edges 
# of length n-1, where each edge, (n1,n2), is a tuple denoting an edge exists between n1 and n2.
# 
# Write a function that given the list of edges, returns the center of the star graph as an integer. There will not be any performance tests, only tests for 
# correctness, and length of the list of edges is guaranteed to be >=3 and not exceed 1000.
# 
# Example
# You are given edges [(1,5),(4,5),(5,2),(3,5)].
# 
# Since 5 is the only node to have an edge to all other nodes, it is the center of the star graph.
# 
# Return 5.
# -----------------------------------------------------------

# Given the edges of a undirected star graph
# of size n-1, return the center of the star graph as an int
def center(graph_edges):
    a0 = graph_edges[0][0]
    a1 = graph_edges[0][1]
    b = graph_edges[1]
    return a0 if a0 in b else a1