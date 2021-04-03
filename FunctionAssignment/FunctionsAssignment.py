#Homework Assignment #2 -Functions



def FavoriteSong():
    print("My favorite song currently is Blessed")
    Artist = "Wizkid Ayo Balogun"
    FeaturedArtist = "Damian Marley"
    Album = "Made in Lagos"
    Genre = "Afrobeats"
    DurationInSeconds = (60 * 4 + 23)
    YearOfReleased = 2020
    MonthOfReleased = "November"
    Video = "Not yet released"
    PersonalRating = "9.999 / 10"

    print(Artist)
    print(FeaturedArtist)
    print(Album)
    print(Genre)
    print(DurationInSeconds)
    print(YearOfReleased)
    print(MonthOfReleased)
    print(Video)
    print(PersonalRating)

def Artist():
    Artist = "Wizkid Ayo Balogun"
    return Artist

def Album():
    Album = "Made In Lagos"
    return Album

def DurationInSeconds():
    DurationInSeconds = (60 * 4 + 23)
    return DurationInSeconds


"""
To calculate the DurationInSeconds,
instead of assigning a direct integer,
I inputed a mathematical expression that
would inturn equate to be that value.

"""
