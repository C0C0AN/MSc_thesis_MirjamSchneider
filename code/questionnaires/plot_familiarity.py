import pandas as pd


def concat_data(x, y):
    '''input path as string + name of new dataset as str
    (avoid using data as the first letters of your result file, because it may lead to unexpected errors)'''

    path = str(x)
    # specify which files to concatenate (change 'data*' depending on how you've named your files)
    allFiles = glob.glob(os.path.join(path,'*.csv'))
    # concatenate all files starting with data*
    df = pd.concat((pd.read_csv(f) for f in allFiles))
    # write csv to directory
    df.to_csv(path + str(y) +'.csv')
    print('done!')

# read in concatenated dataframe
df = pd.read_csv(csvfile)

# create new dataframe
columns = ['subject', 'stimulus', 'familiarity']
familiarity_df = pd.DataFrame(columns=columns)
# fill columns of new data frame with information of the old one
familiarity_df['subject'] = df['subject']
familiarity_df['stimulus'] = df['musikbeispiele_mac']
familiarity_df['familiarity'] = df['rating.response']

# replace stimulus path with stimulus name
familiarity_df.replace('/Users/cocoan/google_drive/CoCoAN/NC2U/NC2U_behavior/scripts/music_genres_inverseMDS/MusicExamples/1.wav', 'alternative', inplace=True)
familiarity_df.replace('/Users/cocoan/google_drive/CoCoAN/NC2U/NC2U_behavior/scripts/music_genres_inverseMDS/MusicExamples/2.wav', 'punk', inplace=True)
familiarity_df.replace('/Users/cocoan/google_drive/CoCoAN/NC2U/NC2U_behavior/scripts/music_genres_inverseMDS/MusicExamples/3.wav', 'metal', inplace=True)
familiarity_df.replace('/Users/cocoan/google_drive/CoCoAN/NC2U/NC2U_behavior/scripts/music_genres_inverseMDS/MusicExamples/4.wav', 'rocknroll', inplace=True)
familiarity_df.replace('/Users/cocoan/google_drive/CoCoAN/NC2U/NC2U_behavior/scripts/music_genres_inverseMDS/MusicExamples/5.wav', 'psychedelic', inplace=True)
familiarity_df.replace('/Users/cocoan/google_drive/CoCoAN/NC2U/NC2U_behavior/scripts/music_genres_inverseMDS/MusicExamples/6.wav', 'baroque', inplace=True)
familiarity_df.replace('/Users/cocoan/google_drive/CoCoAN/NC2U/NC2U_behavior/scripts/music_genres_inverseMDS/MusicExamples/7.wav', 'viennese_classic', inplace=True)
familiarity_df.replace('/Users/cocoan/google_drive/CoCoAN/NC2U/NC2U_behavior/scripts/music_genres_inverseMDS/MusicExamples/8.wav', 'modern_classic', inplace=True)
familiarity_df.replace('/Users/cocoan/google_drive/CoCoAN/NC2U/NC2U_behavior/scripts/music_genres_inverseMDS/MusicExamples/9.wav', 'renaissance', inplace=True)
familiarity_df.replace('/Users/cocoan/google_drive/CoCoAN/NC2U/NC2U_behavior/scripts/music_genres_inverseMDS/MusicExamples/10.wav', 'romantic', inplace=True)
familiarity_df.replace('/Users/cocoan/google_drive/CoCoAN/NC2U/NC2U_behavior/scripts/music_genres_inverseMDS/MusicExamples/11.wav', 'deephouse', inplace=True)
familiarity_df.replace('/Users/cocoan/google_drive/CoCoAN/NC2U/NC2U_behavior/scripts/music_genres_inverseMDS/MusicExamples/12.wav', 'drumnbass', inplace=True)
familiarity_df.replace('/Users/cocoan/google_drive/CoCoAN/NC2U/NC2U_behavior/scripts/music_genres_inverseMDS/MusicExamples/13.wav', 'dubstep', inplace=True)
familiarity_df.replace('/Users/cocoan/google_drive/CoCoAN/NC2U/NC2U_behavior/scripts/music_genres_inverseMDS/MusicExamples/14.wav', 'techno', inplace=True)
familiarity_df.replace('/Users/cocoan/google_drive/CoCoAN/NC2U/NC2U_behavior/scripts/music_genres_inverseMDS/MusicExamples/15.wav', 'trance', inplace=True)
familiarity_df.replace('/Users/cocoan/google_drive/CoCoAN/NC2U/NC2U_behavior/scripts/music_genres_inverseMDS/MusicExamples/16.wav', 'funk', inplace=True)
familiarity_df.replace('/Users/cocoan/google_drive/CoCoAN/NC2U/NC2U_behavior/scripts/music_genres_inverseMDS/MusicExamples/17.wav', 'hiphop', inplace=True)
familiarity_df.replace('/Users/cocoan/google_drive/CoCoAN/NC2U/NC2U_behavior/scripts/music_genres_inverseMDS/MusicExamples/18.wav', 'reggae', inplace=True)
familiarity_df.replace('/Users/cocoan/google_drive/CoCoAN/NC2U/NC2U_behavior/scripts/music_genres_inverseMDS/MusicExamples/19.wav', 'rnb', inplace=True)
familiarity_df.replace('/Users/cocoan/google_drive/CoCoAN/NC2U/NC2U_behavior/scripts/music_genres_inverseMDS/MusicExamples/20.wav', 'soul', inplace=True)

