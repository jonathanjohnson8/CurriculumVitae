"""
Linguist 278: Programming for Linguists
Stanford Linguistics, Fall 2020
Christopher Potts

Assignment 4

Distributed 2020-10-12
Due 2020-10-19

NOTES:

Please submit a modified version of this file, including all the
comments it currently contains.

Your file should not execute any functions when imported as a module
-- all function calls must be placed in the scope of
`if __name__ == '__main__'` at the bottom of this file.

Please name the file ling278_assign04_NAME.py

where NAME is a version of your name containing only letters and/or
underscores. (This will allow me to import your file as a Python
module; more about that later.)
"""


"""===================================================================
1.  [2 points]

Filename globs. We haven't talked about these yet, so you might need
to explore the documentation and experiment on your own a bit to get
a feel for how to solve this:

https://docs.python.org/3/library/glob.html

It's hard for me to write a test for this because it is reading from
your system. So, to help clarify the intended functionality, suppose
that the current directory contains the files

foo.py
bar.PY
baz.doc
maz.txt

and the user calls the function with exts=["py", "doc"]. The result
should be the list of strings ["baz.doc", "foo.py"].

"""

def directory_listing(exts):
    """Use `glob.glob` to return a list of the files in the current
    directory with an extension in the iterable of str `ext`.

    Parameters
    ----------
    ext : tuple of str
        List of extensions. These are specified as strings without
        a preceding period. The logic is case-sensitive -- for
        example exts=['py'] will not match 'foo.PY'.

    Returns
    -------
    list of str -- the filenames in alphabetical order

    """
    import glob



    lolo= []
    for ext in (exts):
        list_of_files =  glob.glob("*" + "." + ext)
        lolo += list_of_files

    return sorted(lolo)

"""===================================================================
2. [2 points]

The NLTK library was installed in your Python environment when you
installed Anaconda. It includes a function `sent_tokenize` that does
a passably good job at parsing English text into sentences.

This question asks you to use `sent_tokenize` by writing a function
that takes a filename as input and returns the list of sentences in
that file, as determined by `sent_tokenize`.

Note: it is likely that trying to do this will return a message the
first time saying that you are missing some NLTK resource files. Part
of the task here is to follow those instructions to get past that
(hopefully small) obstacle.

"""

def sentence_tokenize_file(filename):
    """Use `sent_tokenize` to parse the contents of `filename` into
    sentences.

    Parameters
    ----------
    filename : str
        Full path to the file to parse.

    Returns
    -------
    list of str

    """
    from nltk.tokenize import sent_tokenize


    with open(filename) as f:
        sentences = f.read()
        w = sent_tokenize(sentences)
    return w



def test_sentence_tokenize_file(filename="alice.txt"):
    """To use this test, you need to make sure the value of
    `filename` is the full path to a copy of alice.txt, a
    file we've used a few times before.
    """
    result = sentence_tokenize_file(filename)[-1]
    expected = """Most people start at our Web site which has the main PG search facility:

     http://www.gutenberg.org

This Web site includes information about Project Gutenberg-tm,
including how to make donations to the Project Gutenberg Literary
Archive Foundation, how to help produce our new eBooks, and how to
subscribe to our email newsletter to hear about new eBooks."""
    if result != expected:
        raise AssertionError(
            "`test_sentence_tokenize_file` failed. "
            "Expected final sentence from `sentence_tokenize_file` is\n\n{}"
            "\n\nGot\n\n{}".format(expected, result))
    else:
        print("`test_sentence_tokenize_file` passed")


"""===================================================================
3. [2 points]

The Concreteness dataset is a freely available CSV file released with
this paper:

Brysbaert, Marc; Warriner, Amy Beth; and Kuperman, Victor. 2014.
Concreteness ratings for 40 thousand generally known English word
lemmas. Behavior Research Methods 46(3): 904-911.

A copy of it is available here:

https://web.stanford.edu/class/linguist278/data/Concreteness_ratings_Brysbaert_et_al_BRM.csv

The task for this question is to write a generator over this file.
You should use the csv library to create a reader that parses the
lines of the file. Your function should yield dictionaries where the
keys are the column names in the file. You do not need to worry too
much about what the columns mean, but you do need to do the type
conversions suggested by the variables `float_valued`, `bool_valued`,
`int_valued`, and `str_valued` given in the starter code.

"""

def concreteness_reader(filename):
    """Parse the Concreteness dataset.

    Parameters
    ----------
    filename : str
        Full path to the file to parse.

    Yields
    ------
    dict

    """
    import csv

    float_valued = ['Conc.M', 'Conc.SD', 'Percent_known']
    bool_valued = ['Bigram']
    int_valued = ['Unknown', 'Total', 'SUBTLEX']
    str_valued = ['Word', 'Dom_Pos']


    with open (filename) as f:
        for d in csv.DictReader(f):
            dd = {
                str_valued[0] : d['Word'],
                bool_valued[0] : d['Bigram'] == '1',
                float_valued[0] : float(d['Conc.M']),
                float_valued[1] : float(d['Conc.SD']),
                int_valued[0] : int(d['Unknown']),
                int_valued[1] : int(d['Total']),
                float_valued[2] : float(d['Percent_known']),
                int_valued[2] : int(d['SUBTLEX']),
                str_valued[1] : str(d['Dom_Pos']),
                }
      
            yield dd


