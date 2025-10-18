line = """ To jest
string moj
    wielowierszowy"""

print("bazowy string: ", line)
line = line.split()

dlugosc = 0
najdluzsze_slowo = ''
for i in line:
    if(len(i)>dlugosc):
        dlugosc = len(i)
        najdluzsze_slowo = i

print("najdluzsze slowo: ", najdluzsze_slowo, "jego dlugosc: ", dlugosc)


