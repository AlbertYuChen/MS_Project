#!/usr/bin/env python

from networkx import *
from networkx.generators.degree_seq import *
import matplotlib.pyplot as plt
import networkx as nx

def plot_graph(G):
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


	plt.savefig("example2.png")
	plt.show()

	pass




if __name__ == '__main__':

    plot_graph(G)