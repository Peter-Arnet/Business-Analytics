# -*- coding: utf-8 -*-
"""
Homework 1
"""

#####
# Wind chill calculator
#####


def wind_chill(temp, wind_speed, a=13.12, b=0.6215, c=-11.37, d=0.16, e=0.3965):
    """
    Converts temperature and wind speed into wind-chill index.

    Formula: wci = a + b*T + c*W^d + e*T*W^d, where T is temperature and W is wind speed

    Parameters
        temp: temperature in Celsius
        wind_speed: wind speed in km/h
        a: constant with default value
        b: constant with default value
        c: constant with default value
        d: constant with default value
        e: constant with default value

    Returns:
        Wind chill index.
        If wind speed is lower than 5, return the temperature.
        Otherwise, return the index according to the formula, rounded to integer value

    Example use:
    >>> wind_chill(10, 0)
    10
    >>> wind_chill(-10, 20)
    -18
    >>> wind_chill(-20, 30)
    -33
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    pass  # This is a placeholder for your code - replace it with your implementation


#####
# A brainteaser
#####


def the_35_teaser(n):
    """
    A typical coding interview brainteaser.

    Parameters:
        n: integer

    Returns:
        For n divisible by 3, return '3'
        For n divisible by 5, return '5'
        For n divisible by both 3 and 5, return '35'
        Otherwise, return None.

    Example use:
    >>> the_35_teaser(9)
    '3'
    >>> the_35_teaser(95)
    '5'
    >>> the_35_teaser(300)
    '35'
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    pass # This is a placeholder for your code - replace it with your implementation


#####
# Date string conversion: slash-date format to dash-date format
#####


def convert_day(day_string):
    """
    Converts day string from slash-date to dash-date format

    Assumes day between '1' or '01' and '31'

    Parameters:
    day_string: string containing day number in slash-date format

    Returns:
    string containing day number in dash-date format

    Example use:
    >>> convert_day('8')
    '08'
    >>> convert_day('15')
    '15'
    """
    # Your code here. Don't change anything above.
    pass # This is a placeholder for your code - replace it with your implementation


def convert_month(month_string):
    """
    Converts day string from slash-date to dash-date format

    Assumes month between '1' or '01' and '12'

    Parameters:
    month_string: string containing day number in slash-date format

    Returns:
    string containing month number in dash-date format

    Example use:
    >>> convert_month('3')
    '03'
    >>> convert_month('11')
    '11'
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    pass  # This is a placeholder for your code - replace it with your implementation


def convert_year(year_string):
    """
    Converts day string from slash-date to dash-date format

    Assumes year either between '00' and '99' or between '1000' and '9999'
    
    If year between '00' and '99', assumes the year is in 1919-2018
    
    Parameters:
    year_string: string containing day number in slash-date format

    Returns:
    string containing year number in dash-date format

    Example use:
    >>> convert_year('03')
    '2003'
    >>> convert_year('20')
    '1920'
    >>> convert_year('1945')
    '1945'
    >>> convert_year('1389')
    '1389'
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    pass  # This is a placeholder for your code - replace it with your implementation


def date_conversion(date_string):
    """
    Converts date string from slash format to dash format

    Assume European date ordering (day-month-year).
    Assume that two-digit years are in the past century (1919-2018 is "past century", 2019- is not...).
    Assume that the year of the date is in either range 00 - 99 or 1000 - 9999

    Parameters:
        date_string: string date in "slash" format, eg, 19/8/16, 1/12/1898, 1/1/20 (assume valid dates)

    Returns:
        string date in "dash" format, eg, 19-08-2016, 01-12-1898, 01-01-1920

    Example use:
    >>> print(date_conversion('19/8/16'))
    19-08-2016
    >>> print(date_conversion('01/12/1898'))
    01-12-1898
    >>> print(date_conversion('18/4/20'))
    18-04-1920
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW

    date_as_list = date_string.split('/')  # Use this to split slash format string into a list
    
    # Your code should call the three functions above to solve the problem. 
    # You will need to implement them first.
    pass  # This is a placeholder for your code - replace it with your implementation


##### 
# Robust version of date conversion
#####


def date_conversion_robust(date_string):
    """
    Converts date string from slash format to dash format.
    Checks if input date is valid; if not, prints an error and returns None.

    Valid dates are as follows:
    - European date ordering (day-month-year).
    - Two-digit years are in the past century (1919-2018 is "past century", 2019- is not...).
    - The year of the date is in either range 00 - 99 or 1000 - 9999

    Parameters:
        date_string: string date in "slash" format, eg, 19/8/16, 1/12/1898, 1/1/20 (DO NOT assume every input is a valid date)

    Returns:
        if input was valid: string date in "dash" format, eg, 19-08-2016, 01-12-1898, 01-01-1920
        if input was not valid: print out "Not a valid date", return None

    Example use:
    >>> print(date_conversion_robust('19/8/16'))
    19-08-2016
    >>> print(date_conversion_robust('1/12/1898'))
    01-12-1898
    >>> print(date_conversion_robust('16/3/20'))
    16-03-1920
    >>> print(date_conversion_robust('29/2/2017'))
    Not a valid date.
    None
    >>> print(date_conversion_robust('131/2/1928'))
    Not a valid date.
    None
    >>> print(date_conversion_robust(2))
    Not a valid date.
    None
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW

    date_as_list = date_string.split('/')  # Use this to split slash format string into a list

    # You can call the above functions if you'd like.
    pass  # This is a placeholder for your code - replace it with your implementation





