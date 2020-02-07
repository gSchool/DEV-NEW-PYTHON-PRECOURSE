# Array String Methods 2

### !challenge

* type: code-snippet
* language: python3.6
* id: d27d4372-5782-4123-8b80-e060455dd96e
* title: convertDoubleSpaceToSingle

### !question

Write a function called "convertDoubleSpaceToSingle".

Given a string, "convertDoubleSpaceToSingle" returns the passed in string, with all the double spaces converted to single spaces.

```
output = convertDoubleSpaceToSingle("string  with  double  spaces")
print(output) # --> "string with double spaces"

output = convertDoubleSpaceToSingle("")
print(output) # --> ""
````

Notes:
* In order to do this problem, you should be familiar with "str.split", and the "join" methods.


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
        self.assertEqual(type(main.convertDoubleSpaceToSingle("This  here sentence")), str,
        msg = 'should return a string')

    def test_1(self):
        # it should return the passed in string, with any double spaces converted to single spaces
        self.assertEqual(main.convertDoubleSpaceToSingle("this  here  string"), "this here string",
        msg = 'should return the passed in string, with any double spaces converted to single spaces')


    def test_2(self):
        # it should return the passed in string when there are no double spaces
        self.assertEqual(main.convertDoubleSpaceToSingle("this here string"), "this here string",
        msg = 'should return the passed in string when there are no double spaces')

    def test_3(self):
        # it should return an empty string when passed an empty string
        self.assertEqual(main.convertDoubleSpaceToSingle(""), "",
        msg = 'should return an empty string when passed an empty string')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
