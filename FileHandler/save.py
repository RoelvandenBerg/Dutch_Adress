'''
Created on 9 jan. 2015

@author: Roel van den Berg
'''

def stringify(content, dim=0, seplist=None):
    if not seplist:
        seplist = ["\n", ";", ",", "-", ":"]
    '''
    returns a string of a (multi-dimension)-list
    '''
    if dim == 0 or not seplist[0] or len(seplist) == 0:
        return str(content)
    else:        
        return seplist[0].join([stringify(x, dim-1, seplist[1:]) for x in content])


def save(filename, content, encoding=None, verbose=True, dim=1, end="\n", sep=";", *othersep):
    '''
    filename =  filename
    content =   list (of lists)*
    encoding =  file encoding
    dim =       dimension of content (i.e. [[x,y],[z]] 
                has a dimension of 2, [x,y] a dimension 
                of 1 and x a dimension of 0 
    end =       linebreak character, usually '\n'
    sep =       first seperator, chosen to be ';', 
                standard setting for a '.csv'-file
    othersep =  other sep are the other seperators, 
                apart from 'sep'
    * depending on dimensions of content or string when dimension = 0
    '''
    if verbose:
        print("Saving: %s..." %filename)
    
    #combine first possible seperator with other seperators
    seplist = [end, sep] + list(othersep)
    
    #open and write file
    with open(filename, 'w', encoding=encoding) as f:
        f.write(stringify(content, dim, seplist))
    
    if verbose:
        print("File saved.")


def check_ext(filename, ext):
    if ext[0] != ".":
        ext = "." + ext
    if filename[-1*len(ext):] != ext:
        filename = filename + ext
    return filename
   
 
def csv(filename, content, encoding=None, verbose=True, sep=";", ext="csv"):
    filename = check_ext(filename, ext)
    save(filename, content, encoding, verbose, 2, "\n", sep)


def txt(filename, content, encoding=None, verbose=True, tabs=False, ext="txt"):
    filename = check_ext(filename, ext)
    if not tabs:
        save(filename, content, encoding, verbose, 1, "\n")
    else:
        save(filename, content, encoding, verbose, 2, "\n", "\t")


def string(filename, content, encoding=None, verbose=True):
    save(filename, content, encoding, verbose, dim=0)
