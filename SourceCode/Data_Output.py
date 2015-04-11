#!/usr/bin/env python

from networkx import *
from networkx.generators.degree_seq import *
import matplotlib.pyplot as plt
from Graph_Plotor import plot_graph
import networkx as nx
import os
from Graph_Reader import read_graph
from Random_SelEdg_Graph_Generator import Graph_SelEdg_Generator

def data_output(*args):

	if len(args) == 3:
		G = args[0]
		deg = args[1]
		index  = args[2]
		foldername = "test"

	else: 
		if len(args) == 4:
			G = args[0]
			deg = args[1]
			index  = args[2]
			foldername = args[3]
		else:
			print "wrong input format"

	if G is None:
		print "None Graph"
		return 

	
####### gcon.txt
	gconfilename = foldername + "/AD" + `deg` + "/G" + `index` + "/gcon.txt"
	if not os.path.exists(os.path.dirname(gconfilename)):
	    os.makedirs(os.path.dirname(gconfilename))

	file = open( gconfilename , "w")

	# for x in xrange(0,len(G.adjacency_list())):
	for x in nodes_iter(G):

		# print x, ' '.join(map(str, G.adjacency_list()[x]))
		print >> file, x, ' '.join(map(str, [x for x in all_neighbors(G, x)]))

	file.close


####### gn.txt
	gconfilename = foldername + "/AD" + `deg` + "/G" + `index` + "/gn.txt"
	if not os.path.exists(os.path.dirname(gconfilename)):
	    os.makedirs(os.path.dirname(gconfilename))

	file = open( gconfilename , "w")
	print >> file, "graph G {\n"
	print >> file, "node [shape=circle]; edge [len=1];\n"

	for edgex in G.edges(data = True):

		# print >> file,  `int(edgex[0])` + " -- " + `int(edgex[1])` + ";"
		print >> file,  `edgex[0]` + " -- " + `edgex[1]` + ";"

	print >> file, "}\n"
	file.close


####### cytoscape.txt
	gconfilename = foldername + "/AD" + `deg` + "/G" + `index` + "/layout.sif"
	if not os.path.exists(os.path.dirname(gconfilename)):
	    os.makedirs(os.path.dirname(gconfilename))

	file = open( gconfilename , "w")

	for edgex in G.edges(data = True):
		# print `edgex[0]` + " -- " + `edgex[1]` + ";"
		print >> file, `edgex[0]` + " e " + `edgex[1]`

	file.close


####### generate GraphML.xml
	gconfilename = foldername + "/AD" + `deg` + "/G" + `index` + "/GraphML.xml"
	write_graphml(G, gconfilename)

	return

if __name__ == '__main__':
	nodes_number = 8
	aim_degree = 4

	G = Graph_SelEdg_Generator(nodes_number, aim_degree)
	# G = read_graph("8n4d.xml")
	# G.add_edge(0,220)

	# data_output( G, aim_degree, 0, "test")
	data_output( G, aim_degree, 4)


























