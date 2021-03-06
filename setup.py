﻿from distutils.core import setup

from Cython.Build import cythonize
import numpy

setup(name='cshogi',
      ext_modules=cythonize("cshogi.pyx"),
      include_dirs = [numpy.get_include()])
