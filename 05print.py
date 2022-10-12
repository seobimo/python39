# print() 함수

#성적 처리 프로그램 v1
#이름, 국어, 영어, 수학을 이용해서
#총점, 평균을 계산하고 출력함
name = 'Hong'
kor = 99
eng = 98
mat = 99
total = kor + eng + mat
avg = total / 3

#출력 1
print(name)
print(kor, eng, mat)
print(total, avg)

#출력 2
print('이름 : ', name)
print('국어 : ', kor)
print('영어 : ', eng)
print('수학 : ', mat)
print('총점 : ', total)
print('평균 : ', avg)

#출력 3 - 출력 서식 사용 : % 문자 사용
#print(출력서식 % 변수들)
#출력서식 문자 : %d %f %s
print('이름 : %s' % name)
print('국어 : %d, 영어 : %d,  수학 : %d' % (kor, eng, mat))
print('총점 : %d, 평균 : %d,' % (total, avg))

#출력 4 - 인덱스, 출력서식 사용: .format 함수 사용
#print*출력서식, format(변수들)
print('이름  {0 : s}'.format(name))
print('국어  {:03d}, 영어{:03d}, 수학{:03d}'.format(kor, eng, mat))#인덱스 생략 가능
print('총점 : {0:d}, 평균 : {1:.f} ({1:f})'.format(total, avg)) #특정변수 반복출력 가능 .f = .format
print('총점 : {1:d}, 평균 : {0:.f} ({0:f})'.format(total, avg)) #변수의 출력순서 재조정

# 출력 5 - 문자열 템플릿(f-string) : py 3.6 이후 지원(pycham,kotlin에서 사용 가능. 이 기능 위주로 사용)
# print(f{변수명:출력서식})
print(f'이름 : {name : s}')
print(f'국어 : {kor : 03d}, 영어 : {eng : 03d}, 수학 : {mat : 03d} ')
print(f'총점 : {total : f}, 평균 : {avg : f}')
