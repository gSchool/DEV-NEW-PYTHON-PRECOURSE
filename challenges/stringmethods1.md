# String Methods 1

### !challenge

* type: code-snippet
* language: python3.6
* id: 9a909a65-ed43-4747-ac79-18fb4a9eacc5
* title: get_full_name

### !question

Write a function called "get_full_name".
Given a first and a last name, "get_full_name" returns a single string with the given first and last names separated by a single space.

```
output = get_full_name('Joe', 'Smith')
print(output) # --> 'Joe Smith'
```

### !end-question

### !placeholder

```python

def get_full_name(firstName, lastName):
    # your code here
    pass




```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):
    def test1(self):
        # it should return a string
        self.assertIs(type(main.get_full_name("Harry", "Potter")), str,
        msg = "it should return a string" )

    def test2(self):
        #it should return a full name using firstName and lastName
        self.assertEqual(main.get_full_name("Albus", "Dumbledore"), "Albus Dumbledore", msg = "it should return a full name using firstName and lastName" )

```

### !end-tests

### !explanation
```python

def get_full_name(firstName, lastName):
    return f'{firstName} {lastName}'


```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: bba621c8-20e7-49e3-a5d3-30dd3fc58057
* title: get_length_of_word

### !question

Write a function called "get_length_of_word".
Given a word, "get_length_of_word" returns the length of the given word.

```
output = get_length_of_word('some')
print(output) # --> 4

output = get_length_of_word('')
print(output) # --> 0

```

### !end-question

### !placeholder

```python
def get_length_of_word(word):
    # your code here
    pass




```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):

    def test1(self):
        #it should return the length of the passed in word
        self.assertEqual(main.get_length_of_word("random"), 6, msg = "it should return the length of the passed in word" )

    def test2(self):
        #it should return the length of the passed in word
        self.assertEqual(main.get_length_of_word(""), 0, msg = "it should return the length of an empty word" )

```

### !end-tests

### !explanation
```python
def get_length_of_word(word):
    return len(word)

```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 37a022e4-9104-4ac9-b68b-b63377dd3cb8
* title: get_length_of_two_words

### !question

Write a function called "get_length_of_two_words".
Given 2 words, "get_length_of_two_words" returns the sum of their lengths.

```
output = get_length_of_two_words('some', 'words')
print(output) # --> 9


```

### !end-question

### !placeholder

```python
def get_length_of_two_words(word1, word2):
    # your code here
    pass

```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):

    def test1(self):
        #it should return the sum length of two words
        self.assertEqual(main.get_length_of_two_words('some', 'words'), 9,
        msg = "it should return the sum length of two words" )

    def test2(self):
        #it should return the sum length of two words if one is an empty string
        self.assertEqual(main.get_length_of_two_words('', 'words'), 5,
        msg = "it should return the sum length of two words if one is an empty string" )

```


### !end-tests

### !explanation
```python
def get_length_of_two_words(word1, word2):
    return len(word1) + len(word2)

```
### !end-explanation

### !end-challenge
