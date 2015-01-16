from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from builtins import range
from future import standard_library
standard_library.install_aliases()
from builtins import *
from ..FeatureExtractor import FeatureExtractor

class max_slope_extractor(FeatureExtractor):
    active = True
    extname = 'max_slope' #extractor's name
    def extract(self):
        max_slope = 0
        max_slope_i = 0
        for i in range(len(self.time_data)-1):
            ydiff = self.flux_data[i+1]-self.flux_data[i]
            xdiff = self.time_data[i+1]-self.time_data[i]
            slope = ydiff / xdiff
            if abs(slope) > abs(max_slope):
                max_slope = slope
                max_slope_i = i
        return(max_slope_i)
