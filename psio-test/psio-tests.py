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


class dataHandlerTest(unittest.TestCase):
    pass

class inputHandlerFactoryTest(unittest.TestCase):
    pass

class fabioInputHandlerTest(unittest.TestCase):
    pass

class h5InputHandlerTest(unittest.TestCase):
    pass

class hdf5OutputTest(unittest.TestCase):
    pass



    print("Running a simple test of functionality.")
    print("Requires test data to be available.\n")

    files = [
        "test/test_data/hamamatsu_c4880_maxim/c_02.tif",
        "test/test_data/hamamatsu_c4880_maxim/im_cont2_038.tif"]

    files2 = [
        "test/test_data/lambda750ksi/Calli_align_00004.ndf"]

    path = "/entry/instrument/detector/data"

    dh = DataHandler()
    ndg = DataHandler()

    k = dh.create_reader(files)
    for f in k:
        print ("reading a tif file")

    k2 = ndg.create_reader(files2, path)
    for j in k2:
        print("reading a nexus file")

    print("\n show some data from the tif file reading:")
    dh2 = DataHandler([
        "test/test_data/hamamatsu_c4880_maxim/c_02.tif",
        "test/test_data/hamamatsu_c4880_maxim/im_cont2_038.tif"])
    for j in dh2:
        print(j)

    print("\n show some data from the nexus file reading:")
    dh3 = DataHandler("test/test_data/lambda750ksi/Calli_align_00004.ndf",
                      path="/entry/instrument/detector/data")
    for i in dh3:
        print(i)

    print("Do simple testing by running as a script.")
    print("Requires the test data to be present.\n")

    print("Trying to read different file formats and print its contents:")
    files = ["test/test_data/pilatus1m/calib_agbeh_andre_00001_00001.cbf",
             "test/test_data/hamamatsu_c4880_maxim/c_02.tif",
             "test/test_data/hamamatsu_c4880_maxim/im_cont2_038.tif"]

    io = FabioInputHandler()
    io.inputList(files)
    for i in io:
        print(repr(i))

    print("Needs test data to be present.\n")

    files = ["test/test_data/lambda750ksi/Calli_align_00004.ndf"]
    path = "/entry/instrument/detector/data"

    io = H5InputHandler()
    io.inputList(files, path, None)
    print("Data has been read and is:")
    print(repr(io.getEntry(0)))

    print("Testing the output capabilities.")

    no = HDF5Output("test.h5", mode='w')
    no.addDataField("test", (0, 2, 2))
    no.addDataField("test2", (2, 2))
    no.addCommentToField("test", "com2", "we dont need no")
    no.addAttributeToField("test2", "answer", 42.)

    no.close()
    print("In case of success a new file called test.h5 should have been created.")
try:
    import h5py
except ImportError("h5py is not installed. Please install for full functionality in reading hdf5 data files."):
    pass

try:
    import six
except ImportError("six is not installed. The package will probably not work without it."):
    pass

try:
    import fabio
except ImportError("fabio is not installed. Several file types will not be supported."):
    pass

try:
    import numpy
except ImportError("numpy is not installed. The package will not work without it."):
    pass

try:
    import pyqtgraph
except ImportError("pyqtgraph is not installed. No display will be available."):
    pass

from .dataHandler import DataHandler
from .hdf5Output import HDF5Output
