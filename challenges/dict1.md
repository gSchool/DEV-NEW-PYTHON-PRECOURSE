# Dictionary 1

### !challenge

* type: code-snippet
* language: python3.6
* id: 3469deaf-8010-4036-b39c-902d281a897e
* title: get_item

### !question

Write a function called "get_item".
Given an dictionary and a key, "get_item" returns the value of the given key.

```python
dictionary = {'key': 'value'}

output = get_item(dictionary, 'key')
print(output) # --> 'value'
```

### !end-question

### !placeholder

```python
def get_item(dictionary, key):
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
        self.assertEqual(main.get_item(dictionary, 'David'),
        dictionary['David'],
        msg = "it should return the value of the property located in the dict at the passed in key")

```

### !end-tests

### !explanation

```python
def get_item(dictionary, key):
    return dictionary[key]

```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 62b814e5-85d4-4d5b-8b5b-327692487625
* title: add_item

### !question

Write a function called "add_item".
Given an object, and a key, "add_item" adds a new key on the given dictionary with a value of True.

```python
dictionary = {}
add_item(dictionary, 'my_property')

print(my_dict['my_property']) # --> True
```

### !end-question

### !placeholder

```python
def add_item(dictionary, key):
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
        main.add_item(dictionary, 'my_key')
        self.assertTrue(dictionary['my_key'],
        msg = "it should add a property to the passed in dictionary at the passed in key that is equal to True" )

```


### !end-tests

### !explanation
```python
def add_item(dictionary, key):
    dictionary[key] = True


```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 89e3ad32-7097-4f1b-a4c8-445738b02a39
* title: remove_item

### !question

Write a function called "remove_item".
Given an object and a key, "remove_item" removes the given key from the given dict.

```
dictionary = {'name':'Sam', 'age': 20}
remove_item(dictionary, 'name')

print(dictionary) # --> {'age': 20}
print(dictionary.get('name')) # --> None
```

### !end-question

### !placeholder

```python
def remove_item(dictionary, key):
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
        main.remove_item(dictionary, 'name')

        self.assertIs(dictionary.get('name'), None,
        msg = "it should remove the property from the passed in dictionary at the passed in key" )
```


### !end-tests

### !explanation
```python
def remove_item(dictionary, key):
    dictionary[key] = None

```
### !end-explanation

### !end-challenge
