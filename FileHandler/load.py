'''
Created on 9 jan. 2015

@author: bergr2
'''
import re
from statistics import median


def re_split(sep, string):
    '''
    Splits a string on a seperator e.g. a newline symbol or a semicolon using
    regular expressions.
    '''
    re_pattern = re.compile(r'''((?:[^''' + sep + '''"']|"[^"]*"|'[^']*')+)''')
    return re_pattern.split(string)[1::2]


def open_read(filename, encoding=None, sep=None):
    '''
    Reads filecontents from <filename> and splits on newline symbols and <sep>.
    '''
    with open(filename, "r", encoding=encoding) as f: #open file
        c = f.read() #read file contents
        if sep: #when sep exists: split file contents and on newline
            content = [re_split(sep, x) for x in re_split('\n', c)]
        else: 
            content = re_split('\n', c)
    return content


def try_unicode(filename, encoding, sep):
    '''
    Tries out different types of encodings given in the encoding parameter
    '''
    if len(encoding) == 0:
        raise Exception("Decoding failed with given encodings")
    try:
        return open_read(filename, encoding[0], sep)
    except UnicodeDecodeError:
        return try_unicode(filename, encoding[1:], sep)


def load(filename, sep=";", header=False, same_length=False, verbose=True):
    '''
    File loader, reads contents of a file and returns a list of its contents,
    split on newline and/or seperator(sep).
    Verbose toggles printing out statements to screen. 
    Same_length checks wether the rowsize is constant and removes 
    those rows that differ from the median row length.
    '''
    if verbose:
        print('Loading %s...' % filename)
    
    #handling encoding
    try_unicode(filename, ['utf8', 'latin1'], sep)

    #settings
    if header:
        #remove header row
        content.pop(0)
    if same_length:
        #only keep rows of median length
        m = median([len(x) for x in content])
        content = [x for x in content if len(x) == m]
    
    if verbose:
        print('File loaded.')
    return content


def csv(filename, sep=";", header=False, verbose=True):
    'wrapper function that loads a csv, splits on newline and seperator'
    return load(filename, sep, header, verbose=verbose)


def txt(filename):
    'wrapper function that loads a csv (only splits on newline)'
    return load(filename, sep=None)
