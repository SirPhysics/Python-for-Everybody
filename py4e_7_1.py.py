# Use words.txt as the file name
prompt = input('Please enter the file name.')
fhand = open('words.txt')
fread = fhand.read()
line = fread.upper()
rline =line.rstrip()
print(line)
