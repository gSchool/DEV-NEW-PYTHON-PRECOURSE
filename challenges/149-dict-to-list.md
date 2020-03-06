### !challenge

* type: code-snippet
* language: python3.6
* id: c484fcc2-9db9-4e13-9362-a1377b196679
* title: dict_to_list1

### !question

Write a function called "dict_to_list" which returns a list of all the input dictionary's keys.

```
dictionary = {'name' : 'Sam', 'age' : 25, 'has_pets' : True}
output = dict_to_list(dictionary)
print(output) # -> ['name', 'age', 'has_pets']
```

Do NOT use the word dict.keys method to solve this exercise.

Note that your function should be able to handle any dictionary passed in it regardless of the number of keys.


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
    def test_000(self):
        # should not have the word "keys" anywhere in function body'
        pattern = re.compile(r'keys')
        source = inspect.getsource(main.dict_to_list)
        self.assertIsNone(pattern.search(source),
        msg = 'should not have the word "keys" *anywhere* in function body')


    def test_00(self):
        self.assertIsInstance(main.dict_to_list({'first':1}),list,
        msg = "it should return a list")

    def test0(self):
        dictionary = {'name' : 'Sam', 'age' : 25, 'has_pets' : True}
        self.assertEqual(main.dict_to_list(dictionary),
        ['name', 'age', 'has_pets'],
        msg = "it should return a list of keys")

    def test_1(self):
        # it should not use the multiply operator
        pattern = re.compile(r'\.keys')
        source = inspect.getsource(main.dict_to_list)
        self.assertIsNone(pattern.search(source),
        msg = 'should not call the "keys" method on the input dictionary in the function body')

```

### !end-tests

### !explanation
```python
def dict_to_list(dictionary):
    return [key for key in dictionary]
```
### !end-explanation

### !end-challenge
