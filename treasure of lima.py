#adventure game
import time
print("Welcome to the adventure of the TREASURE OF LIMA")
print("************************************************")
print("You are visiting the AMBER CAVE, Nigeria")
print("To find the TREASURE OF LIMA, you must pass through the Amber Cave deep inside the Cave lies the famous TREASURE OF LIMA")
print("You will journey on an adventure into the Cave filled with Tunnels, with the map")
print("You can only pick one things")
print("sea water(s),Lamp(l),Tent(t),Rope(r),Sticks(s),chocolate(c)or worms(w)")
item= input("What is your choice?")
item2=input("what is your choice")
item3=input("what is your choice")
item4=input("what is your choice")
item5=input("what is your choice")
item6=input("what is your choice")
item7=input("what is your choice")
print("You enter the Cave, there are two tunnels in front of you.")
choice1 = input("Do you take right? enter y or n")
if choice1 =="y":
    print("proceed to the right")
    print("you hear strange sounds")
    time.sleep(3)#add 3 seconds pause here for user to read
    print("The game just begins")
    time.sleep(5)#add 5 seconds pause here for the user to read
    print("YOU CHOSE THE WRONG PATH")
    print("you walked into the dens of gaint rats")
    time.sleep(4)#add 4 seconds pause here for the user to read
    print("you are being chased by the group of gaint rats")
    direction = input("Which direction do you want to go? left, right")
    if direction=="left":
        print("You reached a dead end")
        if item == "w":
            print("feed the rats")
            print("the rats are filled and had a great feast, you are saved")
            time.sleep(5)#add 5 seconds pause here for the user to read
            print("CONGRATULATIONS!ESCAPED DEATH")
        else:
            print("if you had the can of warms you would have made it alive")
            print("----, you DIED!!!!")
    
    print("you can make another choice")
    if item2=="t":
        print ("you found your way out of the AMBER CAVE.")
        time.sleep(3)#add 3 seconds pause here for the the user to read
        print("you are now in the forest of the osumare")
        print("pitch a tent and rest for the night")
    else:
            print("you froze to death")
    print("you wake up to the the sound of a growling monster")
    print("You out of the tent")
    time.sleep(3)#add 3 seconds pause here for the user to read 
    print("you see the monster chasing you")         
    print("you fell into a ditch")
    if item3=="s":
        print("you throw the stick at it")
        print("you realised the monster is a lost dog in the mountain")
        time.sleep(3)#add 3 seconds pause here for the user to read
        print("YOU ARE FEW STEPS TO YOUR DESTINATION")
    else:
        print("you were bitten by the monster")
    print("you are stucked in the ditch")
    if item4=="r":
        print("you got out of the ditch using the rope")
    else:
        time.sleep(3)#add 3 seconds pause here for the user to read
        print("YOU ARE STUCKED")
    print("you find the gate where the TREASURE OF LIMA lies")
    if item5=="s":
        print("YOU FOUND THE TREASURE")
else:
    print("YOU CHOSE DEATH")
choice2= input("Do you want to take the left,y or n")
if choice2=="y":
    time.sleep(5)#add 5 seconds pause here for the user to read
    print("you entered the cave of death")
    print("opps wrong tunnel no way back")
    if item6=="l":
        print("flash the light for signal")
    else:
        print("You are lost")
    print("a chopper appears in the sky")
    print("the pilot asked if you have chocolate")
    if item7=="c":
        print("they throw the chopper rope down and you climbed up")
        print("you are saved")
    else:
        print("DEATH FOUND YOU")
else:
    print("you gave up, go home")

    
    

        
        
        
            
            
    
    
    
