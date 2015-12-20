import unittest
from unittest import TestCase

try:
    import fictitious_module
except ImportError:
    fictitious_module = None

class TC(TestCase):

    @unittest.skip('This test is always skipped (ignored)')
    def test01_a_test_that_is_ignored(self):
        self.fail('This test is ignored (skipped) - does not fail!')    # ignore during coverage check

    @unittest.skipIf(fictitious_module is None, 'This test is skipped because fictitious module is not imported')
    def test02_a_test_that_is_conditionally_ignored(self):
        self.fail('This test is ignored (skipped) - does not fail!')    # ignore during coverage check


