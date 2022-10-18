# dict
# 비순차 자료구조
# 키를 통해 값을 찾는 연관배열 객체
# 선언방법은 { 키:값 } 형태로 정의하고 사용
# 다양한 자료형으로 구성된 데이터를
# 하나의 변수로 접근할 수 있음

member = {'userid':'abc123', 'passwd':'987xyz'}

#dict 값 조회 : 객체명['키명']
print(member['userid'], member['passwd'])

#dict 모든 키 조회 : 객체명.keys()
# for ~ in 반복문으로 조회 가능
print(member.keys())

for key in member.keys():
    print(key, end=' ')

# dict 모든 값 조회 : 객체명.values()
# for ~ in 반복문으로 조회 가능
for value in member.values():
    print(value, end=' ')

# dict 모든 키,값 조회 #1 : 객체명.items()
print(member.items())

for k, v in member.items():
    print(f'({k}, {v})', end=' ')

# dict 모든 키,값 조회 #2 : 키 이용      @추천@

for k in member.keys():
    print(member[k], end=' ')

# dict 모든 키,값 조회 #3 : 객체명.get(키) 이용      @추천@

for k in member.keys():
    print(member.get(k), end=' ')

#dict 동적 생성 #1
user = {}              #사용자 - 이름, 나이, 이메일

#객체명[새로운키] = 새로운값
user['name'] = '홍길동'
user['age'] = 28
user['email'] = 'gd123@hello.com'

print(user)

#dict 동적 생성 #2 : dict(키=값, ...)
user2 = dict(name='홍길동',age=35, email='gd@bye.com')

print(user2)

#dict 동적 생성 3 " list dldyd - [[키, 값],...]
user3 = [['name','홍길동'],['age',35],['email','gd@hi.com']]
print(dict(user3))

#dict 수정하기 : 객체명[기존키] = 새로운값
user['age'] = 30
user['email'] = '123qwe@kor.co.kr'

#dict 삭제하기 : del 객체형 [기존키] - 키와 값 모두 삭제

del user['age']
#객체명.get(키) vs 객체명[키]
user['regdate']      #존재하지 않는 키 호출시 - 오류 표시
#오류 발생시 예외처리 코드로 적절히 대처

user.get('regdate')  #존재하지 않는 키 호출시 - 오류 표시x
#반환 값이 none인지 여부에 따라 오류처리 대처



# dict 자료구조를 이용해서
# 학생 1명분의 성적 데이터를 입력받아 처리
# 저장형식 : { 'name':??, 'kor':??, 'eng':??, 'mat':??,
#             'tot':??, 'avg':??, 'grd':??  }

student = []

name = input('이름은?')
kor = int(input('국어점수는?'))
eng = int(input('영어점수는?'))
mat = int(input('수학점수는?'))
tot = kor + eng + mat
avg = tot / 3
grd = '가'
        if avg >= 90:
            grd = '수'
        elif avg >= 80:
            grd = '우'
        elif avg >= 70:
            grd = '미'
        elif avg >= 60:
            grd = '양'
student = {'names':name, 'kors':kor, 'engs':eng, 'mats':mat, 'tots':tot, 'avgs':avg, 'grds':grd}
#print('student.keys()는:', student.keys())
#print('student.values()는:', student.values())

#for s in student.keys():
#    print(student.get(s), end=' ')

#----------------------------------------------------------------
#다른 방식
std = {}
std['name'] = name
std['kor'] = kor
std['eng'] = eng
std['mat'] = mat
std['tot'] = tot
std['avg'] = avg
std['grd'] = grd

print(std)



# dict 자료구조를 이용해서
# 학생 3명분의 성적 데이터를 입력받아 처리
# 저장형식 : { 'name':??, 'kor':??, 'eng':??, 'mat':??,
#             'tot':??, 'avg':??, 'grd':??  }

#3명분의 성적 데이터를 저장하기 위한 변수 선언
lst = []

for _ in range(3):
    name = input('이름은?')
    kor = int(input('국어점수는?'))
    eng = int(input('영어점수는?'))
    mat = int(input('수학점수는?'))
    tot = kor + eng + mat
    avg = tot / 3
    grd = '가'
    if avg >= 90:
        grd = '수'
    elif avg >= 80:
        grd = '우'
    elif avg >= 70:
        grd = '미'
    elif avg >= 60:
        grd = '양'

std = {'names':name, 'kors':kor, 'engs':eng, 'mats':mat, 'tots':tot, 'avgs':avg, 'grds':grd}
lst.append(std)

#결과 출력
for std in lst:
    print(lst)

#dict 형식 데이터 출력시 예쁘게 표시 : pretty print
from  pprint import pprint as pp

pp(std)