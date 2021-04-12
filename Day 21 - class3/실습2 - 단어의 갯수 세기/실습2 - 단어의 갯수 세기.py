import os
import sys

with open('News.txt', 'r', encoding='utf8') as file:
    strings = file.read()

count = strings.count(' the ') + strings.count('The ')

#print(strings)
print(count)
