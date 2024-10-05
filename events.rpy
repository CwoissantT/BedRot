# Make event banks 
# When choosing an event/chore to do in script.rpy, choose from this bank
# Idk how to implement yet, but for now just write scenarios. They can either be voiced by fairy or you

label nap:
    f "E-eh? Are you sure...? I could-"
    p "I don't care..."

    "You take a nap."
    return

label scrollReels:
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
    $ event = renpy.random.randint(1,2)

    # Possible events
    if event == 1:
        "Event 1"
    else:
        "Event 2"
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