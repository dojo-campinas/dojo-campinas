import unittest
from fizzbuzz import fizzbuzz

class FizzBuzzTestCase(unittest.TestCase):

    def test_se_entra_um_sai_um(self):
        self.assertEqual(fizzbuzz(1), [1])

    def test_entra_dois_sai_um_dois(self):
        self.assertEqual(fizzbuzz(2), [1, 2])

    def test_entra_multiplo_de_tres(self):
        self.assertEqual(fizzbuzz(3), [1,2,"Fizz"])
        self.assertEqual(fizzbuzz(6), [1,2,"Fizz",4,"Buzz","Fizz"])

    def test_entra_multiplo_de_cinco(self):
        self.assertEqual(fizzbuzz(5),  [1,2,"Fizz",4,"Buzz"])
        self.assertEqual(fizzbuzz(10), [1,2,"Fizz",4,"Buzz","Fizz",7,8,"Fizz","Buzz"])
        self.assertEqual(fizzbuzz(15),[1,2,"Fizz",4,"Buzz","Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"])
        self.assertEqual(fizzbuzz(20),[1,2,"Fizz",4,"Buzz","Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz"])

if __name__ == '__main__':
    unittest.main()
