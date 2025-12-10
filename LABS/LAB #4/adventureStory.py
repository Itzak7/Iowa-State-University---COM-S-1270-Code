#Isaac Aguialr              10-2-2025
#adventure 

def main():
    print()
    print("Here we are in Abu Dhabi, the last race of the Formula 1 season! You are currently second in the drivers championship only separated by 1 point from first place."
    "You've made it to Q3 and have time for 1 more lap to secure pole position from your rival!") 
    print()
    Choice1 = input("Do you go do your last lap on a cold set of [S]oft tires or a warm set of [M]edium tires?: ").upper()
    if Choice1 == "S":
        print()
        print("The risk paid off! Your soft tires heated up quickly and had better traction in the corners, resulting in pole position!") 
    elif Choice1 == "M": 
        print()
        print("It was too good to be true as you were flying through the track, but at the last corner had a lock-up and cost the lap! You still maintained your previous fastest lap which keeps you starting in P2!") 
    else:
        print("OOOPS! please enter a valid choice!")
        return
    print()
    print("It's now race day and you feel the nerves setting in. Nonetheless you get ready for the race!")
    print()
    Choice2 = input("You are talking with your engineers about your pit strategy for the race. Do you go for a [3] pit strat or a risky [1] pit strat with 58 racing laps?: ").upper()
    if Choice2 == "1":
        print("You chose a risky 1 pit strat, but your engineers feel confident you can do it! As the 5 red lights disappear you set off, but you don’t push as hard to conserve your tires!")
        print()
        print("As the race begins you start to fall behind the field, but this is all part of your plan as you want to conserve your tires")
        print()
        print("It's lap 20 and everyone comes in for their pit stop, but you stay out and now you're first!")
        print()
        Choice7 = input("Now lap 33, you have a 15 second lead so you come in for pit stop! Do you pit for [S]oft tires or [H]ards?: ").upper()
        if Choice7 == "S":
            print()
            print("Your engineers don't love the choice but trust you!")
        elif Choice7 == "H":
            print()
            print("Your engineers love the choice and you set off to finish the race in a demanding fashion!")
        else:
            print("OOOPS! please enter a valid choice!")
            return
        print()
        print("With 10 laps to go a crash between 2 cars happened resulting in a safety car being released!")
        print()
        Choice8 = input("Do you [P]it now to get a fresh set of tires and finish the race, or do you [S]tay out on your old tires and take first place as your rival goes in to pit?: ").upper()
        if Choice8 == "P":
            print()
            print("You decide to come in for fresh set of Mediums as that was all you had left, and now behind the safety car you are leading the pack and your rival is right behind you!")  
        elif Choice8 == "S":
            print()
            print("You stay out! A bold choice and you begin to worry if your tires will be able to last 10 more laps!")
        else:
            print("OOOPS! please enter a valid choice!")
            return
        print()
        print("After many laps of removing both cars off and cleaning the track the safety car finally comes in, and leaves 1 lap left to settle this championship! "
         "As you and your rival set off the final lap, he gives it everything on you! All comes down to the final corner and it looks like your rival is going to dive bomb on the inside!!!")
        print()
        Choice9 = input("Do you go towards the [I]nside of the corner to defend, or do you go [W]ide and let him have the corner?: ").upper()
        if Choice9 == "I":
            print()
            print("You go for the defense move! But wait, your rival is now to your side! It was a trick and now you lock up and drive off the track and crash!"
            " You end up DNFing from the race and end up in 2nd place in the drivers championship!")
            print("The End!")
        elif Choice9 == "W":
            print()
            print("You decide to keep your wide line and it pays off! Your rival brakes late into the corner and locks up! Resulting in him crashing and now you keep first and WIN THE RACE AND THE DRIVERS CHAMPIONSHIP!!!")
            print("The End!")
        else:
            print("OOOPS! please enter a valid choice!")
            return
    elif Choice2 == "3":
        print()
        print("You chose to go with the safe 3 pit strat that allows you to push more! That's exactly what you do in the race! 5 red lights go out and you fly from the rest of the grid!")
        print()
        Choice3 = input("It's lap 19 and your tires feel dead now so you come in for your first pit. Do you pit for [S]oft tires to go even faster, but have to pit sooner, or pit for [H]ard tires for slightly slower pace but can be out on track more?: ").upper()
        if Choice3 == "S": 
            print()
            print("Oh no your pit crew expected you to pit for Hards so they have to go back and grab the right tires costing you so much time, thus resulting in a 9 second pit stop and now you lost many places!")      
        elif Choice3 == "H":
            print()
            print("Your pit crew was ready for you and clocked the quickest pit stop of the season at 1.8 seconds! More importantly you maintain first place!")    
        else:
            print("OOOPS! please enter a valid choice!")
            return
        print()
        Choice4 = input("It's now lap 31 and you're still second place, so you come in for 2nd pit stop! Do you switch to a [M]edium set or another set of [S]ofts?: ").upper()
        if Choice4 == "M":
            print()
            print("Your engineers didn't love the choice since this stint will be shorter and you'll be slower but they trust your choice!")
        elif Choice4 == "S":
            print()
            print("Good choice! You exit the pit and set the fastest lap of the race! Now with your faster pace you start to cut through the field and aim for 1st!")
        else:
            print("OOOPS! please enter a valid choice!")
            return
        print()
        print("With 10 laps to go a crash between 2 cars happened resulting in a safety car being released!")
        Choice5 = input("Do you [P]it now to get a fresh set of tires and finish the race, or do you [S]tay out on your old tires and take first place as your rival goes in to pit?: ").upper()
        
        if Choice5 == "P":
            print()
            print("You decide to come in for fresh set of Mediums as that was all you had left, and now behind the safety car you are second right behind your rival!")  
        elif Choice5 == "S":
            print()
            print("You stay out! A bold choice and you begin to worry if your tires will be able to last 10 more laps!")
        else:
            print("OOOPS! please enter a valid choice!")
            return
        print()
        print("After many laps of removing both cars off and cleaning the track the safety car finally comes in, and with 1 lap left to settle this championship, you give it everything you got!"
              " The final lap is started and you set off towards first place! But corner after corner he defends your every move except the last where he slips up!")
        print()
        Choice6 = input("Do you go towards the [I]nside of the corner and brake late to overtake him, or do you go [W]ide and brake early in hopes he brakes late and locks up?: ").upper()
        if Choice6 == "I":
            print()
            print("You go for the late lunge and IT WORKS! Your late brake allows you to overtake him in the last corner and win the drivers championship!")
            print("The End!")
        elif Choice6 == "W":
            print()
            print("You decide to brake early and it did not pay off as your rival has a smooth late brake and keeps first place resulting in 2nd place in the race and the championship.")
            print("The End!")
        else:
            print("OOOPS! please enter a valid choice!")
            return
    
    else:
        print("OOOPS! please enter a valid choice!")
        return







if __name__=="__main__":

    main()

