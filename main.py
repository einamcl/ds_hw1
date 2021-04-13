from sys import argv

import pandas as pd
#import sys
import data
#argv[0] = /:C/Users/einam/PycharmProjects/test/main.py
path = "C:\Users\einam\PycharmProjects\test\london.csv"
features = "hum, t1, cnt, season, is_holiday"
"""
    statistic_functions = [statistics.sum, statistics.mean, statistics.med]
    print('Question 1:')
    data = load_data(path, features)
    print_details('summer', data_summer, argv[2], statistic_functions)
if __name__ == "__main__":
"""
data1=data.load_data(path,features)
print(data1)