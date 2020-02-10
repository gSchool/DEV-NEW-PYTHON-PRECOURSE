# String Methods 3

### !challenge

* type: code-snippet
* language: python3.6
* id: ebb36275-fc12-4110-8f39-9ef16ac2aeae
* title: get_length_of_three_words

### !question

Write a function called "get_length_of_three_words".

Given 3 words, "get_length_of_three_words" returns the sum of their lengths.

```
output = get_length_of_three_words('some', 'other', 'words')
print(output) # --> 14
```

### !end-question

### !placeholder

```python
#fill in the function definition below
# be sure to name the function according to the instructions


```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):
    def test2(self):
        # it should return the sum length of three words
        self.assertEqual(main.get_length_of_three_words("coffee","plus","data"), 14,
        msg = "it should return the sum length of three words " )

```

### !end-tests

### !explanation
```python
def get_length_of_three_words(word1, word2, word3):
    return len(word1 + word2 + word3)
```
### !end-explanation

### !end-challenge
