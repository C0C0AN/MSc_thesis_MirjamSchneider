# week 06.08.-10.08.
- worked on visualization and computation of behavioral data, music features and conceptual models
  - met with Klara and Marie and wrote some notes 
  - used Peers toolbox URIAL
  - rdm_concat.py: concatenated all multidimensionalscaling-result-csvs in one pkl-file, concatenated all music-feature-csvs in one pkl-file, conatenated all conceptual-models-csvs (allequal, allunequal, maingenres, random) to one pkl-file
cave: pkl-files have to be in a separate folder where only this file is for further analysis (otherwise ValueError: Buffer has wrong number of dimensions (expected 1, got 2))
  - rdm_avg: average rdm of all participants
  - plot.py: plottet rdm_avg
y-axis was wrong labeled (reversed) so I changed one line in the code, now it is working
  - compare_rdm.py: compared mds-pkl with conceptual-pkl using kendalls tau as distance algorithm and plotted it as barplot, compared mds-pkl with music-features-pkl using pearson and spearman as algorithms and plotted them as violin plots
- finished a first version of my methods chapter 
- RDM computation of activation in rois (matlab)
  - plotting in URIAL also worked out after adding categories as column names
  - have to preprocess all my subjects and compute the RDMs for each sub and each roi in the next week, preprocessing is running
