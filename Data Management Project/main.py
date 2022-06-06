# Data Management Project

import json
# Initialize song list
songs = []

users = []




def newUser(username, password):
	return {
		"username": username,
		"password": password,
		"favoriteSongs": [ ]
	}

users.append(newUser("sahara", "1111"))


# Create dictionary
def newSong(title, artist, genre):
    return {
        "title": title,
        "artist": artist,
        "genre": genre
    }


def linear_search(an_array, item, key):
   for i in range(len(an_array)):
       if an_array[i][key]== item:
           return i
   return -1



# Add songs to list
songs.append(newSong("sultans of swing", "dire straits", "rock n roll"))
songs.append(newSong("sos", "abba", "80s pop"))
songs.append(newSong("lovelier than you", "b.o.b", "pop"))
songs.append(newSong("romeo and juliet", "dire straits", "rock n roll"))
songs.append(newSong("hey there delilah", "plain white t's", "pop"))
songs.append(newSong("white flag", "dido", "pop"))
songs.append(newSong("sit still look pretty", "daya", "pop"))
songs.append(newSong("i'm a believer", "smash mouth", "pop"))
songs.append(newSong("on every street", "dire straits", "rock n roll"))
songs.append(newSong("we are young", "fun", "pop"))
songs.append(newSong("still into you", "paramore", "rock"))
songs.append(newSong("west end girls", "pet shop boys", "techno"))
songs.append(newSong("boulevard of broken dreams", "green day", "rock"))
#Sign up/in page
loop = True
while True:
    print("""\nWhat would you like to do? 
        1.Login 
        2.Sign up 
          """)
    userCommand = int(input("What would you like to do?"))
    if userCommand == 1:
        usernameInput = input("What is your username?").lower()
        pinInput = int(input("What is your pin?"))
        for user in users:
            if usernameInput == user['username'] and pinInput == int(user['password']):
                print("Login successful!")
                loop = False
                newloop = True
                while True:
                    # Print main menu
                    print("""\nWhat would you like to do? 
                                  User Menu
                                    1.Display All Songs
                                    2.Display Songs by Genre
                                    3.Add Song to Favourites List
                                    4.Remove Song from Favourites List
                                    5.Display Favourites List
                                    6.Logout""")
                    # Get user command
                    Number = int(input("Please enter your command"))
                    # Print out entire song list
                    if Number == 1:
                        print(songs)
                    # Filter song results
                    if Number == 2:
                        # Get user input for searching
                        genreSearch = input("Please genre to search for").lower()
                        # Loop through songs and find all songs with that genre
                        for song in songs:
                            if song['genre'] == genreSearch:
                                print(song)
                    # Add to favorite songs
                    if Number == 3:
                        favoriteSong = input(
                            "Please enter the title of the song you would like to add to your favorite list")

                        print(favoriteSong, songs[0:5])
                        if linear_search(songs, favoriteSong, 'title') == -1:
                            print("Song found and added to favorites list")
                        else:
                            print("Song not found")

                    # Remove songs from favorite list
                    if Number == 4:
                        removedSong = input(
                            "Please enter the title of the song you would like to remove from your favorite list")
                        for song in favoritesongs:
                            if song['title'] == removedSong:
                                favoritesongs.remove(song)
                                json_string = json.dumps(favoritesongs)
                                file = open("songnames.txt", "w")
                                file.write(json_string)
                                file.close()
                        print("song removed")
                    # Print out favorites list
                    if Number == 5:
                        # print(favoritesongs)
                        # Load a JSON string from a file
                        file = open("songnames.txt", "r")
                        json_string_from_file = file.read()
                        file.close()

                        # the loads() method will convert a json string to data
                        data2 = json.loads(json_string_from_file)
                        for data in data2:
                            print(data)
                    # Log out
                    if Number == 6:
                        newloop = False
                        print("You have been logged out")
# Create main menu loop


