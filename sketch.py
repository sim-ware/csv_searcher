import pandas as pd


# Use Pandas to read the csv into a DataFrame
#############################################
df = pd.read_csv('search_dataset.csv')


# Having put some examples into a .txt file, read them into a List
##################################################################
f = open('example.txt', 'r')
x = f.readlines()
f.close()

x = [line.strip('\n') for line in x]
