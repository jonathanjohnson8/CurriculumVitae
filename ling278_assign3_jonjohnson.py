"""
Linguist 278: Programming for Linguists
Stanford Linguistics, Fall 2020
Christopher Potts

Assignment 3

Distributed 2020-10-05
Due 2020-10-12

NOTES:

Please submit a modified version of this file, including all the
comments it currently contains.

Your file should not execute any functions when imported as a module
-- all function calls must be placed in the scope of
`if __name__ == '__main__'` at the bottom of this file.

Please name the file ling278_assign03_NAME.py

where NAME is a version of your name containing only letters and/or
underscores. (This will allow me to import your file as a Python
module; more about that later.)
"""

"""===================================================================
1.  [2 points]

Sophisticated title case. The `str` method `title` just capitalizes
every word. In true U.S. title case, a pre-set list of function words
are not capitalized. Your task is to write a function that at least
provides a framework for doing proper title case (even if this
implementation doesn't do everything we want yet).
"""

def proper_title_case(s):
    """Return a title-cased version of `s` using a pre-set list of
    words that are never capitalized unless they are at the start of
    the string.

    Parameters
    ----------
    s : str

    Returns
    -------
    str

    """
    # Stick to this basic list for now. A production version would
    # extend this and perhaps allow the user to specify places where
    # even these words should be capitalized.
    nocaps = ["the", "in", "on", "a", "an", "to", "and"]
    s = " "
    # The rest of the function goes here:
    proper_case = s.strip().split()
    #brackets
    first_word = [proper_case[0].title()]
    for words in proper_case[1:]:
        if words.lower() in nocaps:
            words = words.lower()
        else: 
            words = words.title()
        first_word.append(words)
    return " ".join(first_word)



        


   # if i in parse:

   # if nocaps is [0]  --> .title()

    #x = nocaps.lower()


def test_proper_title_case():
    examples = [
        ["Lost In Translation", "Lost in Translation"],
        ["Back To The Future", "Back to the Future"],
        ["it", "It"],
        ["The Royal Tenenbaums", "The Royal Tenenbaums"],
        ["the insider", "The Insider"]]
    err_count = 0
    for ex, expected in examples:
        result = proper_title_case(ex)
        if result != expected:
            print("test_proper_title_case failed:"
                  "\n\tInput: {}\n\tExpected: {}"
                  "\n\tGot: {}".format(ex, expected, result))
            err_count += 1
    print("{} errors for test_proper_title_case".format(err_count))


"""===================================================================
2.  [1 point]

Unix words file reader
"""

def load_unix_words(filename):
    """Reads in the the Unix words dictionary, which has one word
    per line, and returns the dictionary as a set of strings. No
    regularization of the strings is done by this function except
    for removing any peripheral whitespace or newline characters
    from each word/line.

    You can get the Unix word dictionary here:

    https://web.stanford.edu/class/linguist278/data/unix-words-en.txt

    Make sure you return a set! Details on sets:

    https://docs.python.org/3.7/library/stdtypes.html#set

    Parameters
    ----------
    filename : str
        Full path to the Unix words file.

    Returns
    -------
    set of str

    """
    
    empty_list = []
    with open(filename) as f:
        #file = list of strings where each line is a string
    #there is a new line character at the end of each line: strip(\n)
        for line in f:
            empty_list.append(line.strip())
        #iterating over file : for loop
            #read through each line (remove whitespace): strip()
                #if I see entry, I want to add it to the list
    #create list
    #append word to list
    #change value list to set
    w = set(empty_list)
    return w




def test_load_unix_words(filename):
    """`filename` should be the full path to the Unix words file."""
    err_count = 0
    entries = load_unix_words(filename)
    if not isinstance(entries, set):
        print("test_load_unix_words failed: the return value is not a set")
        err_count += 1
    test_cases = ["Aaron", "Jean-Pierre"]
    for ex in test_cases:
        if ex not in entries:
            print('test_load_unix_words failed: "{}" is not in the return value'.format(ex))
            err_count += 1
    print("{} errors for test_load_unix_words".format(err_count))


"""===================================================================
3.  [2 points]
"""

def get_reversible_words(words):
    """Given a set of str `words`, find all of the elements in it
    whose string reversal is also in `words`. This should include
    palindromes, since they are their own reversibles, and it includes
    single-letter words as a trivial edge case. No preprocessing of
    the strings should be done -- for example, 'Dog' and 'God' are not
    reversable pairs because of the case differences.

    Example:

    >>>> reversible_words({'dog', 'try', 'god', 'ewe'})
    {'dog', 'god', 'ewe'}

    Parameters
    ----------
    words : set of str

    Returns
    -------
    set of str

    """
    empty_list = []

    for elem in words:
        w = elem[::-1]
        if w in words:
            empty_list.append(w)
    return set(empty_list)



def test_get_reversible_words():
    words = {'dog', 'try', 'god', 'ewe'}
    expected = {'dog', 'god', 'ewe'}
    result = get_reversible_words(words)
    if result != expected:
        print("test_get_reversible_words failed;"
              "\n\tExpected {};\n\tGot {}".format(expected, result))
    else:
        print("0 errors for test_get_reversible_words")


"""===================================================================
4.  [1 point]

Reversible Unix words
"""

def get_reversible_unix_words(filename):
    """A simple wrapper function to find the reversible words in the Unix
    word list. `filename` is processed by `load_unix_words`, and the
    output of that is fed to `get_reversible_words`, which is the return
    value of this function. Should be at most three lines of code.

    Parameters
    ----------
    filename : str
        Full path to the Unix words file.

    Returns
    -------
    set of str

    """
    w = load_unix_words(filename)
    return get_reversible_words(w)


