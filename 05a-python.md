# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Similarities: defined order, zero-based indices, negative indices count from
>> the end of a list or tuple, use of the "in" keyword is possible to check
>> if an element exists, and slicing also works in both cases.
>> Differences: tuples are immutable. Lists have append, extend, insert, remove, and people
>> methods whereas tuples don't. Slicing creates a new tuple. Only tuples work as
>> keys in dictionaries since they are immutable.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets are lists with no duplicate entries, are unordered, and each element
>> must be immutable. The set itself can be changed through adding or removing
>> elements, and can be used to perform mathematical set operations such as
>> union, intersection, and symmetric difference.
>>
>> my_set = {1, 2, 2, 3}
>> my_set # returns {1, 2, 3}
>> my_list = [1, 2, 2, 3]
>> my_list # returns [1, 2, 3]
>>
>> Performance depends on what operation is being performed on the set or list.
>> If the set were being iterated over, it is slower than if it were in list form,
>> whereas if it were simply detecting an item in the list, the set would be
>> faster due to it using a hash table as its underlying data structure.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambdas are functions that are not bound to a name and are often used in
>> conjunction with functional concepts such as filter(), map(), and reduce().
>> An example using sorted():
```
student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```
>> In this case, the key is passed in for the sorted() function which is then
>> used as the basis for sorting. The third index in student_tuples is the
>> student's age.

>> The map() function is a function that takes two arguments (function, seq)
>> and applies the function to all elements in the sequence. Used in tandem
>> with a lambda function, we can convert a list of values in Celsius to
>> their corresponding values in Fahrenheit via the map and lambda functions,
>> with the final result made into a list for printing.
```
>>> C = [39.2, 36.5, 37.3, 38, 37.8]
>>> F = list(map(lambda x: (float(9)/5)*x + 32, C))
>>> print(F)
[102.56, 97.7, 99.14, 100.4, 100.03999999999999]
>>> C = list(map(lambda x: (float(5)/9)*(x-32), F))
>>> print(C)
[39.2, 36.5, 37.300000000000004, 38.00000000000001, 37.8]
>>>
```

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are a concise way to create lists and has the following
>> syntax: [ expression for item in list if conditional]. This is equivalent
>> to the following code:
```
for item in list:
  if conditional:
    expression
```
>> Expressed in a different way: new_list = [expression(i) for i in old_list if filter(i)]
>> where new_list is the result, expression(i) is based on the variable used for
>> each element in the old list, for i in old_list is the old_list being
>> iterated over in a for loop, and if filter(i) is the applied filter.

>> Equivalent code using map() and filter() is:
>> new_list = list(map(expression, filter(lambda x: conditional, old_list)))

>> Set comprehensions work if notation is specified:
>> pairs = {(x, x+2) for x in primes if x+2 in primes}

>> as does dictionary comprehensions:
>> d = dict((key, value) for (key, value) in iterable)
>> or
>> d = {key: value for (key, value) in iterable}

>> # this question needs to be revisited.

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  
```
date_start = '01-02-2013'
date_stop = '07-28-2015'
```
>> 937 days

b.  
```
date_start = '12312013'
date_stop = '05282015'
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)
