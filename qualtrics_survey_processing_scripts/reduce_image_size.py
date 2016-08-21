#!/usr/bin/env python

import os, sys
import getpass
import Image

if __name__ == "__main__":
    user = getpass.getuser()
    images_directory = '/home/'+user+'/similar_grasp_images/'
    output_directory = images_directory+'reduced_size_images/'
    recursive_list = [os.path.join(images_directory,o) for o in os.listdir(images_directory) if (os.path.isdir(os.path.join(images_directory,o)) and 'chosen' in o)]
    for directory in recursive_list:
        for img in os.listdir(directory):
            try: 
                im = Image.open(directory+'/'+img)
                size = (im.size[0]/3, im.size[1]/3)
                im = im.resize(size,Image.ANTIALIAS)
                im.save(output_directory+img)
            except IOError, e:
                print img
                print "Cannot open or save the file Error",e


