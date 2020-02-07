# String Methods 3

### !challenge

* type: code-snippet
* language: python3.6
* id: ebb36275-fc12-4110-8f39-9ef16ac2aeae
* title: getLengthOfThreeWords

### !question

Write a function called "getLengthOfThreeWords".

Given 3 words, "getLengthOfThreeWords" returns the sum of their lengths.

```
output = getLengthOfThreeWords('some', 'other', 'words')
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
        self.assertEqual(main.getLengthOfThreeWords("coffee","plus","data"), 14,
        msg = "it should return the sum length of three words " )

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
