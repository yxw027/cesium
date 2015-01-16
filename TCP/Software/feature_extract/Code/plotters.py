from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from builtins import *
try:
    from pylab import *
except:
    pass
from numpy import *
import numpy


class plotter(object):
    def plots(self,properties,what = 'data'):
        if what =='data':
            plot(properties['time_data'],properties['flux_data'],marker='d',label='signal data')
        elif what =='real':
            plot(properties['time_data'],properties['clean_flux_data'],label='clean data from generator',marker='o')
        elif what =='dc_real':
            dc_line = ones(len(properties['time_data']),dtype=float)
            dc_line[:] = properties['dc_real']
            plot(properties['time_data'],dc_line,label='real dc from generator')
        else:
#                       try:
            from . import feature_interfaces
            extractor = feature_interfaces.extractor_fetch(what)
            if what in properties:
                pass
            else:
                print(what,'not available')
                return None
            extractor.plots(properties)
#                       except KeyError:
#                               print "can't plot", what
