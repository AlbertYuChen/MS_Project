#!/usr/bin/env python

from networkx import *
from networkx.generators.degree_seq import *
import matplotlib.pyplot as plt
from Degree_Sequence_Generator import degree_sequence_generator
from Graph_Plotor import plot_graph
import networkx as nx
import random
from random import randint


def even_dis_tree_generator(No_nodes, node_upper_bound):

	nodes_list = [[x] for x in xrange(0,No_nodes)]
	G=nx.Graph()
	G.add_nodes_from( [x for x in xrange(0,No_nodes)] )



	while len(nodes_list) > 1:
		random.shuffle(nodes_list)
		# print nodes_list

		for x in xrange(len(nodes_list)/2 - 1, -1, -1):
			insert_position = randint(0, len(nodes_list[x << 1]) - 1)
			G.add_edge(nodes_list[x << 1][insert_position], nodes_list[(x << 1) + 1][0])
			nodes_list[x << 1] += nodes_list[(x << 1) + 1]
			del nodes_list[(x << 1) + 1]
		# print nodes_list





	return G


if __name__ == '__main__':


	g = even_dis_tree_generator(64,16)






























