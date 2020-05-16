#####
# Load up the csv file first

import csv

def read_trump_tweets(file_name):
    """
    Reads Trump tweets csv file into a list
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


# tweets = read_trump_tweets('trump_tweets.csv')


#####
# Question 4

def str_to_int(L, ind):
    """
    Convert string-form integer entries to integers. 
    
    Parameters:
        L is a list containing list entries. The first entry contains headers so it is skipped.
        ind is the index at each of the list entries to be converted
        
    Returns list with integer entries of the ind entry of each entry of L
    
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
    new_list = []
    for item in L[1:]:
        new_list.append(int(item[ind]))
    return new_list


def value_at_least(L, threshold):
    """
    Collects indices of L where value is at least threshold
    
    Parameters:
        L: a list 
        threshold: value threshold
    
    Returns a list of indices with values at least the threshold
    
    Example use:
    >>> tw = [1, 2, 3]
    >>> value_at_least(tw, 2)
    [1, 2]
    >>> value_at_least([4, 1, 9], 5)
    [2]
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    new_list = []
    for ind in range(len(L)):
        if L[ind] >= threshold:
            new_list.append(ind)  
    return new_list


#####
# Question 5

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


def tweet_length(tweet):
    return len(tweet[0])

    
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
    text = tweet[0]
    count = 0
    for char in text:
        if char.isupper():
            count += 1
    return count


def _run_tweets():
    tweets = read_trump_tweets('trump_tweets.csv')
    retweets = str_to_int(tweets, 2)
    retweet_indices = value_at_least(retweets, 200000)
    print(retweet_indices)
    for tw in retweet_indices:
        print(tweets[tw + 1][0])
    capitals = apply_function(tweets, count_capital_letters, 1)
    capital_indices = value_at_least(capitals, 100)
    print(capital_indices)
    for tw in capital_indices:
        print(tweets[tw + 1][0])
