# bad_script.py

import math, sys  # import things

def f(x, y=0, z=None):  # main function that does stuff
    # make list
    L = []  # list for values
    # loop over x
    for i in range(0, len(x)):  # go over all elements
        v = x[i]  # get value
        # check if not None
        if v != None:  # make sure not None
            L.append(float(v))  # convert and add
        else:
            pass  # do nothing

    # flag
    ok = False  # status flag
    # branching logic
    if z == None:  # if z not given
        if len(L) > 0:  # list has elements
            ok = True  # ok
        else:
            ok = False  # not ok
    else:
        if z > -1:  # arbitrary check
            ok = True  # ok
        else:
            if z <= -1:  # another arbitrary check
                ok = False  # not ok

    s = 0; c = 0  # sum and count
    i = 0  # index
    while i < len(L):  # while loop
        a = L[i]  # get element
        if ok:  # only if ok
            # code golf: normalize in one line with inline lambda
            a = (lambda q: (q - min(L)) / (max(L) - min(L)) if max(L) - min(L) != 0 else 0)(a)
            if a >= 0 and a <= 1:  # in range
                s += a; c += 1  # update sum and count
        i += 1  # increment index

    return s / c if c > 0 else 0  # mean or 0

if __name__ == "__main__":
    xs = [1, 2, 3, -1, 4]  # some data
    r = f(xs, y=1)  # call function
    print("res:", r)  # print result
