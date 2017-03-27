import csv
import re

team = ''
degree_array = []
number_of_degrees = 0

with open('faculty.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        degree_array.append(row['degree'])
print('Degree array is', degree_array)

def find_and_add_degree(my_pattern):
    global number_of_degrees
    global degree_array
    number_of_degrees = 0
    pattern = re.compile(my_pattern, re.IGNORECASE)
    i = 0
    while (i < len(degree_array)):
        if re.match(pattern, degree_array[i]):
            number_of_degrees += 1
            #print(degree_array[i])
            degree_array[i] = re.sub(pattern, '', degree_array[i])
        i += 1
    print('degree_array:', degree_array)

def multiple_degrees(my_pattern):
    global number_of_degrees
    global degree_array
    number_of_degrees = 0
    pattern = re.compile(my_pattern, re.IGNORECASE)
    i = 0
    while (i < len(degree_array)):
        if re.search(pattern, degree_array[i]):
            number_of_degrees += 1
            degree_array[i] = re.sub(pattern, '', degree_array[i])
        i += 1
    print('degree_array:', degree_array)

pattern = r" ?Ph\.?D\.?" # match this pattern
find_and_add_degree(pattern)
print ('found %s instances of phd' % number_of_degrees)
degree_array = [item for item in degree_array if not item == ''] # clear empties
print('after clear: ', degree_array)


pattern = r" ?Sc\.?D\.?"
find_and_add_degree(pattern)
print ('found %s instances of scd' % number_of_degrees)
degree_array = [item for item in degree_array if not item == '']
print('Degree array after clear', degree_array)

pattern = r" ?Ph\.?D\.?" # match this pattern
multiple_degrees(pattern)
print ('found %s instances of phd' % number_of_degrees)
degree_array = [item for item in degree_array if not item == ''] # clear empties
print('after clear: ', degree_array)
