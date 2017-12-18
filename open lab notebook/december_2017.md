# week 04.12.-08.12.
- understood structure of psychopy-experiment of Hanke et al. 2017
  - tried it on my own laptop and at the scanner: it worked so we can use it as basis for our own experiment
  - went through the whole experiment once (at the laptop, t as key for mri-trigger) to get an example for the structure of the output (especially the log-files)
- wrote a [script](https://github.com/MirjamSchneider/MSc_thesis_MirjamSchneider/blob/master/open%20lab%20notebook/make_design.py) to construct our eight different runs for the experiment out of the stimuli-list, a list of different delays and the sequences I computed using OptSeq2
- corrected my own synopsis and made some remarks to the ones of the other students 
- the validation survey is still under progress, problems concerning the different question-items are solved, but embedding the audio files seems to be difficult (talked to a colleague about this, who writes the code for this survey as I have no idea about java-script and websites)

# week 11.12.-15.12.
- wrote our experiment in PsychoPy (using the structure of the experiment of Hanke et al. 2017) with the help of Christoph
  - calibration routine: added the option for the subjects to individually change the volume by keypress and keep the chosen volume through the whole experiment
  - appended a new end-routine (“Das war es schon! Vielen Dank für die Teilnahme am Experiment!”)
- checked our experiment at the MRI-Scanner
  - allocated our keys for changing the volume or going on to the next sample to the buttons of the response box
  - checked headphones: the volume seems to be a bit quiet all in all → maybe we have to turn it to the maximum at the computer itself
  - tried some settings concerning field of view, TR, slices etc. at the scanner
- wanted to check if OptSeq2 code works also for TRs 1.1-1.5, the code does not seem to work any more (“Error: option 6 unknown”) but I did not change anything
  - the code does not recognize the duration time (–ev stimulus1 **6** 2) no matter what number I try
- checked other music related MRI-papers for their MRI-setting to gain information for our own setting

# plan for this week
- transform psychopy-experiment
  - what do we use for calibration? Some of our stimuli or should we create a differing calibration-sound-file?
  - equal distribution of delays (4,6 or 8s) per run, so all runs have equal length
- write a script to read out the log-file output of the experiment and/or make it more clearly arranged
