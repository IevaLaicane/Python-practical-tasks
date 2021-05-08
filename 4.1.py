##open the file
f = open('mbox-short.txt')

count = 0
##remove unnecessary characters
##look only for lines that start with From
##split the line into the words
##take the word with index 1 and print it (email address)
##count the relevant lines
##print the outcome
for line in f:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    print(words[1])
    count = count +1
print("There are", count, "lines in the file with <<From>> as the first word")

