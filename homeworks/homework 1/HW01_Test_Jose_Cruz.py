"""HW01: Testing triangle classification

   Author: Jose J. Cruz
   CWID: 10467076
"""
import unittest
from HW01_Jose_Cruz import is_equilateral, is_isosceles, classify_triangle, \
    is_right


class TriangleTest(unittest.TestCase):
    """Test suite for Triangles function"""

    def test_is_equilateral(self) -> None:
        """Test if the triangle es equilateral"""
        self.assertEqual(is_equilateral(2, 2, 2), True)
        self.assertEqual(is_equilateral(2, 2, 1), False)
        self.assertRaises(TypeError, is_equilateral, 1, 'a', True)
        self.assertRaises(Exception, is_equilateral, 1, 1)
        self.assertRaises(ValueError, is_equilateral, 1, 1, -2)

    def test_is_isosceles(self) -> None:
        """Test if the triangle is isosceles"""
        self.assertEqual(is_isosceles(2, 3, 1), False)
        self.assertEqual(is_isosceles(2, 3, 2), True)
        self.assertRaises(TypeError, is_isosceles, 1, 'a', True)
        self.assertRaises(Exception, is_isosceles, 1, 1)
        self.assertRaises(ValueError, is_isosceles, 1, 1, -2)

    def test_is_right(self) -> None:
        """Test if the triangle is right"""
        self.assertEqual(is_right(2, 3, 1), False)
        self.assertEqual(is_right(3, 4, 5), True)
        self.assertRaises(TypeError, is_right, 1, 'a', True)
        self.assertRaises(Exception, is_right, 1, 1)
        self.assertRaises(ValueError, is_right, 1, 1, -2)

    def test_classify_triangle(self) -> None:
        """Test if can return the correct type of triangle"""
        self.assertEqual(classify_triangle(1, 1, 1), 'equilateral')
        self.assertEqual(classify_triangle(2, 3, 2), 'isosceles')
        self.assertEqual(classify_triangle(3, 4, 5), 'right')
        self.assertEqual(classify_triangle(1, 2, 3), 'scalene')
        self.assertRaises(TypeError, classify_triangle, 1, 'a', True)
        self.assertRaises(Exception, classify_triangle, 1, 1)
        self.assertRaises(ValueError, classify_triangle, 1, 1, -3)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
