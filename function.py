stroke_list1 = [7, 6, 5, 6, 6, 6] #획수 알아내기
stroke_list2 = [6, 7, 6, 5, 6, 6] #획수 알아내기
def nextline(line):
    nextline = []
    for i in range(len(line) - 1):
        rawdata = str(line[i] + line[i+1])
        if len(rawdata) == 2:
            nextline.append(int(rawdata[1]))
        else:
            nextline.append(int(rawdata))
    return nextline


def stroke_to_result(strokelist):
    resultlist = strokelist
    for i in range(4):
        resultlist = nextline(resultlist)
    result = ""
    if resultlist[0] == 0:
        result = str(resultlist[1])
    else:
        result = str(resultlist[0]) + str(resultlist[1])
    return result

print(stroke_to_result(stroke_list1))

def printStroke(strokelist):
    space = ""
    while len(strokelist) > 1:
        print(space, end="")
        for number in strokelist:
            print(str(number), end=" ")
        print('\n')
        strokelist = nextline(strokelist)
        space = space + " "

printStroke(stroke_list1)
hangul_list = [chr(i) for i in range(ord('가'), ord('힣')+1)]
def isHangul(name1, name2):
    hangul_checker = "hangul"
    for name in (name1, name2):
        if name의 글자가 모두 한글:
            pass
        else:
           hangul_checker = ""
    return hangul_checker
