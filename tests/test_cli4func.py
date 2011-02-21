import unittest                         
from abandi import cli4func

class BugFixes(unittest.TestCase):
##    def setUp(self):
##    def tearDown(self):

    def test_main(self):        
        def f(): 
            pass            
        cli4func.main(f)

    def test_no_args(self):        
        def f(): 
            pass            
        cli4func.extractInfo(f)

    def test_no_default_args(self):        
        def f(x, y): 
            pass            
        cli4func.extractInfo(f)

    def test_no_doc(self):        
        def f(x, y=4): 
            pass            
        result = cli4func.extractInfo(f)
        self.assertEqual(result[1], '')
        
    def test_doc(self):        
        def f(x, y=4): 
            '''blabla'''
            pass            
        result = cli4func.extractInfo(f)
        self.assertEqual(result[1], 'blabla')
        
if __name__ == '__main__':      
    unittest.main()
