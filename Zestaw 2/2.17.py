line = """ to jest
string moj
    wielowierszowy"""

print("bazowy string: ", line)
line = line.split()
alf = sorted(line)
print("alfabetycznie: ", alf)
dlug = sorted(line, key=len)
print("dlugosciowo: ", dlug)