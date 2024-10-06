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

