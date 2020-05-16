def search_word(s1, s2):
    """
	Finds the longest substring of s1 that is also in s2
	
	Parameters: 
		s1, s2 - strings
		
	Returns: 
		the longest substring of s1 also contained in s2
   
    Examples:
    >>> search_word("searching for a substring", "subway")
    'sub'
    >>> search_word("dog owner", "catdog oh catdog")
    'dog o'
    >>> search_word("fish", "filet")
    'fi'
    >>> search_word("fish", "ballet")
    ''
    >>> search_word("land a plane", "lane")
    'lane'
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS


def to_chars(s):
    """
    Strips the string s from any non-letter characters (English alphabet), 
    and makes it lower-case.
    
    Parameters:
        string s
    Returns: 
        string with only lower-case chars of the English alphabet
        
    Example use
    >>> to_chars('HeLlo!')
    'hello'
    >>> to_chars("Never (1) odd or (2) even...")
    'neveroddoreven'
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS
    alphabet = 'abcdefghjiklmnopqrstuvwxyz' # English alphabet


def is_palindrome(s):
    """ 
    Palindrome checker
    
    Parameters:
        s is string that has gone through to_chars()
    
    Returns True if s is palindrome, False otherwise
    
    Examples:
    >>> is_palindrome('neveroddoreven')
    True
    >>> is_palindrome(to_chars('A man, a plan, a canal: Panama.'))
    True
    >>> is_palindrome('hello')
    False
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS

