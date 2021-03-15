from algorith.utils.math.ncr import ncr
import numpy as np


link = ("https://math.stackexchange.com/questions/3990877\
       /fast-method-to-\
       convert-catalan-path-to-lexicographic\
       -position/3992082#3992082")


def n_catalan(k, t):
    if t < 0:
        return 0
    elif t == 0:
        return 1
    else:
        return abs(ncr(k+2*t-1, t) - ncr(k+2*t-1, t-1))


def n_catalan2(h, t):
    if t < 0:
        return 0
    elif t == 0:
        return 1
    else:
        return abs(ncr(h+t-1, t) - ncr(h+t-1, t-1))


def path_to_ix(path, k, t):
    """
    path is an array of positions where we got heads.
    TODO: Needs to be fixed. Currently produces wrong
    results for t=4, h=3.
    """
    total_tosses = (k+2*t)
    total_heads = len(path)
    ix = 0
    for i in range(len(path)):
        tosses_left = total_tosses-path[i]
        heads_left = total_heads-i
        tails_left = tosses_left-heads_left
        k = heads_left-tails_left
        ix += n_catalan(k+1, tails_left-1)
    return ix


def ix_to_path(ix, h, t):
    """
    Given an index, returns the Dyck path.
    args:
        ix: The index to be converted.
        t: The number of tails in the path.
        h: The number of heads in the path.
    """
    v = ix
    path = np.zeros(t + h)
    for i in range(t+h):
        tail_paths = n_catalan2(h, t-1)
        if v >= tail_paths:
            path[i] = 1
            h -= 1
            v -= tail_paths
            if h == 0:
                break
        else:
            t -= 1
    return path


if __name__ == "__main__":
    path = ix_to_path(3, 3, 4)
    print(path)
    ix = path_to_ix([3, 4, 5, 6, 7], 2, 3)
    print(ix)
    ix = path_to_ix([1, 4, 5, 6, 7], 2, 3)
    print(ix)
    ix = path_to_ix([1, 3, 5, 6, 7], 2, 3)
