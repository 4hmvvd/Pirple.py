
#File Input and Output (I/O)

"""
"r" = read, "w" = write, "a" = append
"""

VacationSpots = ["Maldives", "Bahamas", "Seycheles", "Cape Verde", "Barbados"]

VacationFile = open("VacationPlaces", "w")

for spots in VacationSpots:
    VacationFile.write(spots + "\n")

VacationFile.close()

VacationFile1 = open("VacationPlaces", "r")

FirstLine = VacationFile1.readline()
print(FirstLine)
SecondLine = VacationFile1.readline()
print(SecondLine)

for line in VacationFile1:
    print(line,end="")
    
VacationFile1.close()

FinalSpot = "Mauritius\n"

VacationFile2 = open("VacationPlaces", "a")
VacationFile2.write(FinalSpot)
VacationFile2.close()

VacationFile3 = open("VacationPlaces", "r")
for line in VacationFile3:
    print(line, end="")

VacationFile3.close()

with open("VacationPlaces","r") as VacationFile4:
    for line in VacationFile4:
        print(line)

"""
using the "with" allows you to open a file without necessirily having to close it
as it was using the direct "open" statement.
Also, "with" statement allow you to add other variables or other instruction to
the string.You can do this while using a for loop("Vacation"+str(i), "r")
unlike the former.
"""
