import unittest
import katas


class TestKatas(unittest.TestCase):

    def test_add(self):
        self.assertEqual(katas.add(10, 4), 14)
        self.assertEqual(katas.add(-9, -2), -11)
        self.assertEqual(katas.add(-5, 3), -2)
        self.assertEqual(katas.add(5, -3), 2)

    def test_multiply(self):
        self.assertEqual(katas.multiply(5, 3), 15)
        self.assertEqual(katas.multiply(5, -3), -15)
        self.assertEqual(katas.multiply(-5, 3), -15)
        self.assertEqual(katas.multiply(-5, -3), 15)

    def test_power(self):
        self.assertEqual(katas.power(3, 3), 27)
        self.assertEqual(katas.power(2, 2), 4)
        self.assertEqual(katas.power(8, 2), 64)
        self.assertEqual(katas.power(10, 3), 1000)
        with self.assertRaises(ValueError):
            katas.power(3, -2)
            katas.power(3, 4.0)

    def test_factorial(self):
        self.assertEqual(katas.factorial(5), 120)
        self.assertEqual(katas.factorial(4), 24)
        self.assertEqual(katas.factorial(3), 6)
        self.assertEqual(katas.factorial(2), 2)
        with self.assertRaises(ValueError):
            katas.factorial(-1)

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(1), 1)
        self.assertEqual(katas.fibonacci(0), 0)
        self.assertEqual(katas.fibonacci(2), 1)
        self.assertEqual(katas.fibonacci(3), 2)
        with self.assertRaises(ValueError):
            katas.fibonacci(-3)


if __name__ == '__main__':
    unittest.main()
