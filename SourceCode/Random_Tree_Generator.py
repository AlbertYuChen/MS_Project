#!/usr/bin/env python

from networkx import *
from networkx.generators.degree_seq import *
import matplotlib.pyplot as plt
from Degree_Sequence_Generator import degree_sequence_generator
from Graph_Plotor import plot_graph
import networkx as nx
import random
from random import randint


def add_edge_tree_generator(No_nodes, node_upper_bound):

	G = nx.Graph()
	G.add_node(0)

	for x in xrange(1,No_nodes):
		n1 = random.choice(G.nodes())
		G.add_node(x)
		while G.degree(n1) >=  node_upper_bound:
			n1 = random.choice(G.nodes())
		G.add_edge(x, n1)

	return G


if __name__ == '__main__':

	g = random_tree_generator(64, 16)	
	print g.nodes(data = True)
	plot_graph(g)











