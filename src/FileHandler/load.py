'''
Created on 9 jan. 2015

@author: bergr2
'''

import re
from statistics import median
import os
from urllib import request
from zipfile import ZipFile
from io import BytesIO

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
directories = [d for d in os.listdir(ROOT_DIR) if os.path.isdir(os.path.join(ROOT_DIR, d))]


def dirlist():
    return {x: os.path.join(ROOT_DIR, x) for x in directories}


def re_split(sep, string):
    '''
    Splits a string on a seperator e.g. a newline symbol or a semicolon using
    regular expressions.
    '''
    re_pattern = re.compile(r'''((?:[^''' + sep + '''"']|"[^"]*"|'[^']*')+)''')
    return re_pattern.split(string)[1::2]


def unzip(zipfile, zippedfile, encoding=None):
    if zippedfile:
        try:
            zfile = ZipFile(zipfile, 'r')
        except AttributeError:
            zfile = ZipFile(BytesIO(zipfile), 'r')
        content = zfile.open(zippedfile).read()
        zfile.close()
        if encoding:
            content = content.decode(encoding)
        return content
    else:
        return zipfile


def open_from_disk(filename, encoding=None, zippedfile=None):
    with open(filename, "r", encoding=encoding) as f: #open file
        return unzip(f.read(), zippedfile) #read file contents and unzips if necessary


def download(url, encoding=None, zippedfile=None):
    url = request.urlopen(url) #download file
    return unzip(url.read(), zippedfile, encoding) #read file contents and unzips if necessary


def open_read(filename, encoding=None, sep=None, zippedfile=None, method=open_from_disk):
    '''
    Reads filecontents from <filename> and splits on newline symbols and <sep>.
    '''
    c = method(filename, encoding, zippedfile)
    if sep: #when sep exists: split file contents and on newline
        content = [re_split(sep, x) for x in re_split('\n', c)]
    else: 
        content = re_split('\n', c)
    return content


def try_unicode(filename, encoding, sep, zippedfile=None, method=open_from_disk):
    '''
    Tries out different types of encodings given in the encoding parameter
    '''
    for enc in encoding:
        try:
            return open_read(filename, encoding=enc, sep=sep, zippedfile=zippedfile, method=method)
        except UnicodeDecodeError:
            pass
    raise Exception("Decoding failed with given encodings")


def load(filename, sep=";", header=False, same_length=False, verbose=True, zippedfile=None, method=open_from_disk):
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
    content = try_unicode(filename=filename, encoding=['utf8', 'latin1'], sep=sep, zippedfile=zippedfile, method=method)

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


def csv(filename, sep=";", header=False, verbose=True, zippedfile=None):
    'wrapper function that loads a csv, splits on newline and seperator'
    return load(filename, sep, header, verbose=verbose)


def download_csv(url, sep=";", header=False, verbose=True, zippedfile=None):
    'wrapper function that downloads a csv from a url, splits on newline and seperator'
    return load(url, sep, header, verbose=verbose, method=download, zippedfile=zippedfile)


def txt(filename):
    'wrapper function that loads a csv (only splits on newline)'
    return load(filename, sep=None, method=open_from_disk)