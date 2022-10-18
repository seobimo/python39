# 집합(set)
# 비순차 열거형 자료구조
# 데이터가 저장된 순서를 기억하지 않음 (인덱스 사용x)
# 단, 집합을 리스트나 튜플로 변환하면 사용가능
# 입력된 데이터의 중복을 허용하지 않음
# 선언방법은 {}안에 값들을 정의하고 사용

#집합 선언
nums = {1, 2, 3, 4, 5}

#접합 출력 #1
nums[0]

#접합 출력 #2
for i in range(len(nums)):       #순차조회 불가
    print(nums[i])

# 접합 출력 #3
for num in nums:             #하나씩 열거해가며 조회 가능
    print(num, end='')

#집합 동적 생성
nums = set()                #{} 는 dict 자료형으로 인식

nums.add(10)
nums.add(20)
nums.add(30)
nums.add(30)                #중복 저장 불가

print(nums)

# 집합 값 제거 : remove(값)
nums.remove(20)
print(nums)

#집합 값 수정 : 기본적으로는 불가. 단 리스트 변환시 사용가능
nums[0] = 000

nums = list(nums)
nums[0] = 999
nums = set(nums)

print(nums)


# ex) 로또 645 : 1 ~ 45사이 임의의 숫자 6개 생성
#단, set을 이영해서 같은 숫자가 출현하지 않도록 작성

import random as rnd

lottos = set()
key = {}

#for _ in range(6):
#lankey = set(rnd.randint(1, 45))
#key.add(lankey)
#print(key)
while True:
    if len(lottos) > 5: break
    lotto = rnd.randint(1, 45)
    lottos.add(lotto)
print(lottos)

# ex) 로또 645 : 1 ~ 45사이 임의의 숫자 6개 생성
#단, list을 이영해서 같은 숫자가 출현하지 않도록 작성

import  random as rnd
lottos = []

#for i in range(6):
#    key = rnd.randint(1, 45)

while True:
    if len(lottos) > 5: break     #종료조건 설정
    lotto = rnd.randint(1, 45)
    if lotto not in lottos:   #생성한 난수가 리스트에 없다면
        lottos.append(lotto)

   # lottos.append(key[i])
print(lottos)

# ex) 로또 645 : 1 ~ 45사이 임의의 숫자 6개 생성
#단, list을 이영해서 같은 숫자가 출현하지 않도록 작성
import random as rnd

lotto = list(range(1, 45+1))      #로또 번호 초기화
print(lotto)
rnd.shuffle(lotto)                #번호를 임의로 섞음
print(lotto)
#로또 번호를 뽑을 인덱스를 난수로 생성하여
#리스트에서 해당 위치의 값을 추출
for _ in range(6):
    rnd.shuffle(lotto)
    idx = rnd.randint(0, len(lotto) - 1)
    print(lotto[idx], end=' ')
    #lotto.remove(lotto[idx])     #비복원추출
    lotto.pop(idx)

