
def binary_search(a, d, lo, hi, asc_order=True):
    while lo < hi:
        mid = (lo+hi)//2
        midval = a[mid]
        if midval < d:
            if asc_order:
                lo = mid+1
            else:
                hi = mid-1
        elif midval > d:
            if asc_order:
                hi = mid-1
            else:
                lo = mid+1
        else:
            return mid
    if a[lo]<=d:
        return lo
    else:
        return int(lo-(asc_order-0.5)*2)


def tst():
    re = binary_search([1,2,3,4,5],2.6,0,4)
    print("Test-1: "+str(re==1))


