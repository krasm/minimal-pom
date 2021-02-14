#!/usr/bin/env python3

import unittest

# longest increasing subaaray
# return length of longest increasing subaray
# x input array
# i last taken
# j current array start
def lis_old(x, i, j):
    print("calculating for last taken: ", i, " and next start ", j)
    if j == len(x):
        return 0
    if i >= 0 and x[i] >= x[j]:
        return lis(x, i, j+1)
    
    return max(lis(x, i, j+1), lis(x, j, j+1) +1)

def lis(x, i, j):
    S = [[0 for i in range(0, len(x)+1)] for j in range(0, len(x)+1)]



    return S[0][len(x)-1]

class LisTestMethods(unittest.TestCase):
    def test1(self):
        self.assertEqual(0, lis([], -1, 0))

    def test2(self):
        self.assertEqual(1, lis([1], -1, 0))

    def test3(self):
        self.assertEqual(1, lis([1], -1, 0))

    def test4(self):
        self.assertEqual(6, lis([0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15], -1, 0))

    def test5(self):
        self.assertEqual(1, lis([5, 4, 3, 2, 1], -1, 0))

    def test6(self):
        self.assertEqual(3, lis([5, 8, 3, 7, 9, 1], -1, 0))

    def test7(self):
        self.assertEqual(6, lis([1, 3, 5, 7, 8, 9], -1, 0))


print(lis([1, 3, 2], -1, 0))