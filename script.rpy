﻿# The script of the game goes in this file.


define f = Character("Fairy", who_color="#ff3875", image="fairy")
define p = Character("[name]")
define pp = MC(p, 2, 3, 0, 3, 0)

# Variables
default napCount = 0 
default peed = False
default trauma = False
default parched = True
default showered = False
default hungry = True


# The game starts here.

label start:
    stop music

    

    "Ugh.... I'm so tired..."
    "I don't remember when the last time I got out of bed was."

    "I don't know if it's even worth it anymore..."

    "..."

    "Random Voice In Your Head" "Congratulations dear customer!" 
    "Random Voice In Your Head" "Through legally dubious means, you have won the opportunity of receiving your very own mental health fairy!"
    "Random Voice In Your Head" "They will do their best to point you in the right direction!"
    scene closedcurtain

    # MEET DA FAIRY 
    play music "塩コショウはかけましょう.mp3"
    show fairy happy
    f "Hello! I'm your personal fairy!"

    show fairy disappointed
    f "You look rather sad... but it's ok! I'm here to help!"
    f "..."

    show fairy neutral
    f "Oh! I forgot to ask, what's your name?"


    python:
        # TODO: Extra dialogue if you put in a blank string
        name = renpy.input("Your name, please!:", length=32)
    
    # if(name == ""): 

    show fairy happy
    f "Nice to meet you formally, [name]!"

    p "Whatever..."

    show fairy disappointed
    f "Oh, that's a sour face for a cute person..."

    show fairy happy
    f "Well, I'll turn that frown upside down!" with vpunch
    f "I'll be next to you alll day, just to encourage you!" with vpunch 
    f "Anything you're able to do is amazing and worth celebrating!" with vpunch
    p "..."

    show fairy neutral
    f "Just note that certain actions will increase your health, like cooking or cleaning."

    show fairy shy
    f "While others, like scrolling on your phone, may not do much at all."

    show fairy nervous
    f "Hmmm..."
    
    show fairy shy
    f "It looks like you're looking pretty tired, [name]. It's ok if you don't instantly feel joy from anything you do right now!"
    f "Being burnt out sucks, hm?"
    p "Now I feel like you're just patronizing me."

    show fairy disappointed
    f "!!!"
    f "Uhm!! Oh dear- I'm so sorry... I- I didn't mean... You're perfectly fine the way you are!"
    p "..."
    show fairy nervous
    p "It's ok. Let's just get started or whatever..."
    

    # Fairy goes into explaining how to play the game. Then we start the phase 1
    scene closedcurtain
    $ pp.setPhase(2, 3, 0)
    play music "Dances and Dames.mp3"
    jump phase1
    

    label phase1:
        show screen status_ui
        

        menu:
            f neutral "Alrighty, what do you want to do?"

            "Drink water" if pp.willpower > 0 and parched:
                $ parched = False
                f "Oh, you're thirsty aren't you?"
                f "Now... what is there to drink around here...?"
                call drinkWater from _call_drinkWater
                
            "Clean" if pp.willpower > 1:
                f "Oh, you're going to clean? That's a great idea!"
                call cleanRoom from _call_cleanRoom

            "Open window" if pp.willpower > 0:
                f "..."
                call window from _call_window
            
            "Scroll Reels" if pp.willpower > 1:
                f "... Are you sure? I mean, you could always-"
                p "I'm fine."

                call scrollReels from _call_scrollReels

            "Nap":
                call nap from _call_nap
                $ napCount += 1
                # Condition after character naps away
                $ pp.maxW = pp.health - 1
                $ pp.setPhase(pp.health, pp.maxW, 0)
                scene black

                scene closedcurtain with Fade(0.5, 1.0, 0.5)
                show fairy shy
                f "Oh dear... Please wake up, [name]!"
                f "I know you're tired... but please, let's try to do something, ok?"

                play music "Backed Vibes Clean.mp3"
                jump phase2
        
        label phase1End:
            if pp.willpower > 0:
                jump phase1
            else:
                hide screen status_ui
                scene black

                p "I fell asleep..."
                scene closedcurtain with Fade(0.5, 1.0, 0.5)

                f "Mornin' sleepyhead! You slept through the rest of the morning, hehe."
                f "It'd be a shame to stay in bed, so..."

                # Condition if character does not nap away
                $ pp.maxW = pp.health + 3
                $ pp.setPhase(pp.health, pp.maxW, 0)
                play music "I Knew a Guy.mp3"
                jump phase2


    label phase2:
        show screen status_ui
        hide fairy shy

        

        menu:
            f neutral "What do you wanna do?"

            "Use the Restroom" if peed == False:
                $ peed = True
                f "Go piss, girl!"
                f "I'll... stay here. I won't peek, I promise!"
                scene bathroom
                call toilet from _call_toilet
                
            "Take a Shower" if pp.willpower >= 2 and not showered:
                $ showered = True
                f "... Um."
                f "I'll just wait outside."
                scene bathroom
                call shower from _call_shower

            "Wash your hair in the sink" if pp.willpower > 1 and not showered:
                f "Great choice! Even if it's not good as washing your hair, it still makes you feel good!"
                call sink from _call_sink

            "Open the window" if pp.willpower > 1:
                f "..."
                scene closedcurtain
                call window from _call_window_1
            
            "Go on Social Media" if pp.willpower > 1 and not trauma:
                f "Oh... well, I guess if you're not going for too long."
                call twitter from _call_twitter
            

            "Nap":
                call nap from _call_nap_1
                $ napCount += 1
                $ pp.maxW = pp.health - 1 # if you nap the phase away
                scene black 
                scene closedcurtain with Fade(0.5, 1.0, 0.5)

                $ pp.setPhase(pp.health, pp.maxW, 0)

                if napCount == 2:
                    pass
                else:
                    play music "Upbeat.mp3"
                jump phase3

        label phase2End:
            if pp.willpower > 0:
                jump phase2
            else:
                scene closedcurtain
                f happy "Up up up! It's evening, and I think we should try and go to the kitchen!"

                $ pp.maxW = pp.health + 3 # If character doesn't nap the phase away
                if trauma:
                    $ pp.maxW = 3
                
                play music "Upbeat.mp3"
                $ pp.setPhase(pp.health, pp.maxW, 0)
                jump phase3

    label phase3:
        

        if napCount == 2:
            play music "Somber.mp3"
            scene closedcurtain 

            menu:
                # fairy sad
                f shy "Do... you want to do anything?" 
                "Nap":
                    call nap from _call_nap_2
                    $ napCount += 1
                    f "..."
                    jump end
            
        else: # NapCount is high enough
            show screen status_ui
            menu:
                f neutral "Choose whatever you wanna do!"

                "Cook" if pp.willpower > 7 and hungry:
                    $ hungry = False
                    scene kitchen
                    call cook from _call_cook
                    
                "Wash Dishes" if pp.willpower > 3:
                    scene kitchen
                    call dishes from _call_dishes

                "Order Takeout" if pp.willpower > 2 and hungry:
                    $ hungry = False
                    scene kitchen
                    call takeout from _call_takeout
                
                "Eat a snack" if pp.willpower > 2:
                    scene kitchen
                    call snack from _call_snack
                
                "Try a Hobby" if pp.willpower > 2:
                    scene bedroom
                    call hobby from _call_hobby

                "Nap":
                    call nap from _call_nap_3
                    $ napCount += 1
                    hide screen status_ui
                    jump end

        label phase3End:
            if pp.willpower > 0:
                jump phase3
            else:
                hide screen status_ui
                jump end


    
    label end:
        if(pp.joy > 5):
            play music "In Your Arms.mp3"
            jump goodEnd
        elif(pp.health > 5):
            play music "Jazz Brunch.mp3"
            jump midEnd
        else:
            play music "bad ending.mp3"
            jump badEnd
        
    
    label goodEnd:
        scene good end 2
        f "You're starting to see the good in the little things!"
        f "The weight that you used to feel just cleaning your room is gone."
        f "You start working on the goals you’ve been putting off, and you always look forward to facing new challenges."

        scene good end 1
        f "Ah... I'm so proud of you, [name]!"
        f "I just know you'll find yourself in a better place, soon. Take care!"
        return
    label badEnd:
        hide screen status_ui
        scene black with fade 
        "It\'s over…… it\'s finally over. I dont need to struggle anymore."
        "The numbness will be gone soon and I can be at peace."
        f "No, no! Please- don't disappear, [name]! You can still go on..."

        "I'm so tired..."
        "..."
        "If I could do it all over again, I\’d try again, I\’d try harder and do my best."
        "Next time, next time I\'ll do better... But for now, it\'s over." 
        f "*Sniffle* ..."
        f "You... can rest now, then..."

        return
    label midEnd:
        scene mid end with fade
        f "... The end!"
        f "Life feels just that bit easier."
        f "You still struggle, just not as much." 
        f "Even if you'll have your ups and downs, but you are definitely on the right path!"
        f "You don’t know what challenges life will bring... but you look at them with less negativity."
        return
    # This ends the game.
    return
