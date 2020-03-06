# Advanced 7

### !challenge

* type: code-snippet
* language: python3.6
* id: 8bf521f7-88bd-47f1-a173-4a0a4d1d8389
* title: is_odd

### !question

Write a function called "is_odd".

Given a number, "is_odd" returns whether the passed in number is odd.

Notes:
* Your function must NOT use the modulo operator (%).
* Your function should work for negative numbers and zero.

```
output = is_odd(17)
print(output) # --> True
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
    def test_00(self):
        # should not have "%" or mod anywhere in function body'
        pattern = re.compile(r'(%|mod\()')
        source = inspect.getsource(main.is_odd)
        self.assertIsNone(pattern.search(source),
        msg = 'should not have "%" or mod() anywhere in function body')

    def test_0(self):
        # it should return a boolean
        self.assertIsInstance(main.is_odd(40), bool,
        msg = 'should return a boolean')


    def test_1(self):
        self.assertFalse(main.is_odd(100),
        msg = 'should return False when a number is even')

    def test_2(self):
        # it should return True when a negative number is odd
        self.assertTrue(main.is_odd(-41),
        msg = 'should return True when a negative number is odd')


    def test_3(self):
        # it should return True when a number is odd
        self.assertTrue(main.is_odd(43),
        msg = 'should return True when a positive number is odd')


    def test_4(self):
        # it should return False when a negative number is even
        self.assertFalse(main.is_odd(-40),
        msg = 'should return False when a negative number is even')


    def test_5(self):
        # it should return False when a number is even
        self.assertFalse(main.is_odd(0),
        msg = 'should return False when a number is 0')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
