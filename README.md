# csv_searcher
# Disclaimers
-edited the dataset to have Columns of id, name, brand

# Pandas // DataFraming
-seemed like the most nimble way to handle a csv in memory
-experience using it before and it has a large vocabulary of in-built functions
  that make handling csv files much simpler for me.

# Fuzzy Matching
-wanted to do subsetting of strings
-didn't allow for fuzz / slight differences in strings that aren't easily
  detectable through code.
-experience using FuzzyMatching packages in past, which allow us to parameterise
  their strictness, seemed ready-made for this challenge.

# MVP
-read the csv to a dataframeYUP
-create a separate .txt file with the example queriesYUP
-read the .txt file and store the query strings as an appropriate form. List of
  Lists?YUP

-see if we can handle for one search term
-take the firstYUP
-fuzz match against the file for the ones with the highest scoreYUP
-and return themYUP

-can we get them to fit the format?YUP
-can we repeat for the whole file, and return the whole output?YUP

  n
score,id,name,brand
score,id,name,brand
...

2
0.9242,564,asos red bag,asos
0.7654,1245,reddish small bag,asos
3
0.6721,6721,prada red shirt,prada
0.6311,13,prada reddish nice shirt,prada
0.5794,56216,bright yello shirt,prada
