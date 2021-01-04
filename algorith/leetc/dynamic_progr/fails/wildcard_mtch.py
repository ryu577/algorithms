import numpy as np

#####################Failed attempt!!######
def mu(s,p,i,j):
    if i==-1:
        if j==-1:
            return True
        for ix in range(j+1):
            if p[ix] !="*":
                return False
        return True
    if j==0:
        if p[0]=="*":
            return True
        elif p[0]=="?":
            if i==0:
                return True
            else:
                return False
        else:
            if i==0 and s[0]==p[0]:
                return True
            else:
                return False
    if p[j]=='*':
        for kk in range(i):
            if mu(s,p,kk,j-1):
                return True
        return False
    elif p[j] == '?':
        return mu(s,p,i-1,j-1)
    else:
        return mu(s,p,i-1,j-1) and (s[i]==p[j])


def memoized_mu_strt(s,p):
    arr = np.ones((len(s),len(p)))*-1
    return memoized_mu(s,p,len(s)-1,len(p)-1,arr)

def memoized_mu(s,p,i,j,arr):
    if arr[i,j]!=-1:
        return bool(arr[i,j])
    if j==0:
        if p[0]=="*":
            arr[i,j] = 1
            return True
        elif p[0]=="?":
            if i==0:
                arr[i,j] = 1
                return True
            else:
                arr[i,j]=0
                return False
        else:
            if i==0 and s[0]==p[0]:
                arr[i,j]=1
                return True
            else:
                arr[i,j]=0
                return False
    if p[j]=='*':
        for kk in range(i+1):
            if memoized_mu(s,p,kk,j-1,arr):
                arr[i,j]=1
                return True
            arr[i,j]=0
            return False
    elif p[j] == '?':
        arr[i,j] = memoized_mu(s,p,i-1,j-1,arr)
        return bool(arr[i,j])
    else:
        arr[i,j] = memoized_mu(s,p,i-1,j-1,arr) and (s[i]==p[j])
        return bool(arr[i,j])

## https://leetcode.com/problems/wildcard-matching/discuss/995627/Python-easiest-Top-Down-DP-Soln
def mu_v2(s,p,i,j):
    ans=0
    if i==0 and j==0:
        return 1
    elif i==0 or j==0:
        if p[j] == "*":
            ans = mu_v2(s,p,i,j-1)
        else:
            ans=0
    elif s[i]==p[j] or p[j]=="?":
        ans = mu_v2(s,p,i-1,j-1)
    elif p[j]=="*":
        ans=mu_v2(s,p,i-1,j) or mu_v2(s,p,i,j-1)
    return ans


def mu_v2_strt(s,p):
    ## Doubt: why do we need to pad?
    s="_"+s
    p="_"+p
    return mu_v2(s,p,len(s)-1,len(p)-1)


if __name__=="__main__":
    s = 'abdcub'
    p = 'a*c?b'
    res = mu_v2_strt(s,p)
    print(res==1)
    s1 = 'abdcb'
    p = 'a*c?b'
    res = mu_v2_strt(s1,p)
    print(res==0)
    s = "aab"
    p = "c*a*b"
    res = mu_v2_strt(s,p)
    print(res==0)
    s=""
    p="******"
    res = mu_v2_strt(s,p)
    print(res==1)
    s="adceb"
    p="*a*b"
    res = mu_v2_strt(s,p)
    print(res==1)
    s="abcabczzzde"
    p="*abc???de*"
    res = mu_v2_strt(s,p)
    print(res==1)


def tst_old():
    s = 'abdcub'
    p = 'a*c?b'
    res = mu(s,p,len(s)-1,len(p)-1)
    print(res)
    s1 = 'abdcb'
    p = 'a*c?b'
    res = mu(s1,p,len(s1)-1,len(p)-1)
    print(res)
    res = memoized_mu_strt(s,p)
    print(res)
    res = memoized_mu_strt(s1,p)
    print(res)
    s = "aab"
    p = "c*a*b"
    res = memoized_mu_strt(s,p)
    print(res)
    res = mu(s,p,len(s)-1,len(p)-1)
    print(res)
    s=""
    p="******"
    res = mu(s,p,len(s)-1,len(p)-1)
    print(res)
    s="adceb"
    p="*a*b"
    res = mu(s,p,len(s)-1,len(p)-1)
    print(res)
    s="abcabczzzde"
    p="*abc???de*"
    res = mu(s,p,len(s)-1,len(p)-1)
    print(res)

