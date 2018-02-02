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

'''This is the test for the dataHandler module.'''

import unittest
from psio import dataHandler


class TestDataHandler(unittest.TestCase):

    def setUp(self):
        self.dh = dataHandler.DataHandler()
        self.dhFAB = dataHandler.DataHandler(["psio_test/test_data/pilatus1m/calib_agbeh_andre_00001_00001.cbf",
                                              "psio_test/test_data/hamamatsu_c4880_maxim/c_02.tif",
                                              "psio_test/test_data/hamamatsu_c4880_maxim/im_cont2_038.tif"])
        self.dhH5 = dataHandler.DataHandler("psio_test/test_data/lambda750ksi/Calli_align_00004.ndf",path="entry/instrument/detector/data")
        self.dhSPC = dataHandler.DataHandler("psio_test/test_data/spec/MnCo15.spc", typehint="spec")

    def test_getters(self):
        self.assertEqual(self.dhH5.getTotalNumberOfEntries(), 1)
        self.assertEqual(self.dhFAB.getTotalNumberOfEntries(), 3)
        self.assertIsNotNone(self.dhH5.getEntry(0))
        with self.assertRaises(TypeError):
            self.dhFAB.getEntry(1)
        with self.assertRaises(IndexError):
            self.dhH5.getEntry(1)

    def test_Iteration(self):
        for d in self.dhFAB:
            pass
        for k in self.dhH5:
            pass
        for j in self.dhSPC:
            pass

    def tearDown(self):
        self.dhFAB = None
        self.dhH5 = None
        self.dhSPC = None
        self.dh = None

if __name__ == '__main__':
    unittest.main()
