### !challenge

* type: code-snippet
* language: python3.6
* id: 5c6e257b-c85d-4a59-9df2-777bc47d4d92
* title: convertArrayToObject3.md

### !question

Write a function called "transformEmployeeData" that transforms some employee data from one format to another.

The argument will look like this:

```
[
    [
        ['firstName', 'Joe'], ['lastName', 'Blow'], ['age', 42], ['role', 'clerk']
    ],
    [
        ['firstName', 'Mary'], ['lastName', 'Jenkins'], ['age', 36], ['role', 'manager']
    ]
]
```

Given that input, the return value should look like this:

```
[
    {'firstName': 'Joe', 'lastName': 'Blow', 'age': 42, 'role': 'clerk'},
    {'firstName': 'Mary', 'lastName': 'Jenkins', 'age': 36, 'role': 'manager'}
]
```

Note that the input may have a different number of rows or different keys than the given sample.

For example, let's say the HR department adds a "tshirtSize" field to each employee record.
Your code should flexibly accommodate that.

### !end-question

### !placeholder

```python
def transformEmployeeData(employeeData):
    # your code here
    pass

```

### !end-placeholder

### !tests


```python
import main
import unittest

class TestScript(unittest.TestCase):
    def test0(self):
        input1 = [[['firstName', 'Joe'], ['lastName', 'Blow'], ['age', 42], ['role', 'clerk']],
                [['firstName', 'Mary'], ['lastName', 'Jenkins'], ['age', 36], ['role', 'manager']]]
        try:
            main.transformEmployeeData(input1)[0]
        except TypeError:
            self.fail('It should return a list of dictionaries')


    def test1(self):
        input1 = [[['firstName', 'Joe'], ['lastName', 'Blow'], ['age', 42], ['role', 'clerk']],
                [['firstName', 'Mary'], ['lastName', 'Jenkins'], ['age', 36], ['role', 'manager']]]
        self.assertIsInstance(main.transformEmployeeData(input1),list,
        msg = "It should return a list of dictionaries")


    def test2(self):
        input1 = [[['firstName', 'Joe'], ['lastName', 'Blow'], ['age', 42], ['role', 'clerk']],
                [['firstName', 'Mary'], ['lastName', 'Jenkins'], ['age', 36], ['role', 'manager']]]
        try:
            main.transformEmployeeData(input1)[0]['firstName']
            self.assertEqual(main.transformEmployeeData(input1)[0]['firstName'],'Joe', msg = "should properly assign key and value pairs")
        except TypeError:
            self.fail("It should return a list of dictionaries")


    def test2(self):
        input1 = [[['firstName', 'Joe'], ['lastName', 'Blow'], ['favoriteIceCream', 'chocolate'], ['role', 'clerk']],
                       [['firstName', 'Carl'], ['lastName', 'Sagan'], ['favoriteIceCream', 'starfruit'], ['role', 'seer']],
                       [['firstName', 'Mary'], ['lastName', 'Jenkins'], ['favoriteIceCream', 'vanilla'], ['role', 'manager']]]
        try:
            main.transformEmployeeData(input1)[0]['firstName']
            self.assertEqual(main.transformEmployeeData(input1)[1]['favoriteIceCream'],'starfruit', msg = "should properly assign key and value pairs")
        except TypeError:
            self.fail("It should return a list of dictionaries")

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
