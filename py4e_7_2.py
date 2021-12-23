# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    fnum = float(line[21:])
    total = total + fnum
    count = count + 1
    #print(count)
   # print(total)
print("Average spam confidence:", total/count)
