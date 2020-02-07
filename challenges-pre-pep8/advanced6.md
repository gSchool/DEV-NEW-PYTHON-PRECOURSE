# Advanced 6

### !challenge

* type: code-snippet
* language: python3.6
* id: e28598a1-0acf-488f-af4d-e8e01e6af1b6
* title: modulo

### !question

Write a function called "modulo".

Given 2 numbers, "modulo" returns the remainder after dividing num1 by num2.

It should behave as described in the Python documentation for the modulo operator given in this section:
https://docs.python.org/3.3/reference/expressions.html#binary-arithmetic-operations

Notes:
* Do NOT use either of the actual built-in modulo operators { mod() or % } anywhere in your code.

* 0 % NUMBER = 0.
* NUMBER % 0 = None.
* If either operand is None or not a number, then the result is None.
* Modulo always returns the sign of the second operand, even if the remainder is 0.

```
output = modulo(25, 4)
print(output) # --> 1

output = modulo(1007, -13)
print(output) # --> -7

output = modulo(1007, 13)
print(output) # --> 6

output = modulo(-1007, 13)
print(output) # --> 7

output = modulo(-7, 3)
print(output) # --> 2

output = modulo(7, -3)
print(output) # --> -2

output = modulo(7, 3)
print(output) # --> 1

output = modulo(-100, 8)
print(output) # --> 4
```

### !end-question

### !placeholder

```python
# your code here


```

### !end-placeholder

### !tests

```python
import main
import unittest
import re, inspect

class TestScript(unittest.TestCase):
    def test_1(self):
        # should not have "%" anywhere in function body'
        pattern = re.compile(r'[%|(mod\()]')
        source = inspect.getsource(main.modulo)
        self.assertIsNone(pattern.search(source),
        msg = 'should not have "%" or mod() anywhere in function body')


    def test_2(self):
        # it should return 0 when there is no remainder
        self.assertEqual(main.modulo(114, 114), 0,
        msg = 'should return 0 when there is no remainder')


    def test_3(self):
        # it should return a negative number when the first number is negative
        self.assertEqual(main.modulo(7, -3), -2,
        msg = 'should return a negative number when the second number is negative')


    def test_4(self):
        # it should return a positive number when the second number is negative
        self.assertEqual(main.modulo(-7, 3), 2,
        msg = 'should return a positive number when the second number is positive')


    def test_5(self):
        # it should return 0 when the first number is 0
        self.assertEqual(main.modulo(0, 2), 0,
        msg = 'should return 0 when the first number is 0')


    def test_6(self):
        # it should return None when the first number is None
        self.assertIsNone(main.modulo(None, 2),
        msg = 'should return None when the first number is None')


    def test_7(self):
        # it should return NaN when the second number is None
        self.assertIsNone(main.modulo(4, None),
        msg = 'should return None when the second number is None')


    def test_8(self):
        # it should return None when the second number is 0
        self.assertIsNone(main.modulo(12, 0),
        msg = 'should return None when the second number is 0')


    def test_9(self):
        # it should return 2 when given 12 and 5
        self.assertEqual(main.modulo(12, 5), 2,
        msg = 'should return 2 when given 12 and 5')


    def test_10(self):
        # it should return minus_1 when given minus_1 and 2
        self.assertEqual(main.modulo(-1, 2), 1,
        msg = 'should return minus_1 when given minus_1 and 2')


    def test_12(self):
        # it should return 1 when given 1 and 2
        self.assertEqual(main.modulo(1, 2), 1,
        msg = 'should return 1 when given 1 and 2')


    def test_13(self):
        # it should return 2 when given 2 and 3
        self.assertEqual(main.modulo(2, 3), 2,
        msg = 'should return 2 when given 2 and 3')


    def test_14(self):
        # it should return -0 when given minus 4 and 2
        self.assertEqual(main.modulo(4, -2), -0,
        msg = 'should return -0 when given minus 4 and 2')

    def test_15(self):
        # it should return 1.5 when given 5.5 and 2
        self.assertEqual(main.modulo(5.5, 2), 1.5,
        msg = 'it should return 1.5 when given 5.5 and 2')

    def test_15(self):
        # it should return 1.5 when given 5.5 and 2
        self.assertEqual(main.modulo(5.5, 2), 1.5,
        msg = 'it should return 1.5 when given 5.5 and 2')

    def test_15(self):
        # it should return -7 when given 1007 and -13
        self.assertEqual(main.modulo(1007, -13), -7,
        msg = ' it should return -7 when given 1007 and -13')

    def test_15(self):
        # it should return 7 when given -1007 and 13
        self.assertEqual(main.modulo(-1007, 13), 7,
        msg = ' it should return 7 when given -1007 and 13')


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
