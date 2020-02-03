# Iteration 1

### !challenge

* type: code-snippet
* language: python3.6
* id: 88612fe6-8ccc-46f4-8301-eac57083ec41
* title: get_index_of

### !question

Write a function called "get_index_of".

Given a character and a string, "get_index_of" returns the first position of the given character in the given string.

Notes:
* Strings are zero indexed, meaning the first character in a string is at position 0.
* When a string contains more than one occurrence of a character, it should return the index of its first occurrence.
* If the character does not exist in the string, it should return -1.
* Do not use any of Python's native methods, i.e., don't use "str.find", "str.index", "str.rfind", "str.rindex",  or similar methods in your implementation. Write the method from scratch.

```
output = get_index_of('a', 'I am a hacker')
print(output) # --> 2
```

### !end-question

### !placeholder

```python
def get_index_of(char, string):
    # your code here
    pass


```

### !end-placeholder

### !tests

```python
import main
import unittest
import re
import inspect

class TestScript(unittest.TestCase):
    def test_0(self):
        # it should not use find or index
        pattern = re.compile(r'\.r?(index|find|search)')
        source = inspect.getsource(main.get_index_of)
        self.assertIsNone(pattern.search(source),
        msg = 'should not have any of the words "find", "index", or "search" in the function')


    def test_1(self):
        # it should return a number
        self.assertEqual(main.get_index_of("a", "I am a hacker"), 2,
        msg = 'should return a number')


    def test_2(self):
        # it should return the index of the first occurrence of a string
        self.assertEqual(main.get_index_of("l", "all the weary horses"), 1,
        msg = 'should return the index of the first occurrence of a string')


    def test_3(self):
        # it should return -1 when the character does not occur in the string
        self.assertEqual(main.get_index_of("x", "I am a hacker"), -1,
        msg = 'should return -1 when the character does not occur in the string')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
