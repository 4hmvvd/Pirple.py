
#What's my favorite song?
  
print("My favorite song currently is Blessed")
print()

FavoriteSong = {"Artist": "Wizkid Ayo Balogun", "Album": "Made in Lagos",
                    "FeaturedArtist": "Damian Marley", "Genre": "Afrobeats",
                    "DurationInSeconds": (60 * 4 + 23),"YearOfReleased": 2020,
                    "MonthOfReleased": "November", "Video": "Not yet released",
                     "PersonalRating": "9.999 / 10"}
for details in FavoriteSong:
    #print(FavoriteSong)
    print(FavoriteSong[details])


def guess():
    
    print("This function allows you to guess the value and key")
    Key = input("Enter the key: ")
    Value = input("Enter the value: ")

    if Key in FavoriteSong:
        Key == FavoriteSong[Key]
        return True
    else:
        return False
    
