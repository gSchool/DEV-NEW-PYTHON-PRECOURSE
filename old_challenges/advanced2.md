# Advanced 2

### !challenge

* type: code-snippet
* language: python3.6
* id: 036e5563-3791-46d3-8d67-780c769396fb
* title: extend

### !question

Write a function called "extend".

Given two dictionaries, "extend" adds properties from the second dictionary to the first.

Notes:
* Add any keys from the 2nd dictionary that are not in the first.
* If the 1st dictionary already has a given key, ignore it (do not overwrite the first dictionary if it already has the given key).
* Do not modify the 2nd dictionary at all.

```
dict1 = {'a': 1, 'b': 2}

dict2 = {'b': 4, 'c': 3}


result = extend(dict1, dict2)

print(result) # --> {'a': 1, 'b': 2, 'c': 3}
print(dict1)  # --> {'a': 1, 'b': 2, 'c': 3}
print(dict2) # --> {'b': 4, 'c': 3}
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
        # it 'should return a dict'
        self.assertIsInstance(main.extend({'a': 1, 'b': 2}, {'a':1,'b': 4, 'c': 3, 'd':17}), dict,
        msg = 'should return a dict')

    def test_1(self):
        # it should extend the first dict with unrepresented properties from the second object
        self.assertEqual(main.extend({'a':1, 'b':2}, {'b': 4, 'c': 3, 'key':'value'}),
        {'a':1, 'b':2, 'c':3, 'key':'value'},
        msg = 'should extend the first dict with unrepresented properties from the second dict')


    def test_2(self):
        # it 'should leave the second dictionary unchanged'
        obj2 = {'a':1, 'b': 4, 'c': 3, 'd':17}
        main.extend({'a':1, 'b':2}, obj2)
        self.assertEqual(obj2, {'a':1,'b': 4, 'c': 3, 'd':17},
        msg = 'should leave the second dictionary unchanged')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
