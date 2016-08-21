#!/usr/bin/env python

import numpy as np
import getpass

if __name__ == "__main__":
    input_file_path = '/home/'+getpass.getuser()+'/similar_grasp_images/images_and_url/'
    fname = 'obj5_urls_obj_name_matricized.csv'
    file_matrix = np.genfromtxt(input_file_path+fname, delimiter=',', dtype='|S')
    output_file_name = '/home/'+getpass.getuser()+'/similar_grasp_images/images_and_url/'+fname.split('_matricized')[0]+'_flattened.csv'
    flattned_matrix = np.reshape
    np.savetxt(output_file_name, np.transpose(file_matrix.reshape(-1)),delimiter = ',', fmt='%s')

