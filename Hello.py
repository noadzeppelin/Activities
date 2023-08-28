# Hello World example
print("Hello, World")

# setting variables and printing them
string = "Hello, World Again!"
sum = 5 + 7
print(string + str(sum))
#This prints out Hello, World Again!12

# creating a function to concat a string together while using one input variable
variable = "Data"

#the x inside the function is only available within the function
def data_science_jobs(x):
    print(x + " Scientist")
    print(x + " Analyst")
    print(x + " Engineer")

#this statement is putting "variable" into the function and at this point variable = x
data_science_jobs(variable)
# this prints out "Data Scientist, Data Analyst, Data Engineer"

# for loop example
for i in string:
    print(i)
# This prints each letter of "Hello, World Again!" on a separate line

# while loop example
x = 53
while x >= 5:
    print(x)
    x = x - 15
#Prints each number from 53 to the last number that's higher than or equal to 5 in increments of 15

#Fizz Buzz exercise
for y in range(100):
    if y % 3 == 0 and y % 5 == 0:
        print("FizzBuzz")
    elif y % 3 == 0:
        print("Fizz")
    elif y % 5 == 0:
        print("Buzz")
    else:
        print(y)
#Prints each number from 1 - 100 as "Fizz", "Buzz", "FizzBuzz", or the number that isn't divisble by 5 or 3

#using the length fucntion and finding position of a string
word = "Hippopotomonstrosesquippedaliophobia"
print(len(word))
thriteenth_letter = word[12]
print(thriteenth_letter)

#prints the number of letters in Hippopotomonstrosesquippedaliophobia

#finding sub strings in string using a conditional
if "phobia" in word:
    print("Phobia means fear")

#doing splices and replaces
num = int(len(word)/2)
num_whole = int(len(word))
print(num)
print(word[0:num])
word2 = word.replace("phobia", "philica")
print(word2)
odd_letters = word[0:num_whole:2]
print(odd_letters)

#More extensive splices and replaces usage
sc = "Savvy Coders"
sc2 = sc.replace("S", "F") and sc.replace("C", "M")
sc2_alt = "F" + sc[1:5] + " " + "M" + sc[7:]
sc3 = sc.replace("Coders", "Riders")
print(sc)
print(sc2)
print(sc2_alt)
print(sc3)

#using f-strings
sc = "My name is python, and today is Friday, June 13 2025."
name = "Stewart"
day = "Tuesday"
month = "August"
num_day = str(8)
year = str(2023)
sentence = f"My name is {name}, and today is {day}, {month} {num_day} {year}."
print(sentence)

#creating team list with roles and creating zip and list functions
team_list = ["Andrew", "Dale", "Roxanne", "Stacey","Stewart"]
new_team_list = team_list[0:3] + team_list[-1:]
team_roles = ["Scrum Master", "Team Member", "Product Owner", "Note Taker"]
num_of_team_members = len(new_team_list)
combined_list = new_team_list + team_roles
print(combined_list)
print(num_of_team_members)
team = zip(new_team_list,team_roles)
team_full = list(team)
print(team_full)
# prints[('Andrew', 'Scrum Master'), ('Dale', 'Team Member'), ('Roxanne', 'Product Owner'), ('Stewart', 'Note Taker')]
word_as_list = []
word_lowercased = word.lower()
for letter in word_lowercased:
    word_as_list.extend(letter)
print(word_as_list)
word_as_list.sort(reverse=True)
print(word_as_list)

#reversing a letter by taking it from a list and putting it back together into a string, using a for loop

word_aphla_reversed = ""
for letter in word_as_list:
    word_aphla_reversed += letter

print(word_aphla_reversed)

#using a function to sort a list by the length of the strings in them
length_of_name = []
def calculate_length(e):
    for name in e:
        length_of_name.append(len(name))

new_list = ["Python", "JavaScript", "SQL", "Java", "C++"]
calculate_length(new_list)
print(length_of_name)
length_of_name.sort()
print(length_of_name)

# to create a specific jupyter notebook use the ".ipynb" at the end

#Using the copy function
new_new_list = new_list.copy()
print(new_new_list)

#using copy, import, and deepcopy to create a new list that can be modified while keeping the original unaltered
new_list = ["red", "blue", "green", "yellow"]
copy = new_list.copy()
import copy
list2 = copy.deepcopy(new_list)
list2[1] = "black"
print(list2 == new_list)
print(list2)
print(new_list)

#adding to a dictionary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
copy_car = car.copy()
copy_car.update({"color": "White"})
copy_car.update({"seats": 2})
print(copy_car)

#Nested loop
adj = ["red", "big", "juicy"]
fruits = ["apple", "orange", "pineapple"]
adj_fruit_list = []
for x in adj:
	for y in fruits:
		adj_fruit_list.append([x,y])
		fruits.remove(y)
	adj.remove(x)
print(adj_fruit_list)

#Less code, same result
for x in adj:
    for y in fruits:
        print(x,y)
        fruits.remove(y)
        break

#Using a while loop
x = 7
while x > 2:
     print(x)
     x = x - 1

#Using a nested while loop
i = 1
while i < 6:
    j = 0
    while j < i:
        print('&',end='')
        j=j+1
    print()
    i=i+1

#Using a nested for loop to break up a 2D list
adj_noun_list = [["red", "apple"], ["yellow", "banana"], ["orange", "orange"]]
broken_list =[]
for x in adj_noun_list:
    for y in x:
        broken_list.append(y)

print(broken_list)  

#Using a for loop to only print out numbers divisble by 5
for x in range(50):
    if not x % 5 == 0:
        continue:
    print(x)

#Using a while loop to take in 5 numbers to create an average
x = 5
sum = 0
count = 0
while x > 0:
    count += 1
    inp = int(input("Please give me a whole integar:"))
    sum += inp
    x -= 1
average = sum/count
print(average)

#random function to create rolling a dice
import random
diceThrow=random.randrange(1,7)
print("Dice throw ...", diceThrow)

#Creating and shuffling a deck of cards
deck_of_cards = []
suites = ["Diamonds", "Hearts", "Clubs", "Spades"]
card_value = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

for x in card_value:
    for y in suites:
        deck_of_cards.append(x + " of " + y)

random.shuffle(deck_of_cards)
print(deck_of_cards)

#Removing vowels
def remove_vowels(string):
    new_string = ""
    for letter in string:
        if not letter in "AEIOUaeiou":
            new_string += letter
    return new_string 

#test case 
string = "I really enjoy the Data Analytics and Python program at SavvyCoders"
remove_vowels(string)