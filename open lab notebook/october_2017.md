# week 16.10.-20.10.

- looked for a tool to normalize the loudness of our audio stimuli
  - found this open source program on [github](https://github.com/slhck/ffmpeg-normalize)
  - used EBU-R128 option  because it measures loudness not only in dezibel but also depending on frequency [similar to the human ear](https://auphonic.com/blog/2012/08/02/loudness-measurement-and-normalization-ebu-r128-calm-act/)
  - problems occur concerning some files that could not be normalized, but could be solved by using another code (but the same program)
- detected that there were two stimuli missing in the baroque-category and created two more
- ethic proposal
  - read examples
  - wrote our own ethic proposal
  - posted the ethic proposal in slack to get some suggestions and corrections from other members of the group
- looked for a tool to apply a fade-in- and fade-out-effect to the stimuli
  - it is possible to do this in audacity “by hand” 
  - found an [instruction and tool](https://github.com/jiaaro/pydub) to code this in python, but I do not know how exactly fading is made here


# week 23.10.-27.10.
- plotted amplitude over time (ms) and power (dB) over frequency (kHz) to compare the stimuli I made with the ones of Hanke et al.
  - Wanted to detect if we used a similar kind of fade-out-effect
  - Also wanted to plot power (dB) over time (ms) but did not find a fitting code 
- wrote samples for the mail and bulletin we want to use to recruit participants for our study
- started to work on the online survey we want to use for stimuli validation
  - used this [open source survey editor](https://surveyjs.io/Editor) to create our own survey
  - decided which question types we want to use (checkbox, radio group, rating, drag & drop (“sortable”), free text)
  - decided what demographic questions we want to ask and how validation should work
