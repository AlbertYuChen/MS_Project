#!/usr/bin/env python

from networkx import *
from networkx.generators.degree_seq import *
import matplotlib.pyplot as plt
from Graph_Plotor import plot_graph
import networkx as nx
from Random_DegSeq_Graph_Generator import Graph_DegSeq_Generator
from Data_Output import data_output
import Random_DegSeq_Graph_Generator
from Random_SelEdg_Graph_Generator import Graph_SelEdg_Generator



if __name__ == '__main__':

	nodes_number = 64
	aim_degree = 14


## degree sequence algorithm
	# valid_counter = 0
	# for x in xrange(0,1):
	# 	G = Graph_SelEdg_Generator(nodes_number, aim_degree)
	# 	if G and Random_DegSeq_Graph_Generator.ave_deg == aim_degree:
	# 		data_output( G, aim_degree, valid_counter )
	# 		valid_counter += 1

	# # print "total valid graphs: ", valid_counter

	# plot_graph( Graph_DegSeq_Generator(aim_degree) )
	# data_output( Graph_SelEdg_Generator(nodes_number, aim_degree), aim_degree, 1 )



## select edge algorithm
	# for x in xrange(0,100):
	# 	G = Graph_SelEdg_Generator(nodes_number, aim_degree)
	# 	data_output( G, aim_degree, x )

	G = Graph_SelEdg_Generator(nodes_number, aim_degree)
		data_output( G, aim_degree, x )