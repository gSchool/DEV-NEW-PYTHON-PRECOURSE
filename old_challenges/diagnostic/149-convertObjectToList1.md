### !challenge

* type: code-snippet
* language: python3.6
* id: c484fcc2-9db9-4e13-9362-a1377b196679
* title: convertObjectToList1.md

### !question

Write a function called "getAllKeys" which returns a list of all the input dictionary's keys.

```
inp = {'name' : 'Sam', 'age' : 25, 'hasPets' : True}
output = getAllKeys(inp)
print(output) # -> ['name', 'age', 'hasPets']
```

Do not use "dict.keys()" to solve this exercise.

Note that your def should be able to handle any dictionary passed in it regardless of the number of keys.


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
        self.assertIsInstance(main.getAllKeys({'first':1}),list,
        msg = "it should return a list")

    def test0(self):
        input1 = {'name' : 'Sam', 'age' : 25, 'hasPets' : True}
        self.assertEqual(main.getAllKeys(input1),
        ['name', 'age', 'hasPets'],
        msg = "it should return a list of keys")

    def test_1(self):
        # it should not use the multiply operator
        pattern = re.compile(r'\.keys')
        source = inspect.getsource(main.getAllKeys)
        self.assertIsNone(pattern.search(source),
        msg = 'should not call the "keys" method on the input dictionary in the function body')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
