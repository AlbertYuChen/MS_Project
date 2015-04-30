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

			graph_path = data_src_path + '/AD' + str(degree)+ "/G" + str(graph_number) + "/GraphML.xml"
			print graph_path
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


	data_src_path_scb = "/Users/chenyu/Workspace/Python/MS_Project/SCB/Routing_Tables"
	data_src_path_eda = "/Users/chenyu/Workspace/Python/MS_Project/EDA/Routing_Tables"
	data_src_path_ud = "/Users/chenyu/Workspace/Python/MS_Project/UP_DOWN_BFS/Routing_Tables"
	
	data_dest_file_scb = "/Users/chenyu/Workspace/Python/MS_Project/Stat_Result" + '/O_SP_SCB.csv'
	data_dest_file_eda = "/Users/chenyu/Workspace/Python/MS_Project/Stat_Result" + '/O_SP_EDA.csv'
	data_dest_file_ud = "/Users/chenyu/Workspace/Python/MS_Project/Stat_Result" + '/O_SP_UD_BFS.csv'


	absorb_OriginalGraph_AverageShortestDistance(data_src_path_scb, data_dest_file_scb)
	absorb_OriginalGraph_AverageShortestDistance(data_src_path_eda, data_dest_file_eda)
	absorb_OriginalGraph_AverageShortestDistance(data_src_path_ud, data_dest_file_ud)










