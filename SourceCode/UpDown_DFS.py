#!/usr/bin/env python

from networkx import *
from networkx.generators.degree_seq import *
import matplotlib.pyplot as plt
from Graph_Plotor import plot_graph
import networkx as nx
from Graph_Reader import read_graph
from Graph_Analyzor import graph_analyzer
from Random_SelEdg_Graph_Generator import Graph_SelEdg_Generator
import operator
from itertools import groupby
from operator import itemgetter
import itertools
import os
import random
from itertools import combinations
from itertools import groupby

G = nx.Graph()
time = -1

def search_dfs_tree(G_in, work_path, Source):
	global time, G
	dfstfile = open( work_path + "/DFST.txt" , "w")

	G = G_in
	time = 0
	nx.set_node_attributes(G, 'label', -1)

	for node in G.nodes(data=True):
		dfs_visit(node[0])

	print G.nodes(data=True)
	dfstfile.close
	return G

def dfs_visit(node_u):
	global time, G

	G.node[node_u]['label'] = time
	time = time + 1
	
	for v in all_neighbors(G, node_u):
		if G.node[v]['label'] == -1:
			
			dfs_visit(v)



# input can be both G path or G
def updown_dfs(G_input):

	if type(G_input) == str:
		G = read_graph(G_input)
		work_path = os.path.dirname(os.path.realpath(G_input))

		udfile = open( work_path + "/pt_UD.txt" , "w")
	else:
		G = G_input
		udfile = open( "pt_UD.txt" , "w")


	node_counter = 0

	random.seed(0)
	Source_Node = 0

	G = search_dfs_tree(G, work_path, Source_Node)

	new_node_list = sorted(G.nodes(data=True), key=lambda x: x[1]['label'])

	# print G.nodes(data=True)
	# print new_node_list
	# print Source_Node

	print >> udfile, "Forbidden  Turns"

	for N in new_node_list:
		# print [x for x in all_neighbors(G, N[0])]
		for pair in itertools.combinations(all_neighbors(G, N[0]), 2):
			# print pair
			if G.node[N[0]]['label'] > G.node[pair[0]]['label'] and G.node[N[0]]['label'] > G.node[pair[1]]['label']:
				print >> udfile, "(%d,%d,%d),%d" % (pair[0], N[0], pair[1], node_counter)
		node_counter = node_counter + 1

	udfile.close
	return


if __name__ == '__main__':

	# g = read_graph("sample_topologies/PE_layout/paperexample1/GraphML.xml")
	# g = read_graph("sample_topologies/8n.xml")
	path  = "sample_topologies/PE_layout/paperexample3/GraphML.xml"
	# updown_dfs(path)
	g = read_graph(path)
	search_dfs_tree(g, "sample_topologies/PE_layout/paperexample3", 1)

	## work on data set

	# # work_path = "/Users/chenyu/Workspace/Python/MS_Project/TestCase/PE_UD_BFS/"
	# work_path = "/Users/chenyu/Workspace/Python/MS_Project/UP_DOWN/"

	# for x in os.walk(work_path):
	# 	xmlfile = x[0] + "/GraphML.xml"
	# 	if os.path.isfile(xmlfile):
	# 		print os.path.dirname(os.path.realpath(xmlfile))
	# 		updown_dfs(xmlfile)



	














	









	









	

