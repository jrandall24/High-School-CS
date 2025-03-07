mbox_short = open('CS2\\mbox-short.txt', 'r')
count_email = {}
for line in mbox_short:
    if line.startswith('From '):
        line = line.lower()
        words = line.split()
        email = words[1]
        count_email[email] = count_email.get(email, 0) + 1
lst = count_email.items()
output = [(email, count) for count, email in lst]
sorted_count = sorted(output, reverse=True)

final = sorted_count[0]
print(final[1], final[0])