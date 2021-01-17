
def perm(t,i,n):
    """
    Based on procedure "perm" in ch6 of Giles and Bassard.
    """
    if i==n:
        print(t)
    else:
        for j in range(i,n+1):
            swap(t,i,j)
            perm(t,i+1,n)
            swap(t,i,j)


def perm2(a,ix):
    """
    My own version of perm.
    """
    if ix==len(a):
        print(a)
    else:
        for j in range(ix+1):
            swap(a,j,ix)
            perm2(a,ix+1)
            swap(a,j,ix)


def swap(a,i,j):
    if i<0 or j>len(a)-1:
        return
    tmp=a[j]
    a[j]=a[i]
    a[i]=tmp


if __name__=="__main__":
    t=[1,2,3]
    #perm(t,0,len(t)-1)
    perm2(t,0)

