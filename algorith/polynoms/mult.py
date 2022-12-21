

def polynom_mult(a, b):
	"""
	Multiplies two polynomials given in coefficient form.
	The input arrays a and b represent the coefficients.
	"""
	# The output polynomial initialized to
	# an array of zeros.
	c = [0]*(len(a)+len(b)-1)
	
	# This double loop is the distributive law
	# of multiplication.
	# Every combination of elements of the two
	# arrays get multiplied.
	for i in range(len(b)):
		for j in range(len(a)):
			c[i+j] += a[i]*b[j]
	return c
