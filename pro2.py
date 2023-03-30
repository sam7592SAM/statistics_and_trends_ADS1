import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def read_data(data, country, years):
    df = pd.read_csv(data, skiprows=4)
    df.drop(columns=['Country Code'], axis=1, inplace=True)
    df1 = df.iloc[country, years]
    df2 = df1.T
    return df1, df2

'''
#def stat_func():
    
'''
def plot(data, kind, title,x,y):
    data.plot(kind=kind)
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.legend(loc='upper right')
    
    
country_list = [19, 35, 43, 46, 49, 76, 87, 115, 129, 257]
year = [33, 43, 53, 63]
'''
country_list = ["Spain", "United States", "United Kingdom", "China", "India", 
                "Brazil", "Congo, Dem. Rep.", "Australia", "Switzerland",
                "Cambodia"]
year = ['1990', '1995', '2000', '2005', '2010', '2015', '2020']
'''


#reading values by calling functions
forest_1, forest_2 = read_data("API_AG.LND.FRST.K2_DS2_en_csv_v2_5346556.csv", 
                               country_list, year)
poptot_1, poptot_2 = read_data("API_SP.POP.TOTL_DS2_en_csv_v2_5350834.csv", 
                               country_list, year)
agrlnd_1, agrlnd_2 = read_data("API_AG.LND.AGRI.ZS_DS2_en_csv_v2_5349988.csv", 
                               country_list, year)
aralnd_1, aralnd_2 = read_data("API_AG.LND.ARBL.ZS_DS2_en_csv_v2_5346580.csv", 
                               country_list, year)

plot(forest_2, 'bar', 'Forest Area (sq.km)', 'Years', 'No(in millions)')
plot(poptot_2, 'bar', 'Population, Total', 'Years', 'No(in millions)')
plot(agrlnd_2, 'line', 'Population, Total', 'Years', 'No(in millions)')
plot(aralnd_2, 'line', 'Population, Total', 'Years', 'No(in millions)')
