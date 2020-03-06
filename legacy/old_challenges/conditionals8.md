# Conditionals 8

### !challenge

* type: code-snippet
* language: python3.6
* id: f328e513-d275-4a7b-aa70-b3ac917ce57a
* title: convertScoreToGrade

### !question

Write a function called "convertScoreToGrade".

Given a score, "convertScoreToGrade" returns a string representing the letter grade corresponding to the given score.

Notes:
* (100 - 90) --> 'A'
* (89  - 80) --> 'B'
* (79  - 70) --> 'C'
* (69  - 60) --> 'D'
* (59  -  0) --> 'F'
* If the given score is greater than 100 or less than 0, it should return 'INVALID SCORE'.

```
output = convertScoreToGrade(91)
print(output) # --> 'A'
```

### !end-question

### !placeholder

```python
def convertScoreToGrade(score):
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
        # it should return a string
        self.assertIsInstance(main.convertScoreToGrade(95), str,
        msg = 'should return a string')


    def test_1(self):
        # it should return 'A' for scores between 90 and 100
        self.assertEqual(main.convertScoreToGrade(95), "A",
        msg = "should return 'A' for scores between 90 and 100")


    def test_2(self):
        # it should return 'B' for scores between 80 and 89
        self.assertEqual(main.convertScoreToGrade(80), "B",
        msg = "should return 'B' for scores between 80 and 89")


    def test_3(self):
        # it should return 'C' for scores between 70 and 79
        self.assertEqual(main.convertScoreToGrade(79), "C",
        msg = "should return 'C' for scores between 70 and 79")


    def test_4(self):
        # it should return 'D' for scores between 60 and 69
        self.assertEqual(main.convertScoreToGrade(60), "D",
        msg = "should return 'D' for scores between 60 and 69")


    def test_5(self):
        # it should return 'F' for 59
        self.assertEqual(main.convertScoreToGrade(59), "F",
        msg = "should return 'F' for 59")


    def test_6(self):
        # it should return 'F' for scores between 0 and 59
        self.assertEqual(main.convertScoreToGrade(50), "F",
        msg = "should return 'F' for scores between 0 and 59")


    def test_7(self):
        # it should return 'F' for 0
        self.assertEqual(main.convertScoreToGrade(0), "F",
        msg = "should return 'F' for 0")


    def test_8(self):
        # it should return 'INVALID SCORE' for scores less than 0
        self.assertEqual(main.convertScoreToGrade(-1), "INVALID SCORE",
        msg = "should return 'INVALID SCORE' for scores less than 0")


    def test_9(self):
        # it should return 'INVALID SCORE' for scores greater than 100
        self.assertEqual(main.convertScoreToGrade(101), "INVALID SCORE",
        msg = "should return 'INVALID SCORE' for scores greater than 100")

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: d53cbbaf-dfb4-44ab-a0a9-9512018da2be
* title: convertScoreToGradeWithPlus

### !question

Write a function called "convertScoreToGradeWithPlusAndMinus".

Given a score, "convertScoreToGradeWithPlusAndMinus" returns a string representing the letter grade corresponding to the given score.

Notes:
* (100 - 90) --> 'A'
* (89  - 80) --> 'B'
* (79  - 70) --> 'C'
* (69  - 60) --> 'D'
* (59  -  0) --> 'F'
* If the given score is greater than 100 or less than 0, it should return 'INVALID SCORE'.
* If the score is between the 0 and 2 (inclusive) of a given range, return the letter with a '-'
* If the score is be the 8 and 9 (inclusive) of a given range, return the letter with a '+'
* There are is no F+ and there is no F-.

```
output = convertScoreToGradeWithPlusAndMinus(91)
print(output) # --> 'A-'
```

### !end-question

### !placeholder

```python
def convertScoreToGradeWithPlusAndMinus(score):
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
        # it should return a string
        self.assertIsInstance(main.convertScoreToGradeWithPlusAndMinus(95), str,
        msg = 'should return a string')


    def test_1(self):
        # it should return 'A+' for scores between 98 and 100
        self.assertEqual(main.convertScoreToGradeWithPlusAndMinus(100), "A+",
        msg = 'should return "A+" for scores between 98 and 100')


    def test_2(self):
        # it should return 'A-' for scores between 90 and 92
        self.assertEqual(main.convertScoreToGradeWithPlusAndMinus(90), "A-",
        msg = 'should return "A-" for scores between 90 and 92')


    def test_3(self):
        # it should return 'A' for scores between 93 and 97
        self.assertEqual(main.convertScoreToGradeWithPlusAndMinus(95), "A",
        msg = 'should return "A" for scores between 93 and 97')


    def test_4(self):
        # it should return 'B+' for scores between 88 and 89
        self.assertEqual(main.convertScoreToGradeWithPlusAndMinus(89), "B+",
        msg = 'should return "B+" for scores between 88 and 89')


    def test_5(self):
        # it should return 'B-' for scores between 80 and 82
        self.assertEqual(main.convertScoreToGradeWithPlusAndMinus(80), "B-",
        msg = 'should return "B-" for scores between 80 and 82')


    def test_6(self):
        # it should return 'B' for scores between 83 and 87
        self.assertEqual(main.convertScoreToGradeWithPlusAndMinus(84), "B",
        msg = 'should return "B" for scores between 83 and 87')


    def test_7(self):
        # it should return 'C+' for scores between 78 and 79
        self.assertEqual(main.convertScoreToGradeWithPlusAndMinus(79), "C+",
        msg = 'should return "C+" for scores between 78 and 79')


    def test_8(self):
        # it should return 'C-' for scores between 70 and 72
        self.assertEqual(main.convertScoreToGradeWithPlusAndMinus(70), "C-",
        msg = 'should return "C-" for scores between 70 and 72')


    def test_9(self):
        # it should return 'C' for scores between 73 and 77
        self.assertEqual(main.convertScoreToGradeWithPlusAndMinus(76), "C",
        msg = 'should return "C" for scores between 73 and 77')


    def test_10(self):
        # it should return 'D+' for scores between 68 and 69
        self.assertEqual(main.convertScoreToGradeWithPlusAndMinus(69), "D+",
        msg = 'should return "D+" for scores between 68 and 69')


    def test_11(self):
        # it should return 'D' for scores between 63 and 67
        self.assertEqual(main.convertScoreToGradeWithPlusAndMinus(64), "D",
        msg = 'should return "D" for scores between 63 and 67')


    def test_12(self):
        # it should return 'D-' for scores between 60 and 62
        self.assertEqual(main.convertScoreToGradeWithPlusAndMinus(60), "D-",
        msg = 'should return "D-" for scores between 60 and 62')


    def test_13(self):
        # it should return 'F' for scores between 0 and 59
        self.assertEqual(main.convertScoreToGradeWithPlusAndMinus(0), "F",
        msg = 'should return "F" for scores between 0 and 59')


    def test_14(self):
        # it should return 'INVALID SCORE' for scores less than 0
        self.assertEqual(main.convertScoreToGradeWithPlusAndMinus(-1), "INVALID SCORE",
        msg = 'should return "INVALID SCORE" for scores less than 0')


    def test_15(self):
        # it should return 'INVALID SCORE' for scores greater than 100
        self.assertEqual(main.convertScoreToGradeWithPlusAndMinus(101), "INVALID SCORE",
        msg = 'should return "INVALID SCORE" for scores greater than 100')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
