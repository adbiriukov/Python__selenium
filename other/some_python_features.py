# 1
# The lambda function definition is:
add_bangs = (lambda value: value + '!!!')
# and the function call is:
a = add_bangs('hello')
print(a)


# 1_1
# Define echo_word as a lambda function: echo_word
echo_word = (lambda word1, echo: word1*echo)

# Call echo_word: result
result = echo_word('hey ', 5)

# Print result
print(result)


# 1_2
# Create a list of strings: spells
spells = ['protego', 'accio', 'expecto patronum', 'legilimens']

# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda item: item + '!!!', spells)

# Convert shout_spells to a list: shout_spells_list
shout_spells_list = list(shout_spells)

# Print the result
print(shout_spells_list)


# 1_3
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda member: len(member) > 6, fellowship)

# Convert result to a list: result_list
result_list = list(result)

# Print result_list
print(result_list)


# 1_4
# Import reduce from functools
from functools import reduce

# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda item1, item2: item1 + item2, stark)

# Print the result
print(result)


# 1_5
# Select retweets from the Twitter DataFrame: result
result = filter(lambda x: x[0:2] == 'RT', tweets_df['text'])

# Create list from filter object result: res_list
res_list = list(result)

# Print all retweets in res_list
for tweet in res_list:
    print(tweet)
######################################################################
######################################################################
######################################################################
# 2
# Define report_status
def report_status(**kwargs):
    """Print out the status of a movie character."""

    print("\nBEGIN: REPORT\n")

    # Iterate over the key-value pairs of kwargs
    for key, value in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(key + ": " + value)

    print("\nEND REPORT")

# First call to report_status()
report_status(name="luke", affiliation="jedi", status="missing")

# Second call to report_status()
report_status(name="anakin", affiliation="sith lord", status="deceased")


# 3
def gibberish(*args):
    """Concatenate strings in *args together."""

    # Initialize an empty string: hodgepodge
    hodgepodge = ''

    # Concatenate the strings in args
    for word in args:
        hodgepodge += word

    # Return hodgepodge
    return hodgepodge

# Call gibberish() with one string: one_word
one_word = gibberish('luke')

# Call gibberish() with five strings: many_words
many_words = gibberish("luke", "leia", "han", "obi", "darth")

# Print one_word and many_words
print(one_word)
print(many_words)


