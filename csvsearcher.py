import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


# Use Pandas to read CSV into DataFrame, and get List of all 'name' values
##########################################################################
df = pd.read_csv('search_dataset.csv')
names = df['name'].tolist()


# Read content of Example .txt file into a List
###############################################
f = open('example.txt', 'r')
x = f.readlines()
f.close()
x = [line.strip('\n') for line in x]


# Obtaining Results; Using FuzzyWuzzy to return a List of each example from .txt
# file's most similar results, and scores.
##########################################
result_scorelist = []

for example in x:
    result = process.extract(example, names, scorer=fuzz.token_sort_ratio, limit=10)
    result_scorelist.append(result)


# Formatting Result; Loop through the List of Results and query them against the
# Original DataFrame to return the rest of the row's values - and turn them into
# a Dictionary, to which we add the score.
###################
result_list = []
for idx,result in enumerate(result_scorelist):
    dfquery_list = []
    for i,res in enumerate(result):
        dfquery_dict = df.loc[df['name'] == res[0]].to_dict('records')[0]
        dfquery_dict['score'] = res[1]
        dfquery_list.append(dfquery_dict)
    result_list.append(dfquery_list)


# Render It; The results are returned as a List of List of Dictionaries, which is
# jarring to read. Here we prettify it slightly.
################################################
for idx,result in enumerate(result_list):
    print('----------------------------')
    print(str(idx) + ')SEARCHTERM:' + str(x[idx]))
    print('----------------------------')
    for idx,item in enumerate(result):
        print('|Score:' + str(item['score']) + '|ID:' + str(item['id']) + '|Name:' + str(item['name']) + '|Brand:' + str(item['brand']))
