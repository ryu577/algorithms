import numpy as np

def mu(s,p,i,j):
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
    elif p[j] == '?':
        return mu(s,p,i-1,j-1)
    else:
        return mu(s,p,i-1,j-1) and (s[i]==p[j])




if __name__=="__main__":
    s = 'abdcub'
    p = 'a*c?b'
    res = mu(s,p,len(s)-1,len(p)-1)
    print(res)
    s = 'abdcb'
    p = 'a*c?b'
    res = mu(s,p,len(s)-1,len(p)-1)
    print(res)
