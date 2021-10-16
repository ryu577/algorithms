# See Remarkable/Topics/Finance/Loan/Pg1

# Excel formula: =PMT(0.01,10,1000)
def pmt(r, t, a):
    rr = (1+r)**t
    return a*r*rr/(rr-1)


def interest_paid(r, t, a):
    u = pmt(r, t, a)
    return (a*r-u)*((1+r)**t-1)/r+u*t


def principal_so_far(r, t, a, t1):
    u = pmt(r, t, a)
    return (u-a*r)/r*((1+r)**t1-1)
