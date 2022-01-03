import re
hand = open(r"C:\Users\kcho4\OneDrive\Desktop\assignment_task.txt")
#print(hand.read())
lst = list()
total = 0
for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]+',line)
    if len(x)>0:
        for num in x:
            lst.append(num)
            fnum = float(num)
            total = total + fnum
        #print(lst)
print(total)
