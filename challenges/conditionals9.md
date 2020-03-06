# Conditionals 9

### !challenge

* type: code-snippet
* language: python3.6
* id: a51b922c-0c0b-42b1-b372-f57a7e3cc12e
* title: get_longest_of_three_words

### !question

Write a function called "get_longest_of_three_words".

Given 3 words, "get_longest_of_three_words" returns the longest of three words.

Notes:
* If there is a tie, it should return the first word in the tie.

```
output = get_longest_of_three_words('these', 'three', 'words')
print(output) # --> 'these'
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
        self.assertIsInstance(main.get_longest_of_three_words("a", "be", "see"), str,
        msg = 'should return a string')


    def test_1(self):
        # it should return the longest of three words
        self.assertEqual(main.get_longest_of_three_words("a", "be", "see"), "see",
        msg = 'should return the longest of three words')


    def test_2(self):
        # it should return the first occurrence of a longest word when there is a tie
        self.assertEqual(main.get_longest_of_three_words("these", "three", "words"), "these",
        msg = 'should return the first occurrence of a longest word when there is a tie')

```

### !end-tests

### !explanation
```python
def get_longest_of_three_words(word1, word2, word3):
    other_words = word2, word3
    result, max_length = word1, len(word1)
    for word in other_words:
        if len(word) > max_length:
            result, max_length = word, len(word)
    return result
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: e70b8323-50dd-4588-a4c7-56138c5c4bdd
* title: find_shortest_of_three_words

### !question

Write a function called "find_shortest_of_three_words".

Given 3 strings, "find_shortest_of_three_words" returns the shortest of the given strings.

Notes:
* If there are ties, it should return the first word in the parameters list.

```
output = find_shortest_of_three_words('a', 'two', 'three')
print(output) # --> 'a'
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
        self.assertIsInstance(main.find_shortest_of_three_words("a", "be", "see"), str,
        msg = 'should return a string')


    def test_1(self):
        # it should return the shortest of three words
        self.assertEqual(main.find_shortest_of_three_words("abacus", "be", "see"), "be",
        msg = 'should return the shortest of three words')


    def test_2(self):
        # it should return the first occurrence of a shortest word when there is a tie
        self.assertEqual(main.find_shortest_of_three_words("these", "apple", "words"), "these",
        msg = 'should return the first occurrence of a shortest word when there is a tie')
```

### !end-tests

### !explanation
```python
def find_shortest_of_three_words(word1, word2, word3):
    other_words = word2, word3
    result, min_length = word1, len(word1)
    for word in other_words:
        if len(word) < min_length:
            result, min_length = word, len(word)
    return result
```
### !end-explanation

### !end-challenge
