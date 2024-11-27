import unittest
from Task1 import singlets

class Task1Tests (unittest.TestCase):
    #Right tests 
    def right_test(self):
/*************  ✨ Codeium Command ⭐  *************/
        """
        Test that the function runs without errors when given the correct input data
        """
/******  8be3c88a-d3c7-4f64-a0a8-a1fdf62071e1  *******/
        pass 
    
    #Wrong input data 
    def wrong_data_input(self):
        with self.assertRaises(TypeError):
            singlets([],null)
    # the length of the string is less than k 
    def string_less_than_k (self):
        with self.assertionRaises(ValueError):
            singlets("one two three",5)
    