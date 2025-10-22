# PROBLEM 1
class SongNode:
    def __init__(self, song, artist=None, next=None):
        self.song = song
        self.next = next
        self.artist = artist

# For testing
def print_linked_list(node):
    current = node
    while current:
        print(current.song, end=" -> " if current.next else "")
        current = current.next
    print()

bad_romance = SongNode("Bad Romance")
party_rock = SongNode("Party Rock Anthem", bad_romance)
uptown_funk = SongNode("Uptown Funk", party_rock)

top_hits_2010s = uptown_funk

print("---PROBLEM 1---")
print_linked_list(top_hits_2010s) # Uptown Funk -> Party Rock Anthem -> Bad Romance

# PROBLEM 2
def get_artist_frequency(playlist):
    freq = {}
    current = playlist
    while current:
        if current.artist in freq:
            freq[current.artist] += 1
        else:
            freq[current.artist] = 1
        current = current.next
    return freq

print("---PROBLEM 2---")
playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

print(get_artist_frequency(playlist))

print("---PROBLEM 3---")
print("---PROBLEM 4---")
print("---PROBLEM 5---")
