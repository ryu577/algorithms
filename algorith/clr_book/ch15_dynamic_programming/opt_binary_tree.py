import numpy as np


## Per fig 15.9, q is 0 indexed while p is 1 indexed.
# This is why 1 will be subtracted from p's indices 
# but not q's. 
def opt_bst_recurse(p,q,i,j):
    w=0
    for l in range(i,j+1):
        w+=p[l-1]#p[l] if p were 1 indexed.
    for l in range(i-1,j+1):
        w+=q[l]
    if j==i-1:
        return q[i-1]
    else:
        minn = np.inf
        for r in range(i,j+1):
            trm = opt_bst_recurse(p,q,i,r-1)+\
                opt_bst_recurse(p,q,r+1,j)+w
            if trm<minn:
                minn=trm
        return minn


def opt_bst_top_dwn_strt(p,q):
    n=len(p)
    ## e is 1 to n+1, 0 to n.
    e = np.ones((n+2,n+1))*np.inf
    w = np.ones((n+2,n+1))*np.inf
    return opt_bst_top_dwn(p,q,1,len(p),e,w)

def opt_bst_top_dwn(p,q,i,j,e,w):
    return 1

if __name__=="__main__":
    p=np.array([.15,.1,.05,.1,.2])
    q=np.array([.05,.1,.05,.05,.05,.1])
    res = opt_bst_recurse(p,q,1,len(p))
    print(res)

