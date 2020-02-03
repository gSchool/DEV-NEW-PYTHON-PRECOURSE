# Objects 2

### !challenge

* type: code-snippet
* language: python3.6
* id: 56940947-7f0a-444b-bb8a-635464d92f45
* title: addFullName

### !question

Write a function called "addFullName".

Given an dictionary that has a "firstName" key and a "lastName" key, "addFullName" adds a "fullName" key whose value is a string with the first name and last name separated by a space.

```
person = {'firstName': 'Jaden', 'lastName': 'Smith'}
addFullName(person)

print(person['fullName']) # --> 'Jaden Smith'
```

### !end-question

### !placeholder

```python
def addFullName(dictionary):
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
        #it should create a fullName key in the dictionary with the firstName and lastName separated by a space
        person = {'firstName': 'Jaden', 'lastName': 'Smith'}
        main.addFullName(person)

        self.assertEqual(person['fullName'],
        'Jaden Smith',
        msg = "it should create a fullName key in the dictionary with value of a string with the firstName and lastName separated by a space")

    def test2(self):
        #it should preserve the original keys of the dictionary
        person = {'firstName': 'James', 'lastName': 'Bond'}
        main.addFullName(person)

        self.assertEqual(person['firstName'],
        'James',
        msg = "it should preserve the original keys of the dictionary")

        self.assertEqual(
            person['lastName'],'Bond', msg = "it should preserve the original keys of the dictionary")        

```


### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: c3b7ef25-71fe-47ff-9a75-2f9965695f31
* title: addDictionary

### !question

Write a function called "addDictionary".

Given two dictionaries and a key, "addDictionary" sets a new value on the 1st dictionary at the given key. The value of that new key is the entire 2nd dictionary.

```python
person1 = {'name': 'Homer Simpson', 'role': 'schlub'}
person2 = {'name': 'Mr. Burns', 'role': 'supervisor'}

result = addDictionary(person1, 'manager', person2)

type(result) # --> None
print(person1)
#--> {'name': 'Homer Simpson', 'role': 'schlub',
#     'manager': {'name': 'Mr. Burns', role: 'supervisor'}
#    }
```

### !end-question

### !placeholder

```python
def addDictionary(dict1, key, dict2):
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
        # "it should return None"
        dict1 = {'song': 'Psycho Killer'}
        dict2 = {'name': 'Talking Heads'}
        self.assertIs(main.addDictionary(dict1, 'artist', dict2), None,
        msg = "it should return None" )

    def test2(self):
        #it should set a new value on the 1st dictionary at the given key. The value of that new key is the entire 2nd dictionary.
        dict1 = {'song': 'Psycho Killer'}
        dict2 = {'name': 'Talking Heads'}
        main.addDictionary(dict1, 'artist', dict2)
        self.assertEqual(
            dict1['artist'],
            dict2,
            msg = "it should set a new value on the 1st dictionary at the given key. The value of that new key is the entire 2nd dictionary." )


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 67b64495-b5b3-4d3a-b3a2-7a471de45c03
* title: isPersonOldEnoughToDrinkAndDrive

### !question

Write a function called "isPersonOldEnoughToDrinkAndDrive".

Given a "person" dict, that contains the key "age", "isPersonOldEnoughToDrinkAndDrive" returns whether the given person is old enough to legally drink and drive in the United States.

Notes:
* The legal drinking age in the United States is 21.
* The legal driving age in the United States is 16.
* It is ALWAYS illegal to drink and drive in the United States.

```
person = {'age': 45}

output = isPersonOldEnoughToDrinkAndDrive(person)
print(output) # --> False
```

### !end-question

### !placeholder

```python
def isPersonOldEnoughToDrinkAndDrive(person):
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
        self.assertIs(type(main.isPersonOldEnoughToDrinkAndDrive({'age': 99})),
        bool,
        msg = "it should return a bool" )

    def test2(self):
        #it should always return false
        self.assertFalse(main.isPersonOldEnoughToDrinkAndDrive({'age': 99}),
        msg = "it should always return False" )

```


### !end-tests

### !explanation

### !end-explanation

### !end-challenge
