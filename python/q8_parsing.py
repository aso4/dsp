# The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv

team = ''
with open('football.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    diff = 1000 # set random high number as diff
    for row in reader:
        if abs(int(row['Goals']) - int(row['Goals Allowed'])) < diff:
            diff = abs(int(row['Goals']) - int(row['Goals Allowed']))
            team = row['Team']
print('Team with the smallest for/against goal differential is', team)
