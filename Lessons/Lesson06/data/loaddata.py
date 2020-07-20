# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 18:15:54 2019

@author: jrizos
"""

import csv
import datetime
import matplotlib.pyplot as plt

def LoadData(symbol_):
    with open('./data/{0}.csv'.format(symbol_), mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        return [(datetime.datetime.strptime(x['Date'], '%Y-%m-%d').date(), float(x['Open']), float(x['High']), float(x['Low']), float(x['Close']), int(x['Volume'])) for x in csv_reader]


def ShowData(symbol_):
    data = LoadData(symbol_)

    data_dates = []
    data_values = []

    for d,o,h,l,c,v in data:
        data_dates.append(d)
        data_values.append(c)

    plt.title('{0} Close Price'.format(symbol_))
    plt.style.use('seaborn-whitegrid')

    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.plot(data_dates, data_values)
    plt.show()
    
tupindex = {'Date':0, 'Open':1, 'High':2, 'Low':3, 'Close':4, 'Volume':5}

def GetValueData(symbol_, type_):
    sdata = []
    stock_data = LoadData(symbol_)
    for x in stock_data:
        sdata.append(x[tupindex[type_]])
        
    return sdata

