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
        email = words[1]
        lst.append(email)

for email in lst:
    counts[email] = counts.get(email,0)+1

count = None
emailmax = None
for k,v in counts.items():
    if count is None or v > count:
        count = v
        emailmax = k

print(emailmax,count)
