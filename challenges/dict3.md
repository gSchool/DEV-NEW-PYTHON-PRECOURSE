# Objects 3

### !challenge

* type: code-snippet
* language: python3.6
* id: eea9cf06-5305-4626-8955-00e5d02563fb
* title: is_person_old_enough_to_drive

### !question

Write a function called "is_person_old_enough_to_drive".

Given a "person" dict, that contains an "age" key, "is_person_old_enough_to_drive" returns whether the given person is old enough to drive.

Notes:
* The legal driving age in the United States is 16.

```
person = {'age': 16}

output = is_person_old_enough_to_drive(person)
print(output) # --> True
```

### !end-question

### !placeholder

```python
def is_person_old_enough_to_drive(person):
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
        self.assertIs(type(main.is_person_old_enough_to_drive({'age': 99})), bool,
        msg = "it should return a bool" )


    def test2(self):
        #it should return True if a person has an age of over 16
        self.assertTrue(main.is_person_old_enough_to_drive({'age': 17}),
        msg = "it should return True if a person has an age of over 16")

    def test3(self):
        #it should return True if a person has an age of over 16
        self.assertTrue(main.is_person_old_enough_to_drive({'age': 16}),
        msg = "it should return True if a person has an age of 16")

    def test4(self):
        #it should return True if a person has an age of over 16
        self.assertFalse(main.is_person_old_enough_to_drive({'age': 9}),
        msg = "it should return False if a person has an age of under 16")

```

### !end-tests

### !explanation
```python
def is_person_old_enough_to_drive(person):
    return person['age'] >= 16
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 6b52bff0-742b-4c12-b361-03d5e7457084
* title: is_person_old_enough_to_vote

### !question

Write a function called "is_person_old_enough_to_vote".

Given a "person" dictionary, that contains a key called "age", "is_person_old_enough_to_vote" returns whether the given person is old enough to vote.

Notes:
* The legal voting age in the United States is 18.

```
dictionary = {'age' 19}

output = is_person_old_enough_to_vote(dictionary)
print(output) # --> True
```

### !end-question

### !placeholder

```python
def is_person_old_enough_to_vote(person):
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
        self.assertIs(type(main.is_person_old_enough_to_vote({'age': 18})), bool,
        msg = "it should return a bool" )

    def test3(self):
        #"should return True if a person has an age of over 18"
        self.assertTrue(main.is_person_old_enough_to_vote({'age': 99}),
        msg = "it should return True if a person has an age of over 18" )

    def test3(self):
        #"it should return True if a person has an age of 18"
        self.assertTrue(main.is_person_old_enough_to_vote({'age': 18}),
        msg = "it should return True if a person has an age of 18" )

    def test3(self):
        #"it should return False if a person has an age of under 18"
        self.assertFalse(main.is_person_old_enough_to_vote({'age': 8}),
        msg = "it should return False if a person has an age of under 18" )

```

### !end-tests

### !explanation
```python
def is_person_old_enough_to_vote(person):
    return person['age'] >= 18
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 53bb0534-cafa-44a2-85ce-1d450e1f79ef
* title: add_list_to_dict

### !question

Write a function called "add_list_to_dict".

Given an dict, a key, and an list, "add_list_to_dict" sets a new value on the dictionary at the given key, with the value set to the given list.

```
mydict = {'name': 'Smiley'}
mylist = [1, 3]

result = add_list_to_dict(myDict, 'key', mylist)
type(result) #-> NoneType
print(mydict['key']) # --> [1, 3]
print(mydict['name']) # --> 'Smiley'
```

### !end-question

### !placeholder

```python
def add_list_to_dict(dictionary, key, arr):
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
        self.assertIs(main.add_list_to_dict({}, "testKey", [1,3,5]), None,
        msg = "it should return None")

    def test2(self):
        #it should set the value at the passed in key on the passed in dict to be the passed in array"
        dictionary = {}
        main.add_list_to_dict(dictionary, "testKey", [1,3,5])

        self.assertEqual(dictionary["testKey"],[1,3,5],
        msg = "it should set the value at the passed in key on the passed in dict to be the passed in array")

    def test3(self):
        #it should set the value at the passed in key on the passed in dict to be the passed in array and keep the other keys unchanged"
        dictionary = {'key1': 'key1', 'key2': 'key2'}
        main.add_list_to_dict(dictionary, "testKey", [1,3,5])

        self.assertEqual(dictionary['key1'],'key1',
        msg = "it should set the value at the passed in key on the passed in dict to be the passed in array and keep the other keys unchanged")

        self.assertEqual(dictionary['key2'],'key2',
        msg = "it should set the value at the passed in key on the passed in dict to be the passed in array and keep the other keys unchanged")

```

### !end-tests

### !explanation
```python
def add_list_to_dict(dictionary, key, arr):
    dictionary[key] = arr
```
### !end-explanation

### !end-challenge
