line = """ To jest
string moj
    wielowierszowy"""

print("bazowy string: ", line)
z_pierwszych = ""
z_ostatnich = ""
line = line.split()
for i in line:
    z_pierwszych += i[0]
    z_ostatnich += i[-1]

print("slowo z pierwszych znakow: ", z_pierwszych, "\nslowo z ostatnich: ", z_ostatnich)