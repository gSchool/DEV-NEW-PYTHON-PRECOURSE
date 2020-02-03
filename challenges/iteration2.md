# Iteration 2

### !challenge

* type: code-snippet
* language: python3.6
* id: 0c21c708-bcb4-4810-a951-c47b6e27184b
* title: get_string_length

### !question

Write a function called "get_string_length".

Given a string, "get_string_length" returns the length of the given string.

Notes:
* Do NOT use any native 'length' methods, e.g., len().


```
output = get_string_length('hello')
print(output) # --> 5
```

### !end-question

### !placeholder

```python
def get_string_length(string):
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
        source = inspect.getsource(main.get_string_length)
        self.assertIsNone(pattern.search(source),
        msg = 'should not have the word "len" anywhere in function body')


    def test_0(self):
        # it should return an int    
        self.assertIsInstance(main.get_string_length("heyo"), int,
        msg = 'it should return an int')


    def test_1(self):
        # it should return the length of a string
        self.assertEqual(main.get_string_length("heyo"), 4,
        msg = 'should return the length of a string')

    def test_2(self):
        # it should return the length of a string
        self.assertEqual(main.get_string_length(""), 0,
        msg = 'should return the length of an empty string as 0')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
