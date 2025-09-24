# problem 1

def lineup(artists, set_times):
    lineup_dict = {}
    for i in range(len(artists)):
        lineup_dict[artists[i]] = set_times[i]
    return lineup_dict

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))

# problem 2

def get_artist_info(artist, festival_schedule):
    if artist in festival_schedule:
        return festival_schedule[artist]
    else:
        return {"message": "Artist not found"}

festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))  

# problem 3

def total_sales(ticket_sales):
    return sum(ticket_sales.values())

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))

# problem 4

def identify_conflicts(venue1_schedule, venue2_schedule):
    conflicts = {}
    for artist, time in venue1_schedule.items():
        if artist in venue2_schedule and venue2_schedule[artist] == time:
            conflicts[artist] = time
    return conflicts

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))

# problem 5

def best_set(votes):
    counts = {}
    
    for voter_id, artist in votes.items():
        if artist not in counts:
            counts[artist] = 0
        counts[artist] += 1
    
    winner = max(counts, key=counts.get)
    return winner

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))

# problem 6

def max_audience_performances(audiences):
    if not audiences:
        return 0
    
    max_size = max(audiences)
    total = sum(a for a in audiences if a == max_size)
    return total

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))

# problem 7

def max_audience_performances(audiences):
    counts = {}
    for a in audiences:
        counts[a] = counts.get(a, 0) + a

    max_size = max(counts.keys())
    return counts[max_size]   

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))