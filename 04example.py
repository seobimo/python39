#


#1
#프로그래밍 언어 실습시 글꼴은
#고정폭 글꼴을 사용할 것을 추천
print('*   *    **    ****    ****    *   *           /////               ')
print('*   *   *  *   *   *   *   *   *   *          | o o |              ')
print('*****  *    *  ****    ****     * *          (|  ^  |)             ')
print('*   *  ******  *   *   *   *     *            | [_] |              ')
print('*   *  *    *  *    *  *    *    *             _____               ')


print('            +---+                                                  ')
print('            |   |                                                  ')
print('        +---+---+                                                  ')
print('        |   |   |                                                  ')
print('    +---+---+---+           /\\ __/\\         -----                ')
print('    |   |   |   |          (   ; ;   )     /  Hello  \             ')
print('+---+---+---+---+          (    -    )    <   Junior  |            ')
print('|   |   |   |   |           |   |   |      \  Coder!  /            ')
print('+---+---+---+---+          (    |    )        -----                ')


#3
rate1 = 1
#1stPlayer = 2       #변수명이 숫자로 시작
#myprogam.java = 3   #.때문에 불가
long = 4
timeLimit = 5
numberOfWindow = 6


#4
x, y, z = 1, 2, 3
s0, v0, t, g = 4, 5, 6, 9.8
print(3 * x, 3 * x + y, x + y / 7)
print(s0 + v0*t + (1/2) * g * t**2)


#6
x = 2.5
y = 1.5
m = 18
n = 4
print(x + n * y - (x + n) * y)
print(m / n + m%n)
print(5 * x - n / 5)
print(1  -(1 - (1 -( - 1( - (1 - n)))))


#7
#숫자 연산자들은 bool 함수를 써야함
print(3 + 4.5 * 2 + 27 / 8)
print(True or False and 3 < 4 or not(5 == 7))
print(True or (3 < 5 and 6 >= 2))
print  ( not True > 'A')  #'A' => bool('A')  #not (True > True)
print(7 % 4 + 3 - 2 / 6 * 'Z') #'Z' => bool('Z')
print('D' + 1 + 'M' % 2 / 3)  #'D','M' => bool('D') bool('M')
print(5.0 / 3 + 3 / 3 )
print(53 % 21 < 45 / 18)
print((4 < 6) or True and False or False and (2 > 3))
print(7 - (3 + 8 * 6 + 3) - (2 + 5 * 2))

#9

#단축식 평가란 표현식을 평가하는 도중에 평가 결과가 확정된 경우,
#나머지 평가 과정을 생략하는 것이다.
#ex) true || Box = TRUE, false || Box = Box
#true && Box = BOX, false && Box = FALSE

print(True and False and True or True) # =print(False)
print(True or True and True and False) # =print(True)
print( (true and false) or (true and not false) or (false and not false)) # =print(False)
print((2 < 3) or (5 > 2) and not(4 == 4) or 9 != 4 ))
#print(true || true && true || true) # = print(True)
print(6 == 9 or 5 < 6 and 8 < 4 or 4 > 3)
#print(false || true && false || true) # = print(False)




#10
#논리식과 산술식(값)이 결합된 수식에서는
#논리식의 결과가 true면 값이 출력  ex) true & (3 < 4) = true
#논리식의 결과가 false면 false가 출력
print(27 / 13 + 4)
print(27 / 13 + 4.0)
print(42.7 % 3 + 18)
print((3 < 4) and 5 / 8)
print(23 / 5 + 23 / 5.0)
print(2.0 + 'a')    #문자와 정수/실수 간 산술 연산 불가
print(2 + 'a')
print('a' + 'b')
print('a' / 'b')
print('a' and not 'b')
print(( double ) 'a' / 'b') #double(float) => x : 문자간 산술연사 불가

#11
name = 'serif'
age = 33
weight = 65.9
print(name, age, weight)


#12
# K나이 - 세는나이(출생시 1살, 해가 바뀌면 + 1)
#        만나이(출생시 0살, 생일이 지나면 + 1)
#        연나이(현재연도 - 출생연도)
birthYear = 1990
currentYear = 2022
isPassBirth = True
age = currentYear - birthYear
print('연나이', age)
print('세는나이'+ age + 1)

#파이선의 if 단축식 : 참일때의 값 if 조건식 else 거짓일때 값
print('만나이', (age + 1) if isPassBirth else age) #조건식이 참이 아닐경우 리턴한다.


#13
# %서식
print('7 x 1 = %d' %(7 * 1))
print('7 x 2 = %d' %(7 * 2))
print('7 x 3 = %d' %(7 * 3))
print('7 x 4 = %d' %(7 * 4))
print('7 x 5 = %d' %(7 * 5))
print('7 x 6 = %d' %(7 * 6))
print('7 x 7 = %d' %(7 * 7))
print('7 x 8 = %d' %(7 * 8))
print('7 x 9 = %d' %(7 * 9))

#.format 서식

print('7 x 1 = {%d}' .format(7 * 1))
print('7 x 2 = {%d}' .format(7 * 2))
print('7 x 3 = {%d}' .format(7 * 3))
print('7 x 4 = {%d}' .format(7 * 4))
print('7 x 5 = {%d}' .format(7 * 5))
print('7 x 6 = {%d}' .format(7 * 6))
print('7 x 7 = {%d}' .format(7 * 7))
print('7 x 8 = {%d}' .format(7 * 8))
print('7 x 9 = {%d}' .format(7 * 9))

#f-string 서식

print('7 x 1 = {7*1:2d}')
print('7 x 2 = {7*2:2d}')
print('7 x 3 = {7*3:2d}')
print('7 x 4 = {7*4:2d}')
print('7 x 5 = {7*5:2d}')
print('7 x 6 = {7*6:2d}')
print('7 x 7 = {7*7:2d}')
print('7 x 8 = {7*8:2d}')
print('7 x 9 = {7*9:2d}')

#14

day = 86400
hour = 3600
min = 60

# %서식
print('하루 : %d ' % day)
print({1234567890 / day} )
print('한 시간 : ' % hour)
#.format

# f-string