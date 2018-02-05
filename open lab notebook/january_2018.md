# week 01.01.-05.01.
- BipoLife training in Dresden for job as student research assistant

# week 08.01.-12.01.
- solved the "delay-problem" in my [script for design construction](https://github.com/MirjamSchneider/MSc_thesis_MirjamSchneider/blob/master/open%20lab%20notebook/make_design.py) using a list including every possible delay (4,6,8) 13 times where every index is picked once per run (added a delay of 0 for the last stimulus)
- submitted second version of ethic proposal
- tried the experiment at the scanner again: did a first functional scan and everything seems to work out
  - tried different values for field of view and other settings
  - wrote a first version of a scanner protocol to document these settings
  - simulated the (complete) experiment at the laptop to see what kind of result-files are written: writes a calibration.csv-file and a trials.csv-file, produces empty log-file and stopped after the forth run – why?
- wrote a first [structure of my thesis](https://github.com/MirjamSchneider/MSc_thesis_MirjamSchneider/blob/master/open%20lab%20notebook/structure_thesis.md)

# week 22.01.-26.01.
- checked psychopy script to see if it breaks again after run 4: script works through whole experiment, wrote csv-files (runs, calibration, trails and whole experiment) and log-file
  - changed some keypresses and added slides (routines “letsgo_scr” and “letsgoon_scr”)
- made 8 sec long moviestimuli to show during experimental runs (mkv files)
  - movie sequences of planet earth (eiswelten, graswelten, meereswelten)
- submitted revised [ehtic proposal](https://github.com/MirjamSchneider/MSc_thesis_MirjamSchneider/tree/master/ethic%20proposal)
  - finally got a positive vote
- talked to Jens about the questionnaire for stimuli validation again
  - Jens set up the online server for the questionnaire
  - I have to write the code for the exact questionnaire (order of items etc.)

# week 22.01.-26.01.
- wrote code for validation questionnaire for Jens
- tested experiment at the scanner again: still problems with psychopy-experiment und the earphones seem to produce artefacts…
- updated scanner protocol 
- tried to include movie sequences in psychopy
  - problems: auditory stimuli do not play during movie, experiment breaks after movie

# week 29.01.-02.02.
- installed GitKraken
- worked on psychopy experiment: still problems including the movie and playing the auditory stimuli simultanously (just one stimulus is played so the experiment does not seem to loop over trials)
  - explained the problem  in psychopy discourse and got the answer that the problem is that I use code that is compiled from Builder view and therefore is difficult to transform
  - found solution using Builder view! (Added movie to trial-block in Builder view and compiled code and saw how it is implemented in the experiment → applied it to my own experiment) 
  - Added column “movie_stim” in run.csv-files so every run has its own movie sequence that is played during auditive stimulation
  - Experiment finally works out incl. movie sequences!
- Added my synopsis, the ethic proposal and some more information about the project on OSF

# plan for this week
- prepare short presentation on methods (for next weeks meeting)
