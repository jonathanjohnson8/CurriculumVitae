"""
Linguist 278: Programming for Linguists
Stanford Linguistics, Fall 2020
Christopher Potts

Assignment 5

Distributed 2020-10-19
Due 2020-10-26

NOTES:

Please submit a modified version of this file, including all the
comments it currently contains.

Your file should not execute any functions when imported as a module
-- all function calls must be placed in the scope of
`if __name__ == '__main__'` at the bottom of this file.

Please name the file ling278_assign05_NAME.py

where NAME is a version of your name containing only letters and/or
underscores. (This will allow me to import your file as a Python
module.)
"""
import re


"""===================================================================
1. [2 points]

On Unix systems (including Apple's OS), egrep is a function that matches
regular expressions in files and other kinds of input. This question
asks you to write your own basic egrep.
"""

def egrep(regex, filename):
    """Python version of egrep. The function iterates through the
    user's file `filename`, line-by-line, stripping off the final
    newline character, and yielding only the lines that match the
    user's regular expression `regex`.

    Note: like basic egrep, a line that contains multiple matches for
    `regex` is yielded only once.

    Parameters
    ----------
    regex : Compiled regular expression
        The pattern to use for matching
    filename : str
        Full path to the file to open and iterate through

    Yields
    ------
    str
        Lines from the file, with newline characters removed.
    """
    with open(filename) as f:
        for line in f:
            line = line.replace('\n', '')
            if regex.search(line):
                yield line
       


def test_egrep():
    import tempfile
    contents = """ab\naAb\nabb\nba\nbbabbabab"""
    with tempfile.NamedTemporaryFile(mode='wt', delete=False) as f:
        f.write(contents)
    regex = re.compile("^a+b+$", re.I)
    iterator = egrep(regex, f.name)
    # Tests
    err_count = 0
    # Checks that `egrep` is an generator:
    try:
        first = next(iterator)
    except TypeError:
        print("Error in test_egrep: `egrep` should be defined as a generator.")
        err_count += 1
        first = None
    if first != "ab":
         print('Error in test_egrep: `egrep` did not yield the expected first element. '
               'Expected "{}"; Got "{}"'.format("ab", first))
         err_count += 1
    results = [first]
    for line in iterator:
        results.append(line)
    expected = ["ab", "aAb", "abb"]
    if results != expected:
        print("Error in test_egrep:\n\tExpected: {}\n\tGot: {}".format(expected, results))
        err_count += 1
    print("test_egrep finished with {} errors".format(err_count))


"""===================================================================
2. [2 points]

Final consonant clusters.
"""

def final_consonant_clusters(filename):
    """Uses `egrep` above to identify all and only the words with an
    uninterrupted string of 4 or more consonants *at the end of the
    line*. Thus,  all you need to do is write the regular expression
    and then feed it and `filename` to `egrep`.

    The intended notion of "consonant" is pre-defined in the string
    variable `consonants`. I left 'y' out for added interest.

    Your regex should be case-insensitive (i.e., you should match
    uppercase clusters even though `consonants` is all lowercase).

    Parameters
    ----------
    filename : str
        Full path to the file to search

    Yields
    ------
    str
    """
    consonants = "bcdfghjklmnpqrstvwxz" # + 'y' # 'y' left out for added interest
    regex = re.compile(r"[%s]{4,4}$" % consonants, re.I)
    return egrep(regex, (filename))

def _test_final_consonant_clusters(filename, expected_match_count):
    """Test that `final_consonant_clusters` returns the expected
    number of matches for `filename`. This is really just a utility
    for creating the actual tests, which are defined just below.
    It's unlikely that you'll want to use this function directly.

    Parameters
    ----------
    filename : str
        Full path to the file to search
    expected_match_count : int
        Expected number of matches

    Raises
    ------
    AssertionError
    """
    result = len(list(final_consonant_clusters(filename)))
    if result != expected_match_count:
        print("Error in `test_final_consonant_clusters_english` for {}\n\t"
              "Expected:{}\n\tGot:{}".format(filename, expected_match_count, result))
    else:
        print("test_final_consonant_clusters completed with 0 errors for {}".format(filename))


