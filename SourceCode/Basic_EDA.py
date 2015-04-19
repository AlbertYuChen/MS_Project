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
from Data_Output import data_output


# input can be both G path or G
def basic_EDA(G_input):

	if type(G_input) == str:
		G = read_graph(G_input)
		work_path = os.path.dirname(os.path.realpath(G_input))
		edafile = open( work_path + "/pt_EDA.txt" , "w")
	else:
		G = G_input
		edafile = open( "pt_EDA.txt" , "w")

	print >> edafile, "Forbidden  Turns"

	print  G_input


	selected_node_num = 0
	valid_node = False

	while True:
		
		if len(G.nodes(data=True)) == 2:
			# print G.nodes(data=True)
			break
		else:
			sorted_degree_nodes = sorted(G.degree().iteritems(), key = itemgetter(1))
			# print sorted_degree_nodes
			
			for midnode in sorted_degree_nodes:

				if G.degree(midnode[0]) == 1:
					selected_node_num += 1
					G.remove_node(midnode[0])
					# print "cut: " + `midnode[0]`
				else:
					# print "select: " + `midnode[0]` 
					data_output( G, 0, 0)

					valid_node = False
					for neighbour in all_neighbors(G, midnode[0]):
						if is_bridge_edge(G, [midnode[0], neighbour]):
							continue
						else:
							for nd in all_neighbors(G, midnode[0]):
								if nd != neighbour:
									# print "(" + `neighbour` + "," + `midnode[0]` + "," + `nd` + ")," + `selected_node_num`
									print >> edafile, "(" + `neighbour` + "," + `midnode[0]` + "," + `nd` + ")," + `selected_node_num`
									valid_node = True
							# selected_node_num += 1
							G.remove_edge(midnode[0], neighbour)
							# print [midnode[0], neighbour]
							break

				if valid_node:
					break
				else:
					continue
		# selected_node_num += 1

	edafile.close
	return


def is_bridge_edge(G, edge):

	if G.degree(edge[0]) == 1 or G.degree(edge[0]) == 1:
		return False
	else:
		G.remove_edge(edge[0], edge[1])
		is_bridge_edge = not nx.is_connected(G)
		G.add_edge(edge[0], edge[1])
		return is_bridge_edge


if __name__ == '__main__':

	# g = read_graph("breakpoint.xml")
	# g = read_graph("error.xml")
	# plot_graph(g)
	# basic_EDA(g)

	# basic_EDA("8n4d.xml")
	# basic_EDA("8n.xml")
	# basic_EDA("paperexample.xml")
	# basic_EDA("myex.xml")
	# basic_EDA("error2.xml")



# ## work on data set
# 	work_path = "/Users/chenyu/Workspace/Python/MS_Project/EDA/"
# 	for x in os.walk(work_path):
# 		xmlfile = x[0] + "/GraphML.xml"
# 		print xmlfile
# 		if os.path.isfile(xmlfile):
# 			basic_EDA(xmlfile)


























