# p78) 숫자 맞추기(1~10)
import random as ran
print('>>숫자 맞추기 게임<<')
com = ran.randint(1, 10) # 1~10 사이 난수 정수 발생

while True :
    my = int(input('예상 숫자를 입력하시오:'))
    if my == com :
        print('축하합니다. 정답입니다.')
        break
    elif com > my :
        print('입력한 수가 더 큽니다.')
    elif com < my :
        print('입력한 수가 더 작습니다')
    else:
        print('다시 도전해 주세요')


# ex30) 숫자 맞추기 (1~100)
#가. 사용자로부터 1 - 100사이의 숫자를 입력 받으세요 (num1)
#나. 변수에 임의의 숫자 3자리를 초기화합니다 (num2)
#다.  num1이 num2보다 크면 “추측한 숫자가 큽니다”라고 출력하세요
#라.  num1이 num2보다 작으면 “추측한 숫자가 작습니다”라고 출력하세요
#마.  num1과 num2가 같으면 “빙고! 숫자를 맞췄습니다”라고 출력하고 종료
import random
num1 = input('1부터 100사이의 숫자를 입력해 주세요')
num2 = random.randint(1, 100)

while True :
    if num1 == num2 :
        print('빙고! 숫자를 맞췄습니다')
        break
    elif num1 > num2 :
        print('추측한 숫자가 큽니다')
    elif num1 < num2 :
        print('추측한 숫자가 작습니다')
else :
    print('다시 입력해 주세요')


# ex25) 복권 당첨 프로그램 - 3자리수 입력/사용자 입력
#난수 범위 - 100 ~ 999 (위치 여부는 상관없이 일치 여부 판단)
#ex) 123 => 123(1), 231(2), 312(3)
#문자열 슬라이싱을 위한 문자열 변환 str 함수 사용
#3개 일치 - 상금 백만원
#2개 일치 - 상금 5만원
#1개 일치 - 상금 1천원
#0개 일치 - 다음 기회에
import random as rnd
#uesrkey = input('숫자 3자리수를 입력해주세요')
#lottokey = rnd.randint(1, 100)

lotto = str(rnd.randint(100,999))
#lotto1 = str(rnd.randint(1, 9))
#lotto2 = str(rnd.randint(1, 9))
#lotto3 = str(rnd.randint(1, 9))
#lotto = lotto1 + lotto2 + lotto3

mykey = input('3자리 복권번호는? (100~999)')
match = 0

#첫째 자리 비교
#if lotto[0] == mykey[0] or lotto[1] == mykey[1] or lotto[2] == mykey[2]:
    #match += 1

    # 둘째 자리 비교
   # if lotto[1] == mykey[1] or lotto[2] == mykey[2] or lotto[3] == mykey[3]:
        #match += 1

        # 셋째 자리 비교
        #if lotto[2] == mykey[2] or lotto[3] == mykey[3] or lotto[1] == mykey[1]:
            #match += 1

#개선된 코드 1
#if lotto[i] == mykey[0] or \
#    lotto[i] == mykey[1] or \
#    lotto[i] == mykey[2]:
#    match += 1

#개선된 코드 1B
#for i in range(3):
#    if lotto[i] == mykey[0]:
#        match += 1
#        if lotto[i] == mykey[1]:
#            match += 1
#            if lotto[i] == mykey[2]:
#                match += 1

#개선된 코드 2
for i in range(3):
    for j in range(3):
        if lotto[i] == mykey[j]:
            match += 1


#당첨 여부 판단
if match == 3:
    print('1등 당첨! 상금 백만원')
elif match == 2:
    print('2등 당첨! 상금 만원')
elif match == 1:
    print('3등 당첨! 상금 천원')
else:
    print('꽝! 아쉽지만 다음 기회에')

print(lotto, mykey, match)