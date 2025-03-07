import string
fhand = open('CS2\\mbox-short.txt')
counts = dict()
for line in fhand:
    line.translate(str.maketrans('', '', string.punctuation))
    line.split()
    for word in line:
        for letter in word.lower():
            if letter.isalpha():
                if letter not in counts:
                    counts[letter] = 1
                else:
                    counts[letter] += 1

lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:27]:
    print(key, val)