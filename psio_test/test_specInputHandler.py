# Copyright (C) 2017  Christoph Rosemann, DESY, Notkestr. 85, D-22607 Hamburg
# email contact: christoph.rosemann@desy.de
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation in version 2
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

'''This is the test for the h5py input module.'''

import unittest
from psio import specInputHandler


class TestspecInputHandler(unittest.TestCase):

    def setUp(self):
        self.dataHandle = specInputHandler.SpecInputHandler()
        self.files = ["psio_test/test_data/spec/MnCo15.spc", ]

    def test_emptyConstructor(self):
        pass

    def test_getAll(self):
        pass

    def test_getEntry(self):
        pass

    def test_getNofEntries(self):
        pass

if __name__ == '__main__':
    unittest.main()
