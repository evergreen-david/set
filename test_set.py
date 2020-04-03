import unittest

import hashlib
import re

class MySet():

    def add(self,x):
        return x+1
    
    def hash_sha1(self, in_str):
        hs_value = hashlib.sha1(in_str.encode())
        print(hs_value.hexdigest())
        return hs_value.hexdigest()

    def hash_value(self, in_str):
        s = self.hash_sha1(in_str)
        num = re.findall('\d+',s)
        num = "".join(num)
        print("num=",end=""), print(int(num)%10)

        return num
    


class UnitTests(unittest.TestCase):

    def setUp(self):
        # Setup code
        self.myset = MySet()
        return 

    def tearDown(self):
        # TearDown
        return

    def add_func(x):
        return x+1

    def test_hash_sha1(self):
        #assert add_func(3) == 3
        #assert self.calculator.add(3) == 4
        
        #assert self.myset.hash_sha1('wecode') == '283463014a3f8ab829fcf9087ff85d50da1d1bb6'
        self.assertEqual(self.myset.hash_sha1('wecode'),'283463014a3f8ab829fcf9087ff85d50da1d1bb6' )

    def test_hash_value(self):

        self.myset.hash_value('wecode')


if __name__ == '__main__':
    unittest.main()

