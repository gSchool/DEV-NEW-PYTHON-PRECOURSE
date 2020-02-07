# Advanced 5

### !challenge

* type: code-snippet
* language: python3.6
* id: 0e621f19-ceb1-4565-8f07-e78a7b8a3adb
* title: sumDigits

### !question

Write a function called "sumDigits".

Given a number, "sumDigits" returns the sum of all its digits.

```
output = sumDigits(1148)
print(output) # --> 14
```

If the number is negative, the first digit should count as negative.

```
output = sumDigits(-316)
print(output) # --> 4
```

Notes:
* In order to use some of the methods that will be most helpful to you, you will most likely want to do some string to number conversion and vice versa.


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

class TestScript(unittest.TestCase):

    def test_0(self):
        # it should return a number
        self.assertIsInstance(main.sumDigits(2002), int,
        msg = 'should return an int')


    def test_1(self):
        # it should sum the digits of a positive number
        self.assertEqual(main.sumDigits(2002), 4,
        msg = 'should sum the digits of a positive number')


    def test_2(self):
        # it should sum the digits of a negative number
        self.assertEqual(main.sumDigits(-2004), 2,
        msg = 'should sum the digits of a negative number')


    def test_3(self):
        # it should sum return 0 if the number is 0
        self.assertEqual(main.sumDigits(0), 0,
        msg = 'should return 0 if the number is 0')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
