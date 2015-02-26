#!/usr/bin/env python

from networkx import *
from networkx.generators.degree_seq import *
import matplotlib.pyplot as plt
from Graph_Plotor import plot_graph
import networkx as nx
from Graph_Reader import read_graph
from Graph_Analyzor import graph_analyzer
from Random_SelEdg_Graph_Generator import Graph_SelEdg_Generator
from Data_Output import data_output


def manuel_creat_graph():
	G = nx.Graph()
	
	# G.add_edge(1,8)
	# G.add_edge(1,7)
	# G.add_edge(1,6)
	# G.add_edge(2,3)
	# G.add_edge(2,4)
	# G.add_edge(2,6)
	# G.add_edge(3,4)
	# G.add_edge(3,8)
	# G.add_edge(4,8)
	# G.add_edge(4,5)
	# G.add_edge(5,4)
	# G.add_edge(5,7)
	# G.add_edge(5,6)
	# G.add_edge(6,7)
	# G.add_edge(7,8)


	# G.add_edge(1,2)
	# G.add_edge(1,3)
	# G.add_edge(2,3)
	# G.add_edge(3,4)
	# G.add_edge(4,5)
	# G.add_edge(5,6)
	# G.add_edge(6,7)
	# G.add_edge(5,7)

	# G.add_edge(1,2)
	# G.add_edge(1,4)
	# G.add_edge(1,5)
	# G.add_edge(2,4)
	# G.add_edge(2,3)
	# G.add_edge(3,4)
	# G.add_edge(3,5)
	# G.add_edge(5,6)
	# G.add_edge(6,7)
	# G.add_edge(7,8)
	# G.add_edge(7,10)
	# G.add_edge(8,9)
	# G.add_edge(8,11)
	# G.add_edge(9,10)
	# G.add_edge(9,11)
	# G.add_edge(10,11)

	G.add_edge(1,2)
	G.add_edge(1,3)
	G.add_edge(2,3)
	G.add_edge(2,4)
	G.add_edge(2,5)
	G.add_edge(3,6)
	G.add_edge(3,7)
	G.add_edge(4,6)
	G.add_edge(5,6)



	return G



if __name__ == '__main__':

	# nodes_number = 8
	# aim_degree = 4
	# g = Graph_SelEdg_Generator(nodes_number, aim_degree)
	# g = basic_SCB(g)

	# g = read_graph("8nd4a.xml")

	# print g.nodes(data=True)
	# print g.edges(data=True)


	g = manuel_creat_graph()


	data_output( g, 0, 3)

	plot_graph(g)

	# graph_analyzer(g)



















