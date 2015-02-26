#!/usr/bin/env python

from networkx import *
from networkx.generators.degree_seq import *
import matplotlib.pyplot as plt
from Graph_Plotor import plot_graph
import networkx as nx
from Graph_Reader import read_graph


def graph_analyzer(G):

	global ave_deg
	ave_deg = 0.0

	# print G.nodes(data=True)
	# print(G.edges(data=True))

	print "connectivity:" + `is_connected(G)`

	average_degree = 0.0
	# for v in range(0, len(G.nodes(data=True))):
	for v in nodes_iter(G):

		average_degree += G.degree(v)
		# print(G.degree(v))

	average_degree /= len(G.nodes(data=True))
	ave_deg = average_degree
	print "degree average:", average_degree

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
	print degree_histogram(G)
	for d in hist:
	    print('%d %d' % (d,hist[d]))




	

if __name__ == '__main__':

	# g = read_graph("test.xml")
	g = read_graph("GraphML.xml")


	graph_analyzer(g)






















