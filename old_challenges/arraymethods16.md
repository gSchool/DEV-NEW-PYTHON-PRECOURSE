# Array Methods 16

### !challenge

* type: code-snippet
* language: python3.6
* id: 99c43844-c828-47d6-a073-db33a9f9bfb7
* title: getLongestWordOfMixedElements

### !question

Write a function called "getLongestWordOfMixedElements".

Given a list of mixed types, "getLongestWordOfMixedElements" returns the longest string in the given list.

Notes:
* If the list is empty, it should return an empty string ("").
* If the list contains no strings it should return an empty string.

```
output = getLongestWordOfMixedElements([3, 'word', 5, 'up', 3, 1])
print(output) # --> 'word'
```

### !end-question

### !placeholder

```python
def getLongestWordOfMixedElements(arr):
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
        self.assertIsInstance(main.getLongestWordOfMixedElements(["these", "are", "strings"]), str,
        msg = 'should return a string')


    def test_1(self):
        # it should return the longest string in a list
        self.assertEqual(main.getLongestWordOfMixedElements([3, "word", 5, "up", 3, 1]), "word",
        msg = 'should return the longest string in a list')


    def test_2(self):
        # it should return the longest string in a list that appears first when there are ties
        self.assertEqual(main.getLongestWordOfMixedElements(["word", 3, 5, 3, "bird", "up", 1, 5]), "word",
        msg = 'should return the longest string in a list that appears first when there are ties')


    def test_3(self):
        # it should return an empty string when the list is empty
        self.assertEqual(main.getLongestWordOfMixedElements([]), "",
        msg = 'should return an empty string when the list is empty')


    def test_4(self):
        # it should return an empty string there are no strings
        self.assertEqual(main.getLongestWordOfMixedElements([1, 2, 4]), "",
        msg = 'should return an empty string there are no strings')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: c73e353f-8655-42e8-8f6b-7e342182ca9c
* title: getLargestNumberAmongMixedElements

### !question

Write a function called "getLargestNumberAmongMixedElements".

Given any list, "getLargestNumberAmongMixedElements" returns the largest number in the given list.

Notes:
* The list might contain values of a type other than numbers.
* If the list is empty, it should return 0.
* If the list contains no numbers, it should return 0.

```
output = getLargestNumberAmongMixedElements([3, 'word', 5, 'up', 3, 1])
print(output) # --> 5
```

### !end-question

### !placeholder

```python
def getLargestNumberAmongMixedElements(arr):
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
        self.assertEqual(main.getLargestNumberAmongMixedElements([3, 5, 3, 1]), (float, int),
        msg = 'should return a number')


    def test_1(self):
        # it should return the largest element in a list
        self.assertEqual(main.getLargestNumberAmongMixedElements([3, "word", 5, "up", 3, 1]), 5,
        msg = 'should return the largest element in a list')


    def test_2(self):
        # it should return the largest element in a list when there are ties
        self.assertEqual(main.getLargestNumberAmongMixedElements(["word", 3, 5, 3, "wordy", "up", 1, 5]), 5,
        msg = 'should return the largest element in a list when there are ties')


    def test_3(self):
        # it should return the largest element in a list when they are all negative
        self.assertEqual(main.getLargestNumberAmongMixedElements([-1, -5, "word", -3]), -1,
        msg = 'should return the largest element in a list when they are all negative')


    def test_4(self):
        # it should return 0 when the list is empty
        self.assertEqual(main.getLargestNumberAmongMixedElements([]), 0,
        msg = 'should return 0 when the list is empty')


    def test_5(self):
        # it should return 0 when there are no numbers
        self.assertEqual(main.getLargestNumberAmongMixedElements(["word", "up"]), 0,
        msg = 'should return 0 when there are no numbers')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
