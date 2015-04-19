'''
Created on Apr 19, 2015

@author: roel
'''
from ..FileHandler.test.test_filehandler import *
from .. import address


class TestAddress(unittest.TestCase):

    def testSmallestDist(self):
        pass
    
    def testStripAccents(self):
        pass


class TestAddressAddress(unittest.TestCase):

    def testStr(self):
        pass


class TestAddressPostalCode(unittest.TestCase):

    def testinit(self):
        pass


class TestAddressHousenumber(unittest.TestCase):

    def testStr(self):
        pass

    def testMatch(self):
        pass

    def testMatchEvenType(self):
        pass


class TestAddressStreet(unittest.TestCase):

    def testAdd(self):
        pass

    def testFind(self):
        pass

    def testFindRDcoord(self):
        pass


class TestAddressCity(unittest.TestCase):

    def testAdd(self):
        pass

    def testFind(self):
        pass


class TestAddressBook(unittest.TestCase):

    def testAdd(self):
        pass

    def testFind(self):
        pass

    def testFindPC(self):
        pass


class TestAddressSearch(unittest.TestCase):

    def testFindRDcoord(self):
        pass

    def testFind(self):
        pass

    def testReset(self):
        pass

    def testFindCityStreet(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()