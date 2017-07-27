# Copyright (C) 2017  Christoph Rosemann, DESY, Notkestr. 85, D-22607 Hamburg
# email contact: christoph.rosemann@desy.de
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation in  version 2
# of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA  02110-1301, USA.


'''This is purely a test package for the psio libary.'''

import unittest

# still to write: include all test cases into a test suite
import test_dataHandler
import test_fabioInputHandler
import test_h5InputHandler
import test_hdf5Output
import test_inputHandlerFactory



def run():
    # initialize the test suite
    loader = unittest.TestLoader()
    suite  = unittest.TestSuite()

    # add tests to the test suite
    suite.addTests(loader.loadTestsFromModule(test_dataHandler))
    suite.addTests(loader.loadTestsFromModule(test_fabioInputHandler))
    suite.addTests(loader.loadTestsFromModule(test_h5InputHandler))
    suite.addTests(loader.loadTestsFromModule(test_hdf5Output))
    suite.addTests(loader.loadTestsFromModule(test_inputHandlerFactory))

    # initialize a runner, pass it your suite and run it
    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)

def run_tests():
    run()
