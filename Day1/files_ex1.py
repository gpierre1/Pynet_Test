#!/usr/bin/env python

### READ ###
f = open("my_file.txt")
for line in f:
    print line.strip()

### Write ###
f = open("new_file.txt", "w")
f.write('whatever2\n')
f.close()


### APPEND ###
with open("new_file.txt", "a") as f:
    f.write('Something else\n')


