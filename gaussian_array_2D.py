"""
Functions used:
numpy.meshgrid()– It is used to create a rectangular grid out of two given one-dimensional arrays representing the Cartesian indexing or Matrix indexing. 
Syntax:

numpy.meshgrid(*xi, copy=True, sparse=False, indexing=’xy’)

---------------------------------------------------------------------------------------


numpy.linspace()– returns number spaces evenly w.r.t interval.
Syntax:

numpy.linspace(start, stop, num = 50, endpoint = True, retstep = False, dtype = None) 

---------------------------------------------------------------------------------------

numpy.exp()– this mathematical function helps the user to calculate the exponential of all the elements in the input array.
Syntax:

numpy.exp(array, out = None, where = True, casting = ‘same_kind’, order = ‘K’, dtype = None)
 
---------------------------------------------------------------------------------------
"""
import numpy as np
print(
    "------------------------------------------------------------------------------")


def gaussian_filter(kernel_size, sigma=1, muu=0):
    x, y = np.meshgrid(np.linspace(-1, 1, kernel_size),
                       np.linspace(-1, 1, kernel_size))
    dst = np.sqrt(x**2+y**2)

    normal = 1/(2.0*np.pi*sigma**2)

    gauss = np.exp(-((dst-muu)**2 / (2.0 * sigma**2))) * normal
    return gauss


kernel_size = 5
gaussian = gaussian_filter(kernel_size)
print("gaussian filter of {} X {} :".format(kernel_size, kernel_size))
print(gaussian)
print("------------------------------------------------------------------------------")


kernel_size = 3
gaussian = gaussian_filter(kernel_size)
print("gaussian filter of {} X {} :".format(kernel_size, kernel_size))
print(gaussian)
print("------------------------------------------------------------------------------")
