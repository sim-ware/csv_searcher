import pandas as pd
from fuzzywuzzy import process


# Use Pandas to read the csv into a DataFrame
#############################################
df = pd.read_csv('search_dataset.csv')
# print(list(df.columns.values))
# print(df.cols())
print(df.head())


# Having put some examples into a .txt file, read them into a List
##################################################################
f = open('example.txt', 'r')
x = f.readlines()
f.close()

x = [line.strip('\n') for line in x]


# Return the FuzzFactor for the First Query
###########################################
#  choices = ["Atlanta Falcons", "New York Jets", "New York Giants", "Dallas Cowboys"]
#  process.extract("new york jets", choices, limit=2)
#  >>> [('New York Jets', 100), ('New York Giants', 78)]
# process.extractOne("cowboys", choices)
#  >>> ("Dallas Cowboys", 90)

# choices = df['one'].tolist()
# process.extract(x[0], choices, limit=10)
