import unittest
import os
def createsuite():
    test_dir=os.path.abspath('./test_case')
    suite=unittest.defaultTestLoader.discover(test_dir, 'test*.py')
    return suite
if __name__=='__main__':
    runner=unittest.TextTestRunner()
    runner.run(createsuite())