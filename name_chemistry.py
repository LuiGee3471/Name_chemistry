from time import sleep

#database
chosung = [
    'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ',
    'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
    ]
joongsung = [
    'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ',
    'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ'
    ] 
jongsung = [
    ' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ',
    'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ',
    'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
    ]
chosung_stroke_number = [
    1, 2, 1, 2, 4, 3, 3, 4, 8, 2,
    4, 1, 2, 4, 3, 2, 3, 4, 3
    ]
joongsung_stroke_number = [
    2, 3, 3, 4, 2, 3, 3, 4, 2, 4,
    5, 3, 3, 2, 4, 5, 3, 3, 1, 2, 1
    ]
jongsung_stroke_number = [
    0, 1, 2, 3, 1, 3, 4, 2, 3, 4, 6, 
    7, 5, 6, 7, 6, 3, 4, 6, 2, 4, 1, 2, 3, 2, 3, 4, 3
    ]
chosung_stroke = {
    letter : chosung_stroke_number[chosung.index(letter)] 
    for letter in chosung
    }
joongsung_stroke = {
    letter : joongsung_stroke_number[joongsung.index(letter)]
    for letter in joongsung
    }
jongsung_stroke = {
    letter : jongsung_stroke_number[jongsung.index(letter)]
    for letter in jongsung
    }
hangul_list = [chr(i) for i in range(ord('가'), ord('힣')+1)]

#functions
def isHangul(name1, name2):
    hangul_checker = "hangul"
    for name in (name1, name2):
        if set([letter for letter in name]).issubset(hangul_list):
            pass
        else:
           hangul_checker = ""
           break
    return hangul_checker
    
def inputName():
    while True:
        name1 = input("첫 번째 이름을 입력하세요: ")
        name2 = input("두 번째 이름을 입력하세요: ")
        hangul_checker = isHangul(name1, name2)
        if hangul_checker == "hangul":
            pass
        else:
            print("한글 이름만 가능합니다. 이름을 다시 입력해주세요.\n")
            continue
        if len(name1) != 3 or len(name2) != 3:
            print("\n이름을 3글자로 입력해주세요.\n")
            continue
        valid = None
        while valid not in ("예", "네", "아니오"):
            valid = input(
                "\n입력하신 이름이 " 
                + name1 
                + ", " 
                + name2 
                + " 맞습니까? (예 / 아니오) "
                )
            if valid == "아니오":
                print("\n이름을 다시 입력해주세요.\n")
            elif valid == "예" or valid == "네":
                print("")
                return(name1, name2)
            else:
                print("\n예, 아니오로 대답해주세요.")

def letter_list(namelist):
    letter_list = []
    for i in range(3):
        letter_list.append(namelist[0][i])
        letter_list.append(namelist[1][i])
    return letter_list

def strokenumber(letterlist):
    base = 44032 #'가'의 유니코드값
    ordData = [ord(letter) for letter in letterlist]
    choindex = [(ordnum - base) // 588 for ordnum in ordData]
    joongindex = [((ordnum - base) % 588) // 28 for ordnum in ordData]
    jongindex = [((ordnum - base % 588) % 28) for ordnum in ordData]
    cholist = [chosung_stroke[chosung[index]] for index in choindex]
    joonglist = [joongsung_stroke[joongsung[index]] for index in joongindex]
    jonglist = [jongsung_stroke[jongsung[index]] for index in jongindex]
    stroke_list = [
        cholist[i] + joonglist[i] + jonglist[i]
        for i in range(len(letterlist))
        ]
    return stroke_list
    
def nextline(line):
    nextline = [
        int(str(line[i] + line[i+1])[1]) if len(str(line[i] + line[i+1])) == 2
         else int(str(line[i] + line[i+1])) for i in range(len(line) - 1)
        ]
    return nextline
    
def printStroke(strokelist):
    space = ""
    while len(strokelist) > 1:
        print(space, end="")
        for number in strokelist:
            print(str(number), end=" ")
        sleep(0.5)
        print('\n')
        strokelist = nextline(strokelist)
        space = space + " "

def stroke_to_result(strokelist):
    resultlist = strokelist
    for i in range(4):
        resultlist = nextline(resultlist)
    return str(resultlist[1]) if resultlist[0] == 0 \
                              else str(resultlist[0]) + str(resultlist[1])

def retry():
    retry = None
    while retry not in ("예", "네", "아니오"):
            retry = input("\n다시 하시겠어요? (예 / 아니오) ")
            if retry == "아니오":
                quit()
            elif retry == "예" or retry == "네":
                name_chemistry()
            else:
                print("\n예, 아니오로 대답해주세요.")

def name_chemistry():
    print("이름 궁합 프로그램입니다. 두 분의 이름을  입력해주세요.\n")
    
    name = inputName()
    
    print(name[0] + "님과 " + name[1] + "님의 이름 궁합을 확인합니다.\n")
    
    letter_list1 = letter_list(name)
    rname = tuple(reversed(name))
    letter_list2 = letter_list(rname)
    
    stroke_list1 = strokenumber(letter_list1)
    stroke_list2 = strokenumber(letter_list2)
    
    print("결과 계산 중...\n")
    sleep(3)
    
    printStroke(stroke_list1)
    result1 = stroke_to_result(stroke_list1)
    
    print("여러분의 1번째 이름 궁합은 " + result1 + "%입니다.")
    print("그리고...\n")
    sleep(1.5)
    
    printStroke(stroke_list2)
    result2 = stroke_to_result(stroke_list2)
    
    print("여러분의 2번째 이름 궁합은 " + result2 + "%입니다.")
    retry()

name_chemistry()