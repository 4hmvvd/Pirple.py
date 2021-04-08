countryList = []

for country in range(3):
    Country = input("Enter country: ")
    countryList.append(Country)
    
print(countryList)

countryDictionary = {}

for country in countryList:
    if country in countryDictionary:
        countryDictionary[country] += 1
    else:
        countryDictionary[country] = 1

print(countryDictionary)
