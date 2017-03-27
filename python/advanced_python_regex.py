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
    print ('pattern is', pattern)
    for degree in degree_array:
        if re.match(pattern, degree):
            number_of_degrees += 1
            print(degree)
            degree = re.sub(pattern, '', degree)
            print('degree is replaced with :', degree)

pattern = r" ?Ph\.?D\.?" # match this pattern
find_and_add_degree(pattern)
print ('phd is', number_of_degrees)
print('Degree array is now', degree_array)

pattern = r" ?Sc\.?D\.?"
find_and_add_degree(pattern)
print ('scd is', number_of_degrees)
print('Degree array is', degree_array)
