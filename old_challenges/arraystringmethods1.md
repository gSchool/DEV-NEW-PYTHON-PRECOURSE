# Array String Methods 1

### !challenge

* type: code-snippet
* language: python3.6
* id: 7efe888f-b6e0-4255-933e-0f6f12bfe7f2
* title: getAllLetters

### !question

Write a function called "getAllLetters".

Given a word, "getAllLetters" returns an array containing every character in the word.

Notes:
* If given an empty string, it should return an empty array.

```
output = getAllLetters('Radagast')
print(output) # --> ['R', 'a', 'd', 'a', 'g', 'a', 's', 't']
```

### !end-question

### !placeholder

```python
def getAllLetters(string):
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
        # it should return an array
        self.assertIsInstance(main.getAllLetters("something like this here"), list,
        msg = 'should return an array')


    def test_1(self):
        # it should return an array containing all the letters in the word
        self.assertEqual(main.getAllLetters("Eowin"), ["E", "o", "w", "i", "n"],
        msg = 'should return a list containing all the letters in the word')


    def test_2(self):
        # it should return an empty array when given an empty string
        self.assertEqual(main.getAllLetters(""), [],
        msg = 'should return an empty array when given an empty string')


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: afe8bb31-31d2-4ef6-b344-e7cbcfe01d1f
* title: getAllWords

### !question

Write a function called "getAllWords".

Given a sentence, "getAllWords" returns an array containing every word in the sentence.

Notes:
* If given an empty string, it should return an empty array.

```
output = getAllWords('Radagast the Brown')
print(output) # --> ['Radagast', 'the', 'Brown']
```

### !end-question

### !placeholder

```python
def getAllWords(string):
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
            # it should return an array
            self.assertIsInstance(main.getAllWords("something like this here"), list,
            msg = 'should return a list')


        def test_1(self):
            # it should return an array containing all the words in the sentence
            self.assertEqual(main.getAllWords("Something like this here"), ["Something", "like", "this", "here"],
            msg = 'should return a list containing all the words in the sentence')


        def test_2(self):
            # it should return an empty array when given an empty string
            self.assertEqual(main.getAllWords(""), [],
            msg = 'should return an empty list when given an empty string')


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
