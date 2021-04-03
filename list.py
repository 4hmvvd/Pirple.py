TestList = ["element1", "element2", "element3"]
    >>> print(TestList[1])
element2
    >>> print(TestList[0])
element1
    >>> Scores = [70, 80.5, 50, 65.4, 45]
    >>> print(Scores)
[70, 80.5, 50, 65.4, 45]
    >>> print(Scores[0:3])
[70, 80.5, 50]
    >>> print(Scores[:])
[70, 80.5, 50, 65.4, 45]
    >>> print(Scores[2:3])
[50]
    >>> Scores[2] = 100
    >>> print(Scores[:])
[70, 80.5, 100, 65.4, 45]
    >>> Scores[1, 2, 3] = []
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    Scores[1, 2, 3] = []
TypeError: list indices must be integers or slices, not tuple
    >>> Scores[1:4] = []
    >>> print(Scores[:])
[70, 45]
    >>> print(Scores[1])
45
    >>> Scores[1] = []
    >>> print(Scores[:])
[70, []]
    >>> Scores[1] = ["Hello", "World"]
    >>> print(Scores[:])
[70, ['Hello', 'World']]
    >>> print(Scores[1])
['Hello', 'World']
    >>> 
KeyboardInterrupt
    >>> print(Scores[1][0])
Hello
    >>> Scores.append(89)
    >>> print(Scores)
[70, ['Hello', 'World'], 89]
    >>> Scores.append(70, 58)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    Scores.append(70, 58)
TypeError: list.append() takes exactly one argument (2 given)
    >>> Scores.append(70)
    >>> Scores.append(58)
    >>> print(Scores)
[70, ['Hello', 'World'], 89, 70, 58]
