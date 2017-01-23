#!/usr/bin/python

#
# Author: Yuri Medvinsky
# Date: 07.30.2016
#                                           INFORMATIONAL
#############################################################################################################################################

'''
This program compares two files from File1 from last week and File2 from this week. Both files contain server names. 
The idea is to identify which servers exists last week but dont exist this week. And which new servers were added this week. 
So what we do is we try to compare the two files. For both files we read the output and assign it to an array. Then we create 
a dictionary (hash) and assign '1' to all values from each key of every file (e.g: server: 1). Then we begin our comparison 
and see if a key if found in file2 that exists in file1. If its not found then we decrement the value by 1 setting it to 0. If 
the servers match then we leave the value at 1. Then we compare file2 with file1 and see if any new servers were added to file2 
from this week. If new server is found then we add value by 1. This means the value goes to 2. In conclusion if the final value 
printed is 0, then last weeks server is missing from this weeks file. If value is 1 then no change took place and all servers are 
in tact. If value 2 is found then a new server was added this week that did not exist last week. And here is the final code.
'''

#############################################################################################################################################

print
print "Legend Reference"
print "0: old server has been removed"
print "1: server has not been changed"
print "2: new server has been added"
print
print


'''  FILE1 '''


# open File1 and assign each line into f1_lines array. Excluding \n newlines
with open('file1') as f1:
  f1_lines = f1.read().splitlines()


# Set Empty Dictionary, f1
f1 = {}
# Create Dictionary and assign value '1' to each key from f1_lines array. 
for i in f1_lines:
    f1[i] = '1'

# Print Original Dictionary
#print 'f1: ', f1








'''  FILE2 '''


# Open File2 and assign each line into f2_lines array. Excluding \n newlines
with open('file2') as f2:
  f2_lines = f2.read().splitlines()


# Set empty dictionary, f2
f2 = {}
# Create Dictionary and assign value '0' to each key from f2_lines array
for i in f2_lines:
    f2[i] = '1'

# Print Dictionary
#print 'f2: ', f2
print








'''  FILE1 compare with FILE2 '''


# Record the following entries that are missing from File2 but are found in File1. If entry is no longer present in File2 then we assign '0' as value to the key found in File1. This basically decrements original value by 1
for k,v in f1.items():
    if not k in f2:
      f1[k]='0'


# Simply print the updated output from dictionary f1. (Prints File1 updated values)
print 'f1 updated: (File1 compare to File2)'
print '-' * 15
for k,v in f1.items():
    print k,v




print
print
print





'''  FILE2 compare with FILE1 '''


# Record the following entries that are missing from File1 but are found in File2. If new entry is found in File2 then this means new server has been added. We then increment original value by 1 and in this case we assign value of 2.
for k,v in f2.items():
    if not k in f1:
      f2[k]='2'


# Simply print the updated output from dictionary f2. (Prints File2 updated values)
print 'f2: updated: (File2 compare to File1)'
print '-' * 15
for k,v in f2.items():
    print k,v







print
print
print





# Here we merge the two updated dictionaries and print the final result
print 'f1 + f2: updated as final result after two dictionary files have been merged into one'
print '-' * 15
# Print one full detail
merged_f1_f2 = dict(f1.items() + f2.items())
for k,v in merged_f1_f2.items():
    print k,v




