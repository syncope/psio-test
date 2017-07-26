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

'''This is the test for the outputBase module.'''

import unittest
from psio import outputBase


class TestOutputBase(unittest.TestCase):

    def setUp(self):
        self.ih1 = h5InputHandler.H5InputHandler()
        self.ih2 = h5InputHandler.H5InputHandler()
        self.ih3 = h5InputHandler.H5InputHandler()

    def test_constructor(self):
        self.assertIsNone(self.ih1._fileList)
        self.assertIsNone(self.ih1._fileIter)
        self.assertIsNone(self.ih1._field)
        self.assertIsNone(self.ih1._dataIter)
        self.assertIsNone(self.ih1._nentries)
        self.assertIsNone(self.ih1._attribute)
        self.assertFalse(self.ih1._singleValue)
        self.assertIsNone(self.ih1._currentFile)
        self.assertEqual(self.ih1._dataDimension, 2)

    def test_listInput(self):
        pass

    def test_setDimension(self):
        pass

    def test_nextFile(self):
        pass

    def test_nofEntries(self):
        pass



'''Base class for output. Functionality implemented by children classes.'''


class OutputBase():
    def write(self):
        pass

    def close(self):
        pass

    def addDataField(self, name, dimension, dtype="float32"):
        pass

    def addAttributeToField(self, fieldname, title, value):
        pass

    def addCommentToField(self, fieldname, title, comment):
        pass


if __name__ == "__main__":
    print("Nothing to do here, class is just an interface definition.")
