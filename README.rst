psio_test exists only to allow unit and package testing for PSIO.

It is much larger in size due to the presence of test data, which is two orders of magnitude larger than the io library on its own.

To run the tests obviously psio must be installed, then the commands

psio_test.run() or psio_test.run_tests()

will execute the tests and show a report.
