#!/usr/bin/env python

import os, sys
import getpass
import Image

if __name__ == "__main__":
    user = getpass.getuser()
    images_directory = '/home/'+user+'/similar_grasp_images/'
    recursive_list = [os.path.join(images_directory,o) for o in os.listdir(images_directory) if (os.path.isdir(os.path.join(images_directory,o)) and 'obj' in o)]
    for directory in recursive_list:
        for img in os.listdir(directory):
            print img
            output_file_name = img.split('_Hand')[0]+'.jpg'
            try: 
                os.rename(directory+'/'+img, directory+'/'+output_file_name)
            except IOError:
                print "Cannot open or save the file"


