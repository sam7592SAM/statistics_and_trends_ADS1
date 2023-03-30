import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def read_data(data, country, years):
    df = pd.read_csv(data, skiprows=4)
    df.drop(columns=['Country Code'], axis=1, inplace=True)
    df1 = df.loc[country, years]
    df2 = df1.T
    return df1, df2

'''
#def stat_func():
    
'''
def plot(data, kind, title,x,y):
    data.plot(kind=kind)
    data.title(title)
    data.xlabel(x)
    data.ylabel(y)


country_list = ["Spain", "United States", "United Kingdom", "China", "India", 
                "Brazil", "Congo, Dem. Rep.", "Australia", "Switzerland",
                "Cambodia"]
year = ['1990', '1995', '2000', '2005', '2010', '2015', '2020']

#reading values by calling functions
forest_1, forest_2 = read_data("API_AG.LND.FRST.K2_DS2_en_csv_v2_5346556.csv", 
                               country_list, year)
poptot_1, poptot_2 = read_data("API_SP.POP.TOTL_DS2_en_csv_v2_5350834.csv", 
                               country_list, year)
agrlnd_1, agrlnd_2 = read_data("API_AG.LND.AGRI.ZS_DS2_en_csv_v2_5349988.csv", 
                               country_list, year)
aralnd_1, aralnd_2 = read_data("API_AG.LND.ARBL.ZS_DS2_en_csv_v2_5346580.csv", 
                               country_list, year)

plot(forest_2, 'line', 'Forest Area (sq.km)', 'Countries', 'No(in millions)')