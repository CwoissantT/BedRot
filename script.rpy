# The script of the game goes in this file.


define f = Character("Fairy")
define p = Character("[name]")

$ napCount = 0;

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
        
        jump phase2

    label phase2:
        jump phase3

    label phase3:
        jump end


    
    label end:
        if(napCount == 3):
            jump badEnd
        
        return
    
    label badEnd:
        "Death shall take thee!!!!!"
        return
    
    # This ends the game.
    return
