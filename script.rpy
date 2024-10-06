# The script of the game goes in this file.


define f = Character("Fairy")
define p = Character("[name]")

# Variables
default napCount = 0 

# Stats
default willpower = 3
default health = 2


# The game starts here.

label start:

    $ drank_water = False

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bedroom

    # MEET DA FAIRY 

    show eileen happy

    f "Oh! I forgot to ask, what's your name?"

    python:
        # TODO: Extra dialogue if you put in a blank string
        name = renpy.input("Your name, please!:", length=32)

    f "Nice to meet you formally, [name]!"

    p "Whatever..."
    

    # Fairy goes into explaining how to play the game. Then we start the phase 1
    jump phase1

    label phase1:
        scene bedroom

        menu:
            f "Alrighty, what do you want to do?"

            "Drink water":
                $ drank_water = True
                call drinkWater
                
            "Clean":
                jump phase1End

            "Open window":
                jump phase1End
            
            "Scroll Reels":
                jump phase1End

            "Nap":
                call nap
                $ napCount += 1
                jump phase2
        
        label phase1End:
            if willpower > 0:
                jump phase1
            else:
                f "Mornin' sleepyhead! You slept through the rest of the morning, hehe."
                f "It'd be a shame to stay in bed, so..."
                jump phase2


    label phase2:

        menu:
            f "What do you wanna do?"

            "Use the Restroom":
                f "Go piss, girl!"
                f "I'll... stay here. I won't peek, I promise!"
                scene bathroom
                jump phase2End
                
            "Take a Shower":
                scene bathroom
                jump phase2End

            "Wash your hair in the sink":
                f "Great choice! Even if it's not good as washing your hair, it still makes you feel good!"
                jump phase2End

            "Open the window":
                scene bedroom
                jump phase2End
            
            "Vent on Twitter":
                jump phase2End

            "Nap":
                call nap
                $ napCount += 1
                jump phase3

        label phase2End:
            if willpower > 0:
                jump phase2
            else:
                f "Up up up! It's evening, and I think we should try and go to the kitchen."
                jump phase3

    label phase3:

        if napCount == 2:
            scene bedroom 

            menu:
                # fairy sad
                f "Do... you want to do anything?" 
                "Nap":
                    call nap
                    $ napCount += 1
                    f "..."
                    jump end
            
        else: # NapCount is high enough
            menu:
                f "Choose whatever you wanna do!"

                "Cook":
                    scene kitchen
                    jump phase3End
                    
                "Wash Dishes":
                    scene kitchen
                    jump phase3End

                "Order Takeout":
                    scene kitchen
                    jump phase3End
                
                "Eat a snack":
                    scene kitchen
                    jump phase3End

                "Nap":
                    call nap
                    $ napCount += 1
                    jump end

        label phase3End:
            if willpower > 0:
                jump phase3
            else:
                jump end


    
    label end:
        if(napCount == 3):
            jump badEnd
        elif(joy):
            jump goodEnd
        else:
            jump midEnd
        
    
    label goodEnd:
        return
    label badEnd:
        "Death shall take thee!!!!!"
        return
    label midEnd:
        return
    # This ends the game.
    return
