### !challenge

* type: code-snippet
* language: python3.6
* id: c27c7922-479a-41ca-a400-d3bc984468f4
* title: convertArrayToObject1.md

### !question


Write a function 'transformFirstAndLast' that takes in a list, and returns a dictionary with:
1) the first element of the list as the dictionary's key, and
2) the last element of the list as that key's value.

Do not change the input list. Assume all elements in the input list will be of type 'string'.

Note that the input list may have a varying number of elements. Your code should flexibly accommodate that.

```
input1 = ['Kevin', 'Bacon', 'Love', 'Heart', 'Costner', 'Hart']
output = transformFirstAndLast(input1)
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
        self.assertIsInstance(main.transformFirstAndLast(['Kevin', 'Bacon']),dict,
        msg = "It should return a dict")

    def test2(self):
        self.assertEqual(main.transformFirstAndLast(['Kevin', 'Bacon', 'Love', 'Heart', 'Costner', 'Hart']), {'Kevin':'Hart'},
        msg = "should properly assign key and value pair")    

    def test3(self):
        input1 = ['Mars', 'Wayne', 'Mary']
        main.transformFirstAndLast(input1)
        self.assertEqual(input1, ['Mars', 'Wayne', 'Mary'],
        msg = 'it should not modify input list')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
