#!/usr/bin/env python

from networkx import *
from networkx.generators.degree_seq import *
import matplotlib.pyplot as plt
from Degree_Sequence_Generator import degree_sequence_generator
from Graph_Plotor import plot_graph
import networkx as nx
import random
from Random_Tree_Generator import add_edge_tree_generator
from Even_Distributed_Random_Tree_Generator import even_dis_tree_generator
from Even_Union_Tree_Generator import even_uino_tree_generator
from Data_Output import data_output

def Graph_SelEdg_Generator(No_nodes, deg_exp, seed):

	global ave_deg
	ave_deg = 0.0

	random.seed(seed);

	# G = add_edge_tree_generator(No_nodes, 16)
	# G = even_dis_tree_generator(No_nodes,16)
	G = even_uino_tree_generator(No_nodes, 16, seed)



	total_degree = No_nodes * 2 - 2

	while (total_degree < No_nodes * deg_exp ):
		n1 = random.choice(G.nodes())
		n2 = random.choice(G.nodes()) 
		while (n1 == n2 or G.degree(n1) >= 16 or G.degree(n2) >= 16):
			n1 = random.choice(G.nodes())
			n2 = random.choice(G.nodes())
		if not G.has_edge (n1,n2) :
			G.add_edge(n1, n2)  
			# print (n1, n2)
			total_degree += 2


	# print "connectivity:" + `is_connected(G)`


	print("Degree histogram")
	hist={}
	d = 0

	# for k in range(0,len(G.nodes(data=True))):
	for k in nodes_iter(G):
		d = G.degree(k)

		if d in hist :
			hist[d]+=1
		else:
			hist[d]=1

	print("degree #nodes")
	for d in hist:
	    print('%d %d' % (d,hist[d]))


	# print("edge list")
	# print(G.edges(data=True))



	average_degree = 0.0
	# for v in range(0, len(G.nodes(data=True))):
	for v in nodes_iter(G):
		average_degree += G.degree(v)
		# print(G.degree(v))

	average_degree /= len(G.nodes(data=True))
	ave_deg = average_degree
	print "degree average:", average_degree


	# histcheck = [ k for k in hist.keys() if k >= 17]
	# if histcheck:
	# 	print "Invalid graph exist 17 degree or larger nodes"
	# 	return None

	return G


if __name__ == '__main__':

	# g = Graph_SelEdg_Generator(10 , 4)

	# print g.nodes(data = True)

	# plot_graph(g)
	# write_graphml(g, "g.xml")

	# gr = read_graphml("g.xml")

	# plot_graph(gr)



# generate radon topology data set
	nodes_number = 8
	aim_degree = 4
	for x in xrange(0,10):
		G = Graph_SelEdg_Generator(nodes_number, aim_degree, x)
		data_output( G, aim_degree, x, "Me")

















