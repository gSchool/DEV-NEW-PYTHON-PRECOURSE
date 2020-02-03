# Advanced 8

### !challenge

* type: code-snippet
* language: python3.6
* id: ee922c51-e401-4df2-821c-93a2080342b1
* title: isEvenWithoutModulo

### !question

Write a function called "isEvenWithoutModulo".

Given a number, "isEvenWithoutModulo" returns whether it is even.

Notes:
* It does so without using the modulo operator (%).
* It should work for negative numbers and zero.

```
output = isEvenWithoutModulo(8)
print(output) # --> True
```

### !end-question

### !placeholder

```python
def isEvenWithoutModulo(num):
    # your code here
    pass

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
        pattern = re.compile(r'(%|mod\(])')
        source = inspect.getsource(main.isEvenWithoutModulo)
        self.assertIsNone(pattern.search(source),
        msg = 'should not have "%" or mod() anywhere in function body')

    def test_1(self):
        # it should return a boolean
        self.assertIsInstance(main.isEvenWithoutModulo(40), bool,
        msg = 'should return a bool')

    def test_2(self):
        # it should return True when a number is even
        self.assertTrue(main.isEvenWithoutModulo(40),
        msg = 'should return True when a number is even')

    def test_3(self):
        # it should return True when a negative number is even
        self.assertTrue(main.isEvenWithoutModulo(-410),
        msg = 'should return True when a negative number is even')

    def test_4(self):
        # it should return False when a number is odd
        self.assertFalse(main.isEvenWithoutModulo(41),
        msg = 'should return False when a number is odd')

    def test_5(self):
        # it should return False when a negative number is odd
        self.assertFalse(main.isEvenWithoutModulo(-111),
        msg = 'should return False when a negative number is odd')
```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
