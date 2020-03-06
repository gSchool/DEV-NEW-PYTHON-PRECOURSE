### !challenge

* type: code-snippet
* language: python3.6
* id: 1c684aae-9cf8-4c7b-907f-eb1e88a7084d
* title: greetCustomer.md

### !question

Write a function called "greetCustomers".

Given a name string and a customerData dictionary, "greetCustomers" returns a greeting string based on how many times that customer has visited the restaurant.  Please refer to the following sample customerData dictionary.

Suppose the customer data is given by:
```
customerData = {'Joe': {'visits': 1},
  'Carol': {'visits': 2},
  'Howard': {'visits': 3},
  'Carrie': {'visits': 4}}
```
The greeting should be different, depending on the name on their reservation.

Case 1 - Unknown customer ( Name is not present in customerData ):

```
output = greetCustomer('Terrance', customerData)
print(output) # --> 'Welcome! Is this your first time?'

```

Case 2 - Customer who has visited only once ( 'visits' value is 1 ):

```
output = greetCustomer('Joe', customerData)
print(output) # --> 'Welcome back, Joe! We're glad you liked us the first time!'

```

Case 3 - Repeat customer: ( 'visits' value is greater than 1 ):

```
output = greetCustomer('Carol', customerData)
print(output) # --> 'Welcome back, Carol! So glad to see you again!'

```

Notes:
* Your function should NOT alter the customerData dictionary to update the number of visits.
* Do NOT hardcode to the exact sample data!
Your program will be tested on different sample data!

* You cannot do something like this:
```
if (firstName === 'Joe'):  # do something

```
It won't work , because YOUR FUNCTION MIGHT BE
TESTED ON A CUSTOMER DICTIONARY THAT DOES NOT HAVE 'JOE' in it.


### !end-question

### !placeholder

```python

def greetCustomer(firstName, customerData):
    # your code here
    pass

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
        self.assertIsInstance(main.greetCustomer('Voldemort', self.data),
        str,
        msg = "it should return a string")

    def test_0(self):
        self.data = {'Alice': {'visits': 1},
          'Bob': {'visits': 2},
          'David': {'visits': 14}}
        self.assertEqual(main.greetCustomer('Voldemort', self.data),
        'Welcome! Is this your first time?',
        msg = "should properly greet a brand new customer")

    def test_1(self):
        self.data = {'Alice': {'visits': 1},
          'Bob': {'visits': 2},
          'David': {'visits': 14}}
        self.assertEqual(main.greetCustomer('Alice', self.data),
        "Welcome back, Alice! We're glad you liked us the first time!",
        msg = "should properly greet a customer who has 1 visit")

    def test_2(self):
        self.data = {'Alice': {'visits': 1},
          'Bob': {'visits': 2},
          'David': {'visits': 14}}
        self.assertEqual(main.greetCustomer('Bob', self.data),
        'Welcome back, Bob! So glad to see you again!',
        msg = "should properly greet a customer who has 2 visits")

    def test_3(self):
        self.data = {'Alice': {'visits': 1},
          'Bob': {'visits': 2},
          'David': {'visits': 14}}
        self.assertEqual(main.greetCustomer('David', self.data),
        'Welcome back, David! So glad to see you again!',
        msg = "should properly greet a customer who has more than 2 visits")

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
