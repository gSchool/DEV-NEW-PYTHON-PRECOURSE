# List Methods 15

### !challenge

* type: code-snippet
* language: python3.6
* id: 4f89dd25-b751-49fe-9fa9-fe8c368c1a7c
* title: find_shortest_string_among_mixed_elements

### !question

Write a function called "find_shortest_string_among_mixed_elements".

Given a list, "find_shortest_string_among_mixed_elements" returns the shortest string within the given list.

Notes:
* If there are ties, it should return the first element to appear in the given list.
* Expect the given list to have values other than strings.
* If the given list is empty, it should return an empty string.
* If the given list contains no strings, it should return an empty string.

```
output = find_shortest_string_among_mixed_elements([4, 'two', 2, 'three'])
print(output) # --> 'two'
```

### !end-question

### !placeholder

```python

def find_shortest_string_among_mixed_elements(arr):
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
        self.assertIsInstance(main.find_shortest_string_among_mixed_elements(["these", "are", "strings"]), str,
        msg = 'should return a string')


    def test_1(self):
        # it should return the shortest string in a list
        self.assertEqual(main.find_shortest_string_among_mixed_elements([3, "string", 5, "up", 3, 1]), "up",
        msg = 'should return the shortest string in a list')


    def test_2(self):
        # it should return the shortest string in a list that appears first when there are ties
        self.assertEqual(main.find_shortest_string_among_mixed_elements(["string", 3, 5, 3, "yo", "up", 1, 5]), "yo",
        msg = 'should return the shortest string in a list that appears first when there are ties')


    def test_3(self):
        # it should return an empty string when the list is empty
        self.assertEqual(main.find_shortest_string_among_mixed_elements([]), "",
        msg = 'should return an empty string when the list is empty')


    def test_4(self):
        # it should return an empty string there are no strings
        self.assertEqual(main.find_shortest_string_among_mixed_elements([1, 2, 4]), "",
        msg = 'should return an empty string there are no strings')

```

### !end-tests

### !explanation
```python
def find_shortest_string_among_mixed_elements(lst):
    if not lst: return ""
    strings = [item for item in lst if type(item) is str]
    if not strings: return ""
    
    str_length, string = len(strings[0]), strings[0]
    for item in strings[1:]:
        if len(item) < str_length:
            str_length, string = len(item), item
    return string
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 0bbe947d-3174-4fe2-98c4-1a84331477d7
* title: find_smallest_number_among_mixed_elements

### !question

Write a function called "find_smallest_number_among_mixed_elements".

Given a list of mixed elements, "find_smallest_number_among_mixed_elements" returns the smallest integer within the given list.

Notes:
* If the given list is empty, it should return 0.
* If the list contains no numbers, it should return 0.

```
output = find_smallest_number_among_mixed_elements([4, 'lincoln', 9, 'octopus'])
print(output) # --> 4
```

### !end-question

### !placeholder

```python
# your code here


```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):
    def test_0(self):
        # it should return a number
        self.assertIsInstance(main.find_smallest_number_among_mixed_elements([3, 5, 3, 1]), (float, int),
        msg = 'should return a number')


    def test_1(self):
        # it should return the smallest element in a list
        self.assertEqual(main.find_smallest_number_among_mixed_elements([3, "string", 5, "up", 3, 1]), 1,
        msg = 'should return the smallest element in a list')


    def test_2(self):
        # it should return the smallest element in a list when there are ties
        self.assertEqual(main.find_smallest_number_among_mixed_elements(["string", 3, 1, 3, "wordy", "up", 1, 5]), 1,
        msg = 'should return the smallest element in a list when there are ties')


    def test_3(self):
        # it should return the smallest element in a list when they are all negative
        self.assertEqual(main.find_smallest_number_among_mixed_elements([-1, -5, "string", -3]), -5,
        msg = 'should return the smallest element in a list when they are all negative')


    def test_4(self):
        # it should return 0 when the list is empty
        self.assertEqual(main.find_smallest_number_among_mixed_elements([]), 0,
        msg = 'should return 0 when the list is empty')


    def test_5(self):
        # it should return 0 when there are no numbers
        self.assertEqual(main.find_smallest_number_among_mixed_elements(["string", "up"]), 0,
        msg = 'should return 0 when there are no numbers')


```

### !end-tests

### !explanation
```python
def find_smallest_number_among_mixed_elements(lst):
    if not lst: return 0
    numbers = [x for x in lst if type(x) is int]
    if not numbers: return 0
    return min(numbers)
```
### !end-explanation

### !end-challenge
