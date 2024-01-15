define teacher = Character("Teacher")

label dayFirst:
    init python:
        import os

        try:
            mkmod("message1.crtxt")
        
        file = open('message1.crtxt')
        file.write('When sun shines and rain pours \nyou will be our without hesitation.')

        
    normalB "(thoughts..) Okay, I am kind of scared of the school, but I need to make some friends"

    teacher "Welcome all first years! This will be your school for the next 3 years, hope we will get on well with each other!\nPlease pick your clubs by next week!"

    return