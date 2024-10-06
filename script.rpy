# The script of the game goes in this file.


define f = Character("Fairy")
define p = Character("[name]")

default napCount = 0

# Testing git

# The game starts here.

label start:

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

        menu:
            f "Alrighty, what do you want to do?"

            "Drink water":
                jump phase1End
                
            "Clean":
                jump phase1End

            "Open window":
                jump phase1End
            
            "Scroll Reels":
                jump phase1End

            "Nap":
                call nap
                $ napCount += 1
                jump phase1End
        
        label phase1End:
            jump phase2

    label phase2:
        f "Let's start phase 2!"
        menu:
            f "Alrighty, what do you want to do?"

            "Use the Restroom":
                jump phase2End
                
            "Take a Shower":
                jump phase2End

            "Wash your hair in the sink":
                f "Great choice! Even if it's not good as washing your hair, it still makes you feel good!"
                jump phase2End

            "Open window":
                jump phase2End
            
            "Vent on Twitter":
                jump phase2End

            "Nap":
                call nap
                $ napCount += 1
                jump phase2End

        label phase2End:
            call phase3

    label phase3:
        if napCount == 2:
            menu:
                # fairy sad
                f "Do... you want to do anything?" 
                "Nap":
                    call nap
                    $ napCount += 1
                    f "..."
                    jump phase3End
            
        else: # NapCount is too high to do anything
            menu:
                f "Alrighty, what do you want to do?"

                "Cook":
                    jump phase3End
                    
                "Wash Dishes":
                    jump phase3End

                "Order Takeout":
                    jump phase3End
                
                "Eat a snack":
                    jump phase3End

                "Nap":
                    call nap
                    $ napCount += 1
                    jump phase3End

        label phase3End:
            jump end


    
    label end:
        if(napCount == 3):
            jump badEnd
        
    
    
    label badEnd:
        "Death shall take thee!!!!!"
        return
    
    # This ends the game.
    return
