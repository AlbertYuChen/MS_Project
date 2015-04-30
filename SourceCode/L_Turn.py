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


def search_bfs_tree(G, work_path, Source):

	bfstfile = open( work_path + "/BFST.txt" , "w")

	nx.set_node_attributes(G, 'label', -1)
	nx.set_node_attributes(G, 'level', -1)

	Q = []
	lev_buf = []
	node_lab = 0
	line_counter = 0
	G.node[Source]['label'] = node_lab
	G.node[Source]['level'] = 0
	Q.append(Source);

	print >> bfstfile, "STree"

	while len(Q) != 0:
		u = Q.pop(0)
		for v in all_neighbors(G, u):
			if G.node[v]['label'] == -1:
				lev_buf.append(v)
				node_lab = node_lab + 1
				G.node[v]['label'] = node_lab
				G.node[v]['level'] = G.node[u]['level'] + 1
				Q.append(v)


		print >> bfstfile, "%3d=> %3d (%3d, %3d):" % (line_counter, u, G.node[u]['level'], G.node[u]['label']), 

		for x in xrange(len(lev_buf)):
			if x <= len(lev_buf) - 2:
				print >> bfstfile, "%3d," % lev_buf[x],
			else:
				print >> bfstfile, "%3d" % lev_buf[x],
		print >> bfstfile, ""

		line_counter = line_counter + 1
		lev_buf[:] = []

	bfstfile.close
	return G


# input can be both G path or G
def updown_bfs(G_input):

	if type(G_input) == str:
		G = read_graph(G_input)
		work_path = os.path.dirname(os.path.realpath(G_input))

		udfile = open( work_path + "/pt_UD.txt" , "w")
	else:
		G = G_input
		udfile = open( "pt_UD.txt" , "w")


	node_counter = 0

	node_list = sorted(G.nodes(data=True), key=lambda x: G.degree(x[0]), reverse=True)
	node_list_group = groupby(node_list, key=lambda x: G.degree(x[0]))

	random.seed(0)
	Source_Node = random.choice(list(list(node_list_group.next())[1]))[0]

	G = search_bfs_tree(G, work_path, Source_Node)

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
	# path  = "sample_topologies/PE_layout/paperexample3/GraphML.xml"
	# updown_bfs(path)


	## work on data set

	work_path = "/Users/chenyu/Workspace/Python/MS_Project/TestCase/PE_UD_BFS/"
	# work_path = "/Users/chenyu/Workspace/Python/MS_Project/UP_DOWN/"

	for x in os.walk(work_path):
		xmlfile = x[0] + "/GraphML.xml"
		if os.path.isfile(xmlfile):
			print os.path.dirname(os.path.realpath(xmlfile))
			updown_bfs(xmlfile)



	














	









	









	

