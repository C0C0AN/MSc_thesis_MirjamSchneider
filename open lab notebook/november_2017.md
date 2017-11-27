# week 01.-03.11.

- worked on supplemental material for the ethic proposal
  - bulletins, subject information, subject agreement
- translated 'Montreal Battery of Evaluation of Amusia' (MBEA; Peretz et al. 2003)

# week 06.-10.11.
- submitted ethic proposal
- gained insight in [psychopy](http://www.psychopy.org/)
- read up on [de Bruijn sequences](https://github.com/MirjamSchneider/MSc_thesis_MirjamSchneider/blob/master/open%20lab%20notebook/De%20Bruijn%20Cycles.pdf) (for stimuli randomisation)

# week 13.-17.11.
- was concerned with randomisation
  - different scripts to generate de Bruijn sequences
  - de Bruijn sequences are not suitable for our experimental design
  - decided to use [Optseq2](https://surfer.nmr.mgh.harvard.edu/optseq/)

# week 20.-24.11.
- computed the stimuli sequences for our experiment using Optseq2 (first level counterbalanced, eight best possible sequences out of 100.000)
  - code: optseq2 --ntp 474 --tr 1 --psdwin 4 8 --ev stimulus1 6 2 --ev stimulus2 6 2 --ev stimulus3 6 2 --ev stimulus4 6 2 --ev stimulus5 6 2 --ev stimulus6 6 2 --ev stimulus7 6 2 --ev stimulus8 6 2 --ev stimulus9 6 2 --ev stimulus10 6 2 --ev stimulus11 6 2 --ev stimulus12 6 2 --ev stimulus13 6 2 --ev stimulus14 6 2 --ev stimulus15 6 2 --ev stimulus16 6 2 --ev stimulus17 6 2 --ev stimulus18 6 2 --ev stimulus19 6 2 --ev stimulus20 6 2 --tnullmin 4 --tnullmax 8 --nkeep 1 --focb nCB1Opt --o IAPS --nsearch 1000
- gave a short presentation on stimuli randomisation in condition rich designs
  - about the tools I tried and why problems occured

# plan for this week
- understand structure of psychopy-experiment of Hanke et al. 2017
- write a first synopsis
- read more about computational models
- revise ethics proposal for second submission

