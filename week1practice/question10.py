songs = [
    "Song A",
    "Song B",
    "Song C",
    "Song D",
    "Song E",
    "Song F",
    "Song G",
    "Song H"
]

print("Complete Playlist:", songs)
print("First 3 Songs:", songs[:3])
print("Last 3 Songs:", songs[-3:])
print("Songs from Position 3 to 6:", songs[2:6])
print("Every Alternate Song:", songs[::2])
print("Playlist in Reverse Order:", songs[::-1])
print("Playlist Without First and Last Song:", songs[1:-1])

# Create a sliced list
short_playlist = songs[2:6]

# Change one song in short_playlist
short_playlist[0] = "New Song"

print("\nOriginal Playlist:", songs)
print("Short Playlist:", short_playlist)