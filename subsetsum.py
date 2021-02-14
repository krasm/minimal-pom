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


x = [3, 34, 4, 12, 5, 2]
print(ssum_dyn(x, 0, 12))
print(ssum_dyn(x, 0, 30))
print(ssum_dyn(x, 0, 5))
    