import math 
import numpy as np


def fft_2(x):
	"""
	Perform a fast Fourier transform
	on the given array of complex numbers.
	""" 
	n = len(x)
	if n == 1: 
		return x
	# The complex roots of unity.
	omega_n = np.exp(1j*2*np.pi/n)
	omega = 1+0j
	# Extact the even indices from array.
	even = fft_2(x[::2]) 
	# Extract the odd indices from array.
	odd = fft_2(x[1::2]) 
	# The result array.
	y = [0]*n
	# The step that merges the two inputs into the
	# final answer. This step takes O(n) time since
	# it is just a single loop.
	for k in range(n//2):
		y[k] = even[k]+omega*odd[k]
		y[k+n//2] = even[k]-omega*odd[k]
		omega = omega*omega_n
	
	return y


def fft_3(x):
	"""
	Perform a fast Fourier transform
	on the given array of complex numbers.
	""" 
	n = len(x)
	if n == 1:
		return x
	# The complex roots of unity.
	omega_n = np.exp(1j*2*np.pi/n)
	omega = 1+0j
	# Extact the even indices from array.
	y_0 = fft_3(x[::3])
	# Extract the odd indices from array.
	y_1 = fft_3(x[1::3])
	y_2 = fft_3(x[2::3])
	# The result array.
	y = [0]*n
	# The step that merges the two inputs into the
	# final answer. This step takes O(n) time since
	# it is just a single loop.
	for k in range(n//3):
		y[k] = y_0[k]+omega*y_1[k]+omega**2*y_2[k]
		y[k+n//3] = \
			y_0[k]+np.exp(2*np.pi*1j/3)*omega*y_1[k]+\
			np.exp(4*np.pi*1j/3)*omega**2*y_2[k]
		y[k+(2*n)//3] = \
			y_0[k]+np.exp(4*np.pi*1j/3)*omega*y_1[k]+\
			np.exp(2*np.pi*1j/3)*omega**2*y_2[k]
		omega = omega*omega_n
	
	return y