def test_concreteness_reader(filename):
    """To use this test, call it with the full path to your
    copy of the Concreteness dataset as the argument."""

    from collections import OrderedDict

    ex = next(concreteness_reader(filename))

    if not isinstance(ex, (dict, OrderedDict)):
        raise AssertionError("`concreteness_reader` should yield dicts")

    expected = {
        'Conc.M': float,
        'Conc.SD': float,
        'Percent_known': float,
        'Bigram': bool,
        'Unknown': int,
        'Total': int,
        'SUBTLEX': int,
        'Word': str,
        'Dom_Pos': str}
    errors = 0
    for k, v in ex.items():
        if not isinstance(v, expected[k]):
            print("For key {}, expected type {} but got {}".format(k, expected[k], type(v)))
            errors += 1
    print("test_concreteness_reader finished with {} errors".format(errors))


"""===================================================================
4. [2 points]

Now that you have a reader for the Concreteness dataset, you'll
probably want to write some functions that use it to do analysis. This
question asks you to write one such function.

The task is to complete `concreteness_mean_stats` so that it gathers
the values at the key 'Conc.M' into a list and then calls the user's
function `func` on the result. You can assume that the user can be
trusted to supply only functions that work on lists of floats. I've
given `max` as a default, but many others should work, including
`mean`, `sd`, and `zscore` from assignment 1.

It's required that your function make use of your
`concreteness_reader`.

"""

def concreteness_mean_stats(filename, func=max):
    """Use `concreteness_reader` to parse `filename` and
    call `func` on the list of all 'Conc.M' values.

    Parameters
    ----------
    filename = str =  Ex. ' alice.txt '
        Full path to the file to parse.

    Yields
    ------
    return value of `func`

    """
   ##work on this code and do it from scratch
    first_list = concreteness_reader(filename)
    test_list = []
    for elem in first_list:
        variable1 = elem['Conc.M']
        test_list.append(variable1)
    return func(test_list)

def test_concreteness_mean_stats(filename):
    """To use this test, call it with the full path to your
    copy of the Concreteness dataset as the argument."""

    def mean(vals):
        return sum(vals) / len(vals)

    tests = [(max, 5.0), (mean, 3.036267), (min, 1.04)]

    errors = 0
    for func, expected in tests:
        result = concreteness_mean_stats(filename, func=func)
        if round(result, 6) != expected:
            print(
                "Error for test_concreteness_mean_stats: "
                "for function {} func, expected {} but got {}".format(
                    func.__name__, expected, result))
            errors += 1
    print("test_concreteness_mean_stats finished with {} errors".format(errors))


"""===================================================================
5. [2 points]

It seems a shame to have to reparse the Concreteness dataset all the
time, but the CSV storage format means that we have to, since CSV
can store only strings. The JSON format is richer in this regard: it
can store ints, floats, lists, and dicts, in addition to strings.

The task for this question is to use `concreteness_reader` to reade
in the Concreteness dataset but then write it to the user's supplied
filename as a JSON file. For this, you'll need to review the
documentation for the `json.dump` method:

https://docs.python.org/3/library/json.html

When you write the JSON, please sort the keys and indent by 4
characters. These things can be specified as part of the call to
`json.dump` -- see the documentation for details.

Tip: you'll need to make use of basic file-writing, as covered here:

http://web.stanford.edu/class/linguist278/notes/ling278_class06.html

"""

def write_concreteness_to_json(src_filename, output_filename):
    """Store the Concreteness dataset in a JSON file, in the format
    determined by `concreteness_reader`.

    Parameters
    ----------
    src_filename : str
        Full path to the file to parse.

    output_filename : str
        Full path to the JSON to create.

    """
    import json
    #empty_list = []
    s_final = src_filename
    with open(output_filename, "w+") as f:
        d = list(concreteness_reader(s_final))
        #for elem in d:
            #empty_list.append(elem)
        json.dump(d,f, sort_keys=True, indent=4)
    
        #print(s, file = output_filename)


"""===================================================================
Place all function calls below the following conditional so that they
are called only if this module is called with

`python ling278_assign04.py`

No functions should execute if it is instead imported with

import ling278_assign04

in the interactive shell.
"""

if __name__ == '__main__':
    exts=["py", "doc"]
    #print(directory_listing(exts))
    #filename = 'alice.txt'
    #print(test_sentence_tokenize_file("alice.txt"))
    filename = 'Concreteness_ratings_Brysbaert_et_al_BRM.csv.crdownload'
    concreteness_reader(filename)
    #print(test_concreteness_reader(filename))
    #(concreteness_mean_stats(filenamez, func=max))
    #test_concreteness_mean_stats(filenamez)
    src_filename = 'Concreteness_ratings_Brysbaert_et_al_BRM.csv.crdownload'
    output_filename = 'Concreteness_ratings_Brysbaert_et_al_BRM.csv.crdownload'
    print(write_concreteness_to_json(src_filename,output_filename))