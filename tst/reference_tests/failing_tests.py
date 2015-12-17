import unittest
from unittest import TestCase

class TC(TestCase):

    @unittest.expectedFailure
    def test01_a_test_that_fails(self):
        self.fail('This test fails, deal with it!')

