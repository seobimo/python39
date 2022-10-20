# 컨프리헨션comprehension
# 다양한 데이터 객체에 사용하는 복잡한 구문을
# 단순하게 작성할 수 있도록 지원

# 파이썬에는 4가지 축약을 지원
# list(py2), set(py3), dict(py3), generator(py3)

# 리스트에 척용하는 축약
# 1 ~ 10 까지의 정수를 생성해서 리스트에 저장
a = list(range(1, 10 + 1))
print(a)

b = []
for i in range(1, 10 + 1):
 b.append(i)
 print(b)

# 리스트 for 축약문
# [for 항목 in 반복 가능 개체]
c = [i for i in range(1, 10 + 1 )]
print(c)

# ex) 1 ~ 20 사이 정수의 짝수를 리스트로 생성
d = []
for i in range(1, 20 + 1):
 if i % 2 == 0 :
  d.append(i)

print(d)
# ---------
d=[]
for i in range(2, 20 + 1, 2):
 d.append(i)
 print(d)
# --------
d = [i for in range(2, 20 + 1)]
print(d)

# ex) 1 ~ 10사이 정수를 제곱한 값을 리스트로 생성
e = []
for i in range(1, 10 + 1):
 e.append(i ** 2)
 print(e)

# ----------
e = [i ** 2 for i in range(1, 10 + 1)]
print(e)



# ex) 아래 각각의 리스트를 이용해서 제곱값을 계산하고
# 새로운 리스트에 생성하세요
val1 = [1, 2, 3, 4, 5]
val2 = [1, 2, 'A', False, 9, 100]

f = []
g = []

for i in val1:
 f.append(i ** 2)
print(f)

for i in val2:          # => 오류 발생 TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
 g.append(i ** 2)
print(g)

# 변수 유형 확인 : type(대상)
print(type(1), type('A'), type(False))

# 조건식을 이용해서 재작성 - 정수일 경우 제곱 연산
h = []
for i in val2:
 if type(i) == int:
  h.append(i ** 2)
print(h)
# ----------
h = []
for i in val2:
 #if type(i) == int, str, bool:  #안되네.,
  h.append(i ** 2)
print(h)


# for if 축약문
# [표현식 for 항목 in 반복가능개채 if 조건]

a = [i ** 2 for i in val1 if i % 2 == 0]
print(a)

b = [i ** 2 for i in val2 if type(i) == int]
print(b)

# 1 ~ 60 사이 정수 중 홀수만 골라 리스트에 저장
c = []
for i in range(1, 60 + 1):
 if i % 2 != 0 :
  c.append(i)
print(c)
# ----------



c = [i for i in range(1, 60 + 1)  if i % 2 == 0 else for i in]

# 1 ~ 60 사이 5의 배수만 골라 리스트에 저장

d = []
for i in range(1, 60 + 1):
 if i % 5 == 0 :
  d.append(i)
print(d)

# ----------
d = [i for i in range(1, 60 + 1) if i % 5 == 0]


# ex) 1 ~ 100 사이 정수 중 임의의 정수가 짝수면 'even',
#홀수면 'odd' 라고 구분해서 리스트에 저장


e = []
for i in range(1, 100 + 1):
 if i % 2 == 0:
  val = 'even'
 else:
  val = 'odd'

 c.append(val)
 print(e)

# for 다중 if 축약문
# [표현식1 if 조건 else 표현식2 for 항목 in 반복가능개채]
f = ['even' if i % 2 == 0 else 'odd' for i in range(1, 100 + 1) ]
print(f)

# ex) 구구단 중 7,8단의 결과값을 리스트에 저장
# [7,14,21 ..., 8,16,24..., 72]
dan = []
for i in range(7, 8 + 1):
 for j in range(1, 9+1):
  dan.append(i * j)
print(f'{i} x {j} = {i * j}')
print(dan)

# 중첩 for 축약
# [표현식 for 항목1 in 반복가능개체1]
# for 항목2 in 반복가능개체2]

gugu = [i * j for i in range(7, 8 + 1) for j in range(1, 9 + 1)]
print(gugu)

# ex) name, grd 리스트의 값들
# 각각의 키와 값으로 딕셔너리에 저장
# 단순하게 작성
# 새로운 dict요소 생성 : 객체명[키이름] = 값
name = ['혜교','지현','수지']
grd = ['우','미','수']
s = []
s[name[0]] = grd[0]
s[name[1]] = grd[1]
s[name[2]] = grd[2]
print(s)

#반복문으로 재작성
s = []
for i in range(len(name)):
 s[name[i]] = grd[i]
 print(s)

# ----------
# 딕셔너리 for 축약문
#{ 키값표현식 for k,v(=key,value) in zip (반복가능개체1, 반복가능개체2) }
 sj = {k:v for  k, v in zip(name, grd)}
 print(sj)

 # ex) 학생과 국어점수에 대한 리스트가 있을때
 # 학생은 키로, 합격여부를 값으로 하는 딕셔너리 객체를 생성
 # 단, 합격여부에는 국어점수가 85점이상인 경우 '합격'
 # 그외는 '불합격'이라고 출력함
 name = ['철수', '영희', '길동', '꺽정']
 kor = [50, 80, 90, 60]
 sj = {k:'합격' if v >= 85 else '불합격' for k, v in zip(name, kor) }
 print(sj)

# -----------
t = []
for i in range(len(name)):
 if kor[i] >= 85 :
  val = '합격'
 else:
  val = '불합격'
 t[name[i]] = val
 print(t)

# 딕셔너리 for if 축약문
# {키: 표현식1 if 조건식 else 표현식2 for k,v in zip(반복가능개체1, 반복가능개체2) }
t = {k:'합격' if v >= 85 else '불합격' for k, v in zip(name, kor) }
print(t)


# p111 ex3)
message = ['spam', 'ham','spam','ham','spam']

# A) spam = 1, ham = 0 이라는 변수 생성
s = [1 if i == 'spam' else 0 for i in message]
print(s)
# ------------

def makeDummy(x):
 val = 0
 if x == 'spam': val = 1
 return val
list(map(makeDummy, message))
print(message)
# B) spam 원소만 추출
spams = [m for m in message if m == 'spam']
print(spams



 def makeSpams(x):
  isSpam = False
  if x == 'spam' : isSpam = True
  return isSpam

list(filter(makeSpams, message))

list(filter(lambda x:X == 'spam', message))

