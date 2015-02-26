#!/usr/bin/env python

from networkx import *
from networkx.generators.degree_seq import *
import matplotlib.pyplot as plt
from Graph_Plotor import plot_graph
import networkx as nx


def read_graph(path):
	G = read_graphml(path)
	rename_node_table = dict(zip([x for x in nodes_iter(G)], [int(x) for x in nodes_iter(G)] ))

	G = nx.relabel_nodes(G,rename_node_table)

	return G

if __name__ == '__main__':

	g = read_graph("8n4d.xml")
	print g.nodes(data=True)
	print g.edges(data=True)

	# graph_analyzer(g)






































