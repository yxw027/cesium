from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import *
from future import standard_library
standard_library.install_aliases()
#!/usr/bin/env python
import os, sys

exec_str = "./generate_weka_classifiers.py -u sh7.5 --n_noisified_per_orig_vosource=50 --n_epochs=8 --n_sources_needed_for_class_inclusion=100 --fit_metric_cutoff=0.05"
os.system(exec_str)

exec_str = "./generate_weka_classifiers.py -u sh7.5 --n_noisified_per_orig_vosource=50 --n_epochs=10 --n_sources_needed_for_class_inclusion=100 --fit_metric_cutoff=0.05"
os.system(exec_str)

exec_str = "./generate_weka_classifiers.py -u sh7.5 --n_noisified_per_orig_vosource=50 --n_epochs=12 --n_sources_needed_for_class_inclusion=100 --fit_metric_cutoff=0.05"
os.system(exec_str)

exec_str = "./generate_weka_classifiers.py -u sh7.5 --n_noisified_per_orig_vosource=50 --n_epochs=15 --n_sources_needed_for_class_inclusion=100 --fit_metric_cutoff=0.05"
os.system(exec_str)

exec_str = "./generate_weka_classifiers.py -u sh7.5 --n_noisified_per_orig_vosource=50 --n_epochs=20 --n_sources_needed_for_class_inclusion=100 --fit_metric_cutoff=0.05"
os.system(exec_str)
