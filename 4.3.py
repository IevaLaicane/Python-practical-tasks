##open the file
f = open('english.txt')

##create an empty dictionary
counts = {}

##read the file and change all the characters to small letters
words = f.read()
words = words.lower()

##create an empty list, iterate through characters in file and check if they belong to alphabeth. Add them to list if they are letters
x = list()
for i in words :
    if i.isalpha() == True :
        x.append(i)

##iterate through the created list and add them to the dictionary, and count the occurance of letters 
for name in x :
    counts[name] = counts.get(name, 0) + 1

##sort the dictionary by the key, create a new list, construct a list of tuples and sort by value
counts.items()
sort = list()
for a, b in counts.items() :
    sort.append ((b, a))
sort = sorted(sort, reverse=True)

##print the result
print(sort)

##do the same for the second file which consists the same text but in italian
d = open('italian.txt')
counts1 = {}
words1 = d.read()
words1 = words1.lower()
y = list()
for i in words1 :
    if i.isalpha() == True :
        y.append(i)
for name in y :
    counts1[name] = counts1.get(name, 0) + 1
counts1.items()
sort1 = list()
for a, b in counts1.items() :
    sort1.append ((b, a))
sort1 = sorted(sort1, reverse=True)
print(sort1)

##compare the lists
print("Following characters from the text in English do not appear in the Italian version:")
for i in counts :
    if i not in counts1:
        print(i)

print("Following characters from the text in Italian do not appear in the English version:")
for i in counts1 :
    if i not in counts:
        print(i)



print("Top 5 most used characters in the English version of the text are ", sort[0][1],",", sort[1][1],",",sort[2][1],",",sort[3][1],",",sort[4][1])
print("Top 5 most used characters in the Italian version of the text are:", sort1[0][1],",", sort1[1][1],",",sort1[2][1],",",sort1[3][1],",",sort1[4][1])