# The script of the game goes in this file.


define f = Character("Fairy", image="fairy")
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

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bedroom

    # MEET DA FAIRY 
    show fairy happy
    f "Oh! I forgot to ask, what's your name?"


    python:
        # TODO: Extra dialogue if you put in a blank string
        name = renpy.input("Your name, please!:", length=32)
    f "Nice to meet you formally, [name]!"

    p "Whatever..."
    

    # Fairy goes into explaining how to play the game. Then we start the phase 1
    scene bedroom
    $ pp.setPhase(2, 3, 0)
    play music "Dances and Dames.mp3"
    jump phase1
    

    label phase1:
        show screen status_ui
        

        menu:
            f neutral"Alrighty, what do you want to do?"

            "Drink water" if pp.willpower > 0 and parched:
                $ parched = False
                f "Oh, you're thirsty aren't you?"
                f "Now... what is there to drink around here...?"
                call drinkWater
                
            "Clean" if pp.willpower > 1:
                f "Oh, you're going to clean? That's a great idea!"
                call cleanRoom

            "Open window" if pp.willpower > 0:
                f "..."
                call window
            
            "Scroll Reels" if pp.willpower > 1:
                f "... Are you sure? I mean, you could always-"
                p "I'm fine."

                call scrollReels

            "Nap":
                call nap
                $ napCount += 1
                # Condition after character naps away
                $ pp.maxW = pp.health - 1
                $ pp.setPhase(pp.health, pp.maxW, 0)
                play music "Backed Vibes (Clean).mp3"
                jump phase2
        
        label phase1End:
            if pp.willpower > 0:
                jump phase1
            else:
                hide screen status_ui
                scene black with fade

                p "I fell asleep..."
                scene bedroom
                f "Mornin' sleepyhead! You slept through the rest of the morning, hehe."
                f "It'd be a shame to stay in bed, so..."

                # Condition if character does not nap away
                $ pp.maxW = pp.health + 3
                $ pp.setPhase(pp.health, pp.maxW, 0)
                play music "I Knew a Guy.mp3"
                jump phase2


    label phase2:
        show screen status_ui

        

        menu:
            f neutral "What do you wanna do?"

            "Use the Restroom" if peed == False:
                $ peed = True
                f "Go piss, girl!"
                f "I'll... stay here. I won't peek, I promise!"
                scene bathroom
                call toilet
                
            "Take a Shower" if pp.willpower >= 2 and not showered:
                f "... Um."
                f "I'll just wait outside."
                scene bathroom
                call shower

            "Wash your hair in the sink" if pp.willpower > 1 and not showered:
                f "Great choice! Even if it's not good as washing your hair, it still makes you feel good!"
                call sink

            "Open the window" if pp.willpower > 1:
                f "..."
                scene bedroom
                call window
            
            "Go on Social Media" if pp.willpower > 1 and not trauma:
                f "Oh... well, I guess if you're not going for too long."
                call twitter
            

            "Nap":
                call nap
                $ napCount += 1
                $ pp.maxW = pp.health - 1 # if you nap the phase away
                $ pp.setPhase(pp.health, pp.maxW, 0)
                jump phase3

        label phase2End:
            if pp.willpower > 0:
                jump phase2
            else:
                scene bedroom
                f happy "Up up up! It's evening, and I think we should try and go to the kitchen!"

                $ pp.maxW = pp.health + 3 # If character doesn't nap the phase away
                if trauma:
                    $ pp.maxW = 3
                $ pp.setPhase(pp.health, pp.maxW, 0)
                jump phase3

    label phase3:
        

        if napCount == 2:
            scene bedroom 

            menu:
                # fairy sad
                f shy "Do... you want to do anything?" 
                "Nap":
                    call nap
                    $ napCount += 1
                    f "..."
                    jump end
            
        else: # NapCount is high enough
            show screen status_ui
            menu:
                f neutral "Choose whatever you wanna do!"

                "Cook" if pp.willpower > 7 and hungry:
                    scene kitchen
                    call cook
                    
                "Wash Dishes" if pp.willpower > 3:
                    scene kitchen
                    call dishes

                "Order Takeout" if pp.willpower > 2 and hungry:
                    scene kitchen
                    call takeout
                
                "Eat a snack" if pp.willpower > 2:
                    scene kitchen
                    call snack

                "Nap":
                    call nap
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
        f "You're starting to see the good in the little things!"
        f "The weight that you used to feel just cleaning your room is gone."
        f "You start working on the goals you’ve been putting off, and you always look forward to facing new challenges."

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
        f "... The end!"
        f "Life feels just that bit easier."
        f "You still struggle, just not as much." 
        f "Even if you'll have your ups and downs, but you are definitely on the right path!"
        f "You don’t know what challenges life will bring... but you look at them with less negativity."
        return
    # This ends the game.
    return
