import random


test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Obtain names here in a list
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")


# Logic to pick random person from the list 
count = (len(names))
todays_pick = random.randint(0,count-1)
bill_payer = (names[todays_pick])
print(f"{bill_payer} is going to buy the meal today!")