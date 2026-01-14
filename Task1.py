import os
file_name = 'sample.txt'
if os.path.exists(file_name):
 with open(file_name, "rt") as file:
    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline()
   # for line in file:
       # print(line.rstrip('\n'))
 print(f"Reading file contain:\n Line 1: {line1} Line 2: {line2}")
else:
 print(f" File '{file_name}' does not exist.\n Creating new file '{file_name}'.")
 with open(file_name, "wt") as file:
     file.write("this is simple file\nit has multiple line\nit has three Lines")

