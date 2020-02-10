# list Methods 7

### !challenge

* type: code-snippet
* language: python3.6
* id: d5349d84-2036-435e-a352-d996dffc92e3
* title: join_three_lists

### !question

Write a function called "join_three_lists".

Given three lists, "join_three_lists" returns an list with the elements of "list1" in order followed by the elements in "list2" in order followed by the elements of "list3" in order.

```
output = join_three_lists([1, 2], [3, 4], [5, 6])
print(output) # --> [1, 2, 3, 4, 5, 6]
```


### !end-question

### !placeholder

```python
def join_three_lists(list1, list2, list3):
    # your code here
    pass


```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):

    def test_0(self):
        # it should return an list
        self.assertIsInstance(main.join_three_lists(['a', 'b'], [1, 3], [True, False]), list,
        msg = 'should return a list')


    def test_1(self):
        # it should return an list with the elements from the first and then the second list
        self.assertEqual(main.join_three_lists(['a', 'b'], [1, 3], [True, False]), ['a', 'b', 1, 3, True, False],
        msg = 'should return a list with the elements from the first and then the second list')


    def test_2(self):
        # it should handle empty lists in the first position
        self.assertEqual(main.join_three_lists([], [1, 3], [True, False]), [1, 3, True, False],
        msg = 'should handle empty list in the first position')


    def test_3(self):
        # it should handle empty lists in the second position
        self.assertEqual(main.join_three_lists(['a', 'b'], [], [True, False]), ['a', 'b', True, False],
        msg = 'should handle empty list in the second position')


    def test_4(self):
        # it should handle empty lists in the third position
        self.assertEqual(main.join_three_lists(['a', 'b'], [1, 3], []), ['a', 'b', 1, 3],
        msg = 'should handle empty list in the third position')


    def test_5(self):
        # it should handle empty lists in all positions
        self.assertEqual(main.join_three_lists([], [], []), [],
        msg = 'should handle empty lists in all positions')


```

### !end-tests

### !explanation
```python
def join_three_lists(list1, list2, list3):
    return list1 + list2 + list3
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: a5d9e27b-ea2f-4134-ad30-ef9366b3c761
* title: add_to_front_of_new

### !question

Write a function called "add_to_front_of_new".

Given a list and an element, "add_to_front_of_new" returns a new list containing all the elements of the given list, with the given element added to the front.

Important: It should be a NEW list instance, not the original list instance.

```
list1 = [1, 2]
output = add_to_front_of_new(list1, 3)
print(output) # --> [3, 1, 2]
print(list1) --> [1, 2]
```

### !end-question

### !placeholder

```python
def add_to_front_of_new(list1, element):
    # your code here
    pass


```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):

    def test_0(self):
        # it should return an list
        self.assertIsInstance(main.add_to_front_of_new([1, 2], 3), list,
        msg = 'should return a list')


    def test_1(self):
        # it should add an element to the end of an list
        self.assertEqual(main.add_to_front_of_new([1, 2], 3), [3, 1, 2],
        msg = 'should add an element to the front of an list')


    def test_2(self):
        # it should add an element to the end of an empty list
        self.assertEqual(main.add_to_front_of_new([], 3), [3],
        msg = 'should add an element to the front of an empty list')


    def test_3(self):
        # it should leave list unmodified
        originalList = [1,2]
        main.add_to_front_of_new(originalList, 3)
        self.assertEqual(originalList, [1, 2],
        msg = 'should leave the original list unmodified')
```

### !end-tests

### !explanation
```python
def add_to_front_of_new(list1, element):
    result = list1[:] # makes a new distinct copy of the original list
    result.insert(0,element)
    return result
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 52e8002f-f926-4b68-b70b-c41fe566ba8c
* title: add_to_back_of_new

### !question

Write a function called "addToBackNew".

Given an list and an element, "addToBackNew" returns a clone of the given list, with the given element added to the end.

Important: It should be a NEW list instance, not the original list instance.

```
list1 = [1, 2]
output = add_to_back_of_new(list1, 3)
print(list1) # --> [1, 2]
print(output) # --> [1, 2, 3]
```

### !end-question

### !placeholder

```python
def add_to_back_of_new(list1, element):
    # your code here
    pass


```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):

    def test_0(self):
        # it should return an list
        self.assertIsInstance(main.add_to_back_of_new([1, 2], 3), list,
        msg = 'should return a list')


    def test_1(self):
        # it should add an element to the end of an list
        self.assertEqual(main.add_to_back_of_new([1, 2], 3), [1, 2, 3],
        msg = 'should add an element to the end of an list')


    def test_2(self):
        # it should add an element to the end of an empty list
        self.assertEqual(main.add_to_back_of_new([], 3), [3],
        msg = 'should add an element to the end of an empty list')


    def test_3(self):
        # it should leave lst unmodified
        originalList = [1,2]
        main.add_to_back_of_new(originalList, 3)
        self.assertEqual(originalList, [1, 2],
        msg = 'should leave original list unmodified')

```

### !end-tests

### !explanation
```python
def add_to_back_of_new(list1, element):
    result = list1[:]
    result.append(element)
    return result
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: dac91596-8674-4ea2-a348-db7120c0fe36
* title: get_all_elements_but_nth

### !question

Write a function called "get_all_elements_but_nth".

Given an list and an index, "get_all_elements_but_nth" returns a new list with all the elements but the nth.

Note: DO NOT MUTATE THE ORIGINAL LIST

```
list1 = ['a', 'b', 'c']
output = get_all_elements_but_nth(list1, 1)
print(output) # --> ['a', 'c']
print(list1) # --> ['a', 'b', 'c']

output = get_all_elements_but_nth(['a', 'b', 'c'], 8)
print(output) # --> ['a', 'b', 'c']
print(list1) # --> ['a', 'b', 'c']

```

### !end-question

### !placeholder

```python
def get_all_elements_but_nth(list1, n):
    # your code here
    pass


```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):

        def test_0(self):
            # it should return a list
            self.assertIsInstance(main.get_all_elements_but_nth([4, 5, 6], 2), list,
            msg = 'should return a list')


        def test_1(self):
            # it should return an list with all the elements of the passed in list, except for the nth
            self.assertEqual(main.get_all_elements_but_nth([4, 5, 6], 0), [5, 6],
            msg = 'should return an list with all the elements of the passed in list, except for the nth')


        def test_2(self):
            # it should return an empty list when passed in a single element list
            self.assertEqual(main.get_all_elements_but_nth([4], 0), [],
            msg = 'should return an empty list when passed in a single element list')


        def test_3(self):
            # it should return a mirror of the original list when passed an n out of range
            self.assertEqual(main.get_all_elements_but_nth([4], 10), [4],
            msg = 'should return a mirror of the original list when passed an n out of range')


        def test_4(self):
            # it should return an empty list when passed in an empty list
            self.assertEqual(main.get_all_elements_but_nth([],0), [],
            msg = 'should return an empty list when passed in an empty list')

```

### !end-tests

### !explanation
```python
def get_all_elements_but_nth(list1, n):
    result = list1[:]
    if len(list1) >= n + 1:
        result.pop(n)
    return result
```
### !end-explanation

### !end-challenge
