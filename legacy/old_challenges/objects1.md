# Objects 1

### !challenge

* type: code-snippet
* language: python3.6
* id: 3469deaf-8010-4036-b39c-902d281a897e
* title: getProperty

### !question

Write a function called "getProperty".
Given an dictionary and a key, "getProperty" returns the value of the property at the given key.

```python
dictionary = {'key': 'value'}

output = getProperty(dictionary, 'key')
print(output) # --> 'value'
```

### !end-question

### !placeholder

```python
def getProperty(dictionary, key):
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
        #"it should return the value of the property located in the dict at the passed in key"
        dictionary = {'David': 'Bowie'}
        self.assertEqual(main.getProperty(dictionary, 'David'),
        dictionary['David'],
        msg = "it should return the value of the property located in the dict at the passed in key")

```

### !end-tests

### !explanation

```python
def getProperty(dictionary, key):
    return dictionary[key]

```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 62b814e5-85d4-4d5b-8b5b-327692487625
* title: addProperty

### !question

Write a function called "addProperty".
Given an object, and a key, "addProperty" sets a new property on the given dictionary with a value of True.

```python
dictionary = {}
addProperty(dictionary, 'my_property')

print(my_dict['my_property']) # --> True
```

### !end-question

### !placeholder

```python
def addProperty(dictionary, key):
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
        #it should add a property to the passed in dictionary at the passed in key that is equal to True
        dictionary = {}
        main.addProperty(dictionary, 'my_key')
        self.assertTrue(dictionary['my_key'],
        msg = "it should add a property to the passed in dictionary at the passed in key that is equal to True" )

```


### !end-tests

### !explanation
```python
def addProperty(dictionary, key):
    dictionary[key] = True


```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 89e3ad32-7097-4f1b-a4c8-445738b02a39
* title: removeProperty

### !question

Write a function called "removeProperty".
Given an object and a key, "removeProperty" removes the given key from the given object.

```
dictionary = {'name':'Sam', 'age': 20}
removeProperty(dictionary, 'name')

print(dictionary) # --> {'age': 20}
print(dictionary.get('name')) # --> None
```

### !end-question

### !placeholder

```python
def removeProperty(dictionary, key):
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
        # it "should remove the property from the passed in dictionary at the passed in key"
        dictionary = {'name': 'James Bond', 'license':'007'}
        main.removeProperty(dictionary, 'name')

        self.assertIs(dictionary.get('name'), None,
        msg = "it should remove the property from the passed in dictionary at the passed in key" )
```


### !end-tests

### !explanation
```python
def removeProperty(dictionary, key):
    dictionary[key] = None

```
### !end-explanation

### !end-challenge
