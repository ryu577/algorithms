
def perm(t,i,n):
    if i==n:
        print(t)
    else:
        for j in range(i,n+1):
            swap(t,i,j)
            perm(t,i+1,j)
            swap(t,i,j)

def swap(a,i,j):
    tmp=a[j]
    a[j]=a[i]
    a[i]=tmp

if __name__=="__main__":
    t=[1,2,3,4]
    perm(t,0,len(t)-1)

