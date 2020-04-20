# 1.We have create a new test case by creating class TestBuiltins which inherits unittest.TestCase. (Inheritance will be explained in further modules)
# 2.The test case contains three separate tests -def test_* functions.
# 3.Test function names have to start with test
# 4.Each of the functions invokes at least one self.assert*function
# 5.The test case and its functions are discovered by unittest when the script is started

#unitestuose svarbiausias dalykas, tai tu testu nepriklausomumas tarpusavyje

import unittest


class TestBuiltins(unittest.TestCase):   #paveldi unittest.TestCase klase (kolkas reikia tai atsiminti)
    def test_membership(self):
        self.assertIn("A", "Andalusia")
        self.assertTrue("A" in "Andalusia")

    def test_instances(self):   #del zodzio test atskiria kur yra testavimui skirta funkcija
        self.assertIsInstance(5, int)
        self.assertTrue(isinstance(5, int))

    def test_falsehood(self):
        self.assertFalse(False)


if __name__ == "__main__":
    unittest.main()
