# List String Methods 2

### !challenge

* type: code-snippet
* language: python3.6
* id: d27d4372-5782-4123-8b80-e060455dd96e
* title: convert_double_space_to_single

### !question

Write a function called "convert_double_space_to_single".

Given a string, "convert_double_space_to_single" returns the passed in string, with all the double spaces converted to single spaces.

Given an empty string, "convert_double_space_to_single" should return an empty string.

```
output = convert_double_space_to_single("string  with  double  spaces")
print(output) # --> "string with double spaces"

output = convert_double_space_to_single("")
print(output) # --> ""
````

Notes:
* In order to do this problem, you should be familiar with "str.split", and the "str.join" methods.


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
        self.assertEqual(type(main.convert_double_space_to_single("This  here sentence")), str,
        msg = 'should return a string')

    def test_1(self):
        # it should return the passed in string, with any double spaces converted to single spaces
        self.assertEqual(main.convert_double_space_to_single("this  here  string"), "this here string",
        msg = 'should return the passed in string, with any double spaces converted to single spaces')


    def test_2(self):
        # it should return the passed in string when there are no double spaces
        self.assertEqual(main.convert_double_space_to_single("this here string"), "this here string",
        msg = 'should return the passed in string when there are no double spaces')

    def test_3(self):
        # it should return an empty string when passed an empty string
        self.assertEqual(main.convert_double_space_to_single(""), "",
        msg = 'should return an empty string when passed an empty string')

```

### !end-tests

### !explanation
```python
def convert_double_space_to_single(string):
    temp = string.split("  ") # two spaces between quotes
    return " ".join(temp) # one space between quotes
```
### !end-explanation

### !end-challenge
