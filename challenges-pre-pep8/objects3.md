# Objects 3

### !challenge

* type: code-snippet
* language: python3.6
* id: eea9cf06-5305-4626-8955-00e5d02563fb
* title: isPersonOldEnoughToDrive

### !question

Write a function called "isPersonOldEnoughToDrive".

Given a "person" dict, that contains an "age" key, "isPersonOldEnoughToDrive" returns whether the given person is old enough to drive.

Notes:
* The legal driving age in the United States is 16.

```
person = {'age': 16}

output = isPersonOldEnoughToDrive(person)
print(output) # --> True
```

### !end-question

### !placeholder

```python
def isPersonOldEnoughToDrive(person):
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
        # it should return a bool
        self.assertIs(type(main.isPersonOldEnoughToDrive({'age': 99})), bool,
        msg = "it should return a bool" )


    def test2(self):
        #it should return True if a person has an age of over 16
        self.assertTrue(main.isPersonOldEnoughToDrive({'age': 17}),
        msg = "it should return True if a person has an age of over 16")

    def test3(self):
        #it should return True if a person has an age of over 16
        self.assertTrue(main.isPersonOldEnoughToDrive({'age': 16}),
        msg = "it should return True if a person has an age of 16")

    def test4(self):
        #it should return True if a person has an age of over 16
        self.assertFalse(main.isPersonOldEnoughToDrive({'age': 9}),
        msg = "it should return False if a person has an age of under 16")

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 6b52bff0-742b-4c12-b361-03d5e7457084
* title: isPersonOldEnoughToVote

### !question

Write a function called "isPersonOldEnoughToVote".

Given a "person" dictionary, that contains a key called "age", "isPersonOldEnoughToVote" returns whether the given person is old enough to vote.

Notes:
* The legal voting age in the United States is 18.

```
dictionary = {'age' 19}

output = isPersonOldEnoughToVote(dictionary)
print(output) # --> True
```

### !end-question

### !placeholder

```python
def isPersonOldEnoughToVote(person):
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
        # it
        self.assertIs(type(main.isPersonOldEnoughToVote({'age': 18})), bool,
        msg = "it should return a bool" )

    def test3(self):
        #"should return True if a person has an age of over 18"
        self.assertTrue(main.isPersonOldEnoughToVote({'age': 99}),
        msg = "it should return True if a person has an age of over 18" )

    def test3(self):
        #"it should return True if a person has an age of 18"
        self.assertTrue(main.isPersonOldEnoughToVote({'age': 18}),
        msg = "it should return True if a person has an age of 18" )

    def test3(self):
        #"it should return False if a person has an age of under 18"
        self.assertFalse(main.isPersonOldEnoughToVote({'age': 8}),
        msg = "it should return False if a person has an age of under 18" )

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 53bb0534-cafa-44a2-85ce-1d450e1f79ef
* title: addArrayToDict

### !question

Write a function called "addArrayToDict".

Given an dict, a key, and an array, "addArrayToDict" sets a new value on the dictionary at the given key, with the value set to the given array.

```
myDict = {'name': 'Smiley'}
myArray = [1, 3]

result = addArrayToDict(myDict, 'key', myArray)
type(result) #-> NoneType
print(myDict['key']) # --> [1, 3]
print(myDict['name']) # --> 'Smiley'
```

### !end-question

### !placeholder

```python
def addArrayToDict(dictionary, key, arr):
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
        # it should return None
        self.assertIs(main.addArrayToDict({}, "testKey", [1,3,5]), None,
        msg = "it should return None")

    def test2(self):
        #it should set the value at the passed in key on the passed in dict to be the passed in array"
        dictionary = {}
        main.addArrayToDict(dictionary, "testKey", [1,3,5])

        self.assertEqual(dictionary["testKey"],[1,3,5],
        msg = "it should set the value at the passed in key on the passed in dict to be the passed in array")

    def test3(self):
        #it should set the value at the passed in key on the passed in dict to be the passed in array and keep the other keys unchanged"
        dictionary = {'key1': 'key1', 'key2': 'key2'}
        main.addArrayToDict(dictionary, "testKey", [1,3,5])

        self.assertEqual(dictionary['key1'],'key1',
        msg = "it should set the value at the passed in key on the passed in dict to be the passed in array and keep the other keys unchanged")

        self.assertEqual(dictionary['key2'],'key2',
        msg = "it should set the value at the passed in key on the passed in dict to be the passed in array and keep the other keys unchanged")

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
