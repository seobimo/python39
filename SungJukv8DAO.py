import awsdbinfo as db

class SungJukv8DAO:
    @staticmethod
    def insert_sungjuk(sj):
        conn, cur = db.openConn()

        sql = ' insert into sungjuk (name, kor, eng, mat, tot, avg, grd) values  (%s, %s, %s, %s, %s, %s, %s) '
        params = [sj.name, sj.kor, sj.eng, sj.mat, sj.tot, sj.avg, sj.grd]

        cur.execute(sql, params)
        cnt = cur.rowcount
        conn.commit()

        db.closeConn(cur, conn)

        return cnt

    @staticmethod
    def select_sungjuk():
        conn, cur = db.openConn()

        sql = 'select name, kor, eng, mat from sungjuk order by sjno'
        cur.execute(sql)
        rows = cur.fetchall()

        db.closeConn(conn, cur)

        return rows

    @staticmethod
    def selectone_sungjuk(name):
        conn, cur = db.openConn()

        sql = 'select * from sungjuk where name= %s'
        cur.execute(sql, [name])
        row = cur.fetchone()

        db.closeConn(conn, cur)

        return row

    @staticmethod
    def update_sungjuk(sj, conn):
        conn, cur = db.openConn()
        sql = 'update sungjuk set kor=%(kr)s, eng=%(en)s, mat=%(mt)s, tot=%(tt)s, avg=%(av)s, grd=%(gd)s, regdate=current_timestamp where name = %(nm)s'
        params = dict(nm=sj.name, kr=sj.kor, en=sj.eng, mt=sj.mat, tt=sj.tot, av=sj.avg, gd=sj.grd)
        cur.execute(sql, params)
        cnt = cur.rowcount
        conn.commit()

        db.closeConn(conn, cur)

        return cnt
    @staticmethod
    def delete_sungjuk(name):
        conn, cur = db.openConn()

        sql = 'delete from sungjuk where name = %s'
        cur.execute(sql, [name])
        cnt = cur.rowcount
        conn.commit()

        db.closeConn(conn, cur)

        return cnt