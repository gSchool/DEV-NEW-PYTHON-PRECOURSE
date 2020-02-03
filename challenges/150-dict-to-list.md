### !challenge

* type: code-snippet
* language: python3.6
* id: af0470f5-db25-4019-881b-3f73c0bda343
* title: convert_dict_to_list2.md

### !question

Write a function called "get_all_values" which returns a list of all the input dictionary's values.

```
inp = {'name' : 'Sam', 'age' : 25, 'hasPets' : True}
output = get_all_values(inp)
print(output) # -> ['Sam', 25, True]
```

Do not use "dict.values()" to solve this exercise.

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
        self.assertIsInstance(main.get_all_values({'first':1, 'second':2}), list,
        msg = "it should return a list")

    def test0(self):
        input1 = {'name' : 'Sam', 'age' : 25, 'hasPets' : True}
        self.assertEqual(main.get_all_values(input1),
        ['Sam', 25, True],
        msg = "it should return a list of values")

    def test_1(self):
        # it should not use the multiply operator
        pattern = re.compile(r'\.values')
        source = inspect.getsource(main.get_all_values)
        self.assertIsNone(pattern.search(source),
        msg = 'should not call the "values" method on the input dictionary in the function body')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
