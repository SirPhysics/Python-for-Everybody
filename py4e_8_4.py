fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
   line = line.rstrip()
   words = line.split()
   for inwords in words:
        if inwords not in lst:
            lst.append(inwords)
   else:
                continue
lst.sort()
print(lst)
