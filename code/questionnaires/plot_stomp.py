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
columns = ['subject', 'music_genres', 'preference_rating']
stomp_df = pd.DataFrame(columns=columns)
# fill columns of new data frame with information of the old one
stomp_df['subject'] = df['participant']
stomp_df['music_genres'] = df['Musikgenres']
stomp_df['preference_rating'] = df['rating_preferences.response']

# replace Klassik with classic
stomp_df.replace('Klassik', 'Classic', inplace=True)

# create dataframe for each stimulus
df_classic = stomp_df.loc[stomp_df['music_genres'] == 'Classic']
df_blues = stomp_df.loc[stomp_df['music_genres'] == 'Blues']
df_country = stomp_df.loc[stomp_df['music_genres'] == 'Country']
df_electronic = stomp_df.loc[stomp_df['music_genres'] == 'Dance/Electronica']
df_folk = stomp_df.loc[stomp_df['music_genres'] == 'Folk']
df_rap = stomp_df.loc[stomp_df['music_genres'] == 'Rap/HipHop']
df_soul = stomp_df.loc[stomp_df['music_genres'] == 'Soul/Funk']
df_religious = stomp_df.loc[stomp_df['music_genres'] == 'Religious']
df_alternative = stomp_df.loc[stomp_df['music_genres'] == 'Alternative']
df_jazz = stomp_df.loc[stomp_df['music_genres'] == 'Jazz']
df_rock = stomp_df.loc[stomp_df['music_genres'] == 'Rock']
df_pop = stomp_df.loc[stomp_df['music_genres'] == 'Pop']
df_metal = stomp_df.loc[stomp_df['music_genres'] == 'Heavy/Metal']
df_soundtrack = stomp_df.loc[stomp_df['music_genres'] == 'Soundtrack/Theme_Song']


# compute meanvalues of music preference
mean_classic = df_classic['preference_rating'].mean()
mean_blues = df_blues['preference_rating'].mean()
mean_country = df_country['preference_rating'].mean()
mean_electronic = df_electronic['preference_rating'].mean()
mean_folk = df_folk['preference_rating'].mean()
mean_rap = df_rap['preference_rating'].mean()
mean_soul = df_soul['preference_rating'].mean()
mean_religious = df_religious['preference_rating'].mean()
mean_alternative = df_alternative['preference_rating'].mean()
mean_jazz = df_jazz['preference_rating'].mean()
mean_rock = df_rock['preference_rating'].mean()
mean_pop = df_pop['preference_rating'].mean()
mean_metal = df_metal['preference_rating'].mean()
mean_soundtrack = df_soundtrack['preference_rating'].mean()


# compute std of music preference
std_classic = df_classic['preference_rating'].std()
std_blues = df_blues['preference_rating'].std()
std_country = df_country['preference_rating'].std()
std_electronic = df_electronic['preference_rating'].std()
std_folk = df_folk['preference_rating'].std()
std_rap = df_rap['preference_rating'].std()
std_soul = df_soul['preference_rating'].std()
std_religious = df_religious['preference_rating'].std()
std_alternative = df_alternative['preference_rating'].std()
std_jazz = df_jazz['preference_rating'].std()
std_rock = df_rock['preference_rating'].std()
std_pop = df_pop['preference_rating'].std()
std_metal = df_metal['preference_rating'].std()
std_soundtrack = df_soundtrack['preference_rating'].std()

# plot figure
import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 14
frequency = (mean_classic, mean_blues, mean_country, mean_electronic, mean_folk, mean_rap, mean_soul, mean_religious, mean_alternative, mean_jazz, mean_rock, mean_pop, mean_metal, mean_soundtrack)
error = (std_classic, std_blues, std_country, std_electronic, std_folk, std_rap, std_soul, std_religious, std_alternative, std_jazz, std_rock, std_pop, std_metal, std_soundtrack)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
ax.barh(index, frequency, align='center', xerr=error,
        color='yellowgreen', ecolor='black')

#plt.ylabel('Music genres')
ax.invert_yaxis()  # labels read top-to-bottom
plt.xlabel('Music genre preference')
ax.set_xlim(left=1, right=7)
plt.title('Results of STOMP')
plt.yticks(index + bar_width, ('classic', 'blues', 'country', 'dance/electronic', 'folk', 'rap/hiphop', 'soul/funk', 'religious', 'alternative', 'jazz', 'rock', 'pop', 'heavy metal', 'soundtrack/theme song'))

plt.tight_layout()
plt.show()