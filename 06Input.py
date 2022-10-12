# input() 함수
#변수명 = input(입력메세지)


#성적 처리 프로그램 v2
#이름, 국어, 영어, 수학을 입력받아
#총점, 평균을 계산하고 출력함
name = input('이름은?')
print('이름 : ' + name)
kor = int(input('국어 점수를 입력해 주세요')) #산술식에 사용해야 함으로 형 변환 필요

eng = int(input('영어 점수를 입력해 주세요'))

mat = int(input('수학 점수를 입력해 주세요'))

total = kor + eng + mat
print(total)
avg = total / 3
print(avg)

#총 칼로리 합계(지방,탄수화물,단백질) 계산 프로그램

gee = int(input('지방의 그램을 입력하세요'))
tan = int(input('탄수화물의 그램을 입력하세요'))
dan = int(input('단백질의 그램을 입력하세요'))
tot = gee * 9 + dan * 4 + tan * 4
print(f'총칼로리 : {tot:c} ,cal')

#풀이 1
fat = 25
carbo = 520
protain = 45

totcal = fat * 9 + carbo * 4 + protain * 4
print(totcal)

#풀이 2
fat = int(input('지방은?'))
carbo = int(input('탄수화물은?'))
protain = float(input('단백질은?'))

totcal = fat * 9 + calbo * 4 + protain * 4
print(f'총칼로리 : {totcal} cal')

#성적처리프로그램의 메뉴화면 작성 1
main_menu = '성적 처리 프로그램 v1 \n'
main_menu += '---------------------'
print('1.성적 데이터 추가')
print('2. 성적 데이터 조회')
print('3. 성적 데이터 상세조회')
print('4. 성적 데이터 수정')
print('5. 성적 데이터 삭제')
print('0. 프로그램 종료')
print('------------------')

print(main_menu)


#성적처리프로그램의 메뉴화면 작성 2
main_menu = '성적 처리 프로그램 v1 \n'
main_menu += '--------------------- \n'
print('1.성적 데이터 추가 \n' )
print('2. 성적 데이터 조회 \n')
print('3. 성적 데이터 상세조회 \n')
print('4. 성적 데이터 수정 \n')
print('5. 성적 데이터 삭제 \n')
print('0. 프로그램 종료 \n')
print('------------------')

print(main_menu)

#성적처리프로그램의 메뉴화면 작성 3
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
print(main_menu)
input('=> 작업을 선택하세요 : ')