#!/usr/bin/env python

from networkx import *
from networkx.generators.degree_seq import *
import matplotlib.pyplot as plt
import networkx as nx
import os
from Graph_Reader import read_graph

def plot_graph(G_input):

	if type(G_input) == str:
		G = read_graph(G_input)
	else:
		G = G_input



	####################	Graph Plotor    ####################
	# degree_sequence=sorted(nx.degree(G).values(),reverse=True) # degree sequence
	# #print "Degree sequence", degree_sequence
	# dmax=max(degree_sequence)

	# plt.loglog(degree_sequence,'b-',marker='o')
	# plt.title("Degree rank plot")
	# plt.ylabel("degree")
	# plt.xlabel("rank")

	## plt.savefig("degree_histogram.png")
	# plt.show()

	# draw graph in inset
	# plt.axes([0.45,0.45,0.45,0.45])


	Gcc=sorted(nx.connected_component_subgraphs(G), key = len, reverse=True)[0]
	pos=nx.spring_layout(Gcc)
	plt.axis('off')
	nx.draw_networkx_nodes(Gcc,pos,node_size=500)
	nx.draw_networkx_edges(Gcc,pos,alpha=0.4)


	labels={}

	for node in G.nodes(data = True):
		labels[node[0]] = `node[0]`
	nx.draw_networkx_labels(Gcc,pos,labels,font_size=16)


	

	if type(G_input) == str:
		work_path = os.path.dirname(os.path.realpath(G_input))
		plt.savefig(work_path + "/8n.png")
	else:
		plt.savefig("8n.png")

	plt.show()

	plt.clf()

	





if __name__ == '__main__':

   plot_graph("/Users/chenyu/Workspace/Python/MS_Project/SourceCode/sample_topologies/8n.xml")

 #    ## work on data set
	# work_path = "/Users/chenyu/Workspace/Python/MS_Project/test/PE_layout/"
	# for x in os.walk(work_path):
	# 	xmlfile = x[0] + "/GraphML.xml"
	# 	if os.path.isfile(xmlfile):
	# 		print os.path.dirname(os.path.realpath(xmlfile))
	# 		plot_graph(xmlfile)




























