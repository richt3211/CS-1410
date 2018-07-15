"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
Do Not Move on to the next function until its tests report 'ok' or your code
may not work as expected.
"""

import unittest
from test_fileToList import TestFileToList
from test_returnFirstString import TestReturnFirstString
from test_strandsAreNotEmpty import TestStrandsAreNotEmpty
from test_strandsAreEqualLengths import TestStrandsAreEqualLengths
from test_findLargestOverlap import TestFindLargestOverlap
from test_findBestCandidate import TestFindBestCandidate
from test_joinTwoStrands import TestJoinTwoStrands

if __name__ == '__main__':
    testCases = [
        TestFileToList,
        TestReturnFirstString,
        TestStrandsAreNotEmpty,
        TestStrandsAreEqualLengths,
        TestFindLargestOverlap,
        TestFindBestCandidate,
        TestJoinTwoStrands
    ]

    allTests = []
    for testCase in testCases:
        allTests.append(unittest.TestLoader().loadTestsFromTestCase(testCase))

    unittest.TextTestRunner().run(unittest.TestSuite(allTests))