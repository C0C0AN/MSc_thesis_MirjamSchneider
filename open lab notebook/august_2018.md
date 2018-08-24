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

# week 13.08.-17.08.
- started to write introduction of thesis 
- finished preprocessing of all subjects incl. roi transformation
- created matrices for each subject for each roi in matlab 
- wrote small script to add column names (genre categories) to csv-files (rdm_add_column_names.py)
- concatenated csv-files of rois to pkls and computed average rdms per rois 
  - plotted average rdms
- compared each roi-pkl with the music-feature-pkl
  - results show mostly very low correlations 
- created all_regions_pkl that includes all average rdms of all rois
  - compared behavioral pkl to this all_regions_pkl → correlation about 0.0 in all regions
- created csv-files in matlab for noisenormalized matrices (pcm)
  - sub-16 as an example, shows a gradient across matrix that makes no sense
- created csv-files in matlab for LDC matrices (rsa)
  - got 1x190 array and I do not get how to transform this into a 20x20 matrix, because the 0-diagonal is missing and I need to mirror the 190 values in a correct way along this diagonal
  - visualization in matlab is possible (but makes no sense), visualization in python not possible

# week 20.08.-24.08.
- wrote parts of introduction to my thesis
  - basic fMRI part 
  - what is a music genre 
  - music feature extraction 
  - aims and hypotheses
  - started with: Previous literature and introduction to RSA and PCM
- read about RSA, PCM and MVPA in general 
- tried some analyses using URIAL
  - there seems to be a problem, Peer is going to look at it
