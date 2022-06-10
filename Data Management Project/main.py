# Data Management Project

#Import JSON
import json
# Initialize song list
songs = []
#Initialize user list
users = []

# Load a JSON string from songnames
file = open("songnames.txt", "r")
json_string_from_file = file.read()
file.close()

# the loads() method will convert a json string to data
data2 = json.loads(json_string_from_file)
for data in data2:
    users.append(data)

#Creating a new user
def newUser(username, password):
	return {
		"username": username,
		"password": password,
		"favoriteSongs": [ ]
	}


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


#Add new user
users.append(newUser("sahara", "1111"))


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
while loop:
    #Choice options
    print("""\nWhat would you like to do? 
        1.Login 
        2.Sign up 
          """)
    #Get user command
    userCommand = int(input("What would you like to do?"))
    #Login attempt
    if userCommand == 1:
        #Get username from user
        usernameInput = input("What is your username? ").lower()
        #Get pin from user
        pinInput = int(input("What is your pin? "))
        #Loop through users to see if they are in user list - if not they do not have an account
        for user in users:
            #Login successful
            if usernameInput == user['username'] and pinInput == int(user['password']):
                print("Login successful!")
                #Store user data in a list
                currentfav = user
                favoritesongs = currentfav["favoriteSongs"]
                #start a new loop for a main menu
                newloop = True
                #Begin loop for new main menu
                while newloop:
                    # Print main menu
                    print("""\nWhat would you like to do? 
                                  User Menu
                                    1.Display All Songs
                                    2.Display Songs by Genre
                                    3.Add Song to Favourites List
                                    4.Remove Song from Favourites List
                                    5.Display Favourites List
                                    6.Save and quit""")
                    # Get user command
                    Number = int(input("Please enter your command"))
                    # Print out entire song list
                    if Number == 1:
                        print(songs)
                    # Filter song results
                    if Number == 2:
                        # Get user input for searching
                        genreSearch = input("Please genre to search for ").lower()
                        # Loop through songs and find all songs with that genre
                        for song in songs:
                            if song['genre'] == genreSearch:
                                print(song)
                    # Add to favorite songs
                    if Number == 3:
                        #Get user input
                        favoriteSong = input(
                            "Please enter the title of the song you would like to add to your favorite list ")
                        #Using linear search function, see if song is in songs list and add it to favorites if it is
                        if linear_search(songs, favoriteSong, 'title') != -1:
                            print("Song found and added to favorites list")
                            favoritesongs.append(favoriteSong)
                        #If song isn't in songs list print a message
                        else:
                            print("Song not found")

                    # Remove songs from favorite list
                    if Number == 4:
                        #Get title of song user would like to remove
                        removedSong = input(
                            "Please enter the title of the song you would like to remove from your favorite list")
                        #Using linear search function, see if desired song to be removed is in favoirtes list and if it is-remove it
                        if linear_search(songs, removedSong, 'title') != -1:
                            #remove song
                            favoritesongs.remove(removedSong)
                            #store new data in file
                            json_string = json.dumps(favoritesongs)
                            file = open("songnames.txt", "w")
                            file.write(json_string)
                            file.close()
                            #Print message
                            print("Song removed")
                        #Print message to show that song isn't in your favorites list
                        else:
                            print("Song not found in your favorites list")
                    # Print out favorites list
                    if Number == 5:
                        # print(favoritesongs)
                        print(favoritesongs)
                    # Log out
                    if Number == 6:
                        #Store users data into file
                        #Store new users information to a json string
                        json_string = json.dumps(users)
                        #Store new json string to file
                        file = open("songnames.txt", "w")
                        file.write(json_string)
                        file.close()
                        #End the new lop
                        newloop = False
                        print("You have been logged out")
                        #Begin old loop - login menu
                        loop = True
            #Print message telling user that there pin or password is incorrect
            else:
                print("The pin or username you are trying to enter is invalid-please try again")
            #End main menu loop
            break
    #Sign up
    if userCommand == 2:
        #Get users desired username and pin
        newUsername = input("Please enter your username ")
        newPin = int(input("Please enter your pin "))
        #Add them to users list
        users.append(newUser(newUsername, newPin))
        #Store data to file
        json_string = json.dumps(users,indent=4)
        file = open("songnames.txt", "w")
        file.write(json_string)
        file.close()



