"""HW11 Question 1: Comparable Objects

Your task is to write a class for web search results which allows sorting based on relevance and 
date.

Please write a class called SearchResult.

The constructor for the SearchResult class should take the following parameters, in this order:
- the title of the search result
- the URL of the search result
- the date of the result as a datetime object (https://docs.python.org/3/library/datetime.html)
- the search term typed in by the user to perform the search

The class should implement the __eq__ and __lt__ methods to allow comparison based on relevance.
Relevance is measured as the number of times the search term appears in the title of the result.
More relevant results are considered "greater" than less relevant results.
If two SearchResults have the same relevance, they should be compared based on their date, with 
more recent results considered "greater."
If two SearchResults have the same relevance and date, they are considered equal.

Make sure to write tests in the tests directory.
"""

from datetime import datetime
