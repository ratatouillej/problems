# This problem is from TopCoder. The original link can be found at
# http://community.topcoder.com/stat?c=problem_statement&pm=12950&rd=15838


# input: str, the original string
# output: int, the number of possible passwords by removing one character from input
def alien_password(input):
    pass
    
    
#### Test code below. ####
import unittest


class TestAlienPassword(unittest.TestCase):
    def test_alien_password(self):
        # Should pass all cases below
        self.assertEqual(1, alien_password('A'))
        self.assertEqual(3, alien_password('ABA'))
        self.assertEqual(7, alien_password('AABACCCCABAA'))
        self.assertEqual(26, alien_password('AGAAGAHHHHFTQLLAPUURQQRRRUFJJSBSZVJZZZ'))
        self.assertEqual(1, alien_password('ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ'))
        # Add your own test cases below
        
        
if __name__ == '__main__':
    unittest.main()
