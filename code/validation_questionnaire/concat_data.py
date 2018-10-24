# function to concatenate data-frames/csv.-files

import glob, os
import pandas as pd

def concat_data(x, y):
    '''input path as string + name of new dataset as str 
    (avoid using data as the first letters of your result file, because it may lead to unexpected errors)'''
    
    path = str(x)
    # specify which files to concatenate (change 'data*' depending on how you've named your files)
    allFiles = glob.glob(os.path.join(path,'data*'))
    # concatenate all files starting with data*
    df = pd.concat((pd.read_csv(f) for f in allFiles))
    # drop unnecessary column
    df.drop(['Unnamed: 0'],axis=1, inplace=True)
    # write csv to directory
    df.to_csv(path + str(y) +'.csv')
    print('done!')
