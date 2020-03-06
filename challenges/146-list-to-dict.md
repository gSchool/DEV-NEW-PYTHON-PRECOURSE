### !challenge

* type: code-snippet
* language: python3.6
* id: c27c7922-479a-41ca-a400-d3bc984468f4
* title: list_to_dict1

### !question


Write a function 'transform_first_and_last' that takes in a list, and returns a dictionary with:
* the first element of the list as the dictionary's key, and
* the last element of the list as that key's value.

Assume all elements in the input list will be of type 'string'.

Note that the input list may have a varying number of elements. Your code should flexibly accommodate that.

```
input1 = ['Kevin', 'Bacon', 'Love', 'Heart', 'Costner', 'Hart']
output = transform_first_and_last(input1)
print(output) #--> {'Kevin':'Hart'}

```

### !end-question

### !placeholder

```python

```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):

    def test1(self):
        self.assertIsInstance(main.transform_first_and_last(['Kevin', 'Bacon']),dict,
        msg = "It should return a dict")

    def test2(self):
        self.assertEqual(main.transform_first_and_last(['Kevin', 'Bacon', 'Love', 'Heart', 'Costner', 'Hart']), {'Kevin':'Hart'},
        msg = "should properly assign key and value pair")    

    def test3(self):
        input1 = ['Mars', 'Wayne', 'Mary']
        main.transform_first_and_last(input1)
        self.assertEqual(input1, ['Mars', 'Wayne', 'Mary'],
        msg = 'it should not modify input list')

```

### !end-tests

### !explanation
```python
def transform_first_and_last(lst):
    return {lst[0]:lst[-1]}
```
### !end-explanation

### !end-challenge
