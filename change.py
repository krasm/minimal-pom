#!/us/bin/env python3

import unittest

def change(value, nominals):
    S = [[0 for i in range(0, len(nominals))] for j in range(0, value+1)]
    result = 0
    for n in range(0, len(nominals)):
        for i in range(1, value+1):
            if i < nominals[n]:
                S[i][n] = 0
            else:
                S[i][n] = S[i-nominals[n]][n] + 1

    return result

class changeTest(unittest.TestCase):
    def test1(self):
        v = change(4, [1, 2, 3])
        self.assertEqual(4, v)

    def test2(self):
        v = change(10, [2, 5, 3, 6])
        self.assertEqual(5, v)
