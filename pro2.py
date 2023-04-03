

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sts

# Defining Functions

# 1. Read Data


def read_data(data, country, years):
    ''' Function to read CSV files. In this assignment four CSV files or
    datasets are chosen. The values of the following files are called using
    this function. Arguments such as data, country and years are used where
    data is used to get the values of the CSV file, country and years are used
    to get the list of countries and years to be read from whole data. This
    function uses filtering technique to take the required values such as
    dropping and retrieving values using iloc[]. Once filtering is done, the
    dataframes are transposed'''
    df = pd.read_csv(data, skiprows=4)
    df.drop(columns=['Country Code'], axis=1, inplace=True)
    df1 = df.iloc[country, years]
    df2 = df1.T
    return df1, df2

# 2. Function to give an overview of the dataframe


def des_fun(data):
    '''This function is used to explore the data using statistical
    tools. Argument data is used to retrieve the data. .describe() method
    is used to explore the dataframe getting the overview and understanding the
    value distribution. .corr() method is used to check the pairwise
    correlation of columns'''
    print(data.describe())
    print(data.corr())

# 3. Function using statistical calculations.


def stat_fun(data):
    '''This function is used to calculate a particular value using statistical
    tools. Statistical tools such as Skewness and Kurtosis are being used here.
    Argument data is passed here.'''
    print("Skewness: ", sts.skew(data))
    print("Kurtosis: ", sts.kurtosis(data))

# 4. Function to plot


def plot(data, kind, title, x, y):
    ''' Function to create plots. This function is used to give an insight of
    the dataframes. Arguments such as data, kind, title, x, y are used. data
    arguement is used to get the dataframe, kind argument is to specify which
    graph to be plotted. title, x, and y are used to label the coordinates on
    the graph'''
    data.plot(kind=kind)
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.legend(loc='upper right', bbox_to_anchor = (1.4, 1.0))
    plt.show()


# Specifying the values to be taken from the datasets.

country_list = [19, 41, 83, 72, 257]
year = [43, 48, 53, 58, 63]


# Specifying country names corresponding with country_list[] list.

country_names = ["Australia", "Canada", "France", "Ecuador", "United States"]


# Datasets called to the read_data(), specifying the country_list and year.

forest_1, forest_2 = read_data("API_AG.LND.FRST.K2_DS2_en_csv_v2_5346556.csv",
                               country_list, year)
poptot_1, poptot_2 = read_data("API_SP.POP.TOTL_DS2_en_csv_v2_5350834.csv",
                               country_list, year)
agrlnd_1, agrlnd_2 = read_data("API_AG.LND.AGRI.ZS_DS2_en_csv_v2_5349988.csv",
                               country_list, year)
aralnd_1, aralnd_2 = read_data("API_AG.LND.ARBL.ZS_DS2_en_csv_v2_5346580.csv",
                               country_list, year)


# Specifying country names to the columns of the dataframes.

forest_2.columns = country_names
poptot_2.columns = country_names
agrlnd_2.columns = country_names
aralnd_2.columns = country_names

# The variable of dataframes called to des_fun().

des_fun(forest_2)
des_fun(aralnd_2)
des_fun(poptot_2)
des_fun(agrlnd_2)

'''
forest_2.to_csv("forest.csv")
aralnd_2.to_csv("araland.csv")
poptot_2.to_csv("poptot.csv")
agrlnd_2.to_csv("agriland.csv")
'''

# Particular value of a dataframe being called to stat_fun().

stat_fun(forest_2["Ecuador"])

# Plotting graphs for various dataframes using plot() and specifying arguements

plot(forest_2, 'bar', 'Forest Area (sq.km)', 'Years', 'No(in millions)')
plot(aralnd_2, 'bar', 'Arable Land (% of land area)', 'Years',
     'Percentage(%)')
plot(poptot_2, 'line', 'Population, Total', 'Years', 'No(in millions)')
plot(agrlnd_2, 'line', 'Agricultural Land (% of land area)', 'Years',
     'Percentage(%)')
