# String Methods 1

### !challenge

* type: code-snippet
* language: python3.6
* id: 9a909a65-ed43-4747-ac79-18fb4a9eacc5
* title: getFullName

### !question

Write a function called "getFullName".
Given a first and a last name, "getFullName" returns a single string with the given first and last names separated by a single space.

```
output = getFullName('Joe', 'Smith')
print(output) # --> 'Joe Smith'
```

### !end-question

### !placeholder

```python

def getFullName(firstName, lastName):
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
        self.assertIs(type(main.getFullName("Harry", "Potter")), str,
        msg = "it should return a string" )

    def test2(self):
        #it should return a full name using firstName and lastName
        self.assertEqual(main.getFullName("Albus", "Dumbledore"), "Albus Dumbledore", msg = "it should return a full name using firstName and lastName" )

```

### !end-tests

### !explanation
```python

def getFullName(firstName, lastName):
    return f'{firstName} {lastName}'


```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: bba621c8-20e7-49e3-a5d3-30dd3fc58057
* title: getLengthOfWord

### !question

Write a function called "getLengthOfWord".
Given a word, "getLengthOfWord" returns the length of the given word.

```
output = getLengthOfWord('some')
print(output) # --> 4

output = getLengthOfWord('')
print(output) # --> 0

```

### !end-question

### !placeholder

```python
def getLengthOfWord(word):
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
        self.assertEqual(main.getLengthOfWord("random"), 6, msg = "it should return the length of the passed in word" )

    def test2(self):
        #it should return the length of the passed in word
        self.assertEqual(main.getLengthOfWord(""), 0, msg = "it should return the length of an empty word" )

```

### !end-tests

### !explanation
```python
def getLengthOfWord(word):
    return len(word)

```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 37a022e4-9104-4ac9-b68b-b63377dd3cb8
* title: getLengthOfTwoWords

### !question

Write a function called "getLengthOfTwoWords".
Given 2 words, "getLengthOfTwoWords" returns the sum of their lengths.

```
output = getLengthOfTwoWords('some', 'words')
print(output) # --> 9


```

### !end-question

### !placeholder

```python
def getLengthOfTwoWords(word1, word2):
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
        self.assertEqual(main.getLengthOfTwoWords('some', 'words'), 9,
        msg = "it should return the sum length of two words" )

    def test2(self):
        #it should return the sum length of two words if one is an empty string
        self.assertEqual(main.getLengthOfTwoWords('', 'words'), 5,
        msg = "it should return the sum length of two words if one is an empty string" )

```


### !end-tests

### !explanation
```python
def getLengthOfTwoWords(word1, word2):
    return len(word1) + len(word2)

```
### !end-explanation

### !end-challenge
