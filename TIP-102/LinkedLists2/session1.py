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

# PROBLEM 3
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next
        
# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


def remove_song(playlist_head, song):
    if not playlist_head:
        return None
    # If head is the node to remove
    if playlist_head.song == song:
        return playlist_head.next

    current = playlist_head
    while current.next:
        if current.next.song == song:
            # skip the node to remove it
            current.next = current.next.next
            return playlist_head
        current = current.next

    return playlist_head


playlist = SongNode("SOS", "ABBA", 
                SongNode("Simple Twist of Fate", "Bob Dylan",
                    SongNode("Dreams", "Fleetwood Mac",
                        SongNode("Lovely Day", "Bill Withers"))))

print("---PROBLEM 3---")
print_linked_list(remove_song(playlist, "Dreams"))

# PROBLEM 4
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

def on_repeat(playlist_head):
    slow = playlist_head
    fast = playlist_head

    while fast and fast.next:
        slow = slow.next    
        fast = fast.next.next 
        if slow == fast: 
            return True

    return False     

print("---PROBLEM 4---")
song1 = SongNode("GO!", "Common")
song2 = SongNode("N95", "Kendrick Lamar")
song3 = SongNode("WIN", "Jay Rock")
song4 = SongNode("ATM", "J. Cole")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2  # cycle back to song2

print(on_repeat(song1))  # True


# PROBLEM 5


# PROBLEM 6
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def count_critical_points(song_audio):
    if not song_audio or not song_audio.next or not song_audio.next.next:
        return 0  # fewer than 3 nodes means no critical points

    count = 0
    prev = song_audio
    curr = song_audio.next

    while curr.next:
        nxt = curr.next
        # check local minima
        if curr.value < prev.value and curr.value < nxt.value:
            count += 1
        # check local maxima
        elif curr.value > prev.value and curr.value > nxt.value:
            count += 1
        # move forward
        prev = curr
        curr = nxt

    return count

print("---PROBLEM 6---")
song_audio = Node(5, Node(3, Node(1, Node(2, Node(5, Node(1, Node(2)))))))
print(count_critical_points(song_audio))  # Output: 3
