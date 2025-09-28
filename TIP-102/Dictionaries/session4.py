# IC

def find_difference(signals1, signals2):
    set1 = set(signals1)
    set2 = set(signals2)
    
    diff1 = list(set1.difference(set2))
    diff2 = list(set2.difference(set1))
    
    return [diff1, diff2]

s1 = [1, 2, 3, 4]
s2 = [2, 3, 5, 9]

print(find_difference(s1, s2))

# problem 1

def most_endangered(species_list):

    if not species_list:
        return None
    
    most_endangered_species = species_list[0]
    
    for species in species_list[1:]:
        if species["population"] < most_endangered_species["population"]:
            most_endangered_species = species
    
    return most_endangered_species["name"]

    # if not species_list:
    #     return None
    
    # return min(species_list, key=lambda species: species["population"])

species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))

# problem 2

def count_endangered_species(endangered_species, observed_species):
    endangered_set = set(endangered_species)
    
    count = 0
    for i in observed_species:
        if i in endangered_set:
            count += 1
    
    return count


endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))  

# problem 3

def navigate_research_station(station_layout, observations):
    index_map = {char: i for i, char in enumerate(station_layout)}
    
    total_time = 0
    current_pos = 0  
    
    for obs in observations:
        next_pos = index_map[obs]
        total_time += abs(current_pos - next_pos)
        current_pos = next_pos
    
    return total_time


station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))

# problem 4

def prioritize_observations(observed_species, priority_species):
    result = []

    for species in priority_species:
        for obs in observed_species:
            if obs == species:
                result.append(obs)

    extras = [obs for obs in observed_species if obs not in priority_species]

    result.extend(sorted(extras))

    return result


observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print(prioritize_observations(observed_species1, priority_species1))
print(prioritize_observations(observed_species2, priority_species2)) 

# problem 5

def distinct_averages(species_populations):
    species_populations.sort() 
    left, right = 0, len(species_populations) - 1
    averages = set() 

    while left < right:
        avg = (species_populations[left] + species_populations[right]) / 2
        averages.add(avg)
        left += 1
        right -= 1

    return len(averages)


species_populations1 = [4,1,4,0,3,5]
species_populations2 = [1,100]

print(distinct_averages(species_populations1))
print(distinct_averages(species_populations2)) 

# problem 6

def max_species_copies(raised_species, target_species):
  species_dict = {}
  target_dict = {}

  for i in range (len(raised_species)):
      if raised_species[i] in species_dict:
          species_dict[raised_species[i]] += 1
      else:
          species_dict[raised_species[i]] = 1

  for word in range (len(target_species)):
      if target_species[word] in target_dict:
        target_dict[target_species[word]] += 1
      else:
        target_dict[target_species[word]] = 1

  res = float('inf')

  for i in target_dict:
    if i not in species_dict:
        return 0  
    res = min(res, species_dict[i] // target_dict[i])
  
  return res

raised_species1 = "abcba"
target_species1 = "abc"
print(max_species_copies(raised_species1, target_species1))  # Output: 1

raised_species2 = "aaaaabbbbcc"
target_species2 = "abc"
print(max_species_copies(raised_species2, target_species2)) # Output: 2

# problem 7

def count_unique_species(ecosystem_data):
  nums = []
  curr = ""

  for i in range(len(ecosystem_data)):
      if ecosystem_data[i].isnumeric():
        curr += ecosystem_data[i]
      else:
        if curr != "":
          nums.append(int(curr))
          curr = ""
      
  if curr != "":
     nums.append(int(curr))
    

  res = list(set(nums))

  return len(res)

ecosystem_data1 = "f123de34g8hi34"
ecosystem_data2 = "species1234forest234"
ecosystem_data3 = "x1y01z001"

print(count_unique_species(ecosystem_data1)) # 3
print(count_unique_species(ecosystem_data2)) # 2
print(count_unique_species(ecosystem_data3)) # 1