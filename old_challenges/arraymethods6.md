# Array Methods 6

### !challenge

* type: code-snippet
* language: python3.6
* id: 8e828b4d-ff6f-4fed-9bab-7d7a1b4b0c1e
* title: removeFromBack

### !question

Write a function called "removeFromBack".

Given an array, "removeFromBack" returns the given array with its last element removed.

Notes:
* You should be familiar with the method 'pop'.

```
output = removeFromBack([1, 2, 3])
print(output) # --> [1, 2]
```

### !end-question

### !placeholder

```python
def removeFromBack(arr):
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
        self.assertIsInstance(main.removeFromBack([1, 2, 3]), list,
        msg = 'should return a list')


    def test_1(self):
        # it should remove the last element from a 3-element list
        self.assertEqual(main.removeFromBack([1, 2, 3]), [1, 2],
        msg = 'should remove the last element from a 3-element list')


    def test_2(self):
        # it should remove the last element from a 2-element array
        self.assertEqual(main.removeFromBack([1, 2]), [1],
        msg = 'should remove the last element from a 2-element list')


    def test_3(self):
        # it should handle an empty array
        self.assertEqual(main.removeFromBack([]), [],
        msg = 'should handle an empty list')

```
### !end-tests

### !explanation

### !end-explanation

### !end-challenge
