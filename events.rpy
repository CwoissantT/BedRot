# Make event banks 
# When choosing an event/chore to do in script.rpy, choose from this bank
# Idk how to implement yet, but for now just write scenarios. They can either be voiced by fairy or you

label nap:
    f "E-eh? Are you sure...? I could-"
    p "I don't care..."

    "You take a nap."
    return

label drinkWater:
    return

label cleanRoom: 
    # "Roll Dice" to choose event, it's a val
    # TODO: Improve random number gen
    $ event = renpy.random.randint(1,3)

    f "Oh, you're going to clean? That's a great idea!"
    # Possible events
    if event == 1:
        "Event 1"
    elif event == 2:
        "Event 2"
    else:
        "Event 3"
    
    return
    
label scrollReels:
    $ event = renpy.random.randint(1,3)

    # Possible events
    if event == 1:
        "I decided to spend my time scrolling reels. I keep getting reels of orange cat behavior."
    elif event == 2:
        "I started scrolling reels, I don\’t remember how I started, but I did. I snapped out of it when I saw a clip from the Hawk Tuah podcast."
    else:
        "My friend sent me a reel, I responded to it, but I needed to see more and more..."
    
    $ pp.update(0, -1, 0)

    return
    
label toilet:
    $ event = renpy.random.randint(1,3)

    # Possible events
    if event == 1:

        "Event 1"
        
    elif event == 2:
        "Event 2"
    else:
        "Event 3"
    return

label shower:
    $ event = renpy.random.randint(1,3)

    # Possible events
    if event == 1:
        "Event 1"
    elif event == 2:
        "Event 2"
    else:
        "Event 3"
    
    return
    
label sink:
    $ event = renpy.random.randint(1,3)

    f "Oh, you're going to clean? That's a great idea!"
    # Possible events
    if event == 1:
        "Event 1"
    elif event == 2:
        "Event 2"
    else:
        "Event 3"
    
    return
    
label twitter:
    $ event = renpy.random.randint(1,3)

    f "Oh, you're going to clean? That's a great idea!"
    # Possible events
    if event == 1:
        "Event 1"
    elif event == 2:
        "Event 2"
    else:
        "Event 3"
    return

label cook:
    $ event = renpy.random.randint(1,3)

    f "Oh, you're going to clean? That's a great idea!"
    # Possible events
    if event == 1:
        "Event 1"
    elif event == 2:
        "Event 2"
    else:
        "Event 3"
    return

label dishes:
    $ event = renpy.random.randint(1,3)

    f "Oh, you're going to clean? That's a great idea!"
    # Possible events
    if event == 1:
        "Event 1"
    elif event == 2:
        "Event 2"
    else:
        "Event 3"
    return

label takeout:
    $ event = renpy.random.randint(1,3)

    f "Oh, you're going to clean? That's a great idea!"
    # Possible events
    if event == 1:
        "Event 1"
    elif event == 2:
        "Event 2"
    else:
        "Event 3"
    return

label snack:
    $ event = renpy.random.randint(1,3)

    f "Oh, you're going to clean? That's a great idea!"
    # Possible events
    if event == 1:
        "Event 1"
    elif event == 2:
        "Event 2"
    else:
        "Event 3"

    return

    

