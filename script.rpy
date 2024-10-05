# The script of the game goes in this file.


define f = Character("Fairy")
define p = Character("[name]")


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
    
    jump nap

    label phase1:
        return
    label phase2:
        return
    label phase3:
        return

    
    label end:
        return

    # This ends the game.
    return
