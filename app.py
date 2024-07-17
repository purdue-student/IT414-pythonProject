import unittest

print("Hello World")


# Step 1: Function to add two numbers


def add(a, b):
    result = a + b
    return result


n1 = int(input("enter the first number:"))
n2 = int(input("enter the second number:"))

print(add(n1, n2))


class TestAddNumbers(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(0, 0), 0)
        self.assertAlmostEqual(add(1.1, 2.2), 3.3)


if __name__ == "__main__":
    unittest.main()
