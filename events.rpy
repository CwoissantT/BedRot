# Make event banks 
# When choosing an event/chore to do in script.rpy, choose from this bank
# Idk how to implement yet, but for now just write scenarios. They can either be voiced by fairy or you

label nap:
    f "E-eh? Are you sure...? I could-"
    p "I don't care..."

    "You take a nap."
    $ napCount++

    return


label clean: 
    # "Roll Dice" to choose event, it's a val
    # TODO: Improve random number gen
    $ event = renpy.random.choice([1, 2, 3])

    f "Oh, you're going to clean? That's a great idea!"
    # Possible events
    if event == 1:
        "Event 1"
    elif event == 2:
        "Event 2"
    else:
        "Event 3"
    
    return