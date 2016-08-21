#!/usr/bin/env python

import numpy as np
import getpass
import copy 

if __name__ == "__main__":
    input_file_folder = '/home/'+getpass.getuser()+'/similar_grasp_images/images_and_url/'
    input_file = input_file_folder+'obj4_urls.csv'
    output_file_url = input_file.split('.csv')[0] + '_url_matricized.csv'
    output_file_obj_name = input_file.split('.csv')[0] + '_obj_name_matricized.csv'
    
    file_data = np.genfromtxt(input_file,delimiter = ',', dtype = '|S')
    file_data = np.transpose(file_data)
    unique_cluster_list = np.array([],dtype='|S50')
    for file_name in file_data[0]:
        idx = file_name.find('sub')
        unique_cluster_list = np.append(unique_cluster_list, file_name[:idx])
    
    unique_cluster_list = np.unique(unique_cluster_list)
    saggrigated_cluster = dict()
    for i,unique_cluster in enumerate(unique_cluster_list):
        saggrigated_cluster[str(i)] = {'cluster_idx': np.array([]), 'file_name': np.array([],dtype='|S50'), 'url': np.array([],dtype='|S150')}
        for j,value in enumerate(file_data[0]):
            if unique_cluster in value:
                saggrigated_cluster[str(i)]['cluster_idx'] = np.append(saggrigated_cluster[str(i)]['cluster_idx'], j)
                saggrigated_cluster[str(i)]['file_name'] = np.append(saggrigated_cluster[str(i)]['file_name'], value)
                saggrigated_cluster[str(i)]['url'] = np.append(saggrigated_cluster[str(i)]['url'], file_data[1][j])
    

    
    # Create array and save
    number_of_images = 6
    output_struct = dict()
    output_struct['url'] = dict()
    output_struct['image_name'] = dict()
    temp_struct_idx = dict()
    for k in range(len(unique_cluster_list)):
        temp_struct_idx[str(k)] = np.array([])
        for p in range(len(file_data[0])):
            output_struct['image_name'][str(k)] = saggrigated_cluster[str(k)]['file_name']
            output_struct['url'][str(k)] = saggrigated_cluster[str(k)]['url']
            if not p in saggrigated_cluster[str(k)]['cluster_idx']:
                temp_struct_idx[str(k)] = np.append(temp_struct_idx[str(k)], p)
        

        #number_of_elements = number_of_images - len(output_struct['image_name'][str(k)])
        number_of_elements = number_of_images - len(saggrigated_cluster[str(k)]['cluster_idx'])
        output_struct['image_name'][str(k)] = np.append(output_struct['image_name'][str(k)], np.random.choice(file_data[0][temp_struct_idx[str(k)].tolist()], number_of_elements))
        output_struct['url'][str(k)] = np.append(output_struct['url'][str(k)],np.random.choice(file_data[1][temp_struct_idx[str(k)].tolist()], number_of_elements))
    
    
    random_matrix = np.meshgrid(np.arange(0,number_of_images),np.arange(0,3))[0]
    for vector in random_matrix:
        np.random.shuffle(vector[1:])
    output_matrix_image = np.array([])
    output_matrix_url = np.array([])
    for r in range(len(unique_cluster_list)):
        for y in range(len(random_matrix)):
            output_matrix_image = np.append(output_matrix_image,output_struct['image_name'][str(r)][random_matrix[y]]) 
            output_matrix_url = np.append(output_matrix_url,output_struct['url'][str(r)][random_matrix[y]])  
    
    output_matrix_image = output_matrix_image.reshape(len(output_matrix_image)/number_of_images, number_of_images)
    output_matrix_url = output_matrix_url.reshape(len(output_matrix_url)/number_of_images, number_of_images)

    np.savetxt(output_file_obj_name, output_matrix_image,fmt='%s',delimiter=',')
    np.savetxt(output_file_url, output_matrix_url,fmt='%s',delimiter=',')






    #random_matrix = np.meshgrid(np.arange(0,len(file_data[0])),np.arange(0,len(file_data[0])))[0]
    #for i in range(1,len(random_matrix)):
    #    value = copy.deepcopy(random_matrix[i,:i])
    #    random_matrix[i,:-i] = random_matrix[i,i:]
    #    random_matrix[i,-i:] = value

    #print random_matrix
    #output_obj_matrix = file_data[0][random_matrix]
