chosung = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
joongsung = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ'] 
jongsung = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
chosung_stroke_number = [1, 2, 1, 2, 4, 3, 3, 4, 8, 2, 4, 1, 2, 4, 3, 2, 3, 4, 3]
joongsung_stroke_number = [2, 3, 3, 4, 2, 3, 3, 4, 2, 4, 5, 3, 3, 2, 4, 5, 3, 3, 1, 2, 1]
jongsung_stroke_number = [0, 1, 2, 3, 1, 3, 4, 2, 3, 4, 6, 7, 5, 6, 7, 6, 3, 4, 6, 2, 4, 1, 2, 3, 2, 3, 4, 3]

chosung_stroke = {letter : chosung_stroke_number[chosung.index(letter)] for letter in chosung}
joongsung_stroke = {letter : joongsung_stroke_number[joongsung.index(letter)] for letter in joongsung}
jongsung_stroke = {letter : jongsung_stroke_number[jongsung.index(letter)] for letter in jongsung}

'''for letter in chosung:
    chosung_stroke[letter] = chosung_stroke_number[chosung.index(letter)]
for letter in joongsung:
    joongsung_stroke[letter] = joongsung_stroke_number[joongsung.index(letter)]
for letter in jongsung:
    jongsung_stroke[letter] = jongsung_stroke_number[jongsung.index(letter)]
'''

name = '윤종석'
ordData = []
base = 44032
for letter in name:
    ordData.append(ord(letter)) #가 = 44032, 힣 = 55203 초성 하나에 588개 각 초성에 모음 28개 종성

choindex = [(ordnum - base) // 588 for ordnum in ordData]
joongindex = [((ordnum - base) % 588) // 28 for ordnum in ordData]
jongindex = [((ordnum - base % 588) % 28) for ordnum in ordData]

#choindex = (ordData[1] - base) // 588
#joongindex = ((ordData[1] - base) % 588) // 28 
#jongindex = ((ordData[1] - base % 588) % 28) 

print(chosung[choindex[0]])
print(joongsung[joongindex[0]])
print(jongsung[jongindex[0]])