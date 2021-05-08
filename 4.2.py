##open the file
f = open('mbox-short.txt')

##create an empty dictionary
counts = dict()

##create an empty list
x = list()

##iterate through the file by removing unnecessary characters and taking only the lines that start with From
##split the lines in words
##find the position of @ in the word at index 1 and get the domain name 
##add domain name to the list

for line in f:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    pos = words[1].find('@')
    domain = words[1] [pos+1:]
    x.append(domain)

##iterate through the list and count each occurance of domain name
for domain in x :
    counts[domain] = counts.get(domain, 0) + 1

##print the outcome
print (counts)