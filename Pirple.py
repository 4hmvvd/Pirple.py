# if statements

click = False
like = 0
click = True

if click == True:
    like = like + 1
    click = False

#print(like)


Temperature = 14
Thermo = 15
#print(Thermo)

if Temperature <= Thermo:
    Thermo = Thermo + 5

#print(Thermo)


Time = "Day"
Sleepy = False
Pajamas = "Off"

if Time == "Night" and Sleepy == True:
    Pajamas = "On"

#print(Pajamas)

Time = "Night"
Sleepy = False
Pajamas = "Off"

if Time == "Night" or Sleepy == True:
    Pajamas = "On"

#print(Pajamas)

Time = "Day"
Sleepy = False
Pajamas = "On"

if Time == "Night":
    Pajamas = "On"

elif Time == "Morning":
    Pajamas = "On"

else:
    Pajamas = "Off"

print(Pajamas)

