# Conditionals 5

### !challenge

* type: code-snippet
* language: python3.6
* id: 9a167567-dfa8-4854-a21c-3d773b0c1ef5
* title: isOddLength

### !question

Write a function called "isOddLength".

Given a word, "isOddLength" returns whether the length of the given word is odd.

```
output = isOddLength('special')
print(output) # --> True

output = isOddLength('')
print(output) # --> False

```

### !end-question

### !placeholder

```python
def isOddLength(word):
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
        # it "should return a boolean"
        self.assertIs(type(main.isOddLength("wow")), bool, msg="it should return a boolean")

    def test2(self):
        #it "should return False if the length of the word is even"
        self.assertFalse(main.isOddLength("arrays"), msg="should return False if the length of the word is even")

    def test3(self):
        #it "should return True if the length of the word is odd"
        self.assertTrue(main.isOddLength("wow"), msg="should return True if the length of the word is odd")

    def test4(self):
        #it "should return False if the string is empty"
        self.assertFalse(main.isOddLength(''), msg="should return False if passed an empty string")
```


### !end-tests

### !explanation
```python
def isOddLength(word):
    return len(word) % 2 == 1

```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 3e56d53e-7025-45e4-a697-fd2851b6495d
* title: isEvenLength

### !question

Write a function called "isEvenLength".

Given a word, "isEvenLength" returns whether the length of the word is even.

```
output = isEvenLength('wow')
print(output) # --> False

output = isEvenLength('')
print(output) # --> True
```

### !end-question

### !placeholder

```python
def isEvenLength(word):
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
        # it "should return a boolean"
        self.assertIs(type(main.isEvenLength("wow")), bool, msg="it should return a boolean")

        def test2(self):
            #it "should return False if the length of the word is odd"
            self.assertFalse(main.isEvenLength("wow"), msg="should return False if the length of the word is even")

        def test3(self):
            #it "should return True if the length of the word is odd"
            self.assertTrue(main.isEvenLength("arrays"), msg="should return True if the length of the word is odd")

        def test4(self):
            #it "should return True if the string is empty"
            self.assertFalse(main.isEvenLength(''), msg="should return True if passed an empty string")
```


### !end-tests

### !explanation
```python
def isEvenLength(word):
    return len(word) % 2 == 0

```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 547a6787-3d47-4a09-83d6-ca86e7aa26c9
* title: isEvenAndGreaterThan10

### !question

Write a function called "isEvenAndGreaterThanTen".

Given a number, "isEvenAndGreaterThanTen" returns whether it is both even and greater than 10.

```
output = isEvenAndGreaterThanTen(13)
print(output) # --> False
```

### !end-question

### !placeholder

```python
def isEvenAndGreaterThanTen(num):
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
        # it should return a boolean
        self.assertIs(type(main.isEvenAndGreaterThanTen(40)), bool, msg="")

    def test2(self):
        #it "should return True if the number is even and greater than 10"
        self.assertTrue(main.isEvenAndGreaterThanTen(40), msg="should return True if the number is even and greater than 10")

    def test3(self):
        #it "should return False if the number is odd"
        self.assertFalse(main.isEvenAndGreaterThanTen(99), msg="it should return False if the number is odd")


    def test4(self):
        #it "should return False if the number is odd"
        self.assertFalse(main.isEvenAndGreaterThanTen(17), msg="it should return False if the number is odd")

    def test5(self):
        #it "should return False if the number is 10"
        self.assertFalse(main.isEvenAndGreaterThanTen(10), msg="it should return False if the number is 10")

    def test6(self):
        #it "should return False if the number is less than 10"
        self.assertFalse(main.isEvenAndGreaterThanTen(4), msg="it should return False if the number is less than 10")    

```

### !end-tests

### !explanation
```python
def isEvenAndGreaterThanTen(num):
    return num % 2 == 0 and num > 10


```
### !end-explanation

### !end-challenge
