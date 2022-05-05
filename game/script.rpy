define player = Character("[povname]")
define DJ = Character("DJ")

init python:
    config.screen_width = 1280
    config.screen_height = 720

label start:

    $ turns = 0
    $ grades = 0
    $ depress = 0
    $ health = 100
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

    return

label driver:

    if turns >= 9:
        jump end

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

    return

label study:

    scene bg grainger with dissolve

    $ grades += 20

    $ depress += 10

    $ health -= 20

    player "역시 학생의 기본은 공부지!"

    player "어디 보자... CS MP에... 랩 리포트에..."

    "한 달 동안 열심히 공부했다." with dissolve

    hide text with dissolve
    with Pause(1)

    player "휴... 이번 달 엄청 열심히 했다."

    $ turns += 1

    jump driver

label party:

    $ grades -= 5

    $ health -= 15

    image club = "bg club.jpg"
    scene club with dissolve

    play music "audio/club.mp3" fadein 1.0 fadeout 1.0

    player "4학년 이대로 보내긴 아쉬우니까 미친듯이 즐겨야해!"

    DJ "크게 소리질러 ~ !"

    player "(분위기에 취해 함성을 지른다)"
    hide text with dissolve
    with Pause(1)

    player "벌써 데킬라 7잔 째인데 ... 딱 한 잔만 더 마시자."

    "한 달 동안 열심히 클럽을 갔다." with dissolve
    hide text with dissolve
    with Pause(1)

    player "이번 달은 너무 과음을 했나..."

    stop music

    play music "audio/main.mp3" fadein 1.0 fadeout 1.0

    $ turns += 1

    jump driver

label games:

    play music "audio/league.mp3"  fadein 1.0 fadeout 1.0

    scene bg rift with dissolve

    $ grades -= 5

    $ gamer += 10 * tier

    $ health -= 10

    $ depress += 5

    "소환사의 협곡에 오신 것을 환영합니다."

    player "아 롤은 못 참지 ㅋㅋ"

    "한 달 동안 미친듯이 게임만 했다..."

    player "아니 우리 정글 뭐하는데"

    play music "audio/main.mp3" fadein 1.0 fadeout 1.0

    $ turns += 1

    jump driver

label dates:

    scene bg date with dissolve

    play music "audio/date.mp3" fadein 1.0 fadeout 1.0

    $ grades -= 5

    $ health -= 1

    $ depress -= 10

    if koibito:
        "데이트를 한다."

        player "이번 달은 여자친구와 함께 한 달을 보내야겠어."
    elif not koibito:
        "애인을 찾아나선다."

        player "소개팅 없나... 친구에게 물어보자."

    play music "audio/main.mp3" fadein 1.0 fadeout 1.0

    $ turns += 1

    jump driver


label sports:
    play music "audio/sport.mp3" fadein 1.0 fadeout 1.0

    $ grades -= 5

    $ athlete += 20

    $ depress -= 5

    image arc = "bg arc.jpg"
    scene arc with dissolve

    player "체력 단련을 위해 ARC에서 운동을 하자!"

    player "벤치 프레스 10회 ... 푸쉬업 15회 ... 스쿼트 20회 ..."

    "근력이 붙은 기분이야." with dissolve

    hide text with dissolve

    player "이번달은 운동을 열심히 했는 걸."

    play music "audio/main.mp3" fadein 1.0 fadeout 1.0

    $ turns += 1

    jump driver

label end:
    if depress > 80:
        jump depression
    elif depress < 50 and health > 50 and grades > 170:
        jump success
    elif gamer > 130:
        jump progamer
    elif athlete > 180:
        jump bodybuilder
    elif grades < 20:
        jump anotheryear
    else:
        jump normal

    return

label normal:
    scene bg graduate with dissolve

    play music "audio/main.mp3" fadein 1.0 fadeout 1.0

    player "큰 문제 없이 졸업할 수 있게 되었다."

    player "무난한 해를 보냈던 것 같다."

    "무사히 졸업에 성공했습니다."

    return

label depression:

    scene bg depress with dissolve

    play music "audio/depression.mp3" fadein 1.0 fadeout 1.0

    player "너무 우울했던 마지막 해였다."

    player "내 정신건강에 너무 신경 쓰지 않았다."

    player "이대로 가면 우울해서 미쳐버릴 것 같아..."

    "우울증에 빠져 회복 불가능하게 되었습니다..."

    return

label success:

    scene bg success with dissolve

    play music "audio/success.mp3" fadein 1.0 fadeout 1.0

    player "공부.. 건강.. 뭐 하나 빠지는 것 없는 완벽한 해를 보냈다."

    player "열심히 한 덕분에 대기업에 취직하게 되었다."

    player "앞으로 행복한 일 밖에 남지 않았어..!"

    "대기업에 취직하였습니다."

    return

label programer:

    scene bg progamer with dissolve

    play music "audio/progamer.mp3" fadein 1.0 fadeout 1.0

    player "게임을 열심히 했더니 프로게이머가 되었다."

    player "북미섭 챌을 찍으니 프로 팀에게 제의가 왔고..."

    player "LCS 프로게이머가 되었다!"

    "프로게이머가 되었습니다."

    return

label bodybuilder:

    scene bg bodybuilder with dissolve

    play music "audio/success.mp3" fadein 1.0 fadeout 1.0

    player "운동을 열심히 했더니 근육이 엄청나게 많이 붙었다."

    player "이 정도면 보디빌더가 되어도 괜찮겠는걸..?"

    "보디빌더가 되었습니다."

    return

label anotheryear:

    scene bg grainger with dissolve

    play music "audio/depression.mp3" fadein 1.0 fadeout 1.0

    player "너무 공부에 집중하지 않았다..."

    player "이 정도 성적이면 졸업할 수 없게 되버려..."

    player "하... 한 학기 더 해야겠다..."

    "졸업 유예가 되었습니다."

    return
