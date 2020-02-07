# Advanced 1

### !challenge

* type: local-snippet
* language: javascript
* id: 6507106d-7850-4631-a2d6-19b34da62bad
* title: countWords

### !question

Write a function called "countWords".

Given a string, "countWords" returns an object where each key is a word in the given string, with its value being how many times that word appeared in the given string.

Notes:
* If given an empty string, it should return an empty object.

```
var output = countWords('ask a bunch get a bunch');
console.log(output); // --> {ask: 1, a: 2, bunch: 2, get: 1}
```

### !end-question

### !placeholder

```js
function countWords(str) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("countWords", function() {
  it("should return an object", function() {
    expect(typeof countWords("ask a bunch try a bunch get a bunch")).to.deep.eq("object");
  });
  it("should return an object where each property gives a word in the string, with its number of appearances", function() {
    var result = {
      ask: 1,
      a: 2,
      bunch: 2,
      get: 1
    };
    expect(countWords("ask a bunch get a bunch")).to.deep.eq(result);
  });
  it("should return an object empty object if passed an empty string", function() {
    expect(countWords("")).to.deep.eq({});
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
