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


# Obtaining Result #TODO: return list of lists for all examples
##################
result_scorelist = []

for example in x:
    print(example)
    result = process.extract(example, names, scorer=fuzz.token_sort_ratio, limit=10)
    print(result)
    result_scorelist.append(result)
# print(result_scorelist)


# Formatting Result
###################
result_list = []
for idx,result in enumerate(result_scorelist):
    print(idx)
    print(result)
    nup = []
    for i,res in enumerate(result):
        print(i)
        print(res)
        yup = df.loc[df['name'] == res[0]]
        yup = yup.to_dict('records')[0]
        yup['score'] = res[1]
        print(yup)
        nup.append(yup)
    # result_list.append(yup)
    result_list.append(nup)
# print(result_list)
print(result_list[-1])

# yup = df.loc[df['name'] == result[0][0]]
# yup = yup.to_dict('records')[0]
# yup['score'] = result[0][1]
# print(yup)





#   n
# score,id,name,brand
# score,id,name,brand
# ...
#
# 2
# 0.9242,564,asos red bag,asos
# 0.7654,1245,reddish small bag,asos
