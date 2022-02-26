import random

#(1) roll the dice, (2)generate random dice nums, (3)call func to show current dice, (4)testing, (5)Move to next phase
def game(num_dice):
    print("\n**************")
    print("     Roll     ")
    print("**************")

#(1) roll the dice
    dice_score = {}
    ran = random.randrange
    input("\npress 'Enter' to roll your dice\n")
    print("You throw your dice on to the table and get:\n")

#(2)generate random nums
    for i in range(num_dice):
        x = ran(1, 6)
        dice_score[i + 1] = x

#(3) call func to show current dice
    showcurrentdice(dice_score)

#(4)testing
#####testing, set the dice numbers, nothing random
    #   dice_score= {1:6,2:5,3:6,4:5,5:5,6:6}
    # print("test dice: ",dice_score)
#####testing
      #   checkdice(dice_score) #skip selectdice func/ all selected dice and check the score

#(5)Move to next phase
    input("\npress 'Enter' to start selecting dice to keep")
    selectdice(dice_score)

#Show the dice selected==========================================
def showcurrentdice(dice_score):
    for i in range (len(dice_score)):
        print ("Dice", str(i+1) + ":", dice_score[i+1])
    return

# (1)LOOP: select a dice to remove from list============================
def selectdice(dice_score):
    print("**************")
    print("Dice selection")
    print("**************")

    print("Which dice would you like to roll again? type the dice number ")

    while True:
        userselect = int(input())
        if userselect in dice_score:
            del dice_score[userselect]
            print(userselect, "has been removed")
            print("your remainimg dice are:", dice_score)
        elif userselect == "":
            print("moving on")
            break
        else:
            print(userselect,"is not a dice.")

    """dicekeepers= str(input())
    print(dicekeepers)
    dicekeepers.split(" ")
    x=0
    for i in dicekeepers:
        x+=1
        #delthis=int(dicekeepers[x])
        del dice_score [dicekeepers[x]]
        print(dicekeepers[x])
        print("x is: ",x)
    print("after deleted",dice_score)
    checkdice(dicekeepers)
    """

# ==============
def checkdice(dice_score):
    print("***************")
    print(" Checking Dice ")
    print("***************")

    print("\nscoring started")
    count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    # how many of each num there are
    for i in dice_score:
        count[dice_score[i]] += 1
    for i in count:
        print("there are", count[i], str(i) + "s")
    cal_score(count)

# ==============
def cal_score(count):
    print("***************")
    print("  Calculating  ")
    print("***************")
    total = 0
    print("\nAdding up points")

    #  1 score
    if count[1] == 1 or count[1] == 2:
        add_total = count[1] * 100
        total += add_total
        print(add_total, "points scored from 1s")
    elif count[1] == 3:
        add_total = 1000
        total += add_total
        print("1000 points scored from 1s")
    elif count[1] == 4:
        add_total = 2000
        total += add_total
        print("2000 points scored from 1s")
    elif count[1] == 5:
        add_total = 4000
        total += add_total
        print("4000 points scored from 1s")
    elif count[1] == 6:
        add_total == 8000
        total += add_total
        print("8000 points scored from 1s")
    else:
        print("You've scored nothing from 1s")

    #  5 score
    if count[5] == 1 or count[5] == 2:
        add_total = count[5] * 50
        total += add_total
        print(add_total, "points scored from 5s")
    elif count[5] == 3:
        add_total = 500
        total += add_total
        print("500 points scored from 5s")
    elif count[5] == 4:
        add_total = 1000
        total += add_total
        print("1000 points scored from 5s")
    elif count[5] == 5:
        add_total = 2000
        total += add_total
        print("2000 points scored from 5s")
    elif count[5] == 6:
        add_total = 4000
        total += add_total
        print("4000 points scored from 5s")
    else:
        print("You've scored nothing from 5s")

    # score  others
    nospecnums = [2, 3, 4, 6]
    for i in range(4):
        y = count[nospecnums[i]]
        if y <= 2:
            print("You've scored nothing from", nospecnums[i])
        elif y == 3:
            add_total = nospecnums[i] * 100
            total += add_total
            print(add_total, "points scored from", nospecnums[i])
        elif y == 4:
            add_total = nospecnums[i] * 100 * 2
            total += add_total
            print(add_total, "points scored from", nospecnums[i])
        elif y == 5:
            add_total = nospecnums[i] * 100 * 2 * 2
            total += add_total
            print(add_total, "points scored from", nospecnums[i])
        elif y == 6:
            add_total = nospecnums[i] * 100 * 2 * 2 * 2
            total += add_total
            print(add_total, "points scored from", nospecnums[i])

    showtotal(total)

# ==============

def showtotal(total):
    print("\nYour total score is:", total)

# ==============

game(6)
