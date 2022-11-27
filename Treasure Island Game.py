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
# For other arts like this please visit the following URL:
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

print("You are walking on road to find treasure. It goes two ways- Left and Right.")
walkway = input("press R for right and L for left. ")
if walkway == "R":
  print("You walk for a while and a reach a lake with an island not so far,this is the Treasure Island. There are some traders nearby who might give you their boat if you ask them or you can swim through the lake")
  lake = input("Press T to ask a Trader or S to Swim across. ")
  if lake == "T":
    print("The Trader lends you his boat for a while. You use it to reach the Treasure Island. You come across three magical doors of colors-Red, Blue and Yellow. Pick a Door.")
    door =input("Select R for Red B for Blue and Y for Yellow. ")
    if door == "R":
      print("You opened the Red Door and a Dragon was sitting leashed with magic but he saw you and blew fire on you. Game over")
    elif door == "B":
      print("The Demon of Water was locked inside the door. You unlocked him and he killed you and also became a problem for the world. Game over.")
    elif door == "Y":
      print("You found the Treasure and returned back gifting some of it to your trader friends and returned to your homeland." + "\nYou won "+"\nHope you enjoyed our game.")
  elif lake == "S":
    print("You tried to swim in the river and when you reached near the island, a crocodile ate you. Game Over")
else:
  print("You come across a Tiger. Game Over")