# 4
# Define shout_echo
def shout_echo(word1, echo = 1):
    """Concatenate echo copies of word1 and three
     exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo() with "Hey": no_echo
no_echo = shout_echo("Hey")

# Call shout_echo() with "Hey" and echo=5: with_echo
with_echo = shout_echo("Hey", 5)

# Print no_echo and with_echo
print(no_echo)
print(with_echo)


# 5
# Define echo_shout()
def echo_shout(word):
    """Change the value of a nonlocal variable"""

    # Concatenate word with itself: echo_word
    echo_word = word * 2

    # Print echo_word
    print(echo_word)

    # Define inner function shout()
    def shout():
        """Alter a variable in the enclosing scope"""

        # Use echo_word in nonlocal scope
        nonlocal echo_word

        # Change echo_word to echo_word concatenated with '!!!'
        echo_word = echo_word + '!!!'

    # Call function shout()
    shout()

    # Print echo_word
    print(echo_word)


# Call function echo_shout() with argument 'hello'
echo_shout('hello')


# 6
# Define echo
def echo(n):
    """Return the inner_echo function."""

    # Define inner_echo
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word

    # Return inner_echo
    return inner_echo

# Call echo: twice
twice = echo(2)

# Call echo: thrice
thrice = echo(3)

# Call twice() and thrice() then print
print(twice('hello'), thrice('hello'))


# 7
# Create a string: team
team = "teen titans"

# Define change_team()
def change_team():
    """Change the value of the global variable team."""

    # Use team in global scope
    global team

    # Change the value of team in global: team
    team = "justice league"
# Print team
print(team)

# Call change_team()
change_team()

# Print team
print(team)


# 8
# Define shout_echo
def shout_echo(word1, echo=3):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Initialize empty strings: echo_word, shout_words
    echo_word = ''
    shout_words = ''

    # Add exception handling with try-except
    try:
        # Concatenate echo copies of word1 using *: echo_word
        echo_word = word1 * echo

        # Concatenate '!!!' to echo_word: shout_words
        shout_words = echo_word + '!!!'
    except:
        # Print error message
        print("word1 must be a string and echo must be an integer.")

    # Return shout_words
    return shout_words

# Call shout_echo
print1 = shout_echo("particle ", echo=3)
print(print1)
# 9
# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Raise an error with raise
    if echo < 0:
        raise ValueError('echo must be greater than or equal to 0')

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo
a = shout_echo("particle ", echo=5)
print(a)


# 10
# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

# Print each list item in flash using a for loop
for person in flash:
    print(person)
print("\n=====================\n")
# Create an iterator for flash: superhero
superhero = iter(flash)

# Print each item from the iterator
print(next(superhero))
print(next(superhero))
print(next(superhero))
print(next(superhero))


# 11
# Create an iterator for range(3): small_value
small_value = iter(range(3))

# Print the values in small_value
print(next(small_value))
print(next(small_value))
print(next(small_value))
print("\n++++++++++++\n")
# Loop over range(3) and print the values
for num in range(3):
    print(num)
print("\n++++++++++++\n")
# Create an iterator for range(10 ** 100): googol
googol = iter(range(10 ** 100))

# Print the first 5 values from googol
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))


# 12
# Create a range object: values
values = range(10, 21)

# Print the range object
print(values)

# Create a list of integers: values_list
values_list = list(values)

# Print values_list
print(values_list)

# Get the sum of values: values_sum
values_sum = sum(values)

# Print values_sum
print(values_sum)


# 13
# Create a list of strings: mutants
mutants = ['charles xavier',
            'bobby drake',
            'kurt wagner',
            'max eisenhardt',
            'kitty pryde']

# Create a list of tuples: mutant_list
mutant_list = list(enumerate(mutants))

# Print the list of tuples
print(mutant_list)

# Unpack and print the tuple pairs
for index1, value1 in enumerate(mutants):
    print(index1, value1)

# Change the start index
for index2, value2 in enumerate(mutants, start=1):
    print(index2, value2)


# 14
mutants = ['charles xavier',
            'bobby drake',
            'kurt wagner',
            'max eisenhardt',
            'kitty pryde']
aliases = ['11111',
            '11111',
            '111111111r',
            '1111111111',
            '11111111111111111']
powers = ['22222222',
            '22222222222',
            '22222222222222',
            '22222222222',
            '222222222222222']

# Create a list of tuples: mutant_data
mutant_data = list(zip(mutants, aliases, powers))

# Print the list of tuples
print(mutant_data)

# Create a zip object using the three lists: mutant_zip
mutant_zip = zip(mutants, aliases, powers)

# Print the zip object
print(mutant_zip)

# Unpack the zip object and print the tuple values
for value1, value2, value3 in mutant_zip:
    print(value1, value2, value3)


# 15
# Create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# Print the tuples in z1 by unpacking with *
print(*z1)

# Re-create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
result1, result2 = zip(*z1)

# Check if unpacked tuples are equivalent to original tuples
print(result1 == mutants)
print(result2 == powers)


# 16
# Initialize an empty dictionary: counts_dict
counts_dict = {}

# Iterate over the file chunk by chunk

# pd is panda library
for chunk in pd.read_csv('tweets.csv', chunksize=10):

    # Iterate over the column in DataFrame
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1

# Print the populated dictionary
print(counts_dict)
# 17
# Define count_entries()
def count_entries(csv_file, c_size, colname):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file, chunksize=c_size):

        # Iterate over the column in DataFrame
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1

    # Return counts_dict
    return counts_dict


# Call count_entries(): result_counts
result_counts = count_entries('tweets.csv', 10, 'lang')

# Print result_counts
print(result_counts)

# 18
# Import package
from urllib.request import urlretrieve

# Import pandas
import pandas as pd

# Assign url of file: url
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Save file locally
urlretrieve(url, 'winequality-red.csv')

# Read file into a DataFrame and print its head
df = pd.read_csv('winequality-red.csv', sep=';')
print(df.head())


# 19
# Import packages
import matplotlib.pyplot as plt
import pandas as pd

# Assign url of file: url
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Read file into a DataFrame: df
df = pd.read_csv(url, ';')

# Print the head of the DataFrame
print(df.head())

# Plot first column of df
pd.DataFrame.hist(df.ix[:, 0:1])
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()


# 20
# Import package
import pandas as pd

# Assign url of file: url
url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'

# Read in all sheets of Excel file: xls
xls = pd.read_excel(url, None)

# Print the sheetnames to the shell
print(xls.keys())

# Print the head of the first sheet (using its name, NOT its index)
print(xls['1700'].head())


# 21
# Import packages
from urllib.request import urlopen, Request

# Specify the url
url = "http://www.datacamp.com/teach/documentation"

# This packages the request: request
request = Request(url)

# Sends the request and catches the response: response
response = urlopen(request)

# Print the datatype of response
print(type(response))

# Be polite and close the response!
response.close()


# 22
# Import packages
from urllib.request import urlopen, Request

# Specify the url
url = "http://www.datacamp.com/teach/documentation"

# This packages the request
request = Request(url)

# Sends the request and catches the response: response
response = urlopen(request)

# Extract the response: html
html = response.read()

# Print the html
print(html)

# Be polite and close the response!
response.close()


# 23
# Import package
import requests

# Specify the url: url
url = "http://www.datacamp.com/teach/documentation"

# Packages the request, send the request and catch the response: r
r = requests.get(url)

# Extract the response: text
text = r.text

# Print the html
print(text)


# 24
# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url: url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extracts the response as html: html_doc
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Prettify the BeautifulSoup object: pretty_soup
pretty_soup = soup.prettify()

# Print the response
print(pretty_soup)


# 25
# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url: url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extract the response as html: html_doc
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Get the title of Guido's webpage: guido_title
guido_title = soup.title

# Print the title of Guido's webpage to the shell
print(guido_title)

# Get Guido's text: guido_text
guido_text = soup.get_text()

# Print Guido's text to the shell
print(guido_text)


# 26
# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extracts the response as html: html_doc
html_doc = r.text

# create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Print the title of Guido's webpage
print(soup.title)

# Find all 'a' tags (which define hyperlinks): a_tags
a_tags = soup.find_all('a')

# Print the URLs to the shell
for link in a_tags:
    print(link.get('href'))



###################################################
####################__PANDA__######################
###################################################
# 27
# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country':names, 'drives_right':dr, 'cars_per_cap':cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)


# 28
# 111111111 row label
# 111111111
import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)


# 29
# 30
# 31
# 32
# 33
# 34
# 35
# 36
# 37
# 38
# 39
# 40
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
#