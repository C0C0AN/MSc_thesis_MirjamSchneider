#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 16:05:24 2018

@author: mirjam
"""
## first go to correct working directory, where the files should be written!
# (e.g. /home/mirjam/Desktop/Masterarbeit/NC2U_BIDS/sub-00/func)

def eventfiles (csvfile, subject):
	# input: csvfile = file from psychopy-log that ends with trials.csv,
	# subject = subject-number (sub-xy)

    # import necessary modules
    import pandas as pd
    
    # read in data frame from psychopy-log
    df = pd.read_csv(csvfile)
    # fill nan-values with dummy-value 'nothing' to avoid error in the following loop
    df = df.fillna('nothing')
    
    # loop over stimulus-column to cut of the '.wav' ending
    for index, stim in enumerate(df['stim']):
        df['stim'][index]=stim[:-4]
    
    # create new dataframe
    columns = ['onset', 'duration', 'pause', 'stimuli', 'run_type']
    events_df = pd.DataFrame(columns=columns)
    # fill columns of new data frame with information of the old one
    events_df['onset'] = df['trial_start_run_time_raw']
    events_df['duration'] = 6
    events_df['pause'] = df['delay']
    events_df['stimuli'] = df['stim']
    events_df['run_type'] = df['run']
    
    # cut dataframe at certain rows to get separate files for each run
    # run_xy = run order in this subject, run = run type (randomised)
    # Zeilen anpassen
    run_01 = events_df.truncate(after=39)
    run_02 = events_df.truncate(before=46, after=85)
    run_03 = events_df.truncate(before=92, after=131)
    run_04 = events_df.truncate(before=138, after=177)
    run_05 = events_df.truncate(before=184, after=223)
    run_06 = events_df.truncate(before=230, after=269)
    run_07 = events_df.truncate(before=276, after=315)
    run_08 = events_df.truncate(before=322, after=361)
    
    # save new files to correct folders
    run_01.to_csv(subject + '_task-NC2U_run-1_events' + '.tsv', sep='\t', index=False)
    run_02.to_csv(subject + '_task-NC2U_run-2_events' + '.tsv', sep='\t', index=False)
    run_03.to_csv(subject + '_task-NC2U_run-3_events' + '.tsv', sep='\t', index=False)
    run_04.to_csv(subject + '_task-NC2U_run-4_events' + '.tsv', sep='\t', index=False)
    run_05.to_csv(subject + '_task-NC2U_run-5_events' + '.tsv', sep='\t', index=False)
    run_06.to_csv(subject + '_task-NC2U_run-6_events' + '.tsv', sep='\t', index=False)
    run_07.to_csv(subject + '_task-NC2U_run-7_events' + '.tsv', sep='\t', index=False)
    run_08.to_csv(subject + '_task-NC2U_run-8_events' + '.tsv', sep='\t', index=False)

    # create file including all runs (if you need it)
    # all_runs_df = pd.concat([run_01, run_02, run_03, run_04, run_05, run_06, run_07, run_08], axis=0)
    # all_runs_df.to_csv(subject + '_task-NC2U_events' + '.tsv', sep='\t', index=False)
