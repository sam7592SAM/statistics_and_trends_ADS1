

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sts


def read_data(data, country, years):
    df = pd.read_csv(data, skiprows=4)
    df.drop(columns=['Country Code'], axis=1, inplace=True)
    df1 = df.iloc[country, years]
    df2 = df1.T
    return df1, df2


def stat_function(data):
    print(data.describe())
    print(data.corr())


def plot(data, kind, title, x, y):
    data.plot(kind=kind)
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.legend(loc='upper right')


country_list = [19, 41, 83, 72, 257]
year = [43, 48, 53, 58, 63]


country_names = ["Australia", "Canada", "France", "Ecuador", "United States"]


'''reading values by calling functions'''


forest_1, forest_2 = read_data("API_AG.LND.FRST.K2_DS2_en_csv_v2_5346556.csv",
                               country_list, year)
poptot_1, poptot_2 = read_data("API_SP.POP.TOTL_DS2_en_csv_v2_5350834.csv",
                               country_list, year)
agrlnd_1, agrlnd_2 = read_data("API_AG.LND.AGRI.ZS_DS2_en_csv_v2_5349988.csv",
                               country_list, year)
aralnd_1, aralnd_2 = read_data("API_AG.LND.ARBL.ZS_DS2_en_csv_v2_5346580.csv",
                               country_list, year)

forest_2.columns = country_names
poptot_2.columns = country_names
agrlnd_2.columns = country_names
aralnd_2.columns = country_names

#forest_2.to_csv("forest.csv")

stat_function(forest_2)
stat_function(aralnd_2)

print("Skew: ", sts.skew(forest_2["Ecuador"]))
print("Kurtosis: ", sts.kurtosis(forest_2["Ecuador"]))


plot(forest_2, 'bar', 'Forest Area (sq.km)', 'Years', 'No(in millions)')
plot(aralnd_2, 'bar', 'Arable Land (% of land area)', 'Years',
     'No(in millions)')
plot(poptot_2, 'line', 'Population, Total', 'Years', 'No(in millions)')
plot(agrlnd_2, 'line', 'Agricultural Land (% of land area)', 'Years',
     'No(in millions)')
