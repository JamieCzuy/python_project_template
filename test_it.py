import sys
from unittest import defaultTestLoader as test_loader
from unittest import TextTestRunner

print('Testing it')
if (len(sys.argv) > 1):
    print('  with these args: ')
    for arg in sys.argv[1:]:
	    print('    %s' % arg)

test_suite = test_loader.discover('tst/', pattern='*tests.py')
test_runner = TextTestRunner(verbosity=2)
test_results = test_runner.run(test_suite)

