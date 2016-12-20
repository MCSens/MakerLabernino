#!/usr/bin/env python
name = "Sandro"
surname = "Veiga"
print name," ",surname

counter = 3
if(counter==5):
    print "Counter ist 5 yo"
else:
    print "Counter ist nicht 5 yo"

min_value = raw_input("Bitte gib die Untere Schranke ein: ")
max_value = raw_input("Bitte gib die Obere Schranke ein: ")
current_value = min_value

print min_value, " < ", max_value
print current_value
while (current_value < max_value):
    print current_value
    current_value = current_value + 1
#!
