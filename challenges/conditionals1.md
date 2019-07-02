# Conditionals 1

### !challenge

* type: code-snippet
* language: python3.6
* id: bbd9c4ac-32ee-4474-b697-35173143e155
* title: isOldEnoughToDrink

### !question

Write a function called "isOldEnoughToDrink".
Given a number, in this case an age, "isOldEnoughToDrink" returns whether a person of this given age is old enough to legally drink in the United States.
Notes:
* The legal drinking age in the United States is 21.

```
output = isOldEnoughToDrink(22)
print(output) # --> True
```

### !end-question

### !placeholder

```python

def isOldEnoughToDrink(age):
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
        #it "should return True if the age is greater than 21"
        self.assertTrue(main.isOldEnoughToDrink(40),"should return True if age is greater than 21")

    def test2(self):
        #it "should return true if the age is 21"
        self.assertTrue(main.isOldEnoughToDrink(21),"should return True if age is 21")

    def test3(self):
        #it "should return false if the age is 20"
        self.assertFalse(main.isOldEnoughToDrink(20),"should return False if age is less than 21")

```

### !end-tests

### !explanation

```python
def isOldEnoughToDrink(age):
    return age >= 21
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 4b181e05-9f6d-4e2d-beaa-ad80ab8d3c26
* title: isOldEnoughToDrive

### !question

Write a function called "isOldEnoughToDrive".
Given a number, in this case an age, "isOldEnoughToDrive" returns whether a person of this given age is old enough to legally drive in the United States.
Notes:
* The legal driving age in the United States is 16.

```
output = isOldEnoughToDrive(22)
print(output) # --> True
```

### !end-question

### !placeholder

```python
def isOldEnoughToDrive(age):
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
        #it "should return true if the age is 16"
        self.assertTrue(main.isOldEnoughToDrive(16),"it should return True if the age greater than or equal to 16")

    def test2(self):
        #it "should return false if the age is less than 16"
        self.assertFalse(main.isOldEnoughToDrive(15),"it should return False if the age is under 16")
```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 8aa5586d-36c6-4677-bd29-bbadd91027b8
* title: isOldEnoughToVote

### !question

Write a function called "isOldEnoughToVote".
Given a number, in this case an age, 'isOldEnoughToVote' returns whether a person of this given age is old enough to legally vote in the United States.
Notes:
* The legal voting age in the United States is 18.

```
output = isOldEnoughToVote(22)
print(output) # --> True
```

### !end-question

### !placeholder

```python
def isOldEnoughToVote(age):
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
        #it "should return whether the age is greater than 18"
        self.assertTrue(main.isOldEnoughToVote(19), "should return True if age is greater than 18")

    def test2(self):
        #it "should return true if the age is 18"
        self.assertTrue(main.isOldEnoughToVote(18), "should return True if age is 18")

    def test3(self):
        #it "should return false if the age is under 18"
        self.assertFalse(main.isOldEnoughToVote(17), "should return False if age is under 18")     
```


### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 4031a186-73da-4384-95c9-8d8510aa67a9
* title: isOldEnoughToDrinkAndDrive

### !question

Write a function called "isOldEnoughToDrinkAndDrive".
Given a number, in this case an age, "isOldEnoughToDrinkAndDrive" returns whether a person of this given age is old enough to legally drink and drive in the United States.
Notes:
* The legal drinking age in the United States is 21.
* It is always illegal to drink and drive in the United States.

```
output = isOldEnoughToDrinkAndDrive(22)
print(output) # --> False
```

### !end-question

### !placeholder

```python
def isOldEnoughToDrinkAndDrive(age):
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
        # it "should return false"
        self.assertFalse(main.isOldEnoughToDrinkAndDrive(99), "No one is old enough to drink and drive.")
```


### !end-tests

### !explanation

### !end-explanation

### !end-challenge
