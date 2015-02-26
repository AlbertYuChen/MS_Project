#!/usr/bin/env python

from networkx import *
from networkx.generators.degree_seq import *
import matplotlib.pyplot as plt
from Degree_Sequence_Generator import degree_sequence_generator
from Graph_Plotor import plot_graph
import networkx as nx
import random
from random import randint


def even_uino_tree_generator(No_nodes, node_upper_bound):

	nodes_list = [[x] for x in xrange(0,No_nodes)]
	G=nx.Graph()
	G.add_nodes_from( [x for x in xrange(0,No_nodes)] )



	while len(nodes_list) > 1:
		branch1 = randint(0, len(nodes_list) - 1)
		branch2 = randint(0, len(nodes_list) - 1)
		add_position = randint(0, len(nodes_list[branch1]) - 1)

		while branch1 == branch2 or \
		 G.degree(nodes_list[branch2][0]) >= node_upper_bound - 1 or \
		 G.degree(nodes_list[branch1][add_position]) >= node_upper_bound - 1:

			branch1 = randint(0, len(nodes_list) - 1)
			branch2 = randint(0, len(nodes_list) - 1)
			add_position = randint(0, len(nodes_list[branch1]) - 1)
			# print G.degree(nodes_list[branch2][0]),  G.degree(nodes_list[branch1][add_position])
		
		G.add_edge(nodes_list[branch1][add_position], \
			nodes_list[branch2][0])	

		nodes_list[branch1] += nodes_list[branch2]
		del nodes_list[branch2]

		# print nodes_list





	return G


if __name__ == '__main__':


	g = even_uino_tree_generator(9,3)
































