# home scripts

define yandere = Character("Yua")
define dandere = Character("Yui")
define normalG = Character("Ichika")
define normalB = Character("Shisuno")
image roomN = "roomNight.png"
image nb = "normalboy.png"


label splashscreen:
    #play music "audio/spalshscreen.wav"   

    scene black
    with Pause(1)

    show text "Vivid Media Presents..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    show text "Dekinai Nogareru Kore Seikatsu (出来ない逃れるこれ生活)" with dissolve
    with Pause(3)
    hide text with dissolve
    with Pause(1)
    show text "Epilepsy WARNING: Flashing Colours!" with dissolve
    with Pause(2)

    stop music fadeout 2.0

    hide text with dissolve
    with Pause(1)

    return


label start:


    scene black with blinds
    play music "audio/ost-normal.ogg"
    normalB"I am so happy that tomorrow will be my school year beggining"
    scene black with fade
    show text "...in the morning..." with dissolve
    with Pause(2)
    scene roomN with fade
    show nb
    normalB "It is finally today! I am so ready to go to a new school! I am so happy!"
    hide nb
    scene black with dissolve
    show text "Chapter 1 - Begining!" with dissolve
    with Pause(3)
    jump dayFirst

    return


label quit:
    stop music
    scene black
    with Pause(1)

    show text "Thanks for playing!" with pixellate
    with Pause(3)

    return
    
    