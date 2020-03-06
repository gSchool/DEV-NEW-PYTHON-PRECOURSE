### !challenge

* type: code-snippet
* language: python3.6
* id: 5c6e257b-c85d-4a59-9df2-777bc47d4d92
* title: convert_list_to_dict3

### !question

Write a function called "transform_employee_data" that transforms some employee data from one format to another.

```
input1 = 
[
    [['firstName', 'Joe'], ['lastName', 'Coltrane'], ['age', 42], ['role', 'clerk']],
    [['firstName', 'Sheila'], ['lastName', 'Jenkins'], ['age', 36], ['role', 'manager']]
]

output1 = transform_employee_data(input1)
print(output1)

[
{'firstName': 'Joe', 'lastName': 'Coltrane', 'age': 42, 'role': 'clerk'}, {'firstName': 'Sheila', 'lastName': 'Jenkins', 'age': 36, 'role': 'manager'}
]
```

```
input2 = 
[ 
    [['id', '4343F5X'], ['location', 'New York']],
    [['id', '2564F5X'], ['location', 'Berlin']]
]

output2 = transform_employee_data(input2)
print(output2)

[ 
    {'id':'4343N9X', 'location':'New York'},
    {'id':'2564B5B', 'location':'Berlin'}
]
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
    def test0(self):
        input1 = [[['firstName', 'Joe'], ['lastName', 'Blow'], ['age', 42], ['role', 'clerk']],
                [['firstName', 'Mary'], ['lastName', 'Jenkins'], ['age', 36], ['role', 'manager']]]
        try:
            main.transform_employee_data(input1)[0]
        except TypeError:
            self.fail('It should return a list of dictionaries')


    def test1(self):
        input1 = [[['firstName', 'Joe'], ['lastName', 'Blow'], ['age', 42], ['role', 'clerk']],
                [['firstName', 'Mary'], ['lastName', 'Jenkins'], ['age', 36], ['role', 'manager']]]
        self.assertIsInstance(main.transform_employee_data(input1),list,
        msg = "It should return a list of dictionaries")


    def test2(self):
        input1 = [[['firstName', 'Joe'], ['lastName', 'Blow'], ['age', 42], ['role', 'clerk']],
                [['firstName', 'Mary'], ['lastName', 'Jenkins'], ['age', 36], ['role', 'manager']]]
        try:
            main.transform_employee_data(input1)[0]['firstName']
            self.assertEqual(main.transform_employee_data(input1)[0]['firstName'],'Joe', msg = "should properly assign key and value pairs")
        except TypeError:
            self.fail("It should return a list of dictionaries")


    def test2(self):
        input1 = [[['firstName', 'Joe'], ['lastName', 'Blow'], ['favoriteIceCream', 'chocolate'], ['role', 'clerk']],
                       [['firstName', 'Carl'], ['lastName', 'Sagan'], ['favoriteIceCream', 'starfruit'], ['role', 'seer']],
                       [['firstName', 'Mary'], ['lastName', 'Jenkins'], ['favoriteIceCream', 'vanilla'], ['role', 'manager']]]
        try:
            main.transform_employee_data(input1)[0]['firstName']
            self.assertEqual(main.transform_employee_data(input1)[1]['favoriteIceCream'],'starfruit', msg = "should properly assign key and value pairs")
        except TypeError:
            self.fail("It should return a list of dictionaries")

```

### !end-tests

### !explanation
```python
# your code here

```
### !end-explanation

### !end-challenge
