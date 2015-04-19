#!/usr/bin/env python

from networkx import *
from networkx.generators.degree_seq import *
import matplotlib.pyplot as plt
from Graph_Plotor import plot_graph
import networkx as nx
from Graph_Reader import read_graph
from Graph_Analyzor import graph_analyzer
import operator
from itertools import groupby
from operator import itemgetter
import itertools
import os


def correctfile(G_path):
	G = read_graph(G_path)

	file = open(os.path.dirname(os.path.realpath(G_path)) + "/gn.txt" , "w")
	print >> file, "graph G {"
	print >> file, "node [shape=circle];"
	print >> file, "edge [len=1];"

	for edgex in G.edges(data = True):

		# print `int(edgex[0])` + " -- " + `int(edgex[1])` + ";"
		print >> file,  `edgex[0]` + " -- " + `edgex[1]` + ";"

	print >> file, "}"
	file.close


if __name__ == '__main__':

	# work_path = "/Users/chenyu/Workspace/Python/MS_Project/test/AD0/G0/GraphML.xml"

	work_path = "/Users/chenyu/Workspace/Python/MS_Project/test/"

	for x in os.walk(work_path):
		xmlfile = x[0] + "/GraphML.xml"

		if os.path.isfile(xmlfile):
			# print xmlfile
			print os.path.dirname(os.path.realpath(xmlfile))
			correctfile(xmlfile)







































