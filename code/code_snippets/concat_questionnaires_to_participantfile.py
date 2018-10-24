#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 14:18:01 2018

@author: mirjam
"""

import glob, os
import pandas as pd

def concat_per_subject (folder, subject):
    # folder = path to folder were questionnaire-result-csv-files are
    # subject = subject-number(sub-xy)
    # concatenate all files ending with .csv
    allFiles = glob.glob(os.path.join(folder, '*.csv'))
    # create new dataframe to store information from csv-files
    df = pd.concat((pd.read_csv(f) for f in allFiles))
    # drop fields with NaN
    df.dropna()
    # write to one tsv-file for each subject
    df.to_csv('quest' + subject + '.tsv')
        
        
def concat_data(x, y):
    '''input path as string + name of new dataset as str
    (avoid using data as the first letters of your result file, because it may lead to unexpected errors)'''

    path = str(x)
    # specify which files to concatenate (change 'data*' depending on how you've named your files)
    allFiles = glob.glob(os.path.join(path,'*.csv'))
    # concatenate all files starting with data*
    df = pd.concat((pd.read_csv(f) for f in allFiles))
    # drop unnecessary column
    # df.drop(['trials.thisRepN: 0'],axis=1, inplace=True)
    # write csv to directory
    df.to_csv(path + str(y) +'.csv')
    print('done!')