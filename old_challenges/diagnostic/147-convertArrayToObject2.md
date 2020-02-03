### !challenge

* type: code-snippet
* language: python3.6
* id: 877a8e09-fe8e-4e6d-b5c1-8163dcbaff47
* title: convertArrayToObject2.md

### !question

Write a function 'fromListToObject' which takes in a list of lists, and returns a dictionary with each pair of elements in the list as a key-value pair.

Example input:
```
input1 = [['make', 'Ford'], ['model', 'Mustang'], ['year', 1964]]
output = fromListToObject(input1)

print(output)  
# -> {'make' : 'Ford', 'model' : 'Mustang', 'year' : 1964}

```

Do not mutate the input. Assume that all elements in the list will be of type 'str'.

Note that the input may have a different number of elements than the given sample.
For instance, if the input had 6 pairs of values instead of 3, your code should flexibly accommodate that.

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
        self.assertIsInstance(main.fromListToObject([['Kevin', 'Bacon']]),dict,
        msg = "It should return a dict")

    def test2(self):
        self.assertEqual(main.fromListToObject([
        ['Kevin', 'Bacon'],[ 'Denzel', 'Washington'],[ 'Uma', 'Thurman']]),
         {'Kevin': 'Bacon', 'Denzel':'Washington', 'Uma':'Thurman' },
        msg = "should properly assign key and value pairs")    

    def test3(self):
        input1 =  [['firstName', 'John'], ['lastName', 'McClane'], ['occupation', 'law enforcement'], ['spouse', 'Holly Gennaro McClane']]
        main.fromListToObject(input1)
        self.assertEqual(input1, [['firstName', 'John'], ['lastName', 'McClane'], ['occupation', 'law enforcement'], ['spouse', 'Holly Gennaro McClane']],
        msg = 'it should not modify input list')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
