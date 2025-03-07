mbox_short = open('CS2\\mbox-short.txt', 'r')
count_hour = {}
for line in mbox_short:
    if line.startswith('From '):
        line = line.lower()
        words = line.split()
        time = words[5].split(':')
        hour = time[0]
        count_hour[hour] = count_hour.get(hour, 0) + 1
lst = list()
for hour, val in list(count_hour.items()):
    lst.append((hour, val))
lst.sort()
for hour, val in lst[:12]:
    print(hour, val)