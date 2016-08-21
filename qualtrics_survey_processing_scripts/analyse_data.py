#!/usr/bin/env python

import csv
import numpy as np
import getpass
from parse_qualtrics_file import parse_file
from group_consecutive import group_consecutives
import os
import copy


def read_comments(question_number, loop_no, obj_name):
    global question, matrix
    new_array = np.unique(loop_no)
    for loop in new_array.tolist():
        vector = matrix[question[question_number][obj_name][loop]['value_idx'], 3:]
        print
        print "Loop number ", loop, "comments"
        for value in vector:
            if len(value) > 1:
                print value

def get_questions_and_obj_name():
    global question
    for key in question.viewkeys():
        print key, question[key].viewkeys()
if __name__ == "__main__":
    input_file = os.getcwd()+'/Similar_cluster_detection.csv'
    input_file_matrix = parse_file(input_file)


    
    # Question to analyze: Top left grasp (black border) is the prime grasp. Select those grasps that will function the same as the prime grasp.
    
    # Question to analyze: Top left grasp (black border) is the prime grasp. Select the grasps that have the same hand pose.

    question = dict()
    results = {'functional':dict(),'hand_pose':dict(),'Number_of_subjects_functional': dict(), 'Number_of_subjects_hand_pose':dict()}
    prime_cluster = ''
    transposed_matrix = np.transpose(input_file_matrix)
    culprit_vector = []
    for idx,vector in enumerate(transposed_matrix):
        for vec in group_consecutives(np.where(vector == '1')[0],step=1):
            if len(vec)>5:
                print "Found: ",idx ,  transposed_matrix[idx,0], vec
                #transposed_matrix[idx,vec] = '0'
                culprit_vector.append(idx)

    matrix = np.transpose(transposed_matrix)[12:-3, :]
    for i in range(len(matrix)):
        vector = matrix[i]
        question_no = vector[0].split('_')
        if len(question_no) > 1:
            if (not question_no[0] in question):
                question[question_no[0]] = dict()
        else:
            question_no = vector[0].split('(')
            if len(question_no) >1:
                question_no[1] = '(' + question_no[1]
                if (not question_no[0] in question):
                    question[question_no[0]] = dict()
            else:
                continue
            


        obj_name = vector[2].split('_')[0]
        if not obj_name == 'n/a':
            cluster_no = vector[2].split('_')[1]
            if not obj_name in question[question_no[0]]:
                question[question_no[0]][obj_name] = dict()
        else:
            continue



        if 'function the same' in vector[1]:
            if not obj_name in results['functional']:
                results['functional'][obj_name] = {'correct': 0, 'false_positive': 0, 'false_negative':0, 'false_positive_image_name': np.array([],dtype='|S'),'false_positive_loop_number':[], 'false_negative_image_name':np.array([],dtype='|S'), 'false_negative_loop_number':[]}
                results['Number_of_subjects_functional'][obj_name] = 0
            loop_no = question_no[1].split('(')[1].split(')')[0]
            image_no = question_no[1].split('(')[0]
            if not loop_no in question[question_no[0]][obj_name]:
                question[question_no[0]][obj_name][loop_no] = dict()
            if image_no =='':
                image_no = '1'

            question[question_no[0]][obj_name][loop_no][image_no+'_'+cluster_no] = len(np.where(vector == '1')[0])

            if image_no == '1':
                prime_cluster = cluster_no
                number_of_users = len(np.where(vector=='1')[0])
                name_of_prime = vector[2]
                results['Number_of_subjects_functional'][obj_name] += len(np.where(vector=='1')[0])
            else:
                if prime_cluster == cluster_no:
                    results['functional'][obj_name]['correct'] = results['functional'][obj_name]['correct'] + len(np.where(vector=='1')[0])
                    false_negative_number = question[question_no[0]][obj_name][loop_no]['1_'+prime_cluster] - len(np.where(vector=='1')[0])
                    results['functional'][obj_name]['false_negative'] += false_negative_number
                    
                    if false_negative_number > 2:
                        results['functional'][obj_name]['false_negative_image_name'] = np.append(results['functional'][obj_name]['false_negative_image_name'], str(number_of_users)+'_'+name_of_prime+'_'+str(false_negative_number)+'_'+vector[2])
                        results['functional'][obj_name]['false_negative_loop_number'].append(loop_no)
                else:
                    results['functional'][obj_name]['false_positive'] = results['functional'][obj_name]['false_positive'] + len(np.where(vector=='1')[0])
                    if len(np.where(vector=='1')[0]) > 2:
                        results['functional'][obj_name]['false_positive_image_name'] = np.append(results['functional'][obj_name]['false_positive_image_name'], str(number_of_users)+'_'+name_of_prime+'_'+str(len(np.where(vector=='1')[0]))+'_'+vector[2])
                        results['functional'][obj_name]['false_positive_loop_number'].append(loop_no)

            if question_no[0].split('.')[1] == '1':
                question[question_no[0]][obj_name][loop_no][image_no+'_'+cluster_no] = len(np.where(vector == '1')[0])
            elif question_no[0].split('.')[1] == '2':
                question[question_no[0]][obj_name][loop_no].pop(image_no+'_'+cluster_no)
                question[question_no[0]][obj_name][loop_no]['value_idx'] = i

        elif 'hand pose' in vector[1]:
            if not obj_name in results['hand_pose']:
                results['hand_pose'][obj_name] = {'correct': 0, 'false_positive': 0, 'false_negative':0, 'false_positive_image_name': np.array([],dtype='|S'),'false_positive_loop_number':[], 'false_negative_image_name':np.array([],dtype='|S'), 'false_negative_loop_number':[]}
                results['Number_of_subjects_hand_pose'][obj_name] = 0
            loop_no = question_no[1].split('(')[1].split(')')[0]
            image_no = question_no[1].split('(')[0]
            if not loop_no in question[question_no[0]][obj_name]:
                question[question_no[0]][obj_name][loop_no] = dict()
            if image_no =='':
                image_no = '1'

            question[question_no[0]][obj_name][loop_no][image_no+'_'+cluster_no] = len(np.where(vector == '1')[0])

            if image_no == '1':
                prime_cluster = cluster_no
                number_of_users = len(np.where(vector=='1')[0])
                name_of_prime = vector[2]
                results['Number_of_subjects_hand_pose'][obj_name] += len(np.where(vector=='1')[0])
            else:
                if prime_cluster == cluster_no:
                    results['hand_pose'][obj_name]['correct'] = results['hand_pose'][obj_name]['correct'] + len(np.where(vector=='1')[0])
                    false_negative_number = question[question_no[0]][obj_name][loop_no]['1_'+prime_cluster] - len(np.where(vector=='1')[0])
                    results['hand_pose'][obj_name]['false_negative'] += false_negative_number

                    if false_negative_number > 2:
                        results['hand_pose'][obj_name]['false_negative_image_name'] = np.append(results['hand_pose'][obj_name]['false_negative_image_name'], str(number_of_users)+'_'+name_of_prime+'_'+str(false_negative_number)+'_'+vector[2])
                        results['hand_pose'][obj_name]['false_negative_loop_number'].append(loop_no)
                else:
                    results['hand_pose'][obj_name]['false_positive'] = results['hand_pose'][obj_name]['false_positive'] + len(np.where(vector=='1')[0])
                    if len(np.where(vector=='1')[0]) > 2:
                        results['hand_pose'][obj_name]['false_positive_image_name'] = np.append(results['hand_pose'][obj_name]['false_positive_image_name'], str(number_of_users)+'_'+name_of_prime+'_'+str(len(np.where(vector=='1')[0]))+'_'+vector[2])
                        results['hand_pose'][obj_name]['false_positive_loop_number'].append(loop_no)

            if question_no[0].split('.')[1] == '1':
                question[question_no[0]][obj_name][loop_no][image_no+'_'+cluster_no] = len(np.where(vector == '1')[0])
            elif question_no[0].split('.')[1] == '2':
                question[question_no[0]][obj_name][loop_no].pop(image_no+'_'+cluster_no)
                question[question_no[0]][obj_name][loop_no]['value_idx'] = i
        

    output_matrix = np.array(['', '','Grasp with similar function','',''])
    output_matrix = np.append([output_matrix], [['Number of samples', 'object No.', 'correct', 'False Positive', 'False Negative']],axis=0)
    key_vector = results['functional'].keys()
    object_name = {'obj5':'Cereal Box','obj2':'Spray Bottle','obj4':'Wine glass','obj15':'Chunk of Foam','obj17':'Ball'}
    for key in key_vector:
        output_matrix = np.append(output_matrix, [[str(results['Number_of_subjects_functional'][key]), object_name[key],  str(results['functional'][key]['correct']), str(results['functional'][key]['false_positive']), str(results['functional'][key]['false_negative'])]],axis=0)

    output_matrix = np.append(output_matrix, [['', '','Grasp with similar hand pose','','']], axis=0)
 
    output_matrix = np.append(output_matrix, [['Number of samples', 'object No.', 'correct', 'False Positive', 'False Negative']],axis=0)

    for key in key_vector:
        output_matrix = np.append(output_matrix, [[str(results['Number_of_subjects_hand_pose'][key]), object_name[key],  str(results['hand_pose'][key]['correct']), str(results['hand_pose'][key]['false_positive']), str(results['hand_pose'][key]['false_negative'])]],axis=0)

    np.savetxt(os.getcwd()+'/results_from_code.csv', output_matrix, fmt='%s', delimiter=',')

        




        #elif "same hand pose":
        #    if not obj_name in results['hand_pose']:
        #        results['hand_pose'][obj_name] = {'correct': 0, 'false_positive': 0, 'false_negative':0}
        #        results['Number_of_subjects_hand_pose'][obj_name] = 0
        #    # the code below is wrong
        #    #for vec in group_consecutives(np.where(vector=='1')[0], step=1):
        #    #    #print len(vec)
        #    #    if len(vec) > 5:
        #    #        print 'found'
        #    loop_no = question_no[1].split('(')[1].split(')')[0]
        #    image_no = question_no[1].split('(')[0]
        #    if not loop_no in question[question_no[0]][obj_name]:
        #        question[question_no[0]][obj_name][loop_no] = dict()
        #    int_vec = np.genfromtxt(vector,delimiter=',')
        #    if image_no == '1':
        #        prime_cluster = cluster_no
        #        results['Number_of_subjects_hand_pose'][obj_name] += len(np.where(vector=='1')[0])
        #    else:
        #        if prime_cluster == cluster_no:
        #            results['hand_pose'][obj_name]['correct'] = results['hand_pose'][obj_name]['correct'] + len(np.where(vector=='1')[0])
        #            results['hand_pose'][obj_name]['false_negative'] += question[question_no[0]][obj_name][loop_no]['1_'+prime_cluster] - len(np.where(vector=='1')[0])
        #        else:
        #            results['hand_pose'][obj_name]['false_positive'] = results['hand_pose'][obj_name]['false_positive'] + len(np.where(vector=='1')[0])
        #            
        #    question[question_no[0]][obj_name][loop_no][image_no+'_'+cluster_no] = len(np.where(int_vec == 1)[0])

