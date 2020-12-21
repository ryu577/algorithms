import numpy as np

# https://wbd.ms/share/v2/aHR0cHM6Ly93aGl0ZWJvYXJkLm1pY3Jvc29mdC5jb20vYXBpL3YxLjAvd2hpdGVib2FyZHMvcmVkZWVtLzA2YjJmZTQ0YWJkYTQ1ZjNiM2NkMTI0OWZmMjExYmY3X0JCQTcxNzYyLTEyRTAtNDJFMS1CMzI0LTVCMTMxRjQyNEUzRA==
def opt_mult(a):
    # The number of matrices
    n = len(a)-1
    m = np.zeros((n,n+1))
    for d_i in range(2,n+1):
        for p in range(n):
            q=p+d_i
            if q>n:
                break
            minn = np.inf
            for i in range(p+1,q):
                minn=min(minn,m[p,i]+m[i,q]+a[p]*a[i]*a[q])
            m[p,q] = minn
    return int(m[0,n])


if __name__=="__main__":
    a = np.arange(4)+2
    res = opt_mult(a)
    print(res)
    a = [30,35,15,5,10,20,25]
    res=opt_mult(a)
    print(res)

