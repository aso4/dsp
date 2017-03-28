import csv
import re

# question 6
# reader = csv.reader(open('faculty.csv'))
#
# faculty_dict = {}
# for row in reader:
#     pattern = re.compile(r"\w+$", re.IGNORECASE)
#     key = re.search(pattern, row[0]) # row[0]
#     key = key.group(0)
#     if key in faculty_dict:
#         # implement your duplicate row handling here
#         # print('duplicate name found, row contains: ', faculty_dict[key])
#         # print('current row:', row[1:])
#         faculty_dict[key].append(row[1:])
#         # print('row now contains:', faculty_dict[key])
#     else:
#         faculty_dict[key] = [row[1:]]
#
# # print(faculty_dict) # print all key value pairs
#
# for key in faculty_dict:
#     print(key, faculty_dict[key])

# question 7
reader = csv.reader(open('faculty.csv'))

professor_dict = {}
for row in reader:
    pattern = re.compile(r"\w+$", re.IGNORECASE)
    lastname = re.search(pattern, row[0])
    lastname = lastname.group(0)
    pattern = re.compile(r"^\w+", re.IGNORECASE)
    firstname = re.search(pattern, row[0])
    firstname = firstname.group(0)
    key = (firstname, lastname)
    if key in professor_dict:
        print('this shouldn\'t happen')
    else:
        professor_dict[key] = row[1:]

for key in professor_dict:
    print(key, professor_dict[key])

# question 8
# reader = csv.reader(open('faculty.csv'))
#
# professor_dict = {}
# for row in reader:
#     pattern = re.compile(r"\w+$", re.IGNORECASE)
#     lastname = re.search(pattern, row[0])
#     lastname = lastname.group(0)
#     pattern = re.compile(r"^\w+", re.IGNORECASE)
#     firstname = re.search(pattern, row[0])
#     firstname = firstname.group(0)
#     key = (lastname, firstname)
#     if key in professor_dict:
#         print('this shouldn\'t happen')
#     else:
#         professor_dict[key] = row[1:]
#
# for key in professor_dict:
#     print(key, professor_dict[key])
