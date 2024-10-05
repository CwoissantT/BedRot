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

    name = renpy.input("Your name, please!:")

    f "Nice to meet you formally, [name]!"
    # TODO: Extra dialogue if you put in a blank string


    

    # This ends the game.

    return
