# Iteration 2

### !challenge

* type: code-snippet
* language: python3.6
* id: 0c21c708-bcb4-4810-a951-c47b6e27184b
* title: getStringLength

### !question

Write a function called "getStringLength".

Given a string, "getStringLength" returns the length of the given string.

Notes:
* Do NOT use any native 'length' methods, e.g., len().


```
output = getStringLength('hello')
print(output) # --> 5
```

### !end-question

### !placeholder

```python
def getStringLength(string):
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
        # should not have the word "len" anywhere in function body'
        pattern = re.compile(r'len')
        source = inspect.getsource(main.getStringLength)
        self.assertIsNone(pattern.search(source),
        msg = 'should not have the word "len" anywhere in function body')


    def test_0(self):
        # it should return an int    
        self.assertIsInstance(main.getStringLength("heyo"), int,
        msg = 'it should return an int')


    def test_1(self):
        # it should return the length of a string
        self.assertEqual(main.getStringLength("heyo"), 4,
        msg = 'should return the length of a string')

    def test_2(self):
        # it should return the length of a string
        self.assertEqual(main.getStringLength(""), 0,
        msg = 'should return the length of an empty string as 0')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
