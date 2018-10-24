## short script to delete first column of all csv-files in a certain directory

import pandas as pd
import glob, os

# path to folder with csv-files
path = '/home/mirjam/Desktop/Masterarbeit/Auswertung/behavior/behavioral_rdms'
allFiles = glob.glob(os.path.join(path, '*.csv'))

# each csv-file will be replaced by a new one without first column (with the exact same filename)
for file in allFiles:
    variable = pd.read_csv(file)
    variable.drop(variable.columns[0], axis=1, inplace=True)
    variable.to_csv(file, index=False)