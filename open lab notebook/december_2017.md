# week 04.12.-08.12.
- understood structure of psychopy-experiment of Hanke et al. 2017
  - tried it on my own laptop and at the scanner: it worked so we can use it as basis for our own experiment
  - went through the whole experiment once (at the laptop, t as key for mri-trigger) to get an example for the structure of the output (especially the log-files)
- wrote a [script](https://github.com/MirjamSchneider/MSc_thesis_MirjamSchneider/blob/master/open%20lab%20notebook/make_design.py) to construct our eight different runs for the experiment out of the stimuli-list, a list of different delays and the sequences I computed using OptSeq2
- corrected my own synopsis and made some remarks to the ones of the other students 
- the validation survey is still under progress, problems concerning the different question-items are solved, but embedding the audio files seems to be difficult (talked to a colleague about this, who writes the code for this survey as I have no idea about java-script and websites)


# plan for this week
- transform psychopy-experiment
  - which keys are mapped in the script? (space, 1, 2, something else?) how will we do it?
  - delete everything concerning the questions
  - what do we use for calibration? Some of our stimuli or should we create a differing calibration-sound-file?
- write a script to read out the log-file output of the experiment and/or make it more clearly arranged
