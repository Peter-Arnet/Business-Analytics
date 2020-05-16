#####
# Load the csv file first

import csv

def read_trump_tweets(file_name):
    """
    Reads Trump tweets csv file into a list
    
    Parameter:
        file_name: csv file containing the tweets
    
    Returns:
        list containing tweets
    """
    try:
        with open(file_name, encoding="utf8") as csvfile:
            data = csv.reader(csvfile, delimiter=',')
            tweet_list = list(data)
        return tweet_list
    except FileNotFoundError:
        print("""
              File not found. Check that the Spyder working directory is correct.
              Change the working directory by clicking on folder icon in the top right part of the window.
              """)


#####
# String to int

def str_to_int(L, ind):
    """
    Convert string-form integer entries in L to integers. 
    
    Parameters:
        L is a list containing list entries. The first entry contains headers so it is skipped.
        ind is the index at each of the list entries to be converted
        
    Returns a new list with integer entries of the ind entry of each entry of L
    
    Example use:
    >>> L = [['Name', 'Favorites'], ['Jay', '1'], ['Jack', '2']]
    >>> y = str_to_int(L, 1)
    >>> print(y)
    [1, 2]
    >>> L = [['Number1', 'Number2'], ['2', '3'], ['1', '5']]
    >>> y = str_to_int(L, 0)
    >>> print(y)
    [2, 1]
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW


def value_at_least(L, threshold):
    """
    Collects indices of L where value is at least threshold
    
    Parameters:
        L: a list 
        threshold: value threshold
    
    Returns a new list of indices with values at least the threshold
    
    Example use:
    >>> tw = [1, 2, 3]
    >>> value_at_least(tw, 2)
    [1, 2]
    >>> value_at_least([4, 1, 9], 5)
    [2]
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW


#####
# Applying functions


def apply_function(a_list, function, start_from):
    """
    Applies parameter function to items of a_list. 
    
	Parameters:
		a_list: a list of lists
		function: a function to be applied to each item of a_list,
		start_from: index of a_list to start from
	
	Returns: 
		a new list with the results.
    """
    new_list = []
    for item in a_list[start_from:]:
        new_list.append(function(item))
    return new_list

    
def count_capital_letters(tweet):
    """
    Counts the number of capital numbers of the tweet
    
    Parameters:
        tweet: list containing tweet text in first item
    
    Returns: 
        integer count of the number of capital letters in the tweet text
    
    Example use:
    >>> count_capital_letters(['HEY YOU', 'date1', 100, 10, 'id'])
    6
    >>> count_capital_letters(['hey YOU', 'date1', 100, 10, 'id'])
    3
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
