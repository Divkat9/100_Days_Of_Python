print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
direction = input(
    "In the treasure island, you can either find money or nirvana. Type left for money and right for nirvana: "
)

if direction == 'left':
    print(
        "you made a decision to find money. Now decide how you want to find it"
    )
    how = input("Type 1 to go on your own. If you need a guide type 2: ")
    if how == '1':
        print("You have decided to go on your own.")
        door = input("Choose to enter the red, yellow or blue door: ")
        if door == 'red':
            print("Bitten by snakes. Game over!")
        elif door == 'yellow':
            print("You found the treasure! You won the game!")
        else:
            print(
                "You selected blue and fell down through the sky door. Game over!"
            )
    elif how == '2':
        print(
            "If you needed a guide, you don't belong in treasure island! Game over!"
        )
    else:
        print("Invalid response. Game over!")
elif direction == 'right':
    print(
        "Money is the cause of mental turmoil. Not receiving the money is the way to Nirvana. Game over!"
    )
else:
    print("Your choice is invalid. Game over!")