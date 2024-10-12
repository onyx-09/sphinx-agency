define config.mouse = {"default":[ ("gui/mouse.png", 1, 1) ] }

label splashscreen:
scene splashscreen

"warning, this game has loads of mature and disturbing things"
"thus it is not for kids or those that are easily disturbed,"
"do you still wish to continue?"
menu:
 "yes":
  "press anywhere to start"

return

label start:
# character

default player_name = "Ash"
define pov = Character("[player_name]")

#bg images
image mc blank = "images/blank.png"

#player name input begins

label playername:
 
    $ player_name = renpy.input("What is your name?", default='Ash', exclude='\\/`{}\'"[]()', length=18)
    $ player_name = player_name.strip()

    if not player_name:
        $ player_name="Ash"


#player input name ends

scene mc blank  # type: ignore


#player input name ends


jump chapter01