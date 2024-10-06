# Make event banks 
# When choosing an event/chore to do in script.rpy, choose from this bank
# Idk how to implement yet, but for now just write scenarios. They can either be voiced by fairy or you

label nap:
    scene bedroom
    f shy "E-eh? Are you sure...? I could-"
    p "I don't care..."

    "You take a nap."
    return

label window:
    $ event = renpy.random.randint(1,3)

    play sound "openWindow.wav"

    # Possible events
    if event == 1:
        "It's been awhile since I opened the window." 
        "It took me a minute because it was stuck in place but it was nice to let in some fresh air."
        
    elif event == 2:
        "I heard the ice cream truck outside, but I decided to let it pass."
        "I remember how fun it felt as a kid to chase the ice cream truck down with my friends."
    else:
        "The window was letting in a golden stream into my room lighting everything up. Everything was glowing now."
        "Everything."

    $ pp.update(1, -1, 0)
    return

label drinkWater:
    $ event = renpy.random.randint(1,3)

    # Possible events
    if event == 1:
        "I wanted something to drink so I got some orange juice from the fridge. I was able to find my favorite my bluey cup!"
        play sound "drinkingSound.mp3"
    elif event == 2:
        "My mouth feels so parched, when was the last time I drank water?"
        play sound "drinkingSound.mp3"
    else:
        "I got my favorite drink, Strawberry Lemonade. It tastes like summer all over again! Yum!"
        play sound "<from 0 to 3>drinkingSound.mp3"

    $ pp.update(2, -1, 0)
    return

label cleanRoom: 
    $ event = renpy.random.randint(1,3)

    # Possible events
    if event == 1:
        "I was looking through my clothes on the floor. Some were clean, some of my underwear? Not so much… "
        $ pp.update(1, -2, 0)
    elif event == 2:
        "There was a weird smell coming from my room."
        "At first, I thought it was my clothes, then the dishes, but then I found a ramen cup, and under that cup an army of cockroaches."
        $ pp.update(1, -2, 0)
    else:
        "There were wrappers all over the floor that were starting to get in the way."
        "Took me 30 minutes just to find all the wrappers."
        f "Your room is looking much better, though!"

        $ pp.update(2, -2, 0)
    
    return
    
label scrollReels:
    $ event = renpy.random.randint(1,3)

    # Possible events
    if event == 1:
        "I decided to spend my time scrolling reels. I keep getting reels of orange cat behavior."
        $ pp.update(0, -1, 0)
    elif event == 2:
        "I started scrolling reels, I don\’t remember how I started, but I did. I snapped out of it when I saw a clip from the Hawk Tuah podcast."
        $ pp.update(-1, -1, 0)
    else:
        "My friend sent me a reel recently. I saw it and it was kind of funny. I'm glad I'm still being thought of by some people."
        $ pp.update(1, -1, 0)

    return
    
label toilet:
    "It is time to relieve myself."
    #sfx toilet
    play sound "<from 0 to 4> toiletFlush.mp3"
    "………………………… gross" # TODO: pause in the middle?
    "at least my bladder doesn't hurt anymore."
    $ pp.update(3, -1, 0)
    return

label shower:
    $ event = renpy.random.randint(1,2)

    # Possible events
    if event == 1:
        "I needed to take a shower, finally."
        "I wanted to feel something, so I put the shower to its hottest setting. "
        play sound "<from 0 to 2>takeShower.mp3"
    else:
        "It felt nice having my skin soak up the warm water around me."
        "I should do this more often!"
        play sound "<from 0 to 2>takeShower.mp3"
    
    $ pp.update(3, -2, 0)
    
    return
    
label sink:
    $ event = renpy.random.randint(1,3)
    # Possible events
    if event == 1:
        "I decided to wash my hair in the sink, it felt kind of greasy."
        "It still feels kind of funny, but I definitely feel cleaner."
    elif event == 2:
        "My hair started to feel tangled and frizzy"
        "It was uncomfortable and weighing me down so some conditioner should make it feel better."
    else:
        "I was looking up some ways to keep my hair healthy, I heard about hair products to keep it hydrated."
        "I didn’t realize I had curly hair!!"
    $ pp.update(2, -1, 0)

    return
    
