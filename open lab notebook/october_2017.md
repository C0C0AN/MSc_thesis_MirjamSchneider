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
