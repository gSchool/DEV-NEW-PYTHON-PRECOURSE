# Array Methods 12

### !challenge

* type: code-snippet
* language: python3.6
* id: 3e9cfffd-1ec6-4243-a91b-4546c2d647aa
* title: findSmallestElement

### !question

Write a function called "findSmallestElement".

Given a list of numbers, "findSmallestElement" returns the smallest number within the given list.

Notes:
* If the given list is empty, it should return 0.

```
output = findSmallestElement([4, 1, 9, 10])
print(output) # --> 1
```

### !end-question

### !placeholder

```python
def findSmallestElement(arr):
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
        # it should return a number
        self.assertIsInstance(main.findSmallestElement([3, 5, 3, 1]), (float, int),
        msg = 'should return a number')


    def test_1(self):
        # it should return the smallest element in a list
        self.assertEqual(main.findSmallestElement([3, 5, 3, 1]), 1,
        msg = 'should return the smallest element in a list')


    def test_2(self):
        # it should return the smallest element in a list when there are ties
        self.assertEqual(main.findSmallestElement([3, 1, 3, 1, 5]), 1,
        msg = 'should return the smallest element in a list when there are ties')


    def test_3(self):
        # it should return the smallest element in a list when they are all negative
        self.assertEqual(main.findSmallestElement([-1, -5, -3]), -5,
        msg = 'should return the smallest element in a list when they are all negative')


    def test_4(self):
        # it should return 0 if the list is empty
        self.assertEqual(main.findSmallestElement([]), 0,
        msg = 'should return 0 if the list is empty')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 3a3527f5-84ad-4d59-8ba5-5e774661e37e
* title: findShortestElement

### !question

Write a function called "findShortestElement".

Given a list, "findShortestElement" returns the shortest string within the given list.

Notes:
* If there are ties, it should return the first element to appear.
* If the given list is empty, it should return an empty string.

```
output = findShortestElement(['a', 'two', 'three'])
print(output) # --> 'a'
```

### !end-question

### !placeholder

```python
def findShortestElement(arr):
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
        # it should return a string
        self.assertEqual(main.findShortestElement(["one", "two", "three"]), str,
        msg = 'should return a string')


    def test_1(self):
        # it should return the shortest element in a list
        self.assertEqual(main.findShortestElement(["a", "two", "three"]), "a",
        msg = 'should return the shortest element in a list')


    def test_2(self):
        # it should return the first shortest element in a list when there are ties
        self.assertEqual(main.findShortestElement(["one", "to", "no"]), "to",
        msg = 'should return the first shortest element in a list when there are ties')

    def test_3(self):
        # it should return an empty string if the list is empty
        self.assertEqual(main.findShortestElement([]), "",
        msg = 'should return an empty string if the list is empty')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
