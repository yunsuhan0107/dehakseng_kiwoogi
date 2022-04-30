define player = Character("[povname]")

init python:
    config.screen_width = 1280
    config.screen_height = 720

label start:

    $ turns = 0
    $ grades = 0
    $ depress = 0
    $ health = 0
    $ athlete = 0
    $ gamer = 0
    $ koibito = True
    $ tier = 0

    play music "audio/start.mp3" fadein 1.0 fadeout 1.0

    python:
        povname = renpy.input("이름을 적어주세요.", length=32)
        povname = povname.strip()

    "현재 애인이 있으신가요?"
    menu:
        "예":
            $ koibito = True
        "아니오":
            $ koibito = False

    "리그 오브 레전드를 하신다면 현재 티어를 골라주세요."

    menu:
        "아이언":
            $ tier = -1
        "브론즈":
            $ tier = 0
        "실버":
            $ tier = 0.5
        "골드":
            $ tier = 1
        "플래티넘":
            $ tier = 2
        "다이아몬드":
            $ tier = 3
        "마스터":
            $ tier = 4
        "그랜드마스터":
            $ tier = 5
        "챌린저":
            $ tier = 10

    show text "당신을 분석 중입니다... 잠시만 기다려주세요." with dissolve
    with Pause(4)

    hide text with dissolve
    with Pause(1)

    stop music

    scene bg quad

    play music "audio/main.mp3" fadein 1.0 fadeout 1.0

    player "내 이름은 [povname]. 이번이 나의 대학 생활 마지막 해다."

    player "3년간 열심히 살아왔지... 이번 년도는 열심히 해서 유종의 미를 거둘거야."

    player "어떻게 살아야 될까... 곰곰히 생각해보자."

    call driver

label driver:

    scene bg quad with dissolve

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

    scene bg grainger with dissolve

    $ grades += 20

    player "역시 학생의 기본은 공부지!"

    player "어디 보자... CS MP에... 랩 리포트에..."

    "한 달 동안 열심히 공부했다." with dissolve

    hide text with dissolve
    with Pause(1)

    player "휴... 이번 달 엄청 열심히 했다."

    $ turns += 1

    if turns > 9:
        jump end
    else:
        jump driver

label party:

    $ grades -= 5

    player "술을 마신다."

    $ turns += 1

    if turns > 9:
        jump end
    else:
        jump driver

label games:

    $ grades -= 5

    player "게임을 한다."

    if turns > 9:
        jump end
    else:
        jump driver

label dates:

    $ grades -= 5

    if koibito:
        player "데이트를 한다."
    elif not koibito:
        player "애인을 찾아나선다."

    if turns > 9:
        jump end
    else:
        jump driver

label sports:
    $ grades -= 5

    player "운동을 한다."

    if turns > 9:
        jump end
    else:
        jump driver
