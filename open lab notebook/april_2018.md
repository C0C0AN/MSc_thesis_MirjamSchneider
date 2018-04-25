# week 02.04.-05.04.
- holidays

# week 09.04.-13.04.
- pliers: had to install duecredit and librosa manually on top so pliers will work (python version issue)
  - created a jupyter-notebook to try out the audio feature extraction example from github (slightly transformed the code and added import of matplotlib.pyplot), documentation: http://tyarkoni.github.io/pliers/
- validation questionnaire
  - problem that occurred: result page messed up the sortable order, finally Jens updated the whole survey to a newer stable version (1.0.16) and now everything works fine
  - questionnaire result file: if a question is skipped, an error occurs
    - wrote if-loop for each item so it is only written to the csv if there is a value in it and otherwise skipped
    - added the item “id” which has to be added manually to the json-string when the data is copied from the online result sheet: this id serves to distinguish the different participants result tables (“questionnaire_data_id.csv”)
as the strings have to be copied manually anyways this seems to be the easiest solution to me

# week 16.04.-20.04.
- worked on music feature extraction using pliers and bregman toolkit
  - it seems possible to extract features using pliers and calculate their distance using bregman (as pliers has no distance calculator)
- repeated some jupyter-notebooks on pandas and numpy including new notebooks form peers workshop
- worked on questionnaire analysis: still some problems occur concerning missing values in certain columns
