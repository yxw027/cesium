from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import range
from future import standard_library
standard_library.install_aliases()
from builtins import *
import numpy
from numpy import random
from scipy import fftpack, stats, optimize
try:
    from pylab import *
except:
    pass

class Example_Methods(object): # Extractors which inherit this object can make use of these methods.
    def example_main_method(self,y,f,x=None,rms=None):
        """ Inputs:
        [y]-data    (array)
        [f]unction  (function)
        [x]-axis    (array)
        [rms] noise (array)
        """
        # Always initialize these in-case they aren't defined:
        if rms is None:
            rms = ones(len(y))
        if x is None:
            x = list(range(len(y)))

        # Do work here.  Call inherited methods if needed.
        # - NOTE: use numpy module for basic math/array tasks.

        # Return a scalar float:
        return sum(y)
