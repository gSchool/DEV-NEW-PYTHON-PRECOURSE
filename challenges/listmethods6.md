# Array Methods 6

### !challenge

* type: code-snippet
* language: python3.6
* id: 8e828b4d-ff6f-4fed-9bab-7d7a1b4b0c1e
* title: remove_from_back

### !question

Write a function called "remove_from_back".

Given an array, "remove_from_back" returns the given array with its last element removed.

Notes:
* You should be familiar with the method 'pop'.

```
output = remove_from_back([1, 2, 3])
print(output) # --> [1, 2]
```

### !end-question

### !placeholder

```python
def remove_from_back(arr):
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
        # it should return an list
        self.assertIsInstance(main.remove_from_back([1, 2, 3]), list,
        msg = 'should return a list')


    def test_1(self):
        # it should remove the last element from a 3-element list
        self.assertEqual(main.remove_from_back([1, 2, 3]), [1, 2],
        msg = 'should remove the last element from a 3-element list')


    def test_2(self):
        # it should remove the last element from a 2-element array
        self.assertEqual(main.remove_from_back([1, 2]), [1],
        msg = 'should remove the last element from a 2-element list')


    def test_3(self):
        # it should handle an empty array
        self.assertEqual(main.remove_from_back([]), [],
        msg = 'should handle an empty list')

```
### !end-tests

### !explanation

### !end-explanation

### !end-challenge
