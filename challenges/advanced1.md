# Advanced 1

### !challenge

* type: code-snippet
* language: python3.6
* id: 6507106d-7850-4631-a2d6-19b34da62bad
* title: count_words

### !question

Write a function called "count_words".

Given a string, "count_words" returns a dictionary where each key is a word in the given string, with its value being how many times that word appeared in the given string.

Notes:
* If given an empty string, it should return an empty dictionary.

```
output = count_words('ask a bunch get a bunch')
print(output) # --> {'ask': 1, 'a': 2, 'bunch': 2, 'get': 1}
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

class TestScript(unittest.TestCase):

    def test_0(self):
        # it should return an object
        self.assertIsInstance(main.count_words("ask a bunch try a bunch get a bunch"), dict,
        msg = 'should return a dict')


    def test_1(self):
        # it should return an object where each property gives a word in the string, with its number of appearances
        result = {'ask': 1, 'a': 2, 'bunch': 2, 'get': 1}
        self.assertEqual(main.count_words("ask a bunch get a bunch"), result,
        msg = 'should return a dict where each key gives a word in the string, with the value its number of appearances')


    def test_2(self):
        # it should return an empty dict if passed an empty string
        self.assertEqual(main.count_words(""), {},
        msg = 'should return an empty dict if passed an empty string')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
