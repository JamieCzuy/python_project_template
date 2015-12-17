from unittest import TestCase

class TC(TestCase):

    # A Note about order:
    #     Tests are orders by file name then test (method) name
    #     Of course your tests should never rely on this ordering
    #     but it is nice to know for finding tests in the results.

    # Note: In results this will show up after test02_...
    def test03_a_third_test_that_passes(self):
        pass

    def test01_a_test_that_passes(self):
        pass

    def test02_a_second_test_that_passes(self):
        pass

