# cd /Users/TiaWang/Documents/python
# python first.py
import csv
import numpy as np 
import matplotlib.pyplot as plt 
import numpy
from pylab import *


def absorb_turn_fraction(data_src_path, data_dest_file):
	table = []
	table_list = []

	Degree_List = [4, 6, 8, 10, 12, 14]


	table.append(xrange(-1,100))

	# lists contains all ratio data;
	for degree in Degree_List:
		table_list.append(degree)
		for graph_number in range(100):
			f = open(data_src_path + '/AD' + `degree` + '/' + 'G' + `graph_number` + '/' + 'res.txt')  
			firstline = f.readline()
			seperate = firstline.split("=", 3)
			lastString = seperate[-1]
			zString = lastString.split("\r", 2)
			z = zString[0]
			zfloat = float(z)
			table_list.append(zfloat)

		table.append(list(table_list))
		del table_list[:] 

	#generate csv file
	myfile = open(data_dest_file, 'w')
	wr = csv.writer(myfile)
	for line_number in xrange(len(table)):
		wr.writerow(table[line_number])


	# reader=csv.reader(open(data_dest_path + '/SCB.csv',"rb"),delimiter=',')
	# x = list(reader)
	# print len(x)


if __name__ == '__main__':

	data_src_path_scb = "/Users/chenyu/Workspace/Python/MS_Project/SCB/Routing_Tables"
	data_src_path_eda = "/Users/chenyu/Workspace/Python/MS_Project/EDA/Routing_Tables"
	data_src_path_ud = "/Users/chenyu/Workspace/Python/MS_Project/UP_DOWN_BFS/Routing_Tables"
	
	data_dest_file_scb = "/Users/chenyu/Workspace/Python/MS_Project/Stat_Result" + '/TF_SCB.csv'
	data_dest_file_eda = "/Users/chenyu/Workspace/Python/MS_Project/Stat_Result" + '/TF_EDA.csv'
	data_dest_file_ud = "/Users/chenyu/Workspace/Python/MS_Project/Stat_Result" + '/TF_UD_BFS.csv'


	absorb_turn_fraction(data_src_path_scb, data_dest_file_scb)
	absorb_turn_fraction(data_src_path_eda, data_dest_file_eda)
	absorb_turn_fraction(data_src_path_ud, data_dest_file_ud)






























