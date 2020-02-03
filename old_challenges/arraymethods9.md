# Array Methods 9

### !challenge

* type: code-snippet
* language: python3.6
* id: f606fc41-1d59-4fa5-8d68-d95dfd88a02e
* title: filterOddLengthWords

### !question

Write a function called "filterOddLengthWords".

Given a list of strings, "filterOddLengthWords" returns a list containing only the elements of the given list whose lengths are odd numbers.

```
output = filterOddLengthWords(['there', 'it', 'is', 'now'])
print(output) # --> ['there', "now']
```

### !end-question

### !placeholder

```python
def filterOddLengthWords(words):
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
        self.assertIsInstance(main.filterOddLengthWords(["there", "it", "is", "now"]), list,
        msg = 'should return a list')


    def test_1(self):
        # it should return a list with only odd-length words
        self.assertEqual(main.filterOddLengthWords(["there", "it", "is", "now"]), ["there", "now"],
        msg = 'should return a list with only odd-length words')


    def test_2(self):
        # it should return an empty list when passed a list with no odd length words
        self.assertEqual(main.filterOddLengthWords(["it", "cats"]), [],
        msg = 'should return an empty list when passed a list with no odd length words')


    def test_3(self):
        # it should return an empty list when passed an empty list
        self.assertEqual(main.filterOddLengthWords([]), [],
        msg = 'should return an empty list when passed an empty list')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 1beb59a5-644c-4508-922f-4d8b4910bf77
* title: filterEvenLengthWords

### !question

Write a function called "filterEvenLengthWords".

Given a list of strings, "filterEvenLengthWords" returns a list containing only the elements of the given list whose length is an even number.

```
output = filterEvenLengthWords(['word', 'words', 'word', 'words'])
print(output) # --> ['word', 'word']
```

### !end-question

### !placeholder

```python
def filterEvenLengthWords(words):
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
        self.assertIsInstance(main.filterEvenLengthWords(["there", "it", "is", "now"]), list,
        msg = 'should return a list')


    def test_1(self):
        # it should return a list with even length words
        self.assertEqual(main.filterEvenLengthWords(["there", "it", "is", "now"]), ["it", "is"],
        msg = 'should return a list with even length words')


    def test_2(self):
        # it should return an empty list when passed a list with no even length words
        self.assertEqual(main.filterEvenLengthWords(["there", "now"]), [],
        msg = 'should return an empty list when passed a list with no even length words')


    def test_3(self):
        # it should return an empty list when passed an empty list
        self.assertEqual(main.filterEvenLengthWords([]), [],
        msg = 'should return an empty list when passed an empty list')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: bed00f94-4f5c-4a82-8cfa-7eaf872368f5
* title: getLengthOfLongestElement

### !question

Write a function called "getLengthOfLongestElement".

Given a list, "getLengthOfLongestElement" returns the length of the longest string in the given list.

Notes:
* It should return 0 if the list is empty.

```
output = getLengthOfLongestElement(['one', 'two', 'three'])
print(output) # --> 5
```

### !end-question

### !placeholder

```python
def getLengthOfLongestElement(arr):
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
            self.assertIsInstance(main.getLengthOfLongestElement(["one", "two", "three"]), (float, int),
            msg = 'should return a number')


        def test_1(self):
            # it should return the length of the longest element in a list
            self.assertEqual(main.getLengthOfLongestElement(["one", "two", "three"]), 5,
            msg = 'should return the length of the longest element in a list')


        def test_2(self):
            # it it should handle ties
            self.assertEqual(main.getLengthOfLongestElement(["one", "two", "no"]), 3,
            msg = 'it should handle ties')


        def test_3(self):
            # it it should return 0 when given an empty list
            self.assertEqual(main.getLengthOfLongestElement([]), 0,
            msg = 'it should return 0 when given an empty list')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
