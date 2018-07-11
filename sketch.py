import pandas as pd
from fuzzywuzzy import process


# Use Pandas to read the csv into a DataFrame
#############################################
df = pd.read_csv('search_dataset.csv')
names = df['name'].tolist()
print(df.head())
print(names[0:9])

# Having put some examples into a .txt file, read them into a List
##################################################################
f = open('example.txt', 'r')
x = f.readlines()
f.close()

x = [line.strip('\n') for line in x]
print(x)

##############
example = x[0]
print(example)




#TODO: Create a Dict, and List to store each one in.
#TODO: Dict should have score//id//name//brand

# mega_l=[]
# for idx, searchterm in enumerate(x):
#     l = []
#     result = process.extract(searchterm, choices, limit=10)
#     print(result)
#     print(idx)
#     print(searchterm)
#     for idx,item in enumerate(result):
#         d={}
#         print(idx)
#         print(item)
#         print(item[0])
#         yup = df.loc[df['name'] == item[0]].to_dict()
#         print(yup)
#         l.append(d)
#     mega_l.append(l)
#
# print(mega_l)


#   n
# score,id,name,brand
# score,id,name,brand
# ...
#
# 2
# 0.9242,564,asos red bag,asos
# 0.7654,1245,reddish small bag,asos
