#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInt(unittest.TestCase):
    """unittest class for max_integer()"""
    def test_docstring(self):
        """Tests for documentation"""
        self.assertTrue(len(__import__('6-max_integer').__doc__) > 0)
        self.assertTrue(len(max_integer.__doc__) > 0)

    def test_pos_int(self):
        """test for list of all positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([3, 2, 1, 0]), 3)
        self.assertEqual(max_integer([3, 2, 14, 1, 0]), 14)
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([1]), 1)

    def test_neg_int(self):
        """test for list of all negative integers"""
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, 1]), 1)
        self.assertEqual(max_integer([-3, 2, 14, 1, 0]), 3)
        self.assertEqual(max_integer([-1, -4]), -1)
        self.assertEqual(max_integer([-4]), -4)

    def test_nested_list(self):
        """test for list of list of all positive integers"""
        self.assertEqual(max_integer([[14, 14], [1, 1], [-420, 420]]), [14, 14])

    def test_not_int(self):
        """test for list of differnt data type except integers"""
        with self.assertRaises(TypeError):
            max_integer([14, 'Naruto', 420])
        with self.assertRaises(TypeError):
            max_integer((14, 'Naruto', 420))
        with self.assertRaises(TypeError):
            max_integer([[14, 14], (1, 1), 420])
        
    def test_dif_num_of_arg(self):
        """test for passing != one argument"""
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3], [1])

    def test_possible_syntax_err(self):
        """test for incorrect syntax that won't raise SyntaxError"""
        self.assertEqual(max_integer([-11, -2, -3, -4, -0]), 0)
        self.assertEqual(max_integer([+11, -2, -3, -4, -0]), 11)

if __name__ == '__main__':
    unittest.main()
