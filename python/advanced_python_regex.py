import csv
import re

team = ''
degree_array = [] # Q1
title_array = [] # Q2
email_array = [] # Q3
number_of_degrees = 0 # Q1
email_prependages = 0 # Q4

with open('faculty.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        degree_array.append(row['degree'])
        title_array.append(row['title'])
        email_array.append(row['email'])

# # question 1
#
# def find_and_add_degree(my_pattern):
#     global number_of_degrees
#     global degree_array
#     number_of_degrees = 0
#     pattern = re.compile(my_pattern, re.IGNORECASE)
#     i = 0
#     while (i < len(degree_array)):
#         if re.search(pattern, degree_array[i]):
#             number_of_degrees += 1
#             #print(degree_array[i])
#             degree_array[i] = re.sub(pattern, '', degree_array[i])
#         i += 1
#     print('degree_array:', degree_array)

# pattern = r" ?Ph\.?D\.?" # match this pattern
# find_and_add_degree(pattern)
# print ('found %s instances of PhD' % number_of_degrees)
# degree_array = [item for item in degree_array if not item == ''] # clear empties
# print('array after clear: ', degree_array)
#
#
# pattern = r" ?Sc\.?D\.?"
# find_and_add_degree(pattern)
# print ('found %s instances of ScD' % number_of_degrees)
# degree_array = [item for item in degree_array if not item == '']
# print('Degree array after clear', degree_array)
#
# pattern = r" ?M\.?S\.?" # match this pattern
# find_and_add_degree(pattern)
# print ('found %s instances of MS' % number_of_degrees)
# degree_array = [item for item in degree_array if not item == ''] # clear empties
# print('after clear: ', degree_array)

# [' MD MPH', ' B.S.Ed.', ' JD MA MPH', '0']
# 2 MPH, 1 B.S. Ed, 1 MD, 1 JD, 1 MA

# question 2
# print('title_array is ', title_array)
# import collections
# counter=collections.Counter(title_array)
# print(counter)
# print(counter.values())

# question 3
# print(email_array)

# question 4
# def replace_before_at(my_pattern):
#     global number_of_domains
#     global email_array
#     email_prependages = 0
#     pattern = re.compile(my_pattern, re.IGNORECASE)
#     i = 0
#     while (i < len(email_array)):
#         if re.search(pattern, email_array[i]):
#             email_prependages += 1
#             email_array[i] = re.sub(pattern, '', email_array[i])
#         i += 1
#     # degree_array = [item for item in degree_array if not item == ''] # clear empties
#     print('degree_array:', email_array)
#
# pattern = r"\w+@" # match this pattern
# replace_before_at(pattern)
# print ('deleted %s instances of email prependages' % email_prependages)
#
# import collections
# counter=collections.Counter(email_array)
# print(counter)
