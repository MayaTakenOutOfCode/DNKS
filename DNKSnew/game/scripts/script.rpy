define yandere = Character("Yua")
define dandere = Character("Yui")
define normalG = Character("Ichika")
define normalB = Character("Shisuno")
#image room = "/images/room.jpg"
#image nb = "images/normalboy.png"


label splashscreen:
    #play music "audio/splashscreen.wav"   

    scene black
    with Pause(1)

    show text "Silly Cat Media Presents..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    show text "Dekinai Nogareru Kore Seikatsu (出来ない逃れるこれ生活)" with dissolve
    with Pause(3)

    stop music fadeout 2.0

    hide text with dissolve
    with Pause(1)

    return


label start:
    scene black

    play music "audio/ost-normal.ogg"

    normalB"I am so happy that tomorrow will be my school year beggining"

    scene black with fade
    show text "...at the morning..." with dissolve
    with Pause(2)

    scene room with fade

    show nb

    normalBoy"It is finally  tomorrow! I am so ready to go to new school!"
    

    return


label quit:
    stop music
    scene black
    with Pause(1)

    show text "Thanks for playing!" with pixellate
    with Pause(3)

    return
    
    