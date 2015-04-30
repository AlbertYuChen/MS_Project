import networkx as nx
import csv
import numpy as np 
import matplotlib.pyplot as plt 
import numpy
from Graph_Reader import read_graph



def absorb_OriginalGraph_AverageShortestDistance(data_src_path, data_dest_file):
	GAverageTable = []
	table_list = []

	GAverageTable.append(xrange(-1,100))

	Degree_List = [4, 6, 8, 10, 12, 14]
	

	for degree in Degree_List:
		table_list.append(degree)
		for graph_number in range(100):
			graph_path = data_src_path + str(degree)+ "/G" + str(graph_number) + "/GraphML.xml"
			g = read_graph(graph_path)
			table_list.append(nx.average_shortest_path_length(g))

		# GAverage = sum(table_list) / 100
		# print table_list
		GAverageTable.append(list(table_list))
		del table_list[:]

	myfile = open(data_dest_file, 'w')
	wr = csv.writer(myfile)
	for line_number in range(len(GAverageTable)):
		wr.writerow(GAverageTable[line_number])	




if __name__ == '__main__':
	data_src_path_scb = "/Users/TiaWang/Documents/python/Teng_Wang/SCB/AD"
	data_dest_file_scb = "/Users/TiaWang/Documents/python/Teng_Wang/AverageShortestPath" + '/SCBOriginalGraph_AverageShortestPath.csv'

	absorb_OriginalGraph_AverageShortestDistance(data_src_path_scb, data_dest_file_scb)















