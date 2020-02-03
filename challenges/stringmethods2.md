# String Methods 2

### !challenge

* type: code-snippet
* language: python3.6
* id: e094a4bd-4b1a-4a9d-847b-634336385767
* title: compute_average_length_of_words

### !question

Write a function called "compute_average_length_of_words".

Given two words, "compute_average_length_of_words" returns the average of their lengths.

```
output = compute_average_length_of_words('code', 'programs')
print(output) # --> 6
```

### !end-question

### !placeholder

```python
def compute_average_length_of_words(word1, word2):
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
        #it should return the average length of the two words
        self.assertEqual(main.compute_average_length_of_words('code', 'programs'), 6,
        msg = "it should return the average length of the two words" )


```

### !end-tests

### !explanation
```python

def compute_average_length_of_words(word1, word2):
    return (len(word1) + len(word2)) / 2



```
### !end-explanation

### !end-challenge
