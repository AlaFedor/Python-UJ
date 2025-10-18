line = """ To jest
string moj
    wielowierszowy"""

print("bazowy string: ", line)
line = line.split()
zlaczone = "".join(line)
dlugosc = len(zlaczone)
print("dlugosc: ", dlugosc)