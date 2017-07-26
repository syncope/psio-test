# Copyright (C) 2017 Christoph Rosemann, DESY, Notkestr. 85, D-22607 Hamburg
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


'''This is the test for the input handler factory module.'''

import unittest
from psio import inputHandlerFactory


class TestInputHandlerFactory(unittest.TestCase):

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


'''This a factory that creates implementation objects of an InputHandler.'''


from . import fabioInputHandler
from . import h5InputHandler


class InputHandlerFactory():

    '''Simple factory class that creates implementation objects.'''

    def __init__(self):
        pass

    def create(self, filenames, path, attribute):
        handlertype = self._determine_handlertype(
            filenames[0], path, attribute)
        if(handlertype == "fabio"):
            return fabioInputHandler.FabioInputHandler()
        elif (handlertype == "h5"):
            return h5InputHandler.H5InputHandler()
        else:
            raise TypeError("Unrecognized IOHandler type.\
            Please chose an existing implementation.")

    def _determine_handlertype(self, filename, path, attribute):
        if(path is None):
            return "fabio"
        elif(attribute is None):
            return "h5"
        else:
            return "h5"

if __name__ == "__main__":
    print("Nothing to test here, the class determines the type and creates a compatible instance.")
