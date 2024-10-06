# The script of the game goes in this file.


define f = Character("Fairy", image="fairy")
define p = Character("[name]")
define pp = MC(p, 2, 3, 0)

# Variables
default napCount = 0 
default peed = False

default phaseH = 15
default phaseW = 3
default phaseJ = 0



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bedroom

    # MEET DA FAIRY 

    

    f "Oh! I forgot to ask, what's your name?"


    python:
        # TODO: Extra dialogue if you put in a blank string
        name = renpy.input("Your name, please!:", length=32)
    f "Nice to meet you formally, [name]!"

    p "Whatever..."
    

    # Fairy goes into explaining how to play the game. Then we start the phase 1
    $ pp.setMaxPhase(phaseH, phaseW, phaseJ)
    $ pp.update(2, phaseW, phaseJ)
    scene bedroom
    jump phase1
    

    label phase1:
        show screen status_ui
        

        menu:
            f neutral "Alrighty, what do you want to do?"

            "Drink water" if pp.willpower > 1:
                f "Oh, you're thirsty aren't you?"
                f "Now... what is there to drink around here...?"
                call drinkWater
                
            "Clean" if pp.willpower > 2:
                f "Oh, you're going to clean? That's a great idea!"
                call cleanRoom

            "Open window" if pp.willpower > 1:
                f "..."
                call window
            
            "Scroll Reels" if pp.willpower > 1:
                f shy "... Are you sure? I mean, you could always-"
                p "I'm fine."

                call scrollReels

            "Nap":
                call nap
                $ napCount += 1
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

                
                $ pp.setMaxPhase(phaseH, phaseH + pp.health, phaseJ)
                $ pp.update(pp.health, pp.maxE, phaseJ)
                jump phase2


    label phase2:
        show screen status_ui

        menu:
            f "What do you wanna do?"

            "Use the Restroom" if peed == False:
                $ peed = True
                f "Go piss, girl!"
                f "I'll... stay here. I won't peek, I promise!"
                scene bathroom
                call toilet
                
            "Take a Shower" if pp.willpower >= 2:
                scene bathroom
                call shower

            "Wash your hair in the sink" if pp.willpower > 1:
                f "Great choice! Even if it's not good as washing your hair, it still makes you feel good!"
                call sink

            "Open the window" if pp.willpower > 1:
                scene bedroom
                call window
            
            "Go on Social Media" if pp.willpower > 1:
                jump phase2End

            "Nap":
                call nap
                $ napCount += 1
                jump phase3

        label phase2End:
            if pp.willpower > 0:
                jump phase2
            else:
                scene bedroom
                f "Up up up! It's evening, and I think we should try and go to the kitchen."
                jump phase3

    label phase3:
        $ hungry = Talse

        if napCount == 2:
            scene bedroom 

            menu:
                # fairy sad
                f "Do... you want to do anything?" 
                "Nap":
                    call nap
                    $ napCount += 1
                    f "..."
                    jump end
            
        else: # NapCount is high enough
            menu:
                f "Choose whatever you wanna do!"

                "Cook" if pp.willpower > 4 and hungry:
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
                    jump end

        label phase3End:
            if pp.willpower > 0:
                jump phase3
            else:
                jump end


    
    label end:
        if(napCount == 3):
            jump badEnd
        elif(pp.joy > 5):
            jump goodEnd
        else:
            jump midEnd
        
    
    label goodEnd:
        f "You're starting to see the good in the little things!"
        f "The weight that you used to feel just cleaning your room is gone."
        f "You start working on the goals you’ve been putting off, and you always look forward to facing new challenges."

        f "Ah... I'm so proud of you, [name]!"
        f "I just know you'll find yourself in a better place, soon. Take care!"
        return
    label badEnd:
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
