import pymysql

url = ''
userid = ''
passwd = ''
dbname = ''


def openConn():
    conn = pymysql.connect(host=url, user=userid, passwd=passwd, database=dbname, charset='utf8')

    cur = conn.cursor()
    return conn, cur

def closeConn(cur, conn):
    cur.close()
    conn.close()