def test_final_consonant_clusters_english(unix_words_filename):
    """If `unix_words_filename` is the `unix-words.txt` file we've
    worked with before --

    http://web.stanford.edu/class/linguist278/data/unix-words-en.txt

    -- then this function tests `final_consonant_clusters`.
    """
    _test_final_consonant_clusters(unix_words_filename, 55)


def test_final_consonant_clusters_german(german_words_filename):
    """If `german_words_filename` is this German word list:

    http://web.stanford.edu/class/linguist278/data/unix-words-de.txt

    then this function tests `final_consonant_clusters` on that file.
    """
    _test_final_consonant_clusters(german_words_filename, 1171)


"""===================================================================
3. [2 points]

Finding vowel sequences.
"""

def vowel_sequence(filename, length):
    """Uses `egrep` above to determine whether filename contains vowel
    sequences of the supplied length (an int).

    Your regex should be case-insensitive (you should match uppercase
    sequences even though `vowels` is all lowercase).

    Parameters
    ----------
    filename : str
        Full path to the file to search.
    length : int
        Length of the vowel sequence to search for.

    Yields
    ------
    str
    """


    #vowels = "aeiou"
    #regex = re.compile(r"[{}]{{{}}}".format(vowels, length), re.I)
    #return egrep(regex, filename)

    
    vowels = "aeiou"
    regex = re.compile(r"([%s]{%s})" % (vowels, length), re.I)
    return egrep(regex,filename)
    
#attributions from course website

"""===================================================================
4. [4 points]

Finding the longest vowel sequences in a file.
"""

def longest_vowel_sequence(filename):
    """Uses `vowel_sequence` to find the longest vowel sequences anywhere
    in `filename`.

    Make sure your function will work appropriately in the unusual
    case where filename contains no vowels at all.

    Parameters
    ----------
    filename : str
        Full path to the file to search

    Returns
    -------
    dict
        create a dictionary where the keys are 'length' & 'matches'
        the value for 'length' should be an integer
        the value for "matches" should be a list []

        the value of 'length' will represent the longest vowel sequence 
        the value of 'matches' will represent the list of lines.
"""


    #length = 1
    #d = {'length': 0, 'matches':[]}
    #while True:
       # matches = list(vowel_sequence(filename, length))
        #if len(matches) == 0:
         #   return d
        #else:
           # d['length'] = length
           # d['matches'] = matches
            #length += 1

   d = {}
    empty_list = []
    with open(filename) as f:
       for line in f:
          # z = len(line)
        empty_list.append(len(line) - 1)
    x = max(empty_list)
    while x in vowel_sequence(filename,x) != []:
        x += 1
    if x - 1 == 0:
        d = {'length': x-1, 'matches': []}
    else:
        d['length'] = x - 1
        d['matches'] = list(vowel_sequence(filename, (x-1)))
    return d


def test_longest_vowel_sequence():
    import tempfile
    contents = """a\nxaex\nxaeiox\nxaeioux\nxaeiouae\nxuuai"""
    with tempfile.NamedTemporaryFile(mode='wt', delete=False) as f:
        f.write(contents)
    err_count = 0
    d = longest_vowel_sequence(f.name)
    expected_length = 7
    if d['length'] != expected_length:
        print("Error in `test_longest_vowel_sequence`"
              "\n\tExpected max length: {}\n\t"
              "Got:{}".format(expected_length, d['length']))
        err_count += 1
    expected_matches = ["xaeiouae"]
    if d['matches'] != expected_matches:
        print("Error in `test_longest_vowel_sequence`"
              "\n\tExpected matches: {}\n\t"
              "Got:{}".format(expected_matches, d['matches']))
        err_count += 1
    print("test_longest_vowel_sequence completed with {} errors".format(err_count))


"""===================================================================
Place all function calls below the following conditional so that they
are called only if this module is called with

`python ling278_assign04.py`

No functions should execute if it is instead imported with

import ling278_assign05

in the interactive shell.
"""

if __name__ == '__main__':
    print(test_egrep)
    length = 'length'
    filename = 'unix-words-en.txt'
    unix_words_filename = 'unix-words-en.txt'
    #length = len(range(0 - 5))
    vowel_sequence(filename, length)
    #german_words_filename = 'german_words_filename.txt'
    #print(test_final_consonant_clusters_german(german_words_filename))
    print(_test_final_consonant_clusters(unix_words_filename, 55))
    #print(longest_vowel_sequence(filename))
    print(test_longest_vowel_sequence())