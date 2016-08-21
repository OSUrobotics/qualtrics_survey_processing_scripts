import csv
import numpy as np
import getpass


def parse_file(filename):
	file_array = []
	with open(filename,'rb') as csvfile:
		file_reader = csv.reader(csvfile, delimiter = ',', quotechar = '"')
		for row in file_reader:
			file_array.append(row)
	
	return np.transpose(np.array(file_array,dtype='|S'))


if __name__ == "__main__":
    input_file = '/home/'+getpass.getuser()+'/online_survey_data/Similar_cluster_detection.csv'
    input_file_matrix = parse_file(input_file)
