# while 반복문
# 횟수와는 상관없이 조건에 따라 반복실행하는 반복문
# 즉, 조건식의 결과가 참이면 실행하고, 거짓일 경우 실행을 중단함

# 변수초기화
# while 조건식:
#    반복실행할 문장
#    증감식


# for 반복변수 in range(시작값, 종료값-1, 증감값): 반복 실행할 문장
# ex) 1 ~ 100 사
# 이 정수 출력
i = 1
while i <= 100:
    print(i, end=' ')
    i += 1

# ex) 1 ~ 100 사이 정수중 홀수만 출력
i = 1
while i <= 100:
    if i % 2 != 0:
        print(i, end=' ')
    i += 1


# ex) 1 ~ 100사이 정수들의 모든 합 계산후 출력
hap = 0
i = 1
while i <= 100:
    hap += i
    i += 1

print(hap)


# ex) 단을 입력받아 해당 단의 구구단을 출력
dan = int(input('단은?'))

i = 1
while i <= 9:
    print(f'{dan} x {i} = {dan*i}')
    i += 1



# p79 ex) 1~100 중에서 3의 배수이지만 2의 배수는 아닌 정수 출력하고,
# 누적합도 계산해서 출력
hap = 0
i = 1
result = ''
while i <= 100:
    if i % 3 == 0 and i % 2 != 0:
        hap += i
        result += str(i) + ' '
    i += 1
print(result)
print(hap)



# 무한루프
# 반복문의 조건식이 언제나 참이면
# 반복을 중단하지 않고 계속 반복을 지속하는 상황
# 단, 무한루프에서 탈출하려면 break를 이용
# while True:
#    반복실행할 문장


# 반복실행 중지 : break
# 반복 실행을 중지하고 반복문에서 나올때사용

# ex 1 ~ 100사이 정수들의 모든합 계산 출력
# 단, 무한루프와 break 이용해서 작성

i = 1
hap = 0
while True:
    if i <= 100: hap += i
    else: break
    i += 1

print(hap)



# ex) 1~1000사이의 모든 정수의 합 출력
# 단, 누적합이 15000을 넘으면 반복문을 중지하고 결과를 출력
i = 1
hap = 0
while True:
    if i <= 1000: hap += i
    if hap > 15000: break
    i += 1

print(hap, i)

#while i <= 1000:
#    if hap > 15000: break
#    hap += i
#    i += 1
#    print(hap, i)


# 성적 처리 프로그램의 메뉴화면 구현
#while문과 break 사용
main_menu = f'''
성적처리 프로그램 v1
----------------------
1.성적 데이터 추가 
2. 성적 데이터 조회
3. 성적 데이터 상세조회 
4. 성적 데이터 수정
5. 성적 데이터 삭제 
0. 프로그램 종료 
------------------ '''

while True:
    print(main_menu)
    menu = input('=> 작업을 선택하세요 : ')

    if menu == '0' : break
    elif menu == '1' :
        print('성적 데이터를 추가합니다.')
    elif menu == '2' :
        print('성적 데이터를 조회합니다.')
    elif menu == '3':
        print('성적 데이터 상세조회합니다.')
    elif menu == '4':
        print('성적 데이터를 수정합니다.')
    elif menu == '5':
        print('기존 성적 데이터를 삭제합니다.')
    else:
        print('잘못된 번호입니다.')


# 성적 처리 프로그램의 메뉴화면 작성 3
main_menu = f'''
성적 처리 프로그램 v1
----------------
1. 성적 데이터 추가
2. 성적 데이터 조회
3. 성적 데이터 상세조회
4. 성적 데이터 수정
5. 성적 데이터 삭제
0. 프로그램 종료
----------------'''

print(main_menu)
input('=> 작업을 선택하세요 : ')


#continue : 반복 실행시 특정 코드 회피
#반복 실행을 유지하면서
# 특정 코드블럭의 실행을 생략하고 싶을때 사용

# ex) 1~1000사이의 모든 정수의 합 출력
# 단, 7의 배수나 9의 배수는 제외하고 누적합을 구함
i = 0
hap = 0
while i <= 1000 :
    i += 1
    if i % 7 == 0 or i % 9 == 0 : continue
    hap += i #상황에 따라 실행될수도, 실행되지 않을수도 있음
print(hap)


# ex4) 아이디, 비밀번호를 입력받아
#미리 설정해둔 아이디, 비밀번호와 일치하면 '로그인 성공!'
#일치하지 않으면 '로그인 실패!' 라고 출력하는 조건문 작성
#아이디: abc123, 비밀번호: 987xyz

id = 'abc123'
pw = '987xyz'
while True:
    main_log = print('로그인을 진행해주세요')
    uid = input('아이디를 입력해 주세요')
    upw = input('비밀번호를 입력해 주세요')

    if uid == id and upw == pw :
        print('로그인이 정상적으로 처리되었습니다.')
        break
    else :
        print('아이디, 혹은 비밀번호를 다시 입력해 주세요')

uid = 'abc123'
pwd = '987xyz'

userid = input('아이디는?')
passwd = input('비밀번호는?')

if userid == uid and passwd == pwd :
    print('로그인 성공')
    break
    #반복문 종료
else :
    print('로그인 실패')

#난수 생성하기
# 파이썬에서 난수를 생성하려면 random 패키지 이용
# 생성방법 : 패키지명. random.randint(시작값, 끝값)

import random as rnd   #별칭으로 패키지명 줄여씀
rnd.seed(2210171044) #난수생성 초기값 지정
#1 ~ 10 사이 임의의 정수 생성
print(rnd.randint(1, 10))

#1~ 45 사이 임의의 영수 6개 생성
for _ in range(6) :               #반복실행시 인덱스가 필요없으면 _ 사용
    print(rnd.randint(1,45), end='')

print(range(rnd.randint(1, 45)),6)




