
ParticipantNumber = 2
ParticipantData = []

registeredParticipants = 0
outputFile = open("ParticipantData.txt", "w")

while(registeredParticipants < ParticipantNumber):
    tempPartData = []   #name, country, age
    name = input("Enter your name: ")
    tempPartData.append(name)
    country = input("Enter your country of origin: ")
    tempPartData.append(country)
    age = int(input("Enter your age: "))
    tempPartData.append(age)    #[name, country, age]
    print(tempPartData)

    ParticipantData.append(tempPartData)
    print(ParticipantData)      #[[name, country, age]]

    registeredParticipants += 1

for participant in ParticipantData:
    for data in participant:
        outputFile.write(str(data)) #The data would be joined without any formatting(spacing)
        outputFile.write(" ")   #This gives space between the data in the list
    outputFile.write("\n")  #This creates a new line after the first element in the parent list.

outputFile.close()

inputFile = open("ParticipantData.txt", "r")

inputList = []

for line in inputFile:
    tempParticipant = line.strip("\n").split()  #.strip("\n") removes the new line function("\n")
    print(tempParticipant)                  #while .split() groups the word individually where there is space and make it an element. 
    inputList.append(tempParticipant)
    print(inputList)

Age = {}
for part in inputList:
    tempAge = int(part[-1]) #This target the last element on the list i.e Age
    if tempAge in Age:
        Age[tempAge] += 1
    else:
        Age[tempAge] = 1

print(Age)

Oldest = 0
Youngest = 100
mostOccuringAge = 0
counter = 0

for tempAge in Age:
    if tempAge > Oldest:
        Oldest = tempAge
    if tempAge < Youngest:
        Youngest = tempAge
    if Age[tempAge] > counter:
        counter = Age[tempAge]
        mostOccuringAge = tempAge
        
print(Oldest)
print(Youngest)
print("Most ocuring Age is:",mostOccuringAge,"with",counter)
inputFile.close()
    
