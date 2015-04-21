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

# input can be both G path or G
def basic_SCB(G_input):



	if type(G_input) == str:
		G = read_graph(G_input)
		work_path = os.path.dirname(os.path.realpath(G_input))
		scbfile = open( work_path + "/pt_SCB.txt" , "w")
	else:
		G = G_input
		scbfile = open( "pt_SCB.txt" , "w")

	print >> scbfile, "Forbidden  Turns"
	
	selected_node_number = 0

	while True:

		if len(G.nodes(data=True)) == 2:

			# print G.nodes(data=True)

			break
		else:	
			sorted_degree_nodes = sorted(G.degree().iteritems(), key = itemgetter(1))
			# print sorted_degree_nodes

			for xnode in sorted_degree_nodes:
				if not is_cut_node(G, xnode[0]) \
				and check_sum_neighbors_deg(G, xnode[0]):
					# print `xnode[0]`
					if G.degree(xnode[0]) > 1:
						# print "combinations:" + `[x for x in itertools.combinations(all_neighbors(G, xnode[0]), 2)]`
						for pair in itertools.combinations(all_neighbors(G, xnode[0]), 2):
							# print "(" + `pair[0]` + "," + `xnode[0]` + "," + `pair[1]` + ")," + `selected_node_number`
							print >> scbfile, "(" + `pair[0]` + "," + `xnode[0]` + "," + `pair[1]` + ")," + `selected_node_number`
					selected_node_number += 1
					G.remove_node( xnode[0] )
					break
	scbfile.close
	return

def check_sum_neighbors_deg(G ,node):

	deg_sum = 0
	neighbors_counter = 0
	for neighbors_node in all_neighbors(G, node):
		deg_sum += G.degree(neighbors_node)
		neighbors_counter += 1

	if  neighbors_counter * neighbors_counter <= deg_sum:
		# print "node: " + `node` + ", neighbors:" + `[k for k in all_neighbors(G, node)]`
		# print "node: " + `node` + ", number of neighbors: " + `neighbors_counter` + ", sum of deg: " + `deg_sum`

		return True
	else:
		return False


def is_cut_node(G, node):
	neighbors = all_neighbors(G, node)

	G.remove_node(node)

	is_cut_node = True
	if nx.is_connected(G):
		is_cut_node = False
	for nd in neighbors:
		G.add_edge(node, nd)

	return is_cut_node



if __name__ == '__main__':

	# nodes_number = 8
	# aim_degree = 4
	# g = Graph_SelEdg_Generator(nodes_number, aim_degree)
	# g = basic_SCB(g)

	# g = read_graph("8n4d.xml")
	# plot_graph(g)

	# print g.nodes(data=True)
	# print g.edges(data=True)


	# basic_SCB("8n4d.xml")
	# basic_SCB("sample_topologies/paperexample.xml")
	# basic_SCB("paperexample3.xml")
	# basic_SCB("myex.xml")




	# a = [1,2,3,4,5]
	# print [x for x in itertools.combinations(a, 3)]




## work on data set
	work_path = "/Users/chenyu/Workspace/Python/MS_Project/test/PE_SCB/"
	for x in os.walk(work_path):
		xmlfile = x[0] + "/GraphML.xml"
		if os.path.isfile(xmlfile):
			print os.path.dirname(os.path.realpath(xmlfile))
			basic_SCB(xmlfile)


























