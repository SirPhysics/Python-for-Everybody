name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
lst = list()

for line in handle:
    line = line.strip()
    if line.startswith("From "):
        words = line.split()
        time = words[5]
        lst.append(time[0:2])

for hour in lst:
    if hour not in counts:
        counts[hour] = 1
    else:
        counts[hour] +=1
#print(sorted(counts.items()))

for key, val in sorted(counts.items()):
    print(key, val)
