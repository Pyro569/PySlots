#import radom because this will be very important to the process
import random

#set a random int so i can make an infinite loop
randomIntForInfLoop = 1

#handle random numbers and checking if rows are the same
def doSlots():
   
    #ask for the betting money
    bettingMoney = int(input("How much money are you going to bet? "))
    
    winnings = 0
    
    losses = 0
    
    #make the random ints for the slots
    slotNum1 = random.randint(1, 9)
    slotNum2 = random.randint(1, 9)
    slotNum3 = random.randint(1, 9)
    slotNum4 = random.randint(1, 9)
    slotNum5 = random.randint(1, 9)
    slotNum6 = random.randint(1, 9)
    slotNum7 = random.randint(1, 9)
    slotNum8 = random.randint(1, 9)
    slotNum9 = random.randint(1, 9)
    
    # make multiplier (1-20) for money to win/lose
    moneyMultiplier = random.randint(1, 20)

    #print the numbers that the user gets
    print()
    print(str(slotNum1) + " " + str(slotNum2) + " " + str(slotNum3))
    print()
    print(str(slotNum4) + " " + str(slotNum5) + " " + str(slotNum6))
    print()
    print(str(slotNum7) + " " + str(slotNum8) + " " + str(slotNum9))
    
    #operations relating to money
    losses = bettingMoney / moneyMultiplier
    winnings = bettingMoney * moneyMultiplier
    moneyLeftOverLost = bettingMoney - losses

    # check to see if any rows are the same, and what to do.
    if slotNum1 == slotNum2 & slotNum2 == slotNum3:
        print("You won. ")
        print("You now have " + str(winnings) + " dollars. ")
        print()
    elif slotNum4 == slotNum5 & slotNum5 == slotNum6:
        print("You won. ")
        print("You now have " + str(winnings) + " dollars. ")
        print()
    elif slotNum7 == slotNum8 & slotNum8 == slotNum9:
        print("You won. ")
        print("You now have " + str(winnings) + " dollars. ")
        print()
    else:
        print()
        print("NO WIN! ")
        print("You lost " + str(losses) + " dollars! ")
        print()
    
#do the slots stuff
while randomIntForInfLoop > 0:
    doSlots();