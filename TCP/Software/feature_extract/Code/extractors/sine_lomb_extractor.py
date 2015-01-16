from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from builtins import *
from ..FeatureExtractor import InterExtractor

from .sine_leastsq_extractor import sine_leastsq_extractor

class sine_lomb_extractor(sine_leastsq_extractor):
    """Fits a sine wave using the lomb result as an estimate """
    active = False
    extname = 'sine_lomb' #extractor's name
    def frequency_estimate(self):
        freq = self.fetch_extr('first_lomb') #2*numpy.pi/20
        return freq
