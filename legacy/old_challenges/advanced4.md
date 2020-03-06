# Advanced 4

### !challenge

* type: code-snippet
* language: python3.6
* id: 5f5d7cf0-c7df-4fb3-aebd-d8791143baec
* title: countAllCharacters

### !question

Write a function called "countAllCharacters".

Given a string, "countAllCharacters" returns a dictionary where each key is a character in the given string. The value of each key should be how many times each character appeared in the given string.

Notes:
* If given an empty string, countAllCharacters should return an empty dictionary.

```
output = countAllCharacters('banana')
print(output) # --> {'b': 1, 'a': 3, 'n': 2}
```

### !end-question

### !placeholder

```python

```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):

    def test_0(self):
        # it should return a dictionary
        self.assertIsInstance(main.countAllCharacters("banana"), dict,
        msg = 'should return a dictionary')


    def test_1(self):
        # it should return a dictionary where each property gives a character in the string, with its number of appearances
        result = {'s': 1, 'a': 3, 'm': 1, 'n': 1, 't': 1, 'h': 1}
        self.assertEqual(main.countAllCharacters("samantha"), result,
        msg = 'should return a dictionary where each property gives a character in the string, with its number of appearances')


    def test_2(self):
        # it should return a dictionary empty dictionary if passed an empty string
        self.assertEqual(main.countAllCharacters(""), {},
        msg = 'should return a dictionary empty dictionary if passed an empty string')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
