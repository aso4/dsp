import csv
import re

team = ''
degree_array = []
number_of_degrees = 0

with open('faculty.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # print('appending: ', row['degree'])
        degree_array.append(row['degree'])
print('Degree array is', degree_array)

def find_and_add_degree(my_pattern):
    global number_of_degrees
    global degree_array
    number_of_degrees = 0
    # i = 0
    pattern = re.compile(my_pattern, re.IGNORECASE)
    print ('pattern is', pattern)
    # while (i < len(degree_array)):
    #     # if not re.match(pattern, degree_array[i]):
    #     #     print("You failed to match %s" % (degree_array[i]))
    #     if not my_pattern: # pattern wasn't inputted
    #         print("Enter a pattern!")
    #     else:
    #         del degree_array[i]
    #         number_of_degrees += 1
    #     i += 1
    for degree in degree_array:
        # if not re.match(pattern, degree):
        #     print('no pattern match')
            # i += 1
            # print("You failed to match %s" % (degree))
        # elif not my_pattern: # pattern wasn't inputted
        #     print("Enter a pattern!")
        if re.match(pattern, degree):
            number_of_degrees += 1
            re.sub(pattern, 'replaced', 'unchanged')
            # print('deleting at index', i)
            # print('deleting ', degree_array[i])
            # del degree_array[i]
            # print("Pattern match")

pattern = r" ?Ph\.?D" # my pattern
find_and_add_degree(pattern)
print ('phd is', number_of_degrees)
print('Degree array is now', degree_array)

pattern = r" ?Sc\.?D\.?"
find_and_add_degree(pattern)
print ('scd is', number_of_degrees)
print('Degree array is', degree_array)
