# Array Methods 9

### !challenge

* type: code-snippet
* language: python3.6
* id: f606fc41-1d59-4fa5-8d68-d95dfd88a02e
* title: filter_odd_length_words

### !question

Write a function called "filter_odd_length_words".

Given a list of strings, "filter_odd_length_words" returns a list containing only the elements of the given list whose lengths are odd numbers.

```
output = filter_odd_length_words(['there', 'it', 'is', 'now'])
print(output) # --> ['there', "now']
```

### !end-question

### !placeholder

```python
def filter_odd_length_words(words):
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
        self.assertIsInstance(main.filter_odd_length_words(["there", "it", "is", "now"]), list,
        msg = 'should return a list')


    def test_1(self):
        # it should return a list with only odd-length words
        self.assertEqual(main.filter_odd_length_words(["there", "it", "is", "now"]), ["there", "now"],
        msg = 'should return a list with only odd-length words')


    def test_2(self):
        # it should return an empty list when passed a list with no odd length words
        self.assertEqual(main.filter_odd_length_words(["it", "cats"]), [],
        msg = 'should return an empty list when passed a list with no odd length words')


    def test_3(self):
        # it should return an empty list when passed an empty list
        self.assertEqual(main.filter_odd_length_words([]), [],
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
* title: filter_even_length_words

### !question

Write a function called "filter_even_length_words".

Given a list of strings, "filter_even_length_words" returns a list containing only the elements of the given list whose length is an even number.

```
output = filter_even_length_words(['word', 'words', 'word', 'words'])
print(output) # --> ['word', 'word']
```

### !end-question

### !placeholder

```python
def filter_even_length_words(words):
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
        self.assertIsInstance(main.filter_even_length_words(["there", "it", "is", "now"]), list,
        msg = 'should return a list')


    def test_1(self):
        # it should return a list with even length words
        self.assertEqual(main.filter_even_length_words(["there", "it", "is", "now"]), ["it", "is"],
        msg = 'should return a list with even length words')


    def test_2(self):
        # it should return an empty list when passed a list with no even length words
        self.assertEqual(main.filter_even_length_words(["there", "now"]), [],
        msg = 'should return an empty list when passed a list with no even length words')


    def test_3(self):
        # it should return an empty list when passed an empty list
        self.assertEqual(main.filter_even_length_words([]), [],
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
* title: get_length_of_longest_element

### !question

Write a function called "get_length_of_longest_element".

Given a list, "get_length_of_longest_element" returns the length of the longest string in the given list.

Notes:
* It should return 0 if the list is empty.

```
output = get_length_of_longest_element(['one', 'two', 'three'])
print(output) # --> 5
```

### !end-question

### !placeholder

```python
def get_length_of_longest_element(arr):
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
            self.assertIsInstance(main.get_length_of_longest_element(["one", "two", "three"]), (float, int),
            msg = 'should return a number')


        def test_1(self):
            # it should return the length of the longest element in a list
            self.assertEqual(main.get_length_of_longest_element(["one", "two", "three"]), 5,
            msg = 'should return the length of the longest element in a list')


        def test_2(self):
            # it it should handle ties
            self.assertEqual(main.get_length_of_longest_element(["one", "two", "no"]), 3,
            msg = 'it should handle ties')


        def test_3(self):
            # it it should return 0 when given an empty list
            self.assertEqual(main.get_length_of_longest_element([]), 0,
            msg = 'it should return 0 when given an empty list')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
