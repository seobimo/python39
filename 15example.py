# ex48) 복리 계산 - 언제쯤 통장잔액 2배?
money = 25000   #통장잔액

inter = 1.06    #이율
limit = money * 2

#while True:
#    if money > limit: break
#    money =  money + (money * 0.06)
#    money = money * inter

for i in range(999):
    if money > limit: break
    money = money * inter

print(f'{i+1} 년째, 잔액은 {money:,.0f}원')
# ex51) 구구단 테이블 출력


# ex53) 입력한 연도의 1월 달력 출력
#( (년도-1)*365 + (년도-1)/4 - (년도-1)/100 + (년도-1)/400)  % 7) + 1 )
#0 : 일, 1 : 월, 2 : 화, … … , 6 : 토
year = int(input('년도는?'))
exyear31 = ((year-1)*365 + (year-1)/4 - (year-1)/100 + (year-1)/400) % 7 + 1

print(int(exyear31))       #2021년 12월 31일의 요일
print(int(exyear31)+1)       #2022년 1월 1일의 요일