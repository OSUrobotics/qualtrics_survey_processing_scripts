#!/usr/bin/env python

import csv
import numpy as np
import getpass
from parse_qualtrics_file import parse_file
from group_consecutive import group_consecutives


if __name__ == "__main__":
    input_file = '/home/'+getpass.getuser()+'/Desktop/online_survey_data/Similar_cluster_detection.csv'
    input_file_matrix = parse_file(input_file)

    matrix = input_file_matrix[12:-3, :]

    Number_of_images = 6
    
    # Question to analyze: Top left grasp (black border) is the prime grasp. Select those grasps that will function the same as the prime grasp.
    
    # Question to analyze: Top left grasp (black border) is the prime grasp. Select the grasps that have the same hand pose.

    question = dict()
    results = {'functional':dict(),'hand_pose':dict(),'Number_of_subjects_functional': dict(), 'Number_of_subjects_hand_pose':dict()}
    prime_cluster = ''
    for i in range(len(matrix)):
        vector = matrix[i]
        question_no = vector[0].split('.1_')
        if not question_no[0] in question:
            question[question_no[0]] = dict()

        obj_name = vector[2].split('_')[0]
        if not obj_name == 'n/a':
            cluster_no = vector[2].split('_')[1]
            if not obj_name in question[question_no[0]]:
                question[question_no[0]][obj_name] = dict()
        else:
            continue


        if 'function the same' in vector[1]:
            if not obj_name in results['functional']:
                results['functional'][obj_name] = {'correct': 0, 'incorrect': 0}
                results['Number_of_subjects_functional'][obj_name] = 0
            loop_no = question_no[1].split('(')[1].split(')')[0]
            image_no = question_no[1].split('(')[0]
            if not loop_no in question[question_no[0]][obj_name]:
                question[question_no[0]][obj_name][loop_no] = dict()
            int_vec = np.genfromtxt(vector,delimiter=',')
            #for vec in group_consecutives(np.where(vector=='1')[0], step=1):
            #    print len(vec)
            #    if len(vec) > 5:
            #        print 'found'
            if image_no == '1':
                prime_cluster = cluster_no
                results['Number_of_subjects_functional'][obj_name] += len(np.where(int_vec==1)[0])
            else:
                if prime_cluster == cluster_no:
                    results['functional'][obj_name]['correct'] = results['functional'][obj_name]['correct'] + len(np.where(int_vec==1)[0])
                else:
                    results['functional'][obj_name]['incorrect'] = results['functional'][obj_name]['incorrect'] + len(np.where(int_vec==1)[0])
                    
            question[question_no[0]][obj_name][loop_no][image_no+'_'+cluster_no] = len(np.where(int_vec == 1)[0])

        elif "same hand pose":
            if not obj_name in results['hand_pose']:
                results['hand_pose'][obj_name] = {'correct': 0, 'incorrect': 0}
                results['Number_of_subjects_hand_pose'][obj_name] = 0
            #for vec in group_consecutives(np.where(vector=='1')[0], step=1):
            #    print len(vec)
            #    if len(vec) > 5:
            #        print 'found'
            loop_no = question_no[1].split('(')[1].split(')')[0]
            image_no = question_no[1].split('(')[0]
            if not loop_no in question[question_no[0]][obj_name]:
                question[question_no[0]][obj_name][loop_no] = dict()
            int_vec = np.genfromtxt(vector,delimiter=',')
            if image_no == '1':
                prime_cluster = cluster_no
                results['Number_of_subjects_hand_pose'][obj_name] += len(np.where(int_vec==1)[0])
            else:
                if prime_cluster == cluster_no:
                    results['hand_pose'][obj_name]['correct'] = results['hand_pose'][obj_name]['correct'] + len(np.where(int_vec==1)[0])
                else:
                    results['hand_pose'][obj_name]['incorrect'] = results['hand_pose'][obj_name]['incorrect'] + len(np.where(int_vec==1)[0])
                    
            question[question_no[0]][obj_name][loop_no][image_no+'_'+cluster_no] = len(np.where(int_vec == 1)[0])




