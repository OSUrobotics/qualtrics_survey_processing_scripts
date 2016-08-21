#!/usr/bin/env python

from bs4 import BeautifulSoup
import codecs
import os
import getpass
from selenium import webdriver
import re


if __name__ == "__main__":
    user_name = getpass.getuser()
    chromedriver = '/home/'+user_name+'/Downloads/chromedriver'
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver  = webdriver.Chrome(chromedriver)
    driver.get("http://oregonstate.qualtrics.com")
    print "--------------------------------------------------------"
    print
    user_input = raw_input(" Please naviagate to graphics library in qualtrics and then press enter")
    print 
    print "--------------------------------------------------------"
    abc  = driver.find_elements_by_css_selector(".thumbnail-description-container")
    new_file = codecs.open('imageURL.csv','w',encoding = 'utf-8')
    urls = {}
    for i in range(0,len(abc)):
        h = abc[i]
        soup = BeautifulSoup(h.get_attribute('innerHTML'))
        url_id = [tag.get('id') for tag in soup.find_all('input')]
        urls[i] = url_id[0].split('_Edit')[0]
        filename = h.text
        new_file.write(filename + ",<img src=https://oregonstate.qualtrics.com/WRQualtricsControlPanel/Graphic.php?IM=" +urls[i]+ " />" +'\n')




