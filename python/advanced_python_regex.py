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
    # print ('pattern is', pattern)
    i = 0
    while (i < len(degree_array)):
        if re.match(pattern, degree_array[i]):
            number_of_degrees += 1
            print(degree_array[i])
            degree_array[i] = re.sub(pattern, '', degree_array[i])
            # print('degree is replaced with :', degree_array[i])
        i += 1
    print('degree_array:', degree_array)
    # for degree in degree_array:
    #     if re.match(pattern, degree):
    #         number_of_degrees += 1
    #         print(degree)
    #         degree = re.sub(pattern, '', degree)
    #         print('degree is replaced with :', degree)
    #         print('degree_array:', degree_array)

pattern = r" ?Ph\.?D\.?" # match this pattern
find_and_add_degree(pattern)
print ('phd is', number_of_degrees)
degree_array = [item for item in degree_array if not item == ''] # clear empties
print('after clear: ', degree_array)


pattern = r" ?Sc\.?D\.?"
find_and_add_degree(pattern)
print ('scd is', number_of_degrees)
degree_array = [item for item in degree_array if not item == '']
print('Degree array after clear', degree_array)
