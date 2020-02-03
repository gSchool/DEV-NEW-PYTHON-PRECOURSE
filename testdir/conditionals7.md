# Conditionals 7

### !challenge

* type: code-snippet
* language: python3.6
* id: b99bc1a5-bc3a-42c5-9372-745bcbea92a7
* title: areValidCredentials

### !question

Write a function called "areValidCredentials".

Given a name and a password, "areValidCredentials", returns True if the name is longer than 3 characters AND the password is at least 8 characters long. Otherwise it returns False.

```
output = areValidCredentials('Ritu', 'mylongpassword')
print(output) # --> True
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
        # it should return a boolean
        self.assertEqual(type(main.areValidCredentials("Ritu", "mylongpassword")), bool,
        msg = 'should return a bool')


    def test_1(self):
        # it should return True if the name is longer than 3 characters and the password is at least 8 characters
        self.assertTrue(main.areValidCredentials("Ritu", "mylongpassword"),
        msg = 'should return True if the name is longer than 3 characters and the password is at least 8 characters')


    def test_2(self):
        # it should return False if the name is less than 3 characters
        self.assertFalse(main.areValidCredentials("me", "mylongpassword"),
        msg = 'should return False if the name is less than 3 characters')


    def test_3(self):
        # it should return False if the password is not at least 8 characters
        self.assertFalse(main.areValidCredentials("Someone", "1234567"),
        msg = 'should return False if the password is not at least 8 characters')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 705f1f9a-9afa-4ae7-be40-ddebbb95204b
* title: findMinLengthOfThreeWords

### !question

Write a function called "findMinLengthOfThreeWords".

Given 3 words, "findMinLengthOfThreeWords" returns the length of the shortest word.

```
output = findMinLengthOfThreeWords('a', 'be', 'see')
print(output) # --> 1
```

### !end-question

### !placeholder

```python
def findMinLengthOfThreeWords(word1, word2, word3):
    # your code here
    pass


```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):
    def test_1(self):
        # it should return the minimum length of three words
        self.assertEqual(main.findMinLengthOfThreeWords("a", "be", "see"), 1,
        msg = 'should return the minimum length of three words')


    def test_2(self):
        # it should return the minimum length of three words when there is a tie
        self.assertEqual(main.findMinLengthOfThreeWords("these", "three", "words"), 5,
        msg = 'should return the minimum length of three words when there is a tie')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: c3fcc0c8-628e-40aa-992a-a85008a3d60d
* title: findMaxLengthOfThreeWords

### !question

Write a function called "findMaxLengthOfThreeWords".

Given 3 words, "findMaxLengthOfThreeWords" returns the length of the longest word.

```
output = findMaxLengthOfThreeWords('a', 'be', 'see')
print(output) # --> 3
```

### !end-question

### !placeholder

```python
def findMaxLengthOfThreeWords(word1, word2, word3):
    # your code here
    pass


```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):

        def test_1(self):
            # it should return the maximum length of three words
            self.assertEqual(main.findMaxLengthOfThreeWords("a", "be", "see"), 3,
            msg = 'should return the maximum length of three words')


        def test_2(self):
            # it should return the maximum length of three words when there is a tie
            self.assertEqual(main.findMaxLengthOfThreeWords("these", "three", "words"), 5,
            msg = 'should return the maximum length of three words when there is a tie')
            
```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
