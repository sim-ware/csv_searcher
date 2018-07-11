# CSV Searcher
# To Run
Clone the Repo, install the requirements, and run:
```
$ python csvsearcher.py
```

# Pandas // DataFraming
I decided to use the Python package Pandas to read in the CSV. In my experience it's quite intuitive, and is good for handling large spreadsheet-like datasets. It also makes it straightforward to read in CSVs, and query them through DataFrames, which I would need to do for this task.

# Fuzzy Matching
I used the Python package Fuzzy-Wuzzy to compare the example strings against the descriptions in the CSV. I initially thought of checking to see if the characters in the strings overlapped, but wanted to have a slightly forgiving element to the search so that it wouldn't discount similar words, or words that don't match entirely. I had previously had to do some address-validation in my time, and I used Fuzzy Matching to check the address for potential matches. It calculates the Levenshtein distance between two words: the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other, whilst also returning a metric for its accuracy. Given how the package satisfied so many of my requirements at once it seemed wise to integrate it into my solution.
