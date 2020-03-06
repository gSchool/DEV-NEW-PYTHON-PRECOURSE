### !challenge

* type: code-snippet
* language: python3.6
* id: 1c684aae-9cf8-4c7b-907f-eb1e88a7084d
* title: greet_customers

### !question

Write a function called "greet_customers".

Given a name string and a customer data dictionary, "greet_customers" returns a greeting string based on how many times that customer has visited the restaurant.  Please refer to the following sample dictionary.

Suppose the customer data is given by:
```
customer_data = 
{'Joe': {'visits': 1},
  'Carol': {'visits': 2},
  'Howard': {'visits': 3},
  'Carrie': {'visits': 4}
}
```
The greeting should be different, depending on the name on their reservation.

Case 1 - Unknown customer ( Name is not present in customer_data ):

```
output = greet_customers('Terrance', customer_data)
print(output) # --> 'Welcome! Is this your first time?'

```

Case 2 - Customer who has visited only once ( 'visits' value is 1 ):

```
output = greet_customers('Joe', customer_data)
print(output) # --> 'Welcome back, Joe! We're glad you liked us the first time!'

```

Case 3 - Repeat customer: ( 'visits' value is greater than 1 ):

```
output = greet_customers('Carol', customer_data)
print(output) # --> 'Welcome back, Carol! So glad to see you again!'

```

Notes:
* Your function does not need to alter the customer_data dictionary to update the number of visits.
Your program will be tested on different sample data.


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
    def test_00(self):
        self.data = {'Alice': {'visits': 1},
          'Bob': {'visits': 2},
          'David': {'visits': 14}}
        self.assertIsInstance(main.greet_customers('Voldemort', self.data),
        str,
        msg = "it should return a string")

    def test_0(self):
        self.data = {'Alice': {'visits': 1},
          'Bob': {'visits': 2},
          'David': {'visits': 14}}
        self.assertEqual(main.greet_customers('Voldemort', self.data),
        'Welcome! Is this your first time?',
        msg = "should properly greet a brand new customer")

    def test_1(self):
        self.data = {'Alice': {'visits': 1},
          'Bob': {'visits': 2},
          'David': {'visits': 14}}
        self.assertEqual(main.greet_customers('Alice', self.data),
        "Welcome back, Alice! We're glad you liked us the first time!",
        msg = "should properly greet a customer who has 1 visit")

    def test_2(self):
        self.data = {'Alice': {'visits': 1},
          'Bob': {'visits': 2},
          'David': {'visits': 14}}
        self.assertEqual(main.greet_customers('Bob', self.data),
        'Welcome back, Bob! So glad to see you again!',
        msg = "should properly greet a customer who has 2 visits")

    def test_3(self):
        self.data = {'Alice': {'visits': 1},
          'Bob': {'visits': 2},
          'David': {'visits': 14}}
        self.assertEqual(main.greet_customers('David', self.data),
        'Welcome back, David! So glad to see you again!',
        msg = "should properly greet a customer who has more than 2 visits")

```

### !end-tests

### !explanation
```python

```
### !end-explanation

### !end-challenge
