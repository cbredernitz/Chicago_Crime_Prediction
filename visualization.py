import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

# Loading data
df = pd.read_csv('Crimes_-_2001_to_present.csv', encoding='utf-8')

# Dropping the random outlier that was misentered from the dataset
df = df[df['Latitude'] > 40]

# Assinging categorical variable to the time of the month
df.loc[df['Date'].str.contains('01/'), 'T_month'] = '1'
df.loc[df['Date'].str.contains('02/'), 'T_month'] = '2'
df.loc[df['Date'].str.contains('03/'), 'T_month'] = '3'
df.loc[df['Date'].str.contains('04/'), 'T_month'] = '4'
df.loc[df['Date'].str.contains('05/'), 'T_month'] = '5'
df.loc[df['Date'].str.contains('06/'), 'T_month'] = '6'
df.loc[df['Date'].str.contains('07/'), 'T_month'] = '7'
df.loc[df['Date'].str.contains('08/'), 'T_month'] = '8'
df.loc[df['Date'].str.contains('09/'), 'T_month'] = '9'
df.loc[df['Date'].str.contains('10/'), 'T_month'] = '10'
df.loc[df['Date'].str.contains('11/'), 'T_month'] = '11'
df.loc[df['Date'].str.contains('12/'), 'T_month'] = '12'

# Plotting
# sns.lmplot( x="Longitude", y="Latitude", data=df, fit_reg=False, hue='Primary Type', legend=False, scatter_kws={"s": 1})
 
# Move the legend to an empty part of the plot
# plt.legend(loc='lower right', fontsize='10')

plt.show()
