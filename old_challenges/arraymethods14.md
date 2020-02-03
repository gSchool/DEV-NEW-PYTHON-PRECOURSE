# Array Methods 14

### !challenge

* type: code-snippet
* language: python3.6
* id: a67d49da-9135-4b9b-96be-37a1accc9b5f
* title: joinArraysOfArrays

### !question

Write a function called "flatten".

Given a list of lists, "flatten" returns a single list containing the elements of the nested lists.

```
output = flatten([[1, 4], [True, False], ['x', 'y']])
print(output) # --> [1, 4, True, False, 'x', 'y']
```


### !end-question

### !placeholder

```python
def flatten(arr):
    # your code here
    pass


```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):

    def test_0(self):
        # it should return a list
        self.assertIsInstance(main.flatten([['a', 'b'], [1, 3], [True, False]]), list,
        msg = 'should return a list')


    def test_1(self):
        # it should return a list with the elements from all the nested lists
        self.assertEqual(main.flatten([['a', 'b'], [1, 3], [True, False]]), ['a', 'b', 1, 3, True, False],
        msg = 'should return a list with the elements from all the nested lists')


    def test_2(self):
        # it should handle empty lists in the first position
        self.assertEqual(main.flatten([[], [1, 3], [True, False]]), [1, 3, True, False],
        msg = 'should handle empty lists in the first position')


    def test_3(self):
        # it should handle empty lists in the second position
        self.assertEqual(main.flatten([['a', 'b'], [], [True, False]]), ['a', 'b', True, False],
        msg = 'should handle empty lists in the second position')


    def test_4(self):
        # it should handle empty lists in the third position
        self.assertEqual(main.flatten([['a', 'b'], [1, 3], []]), ['a', 'b', 1, 3],
        msg = 'should handle empty lists in the third position')


    def test_5(self):
        # it should handle empty lists in all positions
        self.assertEqual(main.flatten([[], [], []]), [],
        msg = 'should handle empty lists in all positions')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