label twitter:
    $ event = renpy.random.randint(1,3)
    play sound "<from 0 to 1>socialMedia.mp3"
    # Possible events
    if event == 1:
        "I saw someone I knew from high school on social media getting married."
        "Meanwhile, the last thing I did was watch Jojo’s weird journey while eating cup ramen..."
        "Oh my god, am I wasting my life...?"
        f shy "Please don't say that about yourself...! I promise you, you're doing enough!"
        $ pp.update(-3, -100, 0)
        $ trauma = True
    elif event == 2:
        "I feel as if I spent hours on Instagram just scrolling."
        "I don't know when, but I stumbled upon some cute puppies. Maybe I should get one."
        $ pp.update(1, -1, 0)
    else:
        "I decided to put it on YouTube and just have it on in the background."
        "It was kind of relaxing to have it on in the background, like I wasn’t alone in my home."
        #TODO: f "Hey, I'm here too!!"
        $ pp.update(1, -1, 0)
    return

label cook:
    $ event = renpy.random.randint(1,3)

    # Possible events
    if event == 1:
        "I wanted something to eat but only had ingredients."
        "Being forced to cook is annoying but at least I can enjoy the smell."
        $ pp.update(6, -7, 3)
    elif event == 2:
        "I feel as if I only just started cooking before the fire alarm went off!"
        "ALL I DID WAS BOIL WATER!" # TODO: with vpunch
        $ pp.update(2, -7, 2)
    else:
        "It’s been a while since I last cooked..."
        "Thankfully I remember how to make the homemade chili my sister taught me."
        $ pp.update(6, -7, 4)
    return

label dishes:
    $ event = renpy.random.randint(1,3)

    # Possible events
    if event == 1:
        "I got on to the dishes as they started to pile up."
        #TODO: Glass breaking sfx
        "One of them slipped and broke on the floor. Now I'm in danger of having blood all over the floor."
        $ pp.update(2, -3, 0)
    elif event == 2:
        "The dishes I have just kept piling up, I sometimes ask myself where they come from as there's so many."
        $ pp.update(3, -3, 0)
    else:
        "I really didn't want to do the dishes today as it was starting to rise higher than the sink."
        "... So I didn't, and just let the dishwasher do all the work."
        $ pp.update(4, -2, 0)
    return

label takeout:
    $ event = renpy.random.randint(1,3)

    # Possible events
    if event == 1:
        "There really wasn’t anything left in the fridge so boobereats will have to do."
        "I just want something cheap so WcDonalds will do."
    elif event == 2:
        "I saw I had a little spending money left and there was a 2-for-1 deal at Baco Tell."
        "My toilet will have a field day tomorrow. ^-^"
    else:
        "I wanted to try some Shendy’s from doorbash. My sandwich had a whole bite taken out of it..."
        f "That was me, sorry..."

        $ pp.update(3, -2, 1)
    return

label snack:
    $ event = renpy.random.randint(1,3)

    # Possible events
    if event == 1:
        "I decided on something quick to eat, some chips always hit the spot."
        $ pp.update(1, -1, 2)
    elif event == 2:
        "Settled on some yogurt, it's a bit old and is more cheese than yogurt at this point."
        $ pp.update(1, -1, 1)
    else:
        "I didn't have time to cook much today so I just settled on a bowl of cereal."
        "Breakfast is important, no matter the time of day."
        $ pp.update(2, -1, 1)
    
    return

label hobby:
    $ event = renpy.random.randint(1,3)

    # Possible events
    if event == 1:
        "I grabbed an old book off of my shelf, I haven\'t read it in awhile."
        "I wonder if im still where I left off..."
    elif event == 2:
        "My sketchbook is filled with old doodles of funny little creatures."
        "Maybe I can make them dance!"
        f "Hey... why do I look like one of those..."
    else:
        "I remember I used to play the flute in middle school. I think I could freshen up on my skills!"
        f "You sound amazing!"
    $ pp.update(0, -1, 2)
    return

    

