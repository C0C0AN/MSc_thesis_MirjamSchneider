# week 05.02.-09.02.
- clicked through whole experiment on my laptop
  - everything worked out, logfile and csvfile are written
- corrected some slides: break was time dependent (now only depends on key), deleted letsgoon-slide because I do not need a trigger regulated slide at this point in the experiment
  - transformed scanner protocol according to changes
- worked on my presentation on analysis methods

# week 12.02.-16.02.
- checked lab.js (https://felixhenninger.github.io/lab.js/) if it is an alternative to Jens questionnaire
  - I do not think so, it is more an alternative to psychopy, but I am not sure if auditory stimuli can be included at all (maybe using html)
  - different question types can be implemented using html (no gui) – no difference to java script except it is a different language (tutorial: https://labjs.readthedocs.io/en/latest/learn/forms/2-elements.html) 
- worked on presentation on methods (still reading the paper)
- wrote my project proposal for the local Brainimaging Facility 

# week 19.02.-23.02.
- tested experiment at the scanner again (using the ‘old’ computer with a new setup)
  - changed monitor settings in code: SetUp Window: size [1360,768], fullscr=True → now the window fits the scanner computer and the presentation screen
  - problem: the video freezes at about 3 min → maybe because there is too much to load for psychopy/the computer 
tried to find some option to preload video but did not found anything 
- converted videos to mp4, but size stayed the same, so I do not know if this will change anything (ffmpeg -i movie.mkv -codec copy movie.mp4)
- worked on presentation on methods

# week 26.02.-02.03.
- worked on online survey with Christoph
  - corrected some errors and typos in the questionnaire script
  - survey runs and information is saved, music stimuli have to be included
- worked on presentation on methods
- tested experiment at the scanner again and the videos still stop in the middle of the run
  - Klara checked the experiment at her laptop and it worked
  - maybe the problem is my "broken" usb-stick or missing updates at the scanner-computer
