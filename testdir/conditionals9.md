# Conditionals 9

### !challenge

* type: code-snippet
* language: python3.6
* id: a51b922c-0c0b-42b1-b372-f57a7e3cc12e
* title: getLongestOfThreeWords

### !question

Write a function called "getLongestOfThreeWords".

Given 3 words, "getLongestOfThreeWords" returns the longest of three words.

Notes:
* If there is a tie, it should return the first word in the tie.

```
output = getLongestOfThreeWords('these', 'three', 'words')
print(output) # --> 'these'
```

### !end-question

### !placeholder

```python
def getLongestOfThreeWords(word1, word2, word3):
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
        self.assertIsInstance(main.getLongestOfThreeWords("a", "be", "see"), str,
        msg = 'should return a string')


    def test_1(self):
        # it should return the longest of three words
        self.assertEqual(main.getLongestOfThreeWords("a", "be", "see"), "see",
        msg = 'should return the longest of three words')


    def test_2(self):
        # it should return the first occurrence of a longest word when there is a tie
        self.assertEqual(main.getLongestOfThreeWords("these", "three", "words"), "these",
        msg = 'should return the first occurrence of a longest word when there is a tie')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: e70b8323-50dd-4588-a4c7-56138c5c4bdd
* title: findShortestOfThreeWords

### !question

Write a function called "findShortestOfThreeWords".

Given 3 strings, "findShortestOfThreeWords" returns the shortest of the given strings.

Notes:
* If there are ties, it should return the first word in the parameters list.

```
output = findShortestOfThreeWords('a', 'two', 'three')
print(output) # --> 'a'
```

### !end-question

### !placeholder

```python
def findShortestOfThreeWords(word1, word2, word3):
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
        self.assertIsInstance(main.findShortestOfThreeWords("a", "be", "see"), str,
        msg = 'should return a string')


    def test_1(self):
        # it should return the shortest of three words
        self.assertEqual(main.findShortestOfThreeWords("abacus", "be", "see"), "be",
        msg = 'should return the shortest of three words')


    def test_2(self):
        # it should return the first occurrence of a shortest word when there is a tie
        self.assertEqual(main.findShortestOfThreeWords("these", "apple", "words"), "these",
        msg = 'should return the first occurrence of a shortest word when there is a tie')
```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
