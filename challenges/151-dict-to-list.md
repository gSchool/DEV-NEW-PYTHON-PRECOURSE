### !challenge

* type: code-snippet
* language: python3.6
* id: 862b3ed4-83e2-4253-9e53-e7d2263c2727
* title: convert_dict_to_list3.md

### !question

Write a function called "convert_dict_to_list" which converts a dictionary literal into a list of lists, like this:

```
inp = {'name': 'Holly', 'age': 35, 'role': 'producer'}
output = convert_dict_to_list(inp)
print(output) # -> [['name', 'Holly'], ['age', 35], ['role', 'producer']]

```

### !end-question

### !placeholder

```python
def convert_dict_to_list(obj):
    # your code here
    pass

```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):
    def test_00(self):
        self.assertIsInstance(main.convert_dict_to_list({'first':1, 'second':2}), list,
        msg = "it should return a list")

    def test0(self):
        input1 = {'name': 'Holly', 'age': 35, 'role': 'producer'}
        self.assertEqual(main.convert_dict_to_list(input1),
        [['name', 'Holly'], ['age', 35], ['role', 'producer']],
        msg = "it should return a list of lists")

    def test1(self):
        input1 = {'name': 'Holly', 'age': 35, 'role': 'producer'}  

        try:
            holly = main.convert_dict_to_list(input1)[0][1]
            self.assertEqual(main.convert_dict_to_list(input1),
            'Holly',
            msg = "it should have the correct nesting")
            
        except TypeError:
            self.fail('It should return a list of lists')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
