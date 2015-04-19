'''
Created on Apr 19, 2015

@author: roel
'''
import unittest
from .. import load

class TestLoad(unittest.TestCase):

    def testDirlist(self):
        dirlist = load.dirlist()
        self.assertTrue(all(x in dirlist for x in ['src', 'data', 'results']), 'missing directories')
    
    def testReSplit(self):
        texts = ['asdfljkeoin";"vasd*(&', 'sldkf";";sldkfj\n;', "lkj'lkj;\n'lkj;asdfasdf\nlaksdfjasdf;\nasdfasdf"]
        sep = [';', '\n']
        cases = [[load.re_split(s, y) for y in texts] for s in sep]
        seperated = [[(len(x), i+1) for i, x in enumerate(y)] for y in cases]
        [[self.assertEqual(*x) for x in y] for y in seperated]
    
    def testTryUnicode(self):
        pass
    
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()