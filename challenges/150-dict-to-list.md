### !challenge

* type: code-snippet
* language: python3.6
* id: af0470f5-db25-4019-881b-3f73c0bda343
* title: dict_to_list.md

### !question

Write a function called "get_vals" which returns a list of all the dictionaryut dictionary's values.

```
dictionary = {'first_name' : 'Sam', 'last_name' : 'Spade'}
output = get_vals(dictionary)
print(output) # -> ['Sam', 'Spade']
```

Do not use the "dict.values" method to solve this exercise.

### !end-question

### !placeholder

```python

```

### !end-placeholder

### !tests

```python
import main
import unittest
import inspect, re

class TestScript(unittest.TestCase):
    def test_00(self):
        self.assertIsInstance(main.get_vals({'first':1, 'second':2}), list,
        msg = "it should return a list")

    def test0(self):
        dictionary = {'name' : 'Sam', 'age' : 25, 'has_pets' : True}
        self.assertEqual(main.get_vals(dictionary),
        ['Sam', 25, True],
        msg = "it should return a list of values")

    def test_1(self):
        pattern = re.compile(r'values')
        source = inspect.getsource(main.get_vals)
        self.assertIsNone(pattern.search(source),
        msg = 'should not call the "values" method on the dictionary in the function body')

```

### !end-tests

### !explanation
```python
def get_vals(dictionary):
    return [dictionary[key] for key in dictionary]
```
### !end-explanation

### !end-challenge
