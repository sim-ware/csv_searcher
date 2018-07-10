import pandas as pd
from fuzzywuzzy import process


# Use Pandas to read the csv into a DataFrame
#############################################
df = pd.read_csv('search_dataset.csv')


# Having put some examples into a .txt file, read them into a List
##################################################################
f = open('example.txt', 'r')
x = f.readlines()
f.close()

x = [line.strip('\n') for line in x]


# Return the FuzzFactor for the First Query
###########################################
choices = df['name'].tolist()
searchterm = x[3]
result = process.extract(searchterm, choices, limit=10)
print(searchterm)
print(result)
