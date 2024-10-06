init python:
    hours = 7
    minute = 55
    count = 0
    time_periods = ("AM", "PM")
    current_time = f"{(hours % 12)+1:02}:{minute:02} {time_periods[count % 2]}"

    def update_clock():
        global hours
        global minute
        global count
        global current_time

        current_time = f"{(hours % 12)+1:02}:{minute:02} {time_periods[count % 2]}"

        # Increment the time every minute or adjust this logic
        minute += 1
        if minute >= 60:
            minute = 0
            hours += 1
        if hours == 12 and minute == 0:
            count += 1

        renpy.restart_interaction()

    class MC:
        def __init__(self, character: Character, health: int, willpower: int, joy: int, maxW: int, maxJ: int):
            # Initialize character attributes
            self.c = character
            self.health = health
            self.willpower = willpower
            self.joy = joy
            self.maxW = maxW
            self.maxJ = maxJ

        def update(self, value_h: int = 0, value_e: int = 0, value_j: int = 0):

            self.health = max(0, min(20, self.health + value_h))
            self.willpower = max(0, min(self.maxW, self.willpower + value_e))
            self.joy = max(0, min(10, self.joy + value_j))
        
        def setPhase(self, health: int = 0, willpower: int = 0, joy: int = 0):
            self.health = health
            self.willpower = willpower
            self.joy = joy

screen clock():
    timer 2.00 action update_clock repeat True
    text "[current_time]"

screen status_ui:
    frame:
        align (0.95, 0.05)  # Position on the screen (right top corner)
        vbox:
            spacing 10  # Space between elements
            
            # Hygiene Bar
            # $ ratioH = pp.health / MC.maxH
            text "Health: [pp.health]":
                size 22
            bar value pp.health range 20:  # Progress bar for hygiene (0 to 100)
                xmaximum 300
            
            # Hunger Bar
            text "Willpower: [pp.willpower]":
                size 22  # Adjust the font size
            bar value pp.willpower range pp.maxW:  # Progress bar for hunger (0 to 100)
                xmaximum 300  # Width of the progress bar
            
            # Joy Bar
            text "Happiness: [pp.joy]":
                size 22
            bar value pp.joy range pp.maxJ:  # Progress bar for joy (0 to 100)
                xmaximum 300

default shirt1 = Drag(
                        d = im.Scale("shirtee.png", 100, 100), 
                        drag_name = "shirt", 
                        drag_raise = True, 
                        dragged = detective_dragged, 
                        align = (renpy.random.randint(1, 6) / 10, renpy.random.randint(1, 10) / 10)
                    )
default shirt2 = Drag(
                        d = im.Scale("shirtee.png", 100, 100), 
                        drag_name = "shirt", 
                        drag_raise = True, 
                        dragged = detective_dragged, 
                        align = (renpy.random.randint(1, 6) / 10, renpy.random.randint(1, 10) / 10)
                    )
default shirt3 = Drag(
                        d = im.Scale("shirtee.png", 100, 100), 
                        drag_name = "shirt", 
                        drag_raise = True, 
                        dragged = detective_dragged, 
                        align = (renpy.random.randint(1, 6) / 10, renpy.random.randint(1, 10) / 10)
                    )
default shirt4 = Drag(
                        d = im.Scale("shirtee.png", 100, 100), 
                        drag_name = "shirt", 
                        drag_raise = True, 
                        dragged = detective_dragged, 
                        align = (renpy.random.randint(1, 6) / 10, renpy.random.randint(1, 10) / 10)
                    )
default shirt5 = Drag(
                        d = im.Scale("shirtee.png", 100, 100), 
                        drag_name = "shirt", 
                        drag_raise = True, 
                        dragged = detective_dragged, 
                        align = (renpy.random.randint(1, 6) / 10, renpy.random.randint(1, 10) / 10)
                    )
default paper1 = Drag(
                        d = im.Scale("paper.png", 100, 100), 
                        drag_name = "paper", 
                        drag_raise = True, 
                        dragged = detective_dragged, 
                        align = (renpy.random.randint(1, 6) / 10, renpy.random.randint(1, 10) / 10)
                    )
default paper2 = Drag(
                        d = im.Scale("paper.png", 100, 100), 
                        drag_name = "paper", 
                        drag_raise = True, 
                        dragged = detective_dragged, 
                        align = (renpy.random.randint(1, 6) / 10, renpy.random.randint(1, 10) / 10)
)
default paper3 = Drag(
                        d = im.Scale("paper.png", 100, 100), 
                        drag_name = "paper", 
                        drag_raise = True, 
                        dragged = detective_dragged, 
                        align = (renpy.random.randint(1, 6) / 10, renpy.random.randint(1, 10) / 10)
)
default paper4 = Drag(
                        d = im.Scale("paper.png", 100, 100), 
                        drag_name = "paper", 
                        drag_raise = True, 
                        dragged = detective_dragged, 
                        align = (renpy.random.randint(1, 6) / 10, renpy.random.randint(1, 10) / 10)
)
default paper5 = Drag(
                        d = im.Scale("paper.png", 100, 100), 
                        drag_name = "paper", 
                        drag_raise = True, 
                        dragged = detective_dragged, 
                        align = (renpy.random.randint(1, 6) / 10, renpy.random.randint(1, 10) / 10)
)

default trash = Drag(
                        d = im.Scale("trashc.png", 125, 125), 
                        drag_name = "trash", 
                        draggable = False, 
                        drag_raise = True, 
                        align = (0.8, 0.8))
default basket = Drag(
                        d = im.Scale("basket.png", 125, 125), 
                        drag_name = "basket", 
                        draggable = False, 
                        drag_raise = True, 
                        align = (0.8, 0.3))

default groupedDrag = DragGroup(shirt1, shirt2, shirt3, shirt4, shirt5, paper1, paper2, paper3, paper4, paper5, trash, basket)
default n = 0

init python:

    def detective_dragged(drag, drop):
        global n

        if drop is not None:
            if drag[0].drag_name == "shirt":
                if (drop.drag_name == "basket"):
                    drag[0].snap(drop.x, drop.y)
                    groupedDrag.remove(drag[0])
                else:
                    n -= 1
            elif drag[0].drag_name == "paper":
                if (drop.drag_name == "trash"):
                    drag[0].snap(drop.x, drop.y)
                    groupedDrag.remove(drag[0])
                else:
                    n -= 1
            n += 1
            
        if (n == 10): return True

screen send_detective_screen:

    # A map as background.
    add im.Blur("bedroom.png", 10) xpos 0 ypos 0
    
    # Now add a smaller UI in the center with margin from the sides.
    frame:
        style "default"  # You can define a style for the white UI frame here.
        background "#696969"  # White background for the UI box.
        xysize (800, 600)  # Define the size of the white UI.
        align (0.5, 0.5)  # Center the frame in the screen.

        # Add the draggroup inside the white UI frame.
        
        add groupedDrag