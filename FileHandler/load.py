'''
Created on 9 jan. 2015

@author: bergr2
'''
import re
from statistics import median

def open_read(filename, encoding=None, sep=None):
    re_pattern_end = re.compile(r'''((?:[^\n"']|"[^"]*"|'[^']*')+)''')
    re_pattern_sep = re.compile(r'''((?:[^''' + sep + '''"']|"[^"]*"|'[^']*')+)''')
    with open(filename, "r", encoding=encoding) as f:
        c = f.read()
        if sep:
            content = [re_pattern_sep.split(x)[1::2] for x in re_pattern_end.split(c)[1::2]]
        else:
            content = re_pattern_end.split(c)[1::2]
    return content


def load(filename, sep=";", header=False, same_length=False, verbose=True):
    if verbose:
        print('Loading %s...' % filename)
    
    #handling encoding
    try:
        content = open_read(filename, sep=sep)
    except UnicodeDecodeError:
        content = open_read(filename, 'utf8', sep)
    except UnicodeDecodeError:
        content = open_read(filename, 'latin1', sep)
    
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
    return load(filename, sep, header, verbose=verbose)


def txt(filename):
    return load(filename, sep=None)


def dirlist():
    return {x: y for x, y in csv("dirlist.cfg", verbose=False)}
    
