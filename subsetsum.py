#!/usr/bin/env python3

def ssum(X, T, result):
    """ X set of positive integers, T - vsum we are looking for """
    xs = set(X)
    xr = set(result)
    if T == 0:
        print(xr)
        return True
    if T < 0 or len(X) == 0: 
        return False
    e = xs.pop()
    xr.add(e)
    return ssum(xs, T, result) or ssum(xs, T - e, xr)

def ssum_dyn(x, i, t):
    
    if t == 0:
        return True
    if t < 0 or i >= len(x):
        return False
    if t < x[i]:
        return ssum_dyn(x, i+1, t)
    return ssum_dyn(x, i+1, t) or ssum_dyn(x, i+1, t-x[i])

def ssum_dyn1(x, t):
    S = [[False for i in range(0, len(x) + 1)] for j in range(0, t+1)]

    for i in range(0, len(x)+1):
        S[0][i] = True
    for i in range(len(x)-1, -1, -1):
        for v in range(0, t):
            if v < x[i]:
                S[v][i] = S[v][i+1]
            else:
                S[v][i] = S[v][i+1] or S[v-x[i]][i+1]

    return S[v][0]
 
print(ssum_dyn1([1, 8, 3], 4)) # True
x = [3, 34, 4, 12, 5, 2]
print(ssum_dyn1(x, 3)) # True
print(ssum_dyn1(x, 12)) # True
print(ssum_dyn1(x, 30)) # False
print(ssum_dyn1(x, 5))  # True
    