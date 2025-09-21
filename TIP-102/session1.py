
# problem 1

def welcome():
	print("Welcome To The Hundred Acre Wood")


welcome()

# problem 2

def greeting(name):
	print(f"Welcome To The Hundred Acre Wood {name}! My name is Christopher Robin.")

greeting("Winnie the Pooh")

# problem 3

def print_catchphrase(character):
	if character == "Pooh":
		print("Oh brother!")
	elif character == "Tigger":
		print("TTFN: Ta-ta for now!")
	elif character == "Eeyore":
		print("Thanks for noticing me.")
	elif character == "Christopher Robin":
		print("Silly old bear.")
	else:
		print(f"Sorry! I don't know {character}'s catchphrase!")

character = "Pooh"
print_catchphrase(character)

character = "Piglet"
print_catchphrase(character)

# problem 4

def get_item(items, x):
	if x > len(items):
		print("None")
	else:
		print(items[x])

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
get_item(items, x)

items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
get_item(items, x)
    

# problem 5

def sum_honey(hunny_jars):
	res = 0
	
	for i in hunny_jars:
		res += i
	print(res)

hunny_jars = [2, 3, 4, 5]
sum_honey(hunny_jars)

hunny_jars = []
sum_honey(hunny_jars)

# problem 6

def doubled(hunny_jars):
	for i in range(len(hunny_jars)):
		hunny_jars[i] *= 2
	print(hunny_jars)

hunny_jars = [1, 2, 3]
doubled(hunny_jars)

# problem 7

def count_less_than(race_times, threshold):
    count = 0
    for time in race_times:
        if time < threshold:
            count += 1
    print(count)


race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
count_less_than(race_times, threshold)

race_times = []
threshold = 4
count_less_than(race_times, threshold)

# problem 8

def print_todo_list(task):
	print("\nPooh's To Dos:")
	for i in range(len(task)):
		print(f"{i}. {task[i]}")
	

task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

task = []
print_todo_list(task)

# problem 9

def can_pair(item_quantities):
    for qty in item_quantities:
        if qty % 2 != 0:  
            print(False)
            return
    print(True)
	
item_quantities = [2, 4, 6, 8]
can_pair(item_quantities)

item_quantities = [1, 2, 3, 4]
can_pair(item_quantities)

item_quantities = []
can_pair(item_quantities)

# problem 10

def split_haycorns(quantity):
    divisors = []
    for i in range(1, int(quantity**0.5) + 1):
        if quantity % i == 0:
            divisors.append(i)
            if i * i != quantity:
                divisors.append(quantity // i)
    divisors.sort()
    print(divisors)

quantity = 6
split_haycorns(quantity)

quantity = 1
split_haycorns(quantity)

# problem 11

def tiggerfy(s):
    chars_to_remove = "tiger"
    new_string = ""
    for char in s:
        if char.lower() not in chars_to_remove:
            new_string += char
    print(new_string)
	
s = "suspicerous"
tiggerfy(s)

s = "Trigger"
tiggerfy(s)

s = "Hunny"
tiggerfy(s)


