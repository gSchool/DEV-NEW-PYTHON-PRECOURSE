# List Methods 16

### !challenge

* type: code-snippet
* language: python3.6
* id: 99c43844-c828-47d6-a073-db33a9f9bfb7
* title: get_longest_word_of_mixed_elements

### !question

Write a function called "get_longest_string_of_mixed_elements".

Given a list of mixed types, "get_longest_string_of_mixed_elements" returns the longest string in the given list.

Notes:
* The list might contain values of a type other than strings.
* If the list is empty, it should return an empty string ("").
* If the list contains no strings it should return an empty string.

```
output = get_longest_string_of_mixed_elements([3, 'string', 5, 'up', 3, 1])
print(output) # --> 'string'
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
        # it should return a string
        self.assertIsInstance(main.get_longest_string_of_mixed_elements(["these", "are", "strings"]), str,
        msg = 'should return a string')


    def test_1(self):
        # it should return the longest string in a list
        self.assertEqual(main.get_longest_string_of_mixed_elements([3, "string", 5, "up", 3, 1]), "string",
        msg = 'should return the longest string in a list')


    def test_2(self):
        # it should return the longest string in a list that appears first when there are ties
        self.assertEqual(main.get_longest_string_of_mixed_elements(["string", 3, 5, 3, "bird", "up", 1, 5]), "string",
        msg = 'should return the longest string in a list that appears first when there are ties')


    def test_3(self):
        # it should return an empty string when the list is empty
        self.assertEqual(main.get_longest_string_of_mixed_elements([]), "",
        msg = 'should return an empty string when the list is empty')


    def test_4(self):
        # it should return an empty string there are no strings
        self.assertEqual(main.get_longest_string_of_mixed_elements([1, 2, 4]), "",
        msg = 'should return an empty string there are no strings')

```

### !end-tests

### !explanation
```python
def get_longest_string_of_mixed_elements(lst):
    if not lst: return ""
    strings = [x for x in lst if type(x) is str]
    if not strings: return ""
    
    max_len, longest_string = 0, ""
    for string in strings:
        if len(string) > max_len:
            max_len, longest_string = len(string), string
    return longest_string


```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: c73e353f-8655-42e8-8f6b-7e342182ca9c
* title: get_largest_number_among_mixed_elements

### !question

Write a function called "get_largest_number_among_mixed_elements".

Given any list, "get_largest_number_among_mixed_elements" returns the largest integer in the given list.

Notes:
* The list will contain integers and strings.
* If the list is empty, it should return 0.
* If the list contains no integers, it should return 0.

```
output = get_largest_number_among_mixed_elements([3, 'string', 5, 'up', 3, 1])
print(output) # --> 5
```

### !end-question

### !placeholder

```python
def get_largest_number_among_mixed_elements(lst):
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
        self.assertIsInstance(main.get_largest_number_among_mixed_elements([3, 5, 3, 1]), (float, int),
        msg = 'should return a number')


    def test_1(self):
        # it should return the largest element in a list
        self.assertEqual(main.get_largest_number_among_mixed_elements([3, "string", 5, "up", 3, 1]), 5,
        msg = 'should return the largest element in a list')


    def test_2(self):
        # it should return the largest element in a list when there are ties
        self.assertEqual(main.get_largest_number_among_mixed_elements(["string", 3, 5, 3, "wordy", "up", 1, 5]), 5,
        msg = 'should return the largest element in a list when there are ties')


    def test_3(self):
        # it should return the largest element in a list when they are all negative
        self.assertEqual(main.get_largest_number_among_mixed_elements([-1, -5, "word", -3]), -1,
        msg = 'should return the largest element in a list when they are all negative')


    def test_4(self):
        # it should return 0 when the list is empty
        self.assertEqual(main.get_largest_number_among_mixed_elements([]), 0,
        msg = 'should return 0 when the list is empty')


    def test_5(self):
        # it should return 0 when there are no numbers
        self.assertEqual(main.get_largest_number_among_mixed_elements(["word", "up"]), 0,
        msg = 'should return 0 when there are no numbers')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
