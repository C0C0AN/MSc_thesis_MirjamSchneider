import pandas as pd


def concat_data(x, y):
    '''input path as string + name of new dataset as str
    (avoid using data as the first letters of your result file, because it may lead to unexpected errors)'''

    path = str(x)
    # specify which files to concatenate (change 'data*' depending on how you've named your files)
    allFiles = glob.glob(os.path.join(path,'*.csv'))
    # concatenate all files starting with data*
    df = pd.concat((pd.read_csv(f) for f in allFiles))
    # drop fields with NaN
    df.dropna()
    # write csv to directory
    df.to_csv(path + str(y) +'.csv')
    print('done!')

# read in concatenated dataframe
df = pd.read_csv(csvfile)

# create new dataframe
columns = ['subject', 'pop', 'rock', 'hiphop', 'latin', 'soul', 'hardrock', 'electronic', 'new_age', 'folk', 'classic', 'jazz']
mpqr_df = pd.DataFrame(columns=columns)
# fill columns of new data frame with information of the old one
mpqr_df['subject'] = df['participant']
mpqr_df['pop'] = df['rating_pop.response']
mpqr_df['rock'] = df['rating_rock.response']
mpqr_df['hiphop'] = df['rating_hiphop.response']
mpqr_df['latin'] = df['rating_latin.response']
mpqr_df['soul'] = df['rating_soul.response']
mpqr_df['hardrock'] = df['rating_hardrock.response']
mpqr_df['electronic'] = df['rating_electronic.response']
mpqr_df['new_age'] = df['rating_newage.response']
mpqr_df['folk'] = df['rating_folk.response']
mpqr_df['classic'] = df['rating_classic.response']
mpqr_df['jazz'] = df['rating_jazz.response']


# compute meanvalues of genre rating
mean_pop = mpqr_df['pop'].mean()
mean_rock = mpqr_df['rock'].mean()
mean_hiphop = mpqr_df['hiphop'].mean()
mean_latin = mpqr_df['latin'].mean()
mean_soul = mpqr_df['soul'].mean()
mean_hardrock = mpqr_df['hardrock'].mean()
mean_electronic = mpqr_df['electronic'].mean()
mean_new_age = mpqr_df['new_age'].mean()
mean_folk = mpqr_df['folk'].mean()
mean_classic = mpqr_df['classic'].mean()
mean_jazz = mpqr_df['jazz'].mean()

# compute std of genre rating
std_pop = mpqr_df['pop'].std()
std_rock = mpqr_df['rock'].std()
std_hiphop = mpqr_df['hiphop'].std()
std_latin = mpqr_df['latin'].std()
std_soul = mpqr_df['soul'].std()
std_hardrock = mpqr_df['hardrock'].std()
std_electronic = mpqr_df['electronic'].std()
std_new_age = mpqr_df['new_age'].std()
std_folk = mpqr_df['folk'].std()
std_classic = mpqr_df['classic'].std()
std_jazz = mpqr_df['jazz'].std()


# plot figure
import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 11
frequency = (mean_pop, mean_rock, mean_hiphop, mean_latin, mean_soul, mean_hardrock, mean_electronic, mean_new_age, mean_folk, mean_classic, mean_jazz)
error = (std_pop, std_rock, std_hiphop, std_latin, std_soul, std_hardrock, std_electronic, std_new_age, std_folk, std_classic, std_jazz)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
ax.barh(index, frequency, align='center', xerr=error,
        color='yellowgreen', ecolor='black')

plt.ylabel('Music genres')
ax.invert_yaxis()  # labels read top-to-bottom
plt.xlabel('Music genre preference')
ax.set_xlim(left=1, right=5)
plt.title('Results of MPQR')
plt.yticks(index + bar_width, ('pop', 'rock', 'hiphop', 'latin', 'soul', 'hardrock', 'electronic', 'new_age', 'folk', 'classic', 'jazz'))

plt.tight_layout()
plt.show()