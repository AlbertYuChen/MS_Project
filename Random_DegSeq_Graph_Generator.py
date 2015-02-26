#!/usr/bin/env python

from networkx import *
from networkx.generators.degree_seq import *
import matplotlib.pyplot as plt
from Degree_Sequence_Generator import degree_sequence_generator
from Graph_Plotor import plot_graph
import networkx as nx


# z=[4,4,4,4,2,2,2,2]


def Graph_DegSeq_Generator(deg_exp):

	global ave_deg
	ave_deg = 0.0

	degree_hist = {
		0: [1, 18],
		4: [2, 7], #need run 1000
		6: [2, 10],  #need run 2000
		8: [2, 15],  #need run 6000
		10: [5, 15],  #need run 60000
		12: [9, 17],  #need run 12000
		14: [14, 17], #need run 40000
	}
	
	z = degree_sequence_generator( 64 , degree_hist[deg_exp][0], degree_hist[deg_exp][1])

	print "Degree sequence validity: ", is_valid_degree_sequence(z)

	print("Configuration model")
	# configuration model
	G=configuration_model(z)  
	# degree sequence
	degree_sequence=list(degree(G).values()) 
	# To remove parallel edges:
	G=nx.Graph(G)
	# To remove self loops:
	G.remove_edges_from(G.selfloop_edges())


	# print("Degree sequence %s" % degree_sequence)
	print("Degree histogram")
	hist={}
	d = 0

	for k in range(0,len(G.nodes(data=True))):
		d = G.degree(k)

		if d in hist :
			hist[d]+=1
		else:
			hist[d]=1

	print("degree #nodes")
	for d in hist:
	    print('%d %d' % (d,hist[d]))


	# print("edge list")
	# print(G.edges(data=True))

	average_degree = 0.0
	for v in range(0, len(z)):
		average_degree += G.degree(v)
		# print(G.degree(v))

	average_degree /= len(z)
	ave_deg = average_degree
	print "degree average:", average_degree


	histcheck = [ k for k in hist.keys() if k >= 17]
	if histcheck:
		print "Invalid graph exist 17 degree or larger nodes"
		return None

	return G



if __name__ == '__main__':

	data_output( 4 )
















