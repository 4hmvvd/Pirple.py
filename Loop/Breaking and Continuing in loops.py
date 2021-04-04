#Using breaks and continue in loops

Participants = ["Ahmed", "Ibrahim", "Ruqqoyya", "Maryam", "Mustapha"]

position = 1

for name in Participants:
    if name == "Ruqqoyya":
        break
    position = position + 1

print(position)


#Different approach using indexing

for i in range(len(Participants)):
    print(i)
    if Participants[i] == "Maryam":
        print("Break")
        break
    print("Not Break")

print(i+1)

#Using Continue in for loop

for n in range(10):
    if n%3 == 0:
        print(n)
        print("Divisible by 3")
        continue
    
    print(n)
    print("Not Divisible by 3")

#Using while loop and break

i = 1
while True:
    if i%3 == 0:
        break
    print(i)
    i += 1
