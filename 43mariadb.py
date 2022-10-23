#MariaDB로 데이터 다루기 1 - select
# pymsql 모듈을 먼저 설치 : pip install pymysql
import pymysql

url = 'bigdatadb.ctumpltxg2f6.ap-northeast-2.rds.amazonaws.com'
userid ='admin'
passwd = 'Bigdata_2022'
dbname = 'bigdata'

conn = pymysql.connect(host=url, user=userid, password=passwd, database=dbname, charset='utf8')

cur = conn.cursor()
sql = 'select userid, passwd, name, email from member'
cur.execute(sql)

result = ''
rows = cur.fetchall()               # 실행 결과집합 모두 가져옴
for row in rows:
    result += f'{row[0]} {row[1]} {row[2]} {row[3]} \n'     # 출력 결과 누적

cur.close()
conn.close()

print(result)

# MariaDB로 데이터 다루기 #2 - insert
import pymysql

uid = input('id')
upw = input('pw')
name = input('name')
email = input('email')

conn = pymysql.connect(host=url, user=userid, password=passwd, database=dbname, charset='utf8')
cur = conn.cursor()


# 매개변수 placeholder(%)를 이용해서 실제값 지정
sql = f' insert into member(userid, passwd, name, email) values (%s, %s, %s, %s)'
params = (uid, upw, name, email)
cur.execute(sql, params)
conn.commit()    # 테이블에 값 저장하기 위해 commit 호출
print(cur.rowcount, '행이 추가됨')

cur.close()
conn.close()





