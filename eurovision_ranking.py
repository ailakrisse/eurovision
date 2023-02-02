# a program to help you create your eurovision ranking
# works with a .txt input file that contains a list of the song you wanna rank as a command line argument
# the file with the songs has to be in the same directory as the code tho

import random
import sys

# just opens your song list and reads it into a list
with open(sys.argv[1], "r") as file:
	songs_list = file.readlines()

songscores = {}
songs = []

for song in songs_list:
	song = song.rstrip("\n")
	songs.append(song)
	songscores[song] = 0

# function to value of the preferred key (song)
def preferences(song1, song2):
	global songscores
	print("\nWhich song do you prefer?")
	print("Song 1: ", song1, "or Song 2:", song2 + "?")
	pref = int(input("Type 1 or 2\n"))
	if pref == 1:
		songscores[song1] += 1
	if pref == 2:
		songscores[song2] += 1
# 	else:
# 		print("Please enter a '1' or a '2', nothing else")
# 		songscores = preferences(song1, song2)
	return songscores

# goes through every song pair, means that it will obv take longer the more songs are on the list
# doable for UMK or Vidbir, absolute hell for FiK or Sanremo
def all_rank():
	for song1 in songs:
		for song2 in songs:
			if song1 != song2:
				songscores = preferences(song1, song2)
	return songscores
				
# doesn't necessarily go through every song pair, instead chooses random pairs
def random_rank():
	# enter how many rounds you're willing to go through, i.e. how much time you got
	rounds = int(input("How many rounds do you want to do?\n"))
	while rounds > 0:
		song1 = songs[(random.randint(0,(len(songs)-1)))]
		song2 = songs[(random.randint(0,(len(songs)-1)))]
		if song1 != song2:
			songscores = preferences(song1, song2)
			rounds -= 1
	return songscores

print("Do you want to go through all songs in order or only do a specific number of rounds?")
decision = input("enter '1' for the all-option, or enter '2' for the random-option\n")

if decision == "1":
	songscores = all_rank()
if decision == "2":
	songscores = random_rank()
# else:
# 	print("Please enter a '1' or a '2', nothing else")

# sort and print the dict with the song scores
sorted_scores = sorted(songscores.items(), key=lambda x:x[1])
for songscore in sorted_scores:
	print(songscore[0], "\t", songscore[1])