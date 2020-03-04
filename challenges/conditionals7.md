# Conditionals 7

### !challenge

* type: code-snippet
* language: python3.6
* id: b99bc1a5-bc3a-42c5-9372-745bcbea92a7
* title: are_valid_credentials

### !question

Write a function called "are_valid_credentials".

Given a name and a password, "are_valid_credentials", returns True if the name is longer than 3 characters AND the password is at least 8 characters long. Otherwise it returns False.

```
output = are_valid_credentials('Ritu', 'mylongpassword')
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
        self.assertEqual(type(main.are_valid_credentials("Ritu", "mylongpassword")), bool,
        msg = 'should return a bool')


    def test_1(self):
        # it should return True if the name is longer than 3 characters and the password is at least 8 characters
        self.assertTrue(main.are_valid_credentials("Ritu", "mylongpassword"),
        msg = 'should return True if the name is longer than 3 characters and the password is at least 8 characters')


    def test_2(self):
        # it should return False if the name is less than 3 characters
        self.assertFalse(main.are_valid_credentials("me", "mylongpassword"),
        msg = 'should return False if the name is less than 3 characters')


    def test_3(self):
        # it should return False if the password is not at least 8 characters
        self.assertFalse(main.are_valid_credentials("Someone", "1234567"),
        msg = 'should return False if the password is not at least 8 characters')

```

### !end-tests

### !explanation
```python
def are_valid_credentials(name, password):
    return len(name) > 3 and len(password) > 8
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 705f1f9a-9afa-4ae7-be40-ddebbb95204b
* title: find_min_length_of_three_words

### !question

Write a function called "find_min_length_of_three_words".

Given 3 words, "find_min_length_of_three_words" returns the length of the shortest word.

```
output = find_min_length_of_three_words('a', 'be', 'see')
print(output) # --> 1
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
    def test_1(self):
        # it should return the minimum length of three words
        self.assertEqual(main.find_min_length_of_three_words("a", "be", "see"), 1,
        msg = 'should return the minimum length of three words')


    def test_2(self):
        # it should return the minimum length of three words when there is a tie
        self.assertEqual(main.find_min_length_of_three_words("these", "three", "words"), 5,
        msg = 'should return the minimum length of three words when there is a tie')

```

### !end-tests

### !explanation
```python
def find_min_length_of_three_words(word1, word2, word3):
    return min(len(word1), len(word2), len(word3))


```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: c3fcc0c8-628e-40aa-992a-a85008a3d60d
* title: find_max_length_of_three_words

### !question

Write a function called "find_max_length_of_three_words".

Given 3 words, "find_max_length_of_three_words" returns the length of the longest word.

```
output = find_max_length_of_three_words('a', 'be', 'see')
print(output) # --> 3
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

        def test_1(self):
            # it should return the maximum length of three words
            self.assertEqual(main.find_max_length_of_three_words("a", "be", "see"), 3,
            msg = 'should return the maximum length of three words')


        def test_2(self):
            # it should return the maximum length of three words when there is a tie
            self.assertEqual(main.find_max_length_of_three_words("these", "three", "words"), 5,
            msg = 'should return the maximum length of three words when there is a tie')
            
```

### !end-tests

### !explanation
```python
def find_max_length_of_three_words(word1, word2, word3):
    return max(len(word1), len(word2), len(word3))


```
### !end-explanation

### !end-challenge