# create dataframe for each stimulus
df_alternative = familiarity_df.loc[familiarity_df['stimulus'] == 'alternative']
df_punk = familiarity_df.loc[familiarity_df['stimulus'] == 'punk']
df_metal = familiarity_df.loc[familiarity_df['stimulus'] == 'metal']
df_rocknroll = familiarity_df.loc[familiarity_df['stimulus'] == 'rocknroll']
df_psychedelic = familiarity_df.loc[familiarity_df['stimulus'] == 'psychedelic']
df_baroque = familiarity_df.loc[familiarity_df['stimulus'] == 'baroque']
df_viennese_classic = familiarity_df.loc[familiarity_df['stimulus'] == 'viennese_classic']
df_modern_classic = familiarity_df.loc[familiarity_df['stimulus'] == 'modern_classic']
df_renaissance = familiarity_df.loc[familiarity_df['stimulus'] == 'renaissance']
df_romantic = familiarity_df.loc[familiarity_df['stimulus'] == 'romantic']
df_deephouse = familiarity_df.loc[familiarity_df['stimulus'] == 'deephouse']
df_drumnbass = familiarity_df.loc[familiarity_df['stimulus'] == 'drumnbass']
df_dubstep = familiarity_df.loc[familiarity_df['stimulus'] == 'dubstep']
df_techno = familiarity_df.loc[familiarity_df['stimulus'] == 'techno']
df_trance = familiarity_df.loc[familiarity_df['stimulus'] == 'trance']
df_funk = familiarity_df.loc[familiarity_df['stimulus'] == 'funk']
df_hiphop = familiarity_df.loc[familiarity_df['stimulus'] == 'hiphop']
df_reggae = familiarity_df.loc[familiarity_df['stimulus'] == 'reggae']
df_rnb = familiarity_df.loc[familiarity_df['stimulus'] == 'rnb']
df_soul = familiarity_df.loc[familiarity_df['stimulus'] == 'soul']

# compute meanvalues of familiarity
mean_alternative = df_alternative['familiarity'].mean()
mean_punk = df_punk['familiarity'].mean()
mean_metal = df_metal['familiarity'].mean()
mean_rocknroll = df_rocknroll['familiarity'].mean()
mean_psychedelic = df_psychedelic['familiarity'].mean()
mean_baroque = df_baroque['familiarity'].mean()
mean_classic = df_viennese_classic['familiarity'].mean()
mean_modern = df_modern_classic['familiarity'].mean()
mean_renaissance = df_renaissance['familiarity'].mean()
mean_romantic = df_romantic['familiarity'].mean()
mean_deephouse = df_deephouse['familiarity'].mean()
mean_drumnbass = df_drumnbass['familiarity'].mean()
mean_dubstep = df_dubstep['familiarity'].mean()
mean_techno = df_techno['familiarity'].mean()
mean_trance = df_trance['familiarity'].mean()
mean_funk = df_funk['familiarity'].mean()
mean_hiphop = df_hiphop['familiarity'].mean()
mean_reggae = df_reggae['familiarity'].mean()
mean_rnb = df_rnb['familiarity'].mean()
mean_soul = df_soul['familiarity'].mean()

# compute sd of familiarity
std_alternative = df_alternative['familiarity'].std()
std_punk = df_punk['familiarity'].std()
std_metal = df_metal['familiarity'].std()
std_rocknroll = df_rocknroll['familiarity'].std()
std_psychedelic = df_psychedelic['familiarity'].std()
std_baroque = df_baroque['familiarity'].std()
std_classic = df_viennese_classic['familiarity'].std()
std_modern = df_modern_classic['familiarity'].std()
std_renaissance = df_renaissance['familiarity'].std()
std_romantic = df_romantic['familiarity'].std()
std_deephouse = df_deephouse['familiarity'].std()
std_drumnbass = df_drumnbass['familiarity'].std()
std_dubstep = df_dubstep['familiarity'].std()
std_techno = df_techno['familiarity'].std()
std_trance = df_trance['familiarity'].std()
std_funk = df_funk['familiarity'].std()
std_hiphop = df_hiphop['familiarity'].std()
std_reggae = df_reggae['familiarity'].std()
std_rnb = df_rnb['familiarity'].std()
std_soul = df_soul['familiarity'].std()


# plot figure
import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 20
frequency = (mean_alternative, mean_punk, mean_metal, mean_rocknroll, mean_psychedelic, mean_baroque, mean_classic, mean_modern,
             mean_renaissance, mean_romantic, mean_deephouse, mean_drumnbass, mean_dubstep, mean_techno, mean_trance, mean_funk, mean_hiphop, mean_reggae, mean_rnb, mean_soul)
error = (std_alternative, std_punk, std_metal, std_rocknroll, std_psychedelic, std_baroque, std_classic, std_modern, std_renaissance, std_romantic, std_deephouse, std_drumnbass,\
        std_dubstep, std_techno, std_trance, std_funk, std_hiphop, std_reggae, std_rnb, std_soul)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
ax.barh(index, frequency, align='center', xerr=error,
        color='green', ecolor='black')

plt.ylabel('Stimuli')
ax.invert_yaxis()  # labels read top-to-bottom
plt.xlabel('Familiarity rating of stimuli')
ax.set_xlim(left=1, right=5)
plt.title('Familiarity rating of music stimuli used in this study')
plt.yticks(index + bar_width, (
'alternative', 'punk', 'heavy metal', 'rock_n_roll', 'psychedelic', 'baroque', 'viennese classic', 'modern classic',
'renaissance', 'romantic', 'deephouse', 'drum_n_bass', 'dubstep', 'techno', 'trance', 'funk', 'hiphop', 'reggae',
'r_n_b', 'soul'))

plt.tight_layout()
plt.show()