def weather():
    print("This program checks if ColdWeather is True or False")
    Temperature = int(input("Enter the value of temperature in celcius: "))
    Dressing = "Wear Sweater"
    ColdWeather = True

    if Temperature <= 10:
        Dressing = "Wear Sweater"
        ColdWeather = True

    elif Temperature > 10:
        Dressing = "Do Not Wear Sweater"
        ColdWeather = False
        
    print(Dressing)
    return ColdWeather

