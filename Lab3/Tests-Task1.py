import unittest
from Task1 import singlets

class Task1Tests (unittest.TestCase):
    #Right tests 
    def right_test(self):
        pass 
    
    #Wrong input data 
    def wrong_data_input(self):
        with self.assertRaises(TypeError):
            singlets([],null)
    # the length of the string is less than k 
    def string_less_than_k (self):
        with self.assertionRaises(ValueError):
            singlets("one two three",5)
    