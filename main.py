print('''
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@P @@@@@@@@@@@@@P"@@@ @@@@@ @@@@@ @@@@@@   @@   @@@ @@@@@@@@@@@@P"@
@@P          a@@            a@@@  @@@@  @@@@  @  @@ @ @@ @ @@@  @  @@       a@
@@@@@@@  @@@@@@@  @@@  @@@  @@@          @@@  @  @@   @@   @@@  @  @@  @@@  @@
@@@@@@@  @@@@@@@            @@@@  @@@@  @@@      @@@@@@@@@@@@      @@       @@
@@@@@@@  @@@@P@@  @@@  @@@  @@@@  @@@@  @@@@  @  @@        @@@  @  @@@@@@@@@@@
@@            @@            @@@@  @@@@  @P@@  @  @@ @@  @@ @@@  @  @@       @@
@@@@@@@  @@@@@@@@@@@@  @@@@@@@            @@  @  @@        @@@  @  @@  @@@  @@
@@@@@@@  @@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@    @@ @@  @@ @@@@    @@       @@
@@@@@@@  @@@@@@@@          @@@@@@ @@@@ @@@@@@@  @@@        @@@@@  @@@  @@@  @@
@@@@@@@  @@@@@@@@@@@@  @@@@@@@@@  @@@@  @@@@@  @ @@@@@  @@P@@@@  @ @@       @@
@@@@@@@  @@@@@@@@@@@@  @@@@P@@@  @@@@@@  @@@  @@@ @        @@@  @@@ @  @@@  @@
@@@@@@@  @@@@@@@            @@  @@@@@@@@  @  @@@@ @@@@  @@@@@  @@@@ @  @@P  @@
@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@ @ @@@@@@@@@@ @@@@@@ @@@@@@@  @@@ o@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Z.LIN@22/10/94@
''')
print("Welcome to 'Too Hot to Handle'.\n")
print("Your need to resist all tentation during this adventure or not...\n") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
step1 = input("You see a very hot guy. Do you want to talk to him? Type 'Yes' or 'No'?\n")

step_one = step1.lower()


if step_one == 'no':
  print("Well you will stay single forever.\nSee you next time!\n")
elif step_one == 'yes':
  step2 = input("He introduce himself and invite you for a drink. Do you want 'wine' or 'water'?\n")
  step_two = step2.lower()
  if step_two == 'wine':
    step4 = input("Looks like is starting to get steamy. Wine at the 'pool' in the 'living room' or the 'bedroom'?\n")
    step_four = step4.lower()
    if step_four == "pool":
      print("After a bit of wine, you feel hot and jump in the pool with your new partner!\n")
    elif step_four == "living room":
      print("Living room is cozy and you guys drink more wine while talking fun of each other.\n")
    elif step_four == "bedroom":
      print("Guess tonight there is more than wine to it! xoxo\n")
    else:
      step5 = input("Sorry, I didn't quite catch where you want to take your wine? Pool, living room or bedroom?\n")
      step_five = step5.lower()
  elif step_two == 'water':
    print("That's awkward, but we will allow that. Enjoy your iced water.\nSee you next time!\n")
  else:
    step2 = input("Wine or water my love?\n")
    step_two = step2.lower()

    if step_two == 'wine':
      step4 = input("Looks like is starting to get steamy. Wine at the 'pool' in the 'living room' or the 'bedroom'?\n")
      step_four = step4.lower()
      if step_four == "pool":
        print("After a bit of wine, you feel hot and jump in the pool with your new partner!\n")
      elif step_four == "living room":
        print("Living room is cozy and you guys drink more wine while talking fun of each other.\n")
      elif step_four == "bedroom":
        print("Guess tonight there is more than wine to it! xoxo\n")
      else:
        step5 = input("Sorry, I didn't quite catch where you want to take your wine? Pool, living room or bedroom?\n")
        step_five = step5.lower()
    
    elif step_two == 'water':
      print("That's awkward, but we will allow that. Enjoy your iced water.\nSee you next time!\n")
else:
  step3 = input("Could you confirm again with 'yes' or 'no'?\n")
  step_three = step3.lower()
  if step_three == 'no':
    print("Well you will stay single forever.\n")
  
print("Thank you for playing my game!")