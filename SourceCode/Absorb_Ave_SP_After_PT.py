import csv
import numpy as np 
import matplotlib.pyplot as plt 

def absorb_averageshortestpath_afterPT(data_src_path, data_dest_file, file_name):

	lists = []
	FinalTable = []
	Degree_List = [4, 6, 8, 10, 12, 14]
	FinalTable.append(xrange(-1,100))

	# lists contains all ratio data;
	for degree in Degree_List:
		lists.append(degree)
		for graph_number in range(100):

			f = open(data_src_path + '/AD' + str(degree) + '/' + 'G' + str(graph_number) + '/' + file_name)  
			firstline = f.readline()
			seperate = firstline.split("|", 2)
			firstString = seperate[0]
			longString = firstString.split(" ", 3)
			nospaceList = [x for x in longString if x]
			average = nospaceList[-1]
			average = float(average)
			lists.append(average)
		FinalTable.append(list(lists))
		del lists[:]

	#generate csv file
	myfile = open(data_dest_file, 'w')
	wr = csv.writer(myfile)
	for line_number in range(len(FinalTable)):
		wr.writerow(FinalTable[line_number])


	


if __name__ == '__main__':


	data_src_path_scb = "/Users/chenyu/Workspace/Python/MS_Project/SCB/Routing_Tables"
	data_src_path_eda = "/Users/chenyu/Workspace/Python/MS_Project/EDA/Routing_Tables"
	data_src_path_ud = "/Users/chenyu/Workspace/Python/MS_Project/UP_DOWN_BFS/Routing_Tables"
	
	data_dest_file_scb = "/Users/chenyu/Workspace/Python/MS_Project/Stat_Result" + '/SP_SCB.csv'
	data_dest_file_eda = "/Users/chenyu/Workspace/Python/MS_Project/Stat_Result" + '/SP_EDA.csv'
	data_dest_file_ud = "/Users/chenyu/Workspace/Python/MS_Project/Stat_Result" + '/SP_UD_BFS.csv'


	absorb_averageshortestpath_afterPT(data_src_path_scb, data_dest_file_scb, 'DStat_SCB.txt')
	absorb_averageshortestpath_afterPT(data_src_path_eda, data_dest_file_eda, 'DStat_EDA.txt')
	absorb_averageshortestpath_afterPT(data_src_path_ud, data_dest_file_ud, 'DStat_UD.txt')

































	