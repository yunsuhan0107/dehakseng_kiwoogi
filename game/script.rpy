# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define player = Character("[povname]")

# The game starts here.

label start:

    python:
        povname = renpy.input("What is your name?", length=32)
        povname = povname.strip()

    scene bg quad

    player "내 이름은 [povname]. 이번이 나의 대학 생활 마지막 해다."

    player "3년간 열심히 살아왔지... 이번 년도는 열심히 해서 유종의 미를 거둘거야."

    player "어떻게 살아야 될까... 곰곰히 생각해보자."

    call driver

    return

label driver:

    "이번 달은 무엇에 집중하며 보낼까?"

    menu:
        "공부":
            jump study
        "파티":
            jump party
        "게임":
            jump games
        "연애":
            jump dates
        "운동":
            jump sports

label study:
    player "공부를 한다."

    return

label party:
    player "술을 마신다."

    return

label games:
    player "게임을 한다."

    return

label dates:
    player "연애를 한다."

    return

label sports:
    player "운동을 한다."

    return
