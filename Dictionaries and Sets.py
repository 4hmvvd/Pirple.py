
#List and Dictionary

CountryList = []

for i in range(3):
    Country = input("Enter country: ")
    CountryList.append(Country)
print(CountryList)

CountryDictionary = {}

for country in CountryList:
    if country in CountryDictionary:
        CountryDictionary[country] += 1
    else:
        CountryDictionary[country] = 1

print(CountryDictionary)


#Using while loop in Dictionary

BlackShoes = {40:3, 42:4, 37:0, 54:0}
print(BlackShoes)

while(True):
    Size = int(input("\nEnter your shoe size: "))
    if Size < 0:
        break
    if Size > 0:
        BlackShoes[Size] -= 1
    else:
        print("Size NOT available")
    print(BlackShoes)
