define asha   = Character("Asha", color="#FFD700")
define rayen  = Character("Elder Rayen", color="#ADD8E6")
define xarvox = Character("Xarvox", color="#FF3333")

define slowdissolve = Dissolve(2.0)
define flash        = Fade(0.1, 0.1, 0.1, color="#FFFFFF")

transform fullscreen:
    fit "cover"
    xalign 0.5
    yalign 0.5

default courage = 0            

label start:

    play music "theme.mp3" fadein 1.0
    scene black
    with fade

    "In a quiet village surrounded by mountains and starlit skies…"

    scene bg village-day at fullscreen
    show asha_happy at left
    with dissolve

    asha "The sky feels different today. Like something is coming."

    "A streak of light blazes overhead. A meteor slams into the forest!"

    play sound "explosion.mp3"
    asha "What was that?! I need to see."

    hide asha_happy
    scene bg forest-night at fullscreen
    with fade

    "You find the meteor glowing with strange energy."

    "As you touch it—"
    scene white with dissolve
    "Energy surges through your body." with slowdissolve

    scene bg forest-night at fullscreen
    show rayen_neutral at left

    rayen "Child of the stars… you have been chosen."

    show asha_happy at center
    asha "Wh-who are you?"

    rayen "Rayen, last guardian of the Lightstorm. Darkness stirs; only you can hold it back."

    menu:
        "Accept your destiny":
            $ courage += 1
            jump accept_power
        "Refuse":
            jump deny_power

label deny_power:

    asha "I… I’m just a girl. I can’t do this."
    rayen "If you turn away, all you love will burn."

    "You glimpse visions of ruin: the village engulfed in flames."
    $ courage -= 1
    jump accept_power

label accept_power:

    stop music fadeout 1.5
    play music "shrine.mp3"
    scene bg shrine at fullscreen
    with fade

    rayen "Feel the light in your veins. Guide it."

    show asha_training1 at center with flash
    "You learn to bend wind."
    hide asha_training1

    show asha_training2 at center with flash
    "You leap across mountains."
    hide asha_training2

    rayen "The trial comes tonight."

    stop music fadeout 1.5
    play music "battle.mp3" fadein 0.5

    scene bg village-burn at fullscreen
    with fade

    "The village is ablaze. Screams echo."

    rayen "Xarvox is here. Show him the light!"

    jump mid_battle

label mid_battle:

    show xarvox_evil at right
    show asha_battle at left
    with flash

    xarvox "So this is the planet’s new spark? Pathetic."
    asha  "Leave them alone!"

    menu:
        "Blast him with light":
            $ courage += 1
            "Your beam scorches his armor."
        "Shield the villagers first":
            "You raise a barrier of wind, saving lives."
            $ courage += 2

    xarvox "Amusing. Meet me where stars fall, girl. If you dare."
    hide xarvox_evil
    hide asha_battle
    "He vanishes in crackling darkness."

    jump showdown

label showdown:

    scene bg battlefield at fullscreen
    with fade

    rayen "This wasteland is a conduit of power. Win here, or night consumes all."

    show xarvox_evil at right with flash
    show asha_battle at left

    xarvox "One last spark before oblivion!"

    menu:
        "Charge head-on":
            "Light erupts from your fists. You clash mid-air."
            $ courage += 1
        "Outsmart him":
            "You bend wind, circle behind, strike his power core."
            $ courage += 2

    if courage >= 3:
        jump good_ending
    else:
        jump sacrifice_ending

label good_ending:

    play music "ending.mp3" fadein 1.0
    xarvox "No… impossible!"
    "He disintegrates in a burst of light."

    scene bg village-day at fullscreen
    show asha_training2 at center
    with slowdissolve
    "Dawn rises over a peaceful village."
    asha "I’ll guard this world — always."

    return

label sacrifice_ending:

    play music "ending.mp3" fadein 1.0
    xarvox "You cannot win!"
    asha "Maybe not… but I can end you."

    "You release all remaining power in a blinding flash."
    scene white with flash
    "Xarvox is gone. So is your light."

    scene bg village-day at fullscreen
    show asha_happy at center
    show rayen_neutral at right
    with slowdissolve
    rayen "You saved us at great cost, Asha."
    asha "A guardian needs no powers — only courage."

    return
