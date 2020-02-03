### !challenge

* type: code-snippet
* language: python3.6
* id: 862b3ed4-83e2-4253-9e53-e7d2263c2727
* title: convertObjectToList3.md

### !question

Write a function called "convertObjectToList" which converts a dictionary literal into a list of lists, like this:

```
inp = {'name': 'Holly', 'age': 35, 'role': 'producer'}
output = convertObjectToList(inp)
print(output) # -> [['name', 'Holly'], ['age', 35], ['role', 'producer']]

```

### !end-question

### !placeholder

```python
def convertObjectToList(obj):
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
        self.assertIsInstance(main.convertObjectToList({'first':1, 'second':2}), list,
        msg = "it should return a list")

    def test0(self):
        input1 = {'name': 'Holly', 'age': 35, 'role': 'producer'}
        self.assertEqual(main.convertObjectToList(input1),
        [['name', 'Holly'], ['age', 35], ['role', 'producer']],
        msg = "it should return a list of lists")

    def test1(self):
        input1 = {'name': 'Holly', 'age': 35, 'role': 'producer'}  

        try:
            holly = main.convertObjectToList(input1)[0][1]
            self.assertEqual(main.convertObjectToList(input1),
            'Holly',
            msg = "it should have the correct nesting")
            
        except TypeError:
            self.fail('It should return a list of lists')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
