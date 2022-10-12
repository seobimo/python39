# ex) 주민번호에서 생년과 월, 일, 성별을 추출해서
#각 변수에 적절히 저장하세요
jumin = '202205092123456'

year = jumin[0:4]
month = jumin[4:6]
day = jumin[6:8]
gender = jumin[-5]
print(year, month, day, gender)
#14 - 시간계산

#하루는 86400초이다. 입력값이 1234567890일 경우 며칠인지 계산하여라
#한 시간은 3600초이다. 입력값이 98765일 경우 몇 시간인지 계산하여라
#일 분은 60초이다. 입력값이 12345일 경우 몇 분인지 계산하여라.
time = 1234567890
days = time // 86400

time = 98765
hour = time // 3600

time = 12345
min = time // 60


#16 - 잔돈게산

#지불급액은 ???이고,
#받은금액은 ???이고,
#잔액은 ??? 월 입니다.

#5만원권 ?장,
#만원권 ?장
#5천원권 ?장
#천원권 ? 장
#50원은 ? 장,
#10원은 ?장
#10원은 ?장

cost = 2500
money = 50000
charge = money - cost #47500

#5만원권
w50k = int(charge / 50000)
charge = charge - (w50k * 50000)

#1만원권
w10k = int(charge / 10000)
charge = charge - (w10k * 10000)

#5천원권
w5k = int(charge / 5000)
charge = charge - (w5k * 5000)

#1천원권
w1k = int(charge / 1000)
charge = charge - (w1k * 1000)

#500원권
w5m = int(charge / 500)
charge = charge - (w5m * 500)

#100원권
w1m = int(charge / 100)
charge = charge - (w1m * 100)

#50원권
w50 = int(charge / 50)
charge = charge - (w50 * 50)

#10원권
w10 = int(charge / 10)
charge = charge - (w10 * 10)

print(w50k, w10k, w5k, w1k, w5m, w1m, w50, w10)

#파이썬에서 제공하는 몫/나머지 연산자를 이용하면
#수식이 좀 더 간단해짐

cost = int(input('비용은?'))
money = int(input('지불금액은?'))
charge = money - cost

print(f'''
#지불급액은 {cost}이고,
#받은금액은 {money}이고,
#잔액은 {charge}원 입니다.

''')
#5만원권
w50k = charge // 50000
charge = charge % 50000

#1만원권
w10k = charge // 10000
charge = charge % 10000

#5천원권
w5k = charge // 5000
charge = charge % 5000

#1천원권
w1k = charge // 1000
charge = charge % 1000

#500원권
w5m = charge // 500
charge = charge % 500

#100원권
w1m = charge // 100
charge = charge % 100

#50원권
w50 = charge // 50
charge = charge % 50

#10원권
w10 = charge // 10
charge = charge % 10

print(f'''
오만원권 {w50k}장,
만원권 {w10k}장,
오천원권 {w5k}장,
천원권  {w1k}장,
500원은 {w5m}장,
100원은 {w1m}장,
50원은 {w50}장,
10원은 {w10}장,
입니다.
''')