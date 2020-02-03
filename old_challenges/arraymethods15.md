# Array Methods 15

### !challenge

* type: code-snippet
* language: python3.6
* id: 4f89dd25-b751-49fe-9fa9-fe8c368c1a7c
* title: findShortestWordAmongMixedElements

### !question

Write a function called "findShortestWordAmongMixedElements".

Given a list, "findShortestWordAmongMixedElements" returns the shortest string within the given list.

Notes:
* If there are ties, it should return the first element to appear in the given list.
* Expect the given list to have values other than strings.
* If the given list is empty, it should return an empty string.
* If the given list contains no strings, it should return an empty string.

```
output = findShortestWordAmongMixedElements([4, 'two', 2, 'three'])
print(output) # --> 'two'
```

### !end-question

### !placeholder

```python

def findShortestWordAmongMixedElements(arr):
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
        self.assertIsInstance(main.findShortestWordAmongMixedElements(["these", "are", "strings"]), str,
        msg = 'should return a string')


    def test_1(self):
        # it should return the shortest string in a list
        self.assertEqual(main.findShortestWordAmongMixedElements([3, "word", 5, "up", 3, 1]), "up",
        msg = 'should return the shortest string in a list')


    def test_2(self):
        # it should return the shortest string in a list that appears first when there are ties
        self.assertEqual(main.findShortestWordAmongMixedElements(["word", 3, 5, 3, "yo", "up", 1, 5]), "yo",
        msg = 'should return the shortest string in a list that appears first when there are ties')


    def test_3(self):
        # it should return an empty string when the list is empty
        self.assertEqual(main.findShortestWordAmongMixedElements([]), "",
        msg = 'should return an empty string when the list is empty')


    def test_4(self):
        # it should return an empty string there are no strings
        self.assertEqual(main.findShortestWordAmongMixedElements([1, 2, 4]), "",
        msg = 'should return an empty string there are no strings')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 0bbe947d-3174-4fe2-98c4-1a84331477d7
* title: findSmallestNumberAmongMixedElements

### !question

Write a function called "findSmallestNumberAmongMixedElements".

Given a list of mixed elements, "findSmallestNumberAmongMixedElements" returns the smallest number within the given list.

Notes:
* If the given list is empty, it should return 0.
* If the list contains no numbers, it should return 0.

```
output = findSmallestNumberAmongMixedElements([4, 'lincoln', 9, 'octopus'])
print(output) # --> 4
```

### !end-question

### !placeholder

```python
def findSmallestNumberAmongMixedElements(arr):
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
        self.assertIsInstance(main.findSmallestNumberAmongMixedElements([3, 5, 3, 1]), (float, int),
        msg = 'should return a number')


    def test_1(self):
        # it should return the smallest element in a list
        self.assertEqual(main.findSmallestNumberAmongMixedElements([3, "word", 5, "up", 3, 1]), 1,
        msg = 'should return the smallest element in a list')


    def test_2(self):
        # it should return the smallest element in a list when there are ties
        self.assertEqual(main.findSmallestNumberAmongMixedElements(["word", 3, 1, 3, "wordy", "up", 1, 5]), 1,
        msg = 'should return the smallest element in a list when there are ties')


    def test_3(self):
        # it should return the smallest element in a list when they are all negative
        self.assertEqual(main.findSmallestNumberAmongMixedElements([-1, -5, "word", -3]), -5,
        msg = 'should return the smallest element in a list when they are all negative')


    def test_4(self):
        # it should return 0 when the list is empty
        self.assertEqual(main.findSmallestNumberAmongMixedElements([]), 0,
        msg = 'should return 0 when the list is empty')


    def test_5(self):
        # it should return 0 when there are no numbers
        self.assertEqual(main.findSmallestNumberAmongMixedElements(["word", "up"]), 0,
        msg = 'should return 0 when there are no numbers')


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
