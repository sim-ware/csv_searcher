import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


# Use Pandas to read the csv into a DataFrame
#############################################
df = pd.read_csv('search_dataset.csv')
names = df['name'].tolist()


# Having put some examples into a .txt file, read them into a List
##################################################################
f = open('example.txt', 'r')
x = f.readlines()
f.close()

x = [line.strip('\n') for line in x]


# Obtaining Result
##################
result_scorelist = []

for example in x:
    result = process.extract(example, names, scorer=fuzz.token_sort_ratio, limit=10)
    result_scorelist.append(result)


# Formatting Result
###################
result_list = []
for idx,result in enumerate(result_scorelist):
    dfquery_list = []
    for i,res in enumerate(result):
        dfquery = df.loc[df['name'] == res[0]]
        dfquery = dfquery.to_dict('records')[0]
        dfquery['score'] = res[1]
        dfquery_list.append(dfquery)
    result_list.append(dfquery_list)
print(result_list)
print(len(result_list))


#   n
# score,id,name,brand
# score,id,name,brand
# ...
#
# 2
# 0.9242,564,asos red bag,asos
# 0.7654,1245,reddish small bag,asos
