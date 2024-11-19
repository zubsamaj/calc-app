# Unit tests for C:\Users\T0245521\Downloads\newui\calc-app\updated_code.py

 
import unittest

def calculate_area_of_rectangle(width, height):
    # Calculate the area of a rectangle
    area = width * height
    return area

class TestCalculateAreaOfRectangle(unittest.TestCase):

    def test_normal_input(self):
        width = 5
        height = 10
        self.assertEqual(calculate_area_of_rectangle(width, height), 50)

    def test_edge_case_empty_input(self):
        with self.assertRaises(ValueError):
            calculate_area_of_rectangle(0, 0)

    def test_edge_case_negative_numbers(self):
        with self.assertRaises(ValueError):
            calculate_area_of_rectangle(-5, 10)
        with self.assertRaises(ValueError):
            calculate_area_of_rectangle(5, -10)

    def test_edge_case_zero_input(self):
        with self.assertRaises(ValueError):
            calculate_area_of_rectangle(0, 0)

    def test_edge_case_non_numeric_input(self):
        with self.assertRaises(TypeError):
            calculate_area_of_rectangle("five", 10)

    def test_edge_case_non_numeric_width(self):
        with self.assertRaises(TypeError):
            calculate_area_of_rectangle("five", 10)

    def test_edge_case_non_numeric_height(self):
        with self.assertRaises(TypeError):
            calculate_area_of_rectangle(5, "ten")

if __name__ == '__main__':
    unittest.main()


    
import unittest

def calculate_area_of_rectangle(width, height):
    # Calculate the area of a rectangle
    area = width * height
    return area

class TestCalculateAreaOfRectangle(unittest.TestCase):

    def test_normal_input(self):
        width = 5
        height = 10
        self.assertEqual(calculate_area_of_rectangle(width, height), 50)

    def test_edge_case_empty_input(self):
        with self.assertRaises(ValueError):
            calculate_area_of_rectangle(0, 0)

    def test_edge_case_negative_numbers(self):
        with self.assertRaises(ValueError):
            calculate_area_of_rectangle(-5, 10)
        with self.assertRaises(ValueError):
            calculate_area_of_rectangle(5, -10)

    def test_edge_case_zero_input(self):
        with self.assertRaises(ValueError):
            calculate_area_of_rectangle(0, 0)

    def test_edge_case_non_numeric_input(self):
        with self.assertRaises(TypeError):
            calculate_area_of_rectangle("five", 10)

    def test_edge_case_non_numeric_width(self):
        with self.assertRaises(TypeError):
            calculate_area_of_rectangle("five", 10)

    def test_edge_case_non_numeric_height(self):
        with self.assertRaises(TypeError):

44RwZtLmb0FgwviMXtwS