def test_get_reversible_unix_words(filename):
    """`filename` should be the full path to the Unix words file."""
    result = get_reversible_unix_words(filename)
    expected_sample = {'yak', 'kitab', 'Y', 'M', 'u'}
    err_count = 0
    for ex in expected_sample:
        if ex not in result:
            print('test_get_reversible_unix_words failed: "{}" is not in the return value'.format(ex))
            err_count += 1
    for ex in result:
        if ex[::-1] not in result:
            print('test_get_reversible_unix_words failed: '
                  '"{}" is in the return value but not its reversal'.format(ex))
    print("{} errors for test_get_reversible_unix_words".format(err_count))


"""===================================================================
5.  [4 points] Cristian Danescu-Niculescu-Mizil released a large corpus
of U.S. Supreme Court Dialogues:

https://confluence.cornell.edu/display/llresearch/Supreme+Court+Dialogs+Corpus

For this problem, download and unpack the corpus (via the link named
DATA), and open up the file supreme.conversations.txt so that you can
get a feel for its format.

Your goal is to produce an iterator function called
`supremes_iterator` that goes through 'supreme.conversations.txt'
line-by-line, yielding a dict with the structure described in the
docstring for `supremes_iterator` below.
"""

def supremes_iterator(filename):
    """Process the Supremes 'supreme.conversations.txt` line-by-line
    yielding dictionaries with the following structure, where the
    capital letter strings at left are the keys, the type for the
    values is given right after them in parentheses, and the desired
    logic is explained after the colon.

    CASE_ID (str): unique id of the case
    UTTERANCE_ID (int): unique id of the utterance
    AFTER_PREVIOUS (bool): True or False (the Python booleans)
    SPEAKER (str): from the file
    IS_JUSTICE in {JUSTICE, NOT JUSTICE} (bool): True if file value is 'JUSTICE', else False
    JUSTICE_VOTE (str): the string from the file or None (the Python object) if the str is 'NA'
    PRESENTATION_SIDE (str): the string from the file
    UTTERANCE (str): the text produced by the speaker
    WORDS (list of strs): UTTERANCE tokenized according to your tokenizer

    For WORDS, write a separate function called `supremes_tokenizer`. This
    can be a new function or one you wrote for a previous assignment or
    in-class exercise. The important thing is that it is a separate
    function from `supremes_iterator`.

    Parameters
    ----------
    filename : str
        Full path to 'supreme.conversations.txt'

    Yields
    ------
    dict, in the above format

    """
    # Danescu's custom field separator:
    sep = " +++$+++ "
    
    d = {}

    with open (filename) as f:
        for elem in f:
            entries = elem.split(sep)
            #yield{
            d['CASE_ID'] = str(entries[0])
            d['UTTERANCE_ID'] = int(entries[1])
            d['AFTER_PREVIOUS'] = (str(entries[2] == 'TRUE'))
            d['SPEAKER'] = str(entries[3])
            d['IS_JUSTICE'] = str(entries[4]) == 'JUSTICE' 
            if str(entries[5]) == 'NA':
                d['JUSTICE_VOTE'] = None
            else:
                d['JUSTICE_VOTE'] =  str(entries[5])
            d['PRESENTATION_SIDE'] = str(entries[6])
            d['UTTERANCE'] = str(entries[7])
            d['WORDS'] = supremes_tokenizer(str(entries[7]))
            #}
            yield d

def supremes_tokenizer(s):
    """Simple tokenizer, with whatever logic you like. You won't be
    judged on the quality of the tokenizer, but rather only that it
    has the right argument and return value types.

    Parameters
    ----------
    s : str

    Returns
    -------
    list of str

    """
    import string

    # This is a str of concatenated punctuation marks:
    punct = string.punctuation
    result = []
    s = s.lower()
    #initial list of tokens, then iterate over values instead of indices
    new_tokens = s.strip().split()
    for i in new_tokens:
        w = i.strip(punct)
        result.append(w)
    return result


def test_supremes_iterator(filename):
    """This is a very partial test. You might want to expand it so
    that it tests the full specification for `supremes_iterator`.
    """
    iterator = supremes_iterator(filename)
    example = next(iterator)
    expected_keys = {'AFTER_PREVIOUS', 'UTTERANCE_ID', 'IS_JUSTICE',
                     'PRESENTATION_SIDE', 'SPEAKER', 'UTTERANCE',
                     'JUSTICE_VOTE', 'CASE_ID', 'WORDS'}
    err_count = 0
    if set(example.keys()) != expected_keys:
        print("test_supremes_iterator error: Unexpected key set")
        err_count += 1
    if not isinstance(example['UTTERANCE_ID'], int):
        print("test_supremes_iterator error: Unexpected type for line 1 'UTTERANCE_ID'")
        err_count += 1
    if example['IS_JUSTICE'] is not True:
        print("test_supremes_iterator error: Unexpected value for line 1 'IS_JUSTICE'")
        err_count += 1
    print("{} errors for test_supremes_iterator".format(err_count))


"""===================================================================
Place all function calls below the following conditional so that they
are called only if this module is called with

`python ling278_assign03_NAME.py`

No functions should execute if it is instead imported with

import ling278_assign03_NAME

in the interactive shell.
"""

if __name__ == '__main__':
    s = " "
    #print(proper_title_case(s))
    #print(test_proper_title_case())
    #print(load_unix_words("unix-words-en.txt"))
    filenamef = 'unix-words-en.txt'
    print(test_get_reversible_words())
    print(get_reversible_unix_words(filenamef))
    print(test_get_reversible_unix_words(filenamef))
    filenamez = 'supreme.conversations.txt'
    print(supremes_iterator(filenamez))
    print(supremes_tokenizer(s))
    print(test_supremes_iterator(filenamez))