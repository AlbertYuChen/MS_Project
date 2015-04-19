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

def search_bfs_tree():


	pass

# input can be both G path or G
def updown_bfs(G_input):

	if type(G_input) == str:
		G = read_graph(G_input)
		work_path = os.path.dirname(os.path.realpath(G_input))
		udfile = open( work_path + "/pt_UD.txt" , "w")
	else:
		G = G_input
		udfile = open( "pt_UD.txt" , "w")

	print >> udfile, "Forbidden  Turns"


	udfile.close
	return


if __name__ == '__main__':

	# basic_SCB("8n4d.xml")
	g = read_graph("sample_topologies/paperexample3.xml")
	# basic_SCB("paperexample3.xml")
	# basic_SCB("myex.xml")
	print(list(nx.bfs_edges(g, 1)))

	plot_graph(g)














	









	









	

