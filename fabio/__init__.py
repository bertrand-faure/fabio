# coding: utf-8
#
#    Project: X-ray image reader
#             https://github.com/silx-kit/fabio
#
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France
#
#    Principal author:       Jérôme Kieffer (Jerome.Kieffer@ESRF.eu)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import absolute_import, print_function, division

__doc__ = """FabIO module"""
__author__ = "Jérôme Kieffer"
__contact__ = "Jerome.Kieffer@ESRF.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "24/07/2017"
__status__ = "stable"


import sys
import logging

if "ps1" in dir(sys):
    # configure logging with interactive console
    logging.basicConfig()

import os
project = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
try:
    from ._version import __date__ as date  # noqa
    from ._version import version, version_info, hexversion, strictversion  # noqa
except ImportError:
    raise RuntimeError("Do NOT use %s from its sources: build it and use the built version" % project)

from . import fabioimage
factory = fabioimage.FabioImage.factory
from . import openimage
from .fabioutils import COMPRESSORS, jump_filename, FilenameObject, \
        previous_filename, next_filename, deconstruct_filename, \
        extract_filenumber, getnum, construct_filename, exists

# Compatibility with outside world:
filename_object = FilenameObject

from .openimage import openimage as open
from .openimage import openheader as openheader


def tests():
    """
    Run the FabIO test suite.

    If the test-images are not already installed (via the debian package for example),
    they need to be downloaded from sourceforge.net, which make take a while.
    Ensure your network connection is operational and your proxy settings are correct,
    for example:

    export http_proxy=http://proxy.site.com:3128
    """
    from . import test
    test.run_tests()


def benchmarks():
    """
    Run the benchmarks
    """
    from . import benchmark
    res = benchmark.run()
    return res
