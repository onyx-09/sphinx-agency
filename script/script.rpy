define config.mouse = {"default":[ ("gui/mouse.png", 1, 1) ] }


label splashscreen:
scene splashscreen

"This game contains themes of violence, abuse, and psychological distress and heavy topics."
"that can be found in our website:"
"Player discretion is advised."
"if you relate to a character and feel like you are going through the same"
"please seek help and not let youreself suffer"
"do you wish to continue?"
menu:
 "yes":
  "press anywhere to start"
 "no":
  "if you don't feel comfrtable with the said topics please delete the game."

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