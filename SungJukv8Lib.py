from SungJukVO import SungJukVO
from SungJukv8DAO import SungJukv8DAO as sjdao

# sungjuk.dat 파일을 읽어서 sjs 변수에 초기화
class SungJukv8Lib:
    @staticmethod
    def display_Menu():
        main_menu = f'''
        성적 처리 프로그램 v8
        ----------------
        1. 성적 데이터 추가
        2. 성적 데이터 조회
        3. 성적 데이터 상세조회
        4. 성적 데이터 수정
        5. 성적 데이터 삭제
        0. 프로그램 종료
        ----------------'''
        print(main_menu)
        menu = input('메뉴를 입력하세요: ')

        return menu

    # private function 으로 선언
    @staticmethod
    def __input_sungjuk():
        name = input('이름은?')
        kor = int(input('국어는?'))
        eng = int(input('영어는?'))
        mat = int(input('수학은?'))

        # sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat}
        sj = [name, kor, eng, mat]
        return SungJukVO(name, kor, eng, mat)

    @staticmethod
    def add_sungjuk():
        # 성적 데이터 입력받기
        sj = SungJukv8Lib.__input_sungjuk()

        # 입력받은 성적데이터 처리
        SungJukv8Lib.__computesungjuk(sj)

        # 성적 데이터 테이블에 저장
        if sjdao.insert_sungjuk(sj) > 0:
            print('성적 데이터 추가 완료')

    @staticmethod
    def read_sungjuk():
        hdr = '이름 국어 영어 수학\n'
        hdr += '------------------'
        print(hdr)

        # 성적테이블에서 '이름/국어/영어/수학' 만 select해서 출력
        rows = sjdao.select_sungjuk()

        result = ''         # 출력할 결과를 담아둘 변수 선언
        for row in rows:
            result += f'{row[0]} {row[1]} {row[2]} {row[3]} \n'

        print(result)

    @staticmethod
    def readone_sungjuk():
        name = input('조회할 학생의 이름은?')

        hdr = '이름 국어 영어 수학 총점 평균 학점\n'
        hdr = '------------------------------\n'
        print(hdr)

        row = sjdao.selectone_sungjuk(name)
        result = f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]:.1f} {row[7]} '
        print(result)

    @staticmethod
    def modify_sungjuk():
        name = input('수정할 데이터의 학생 이름은?')

        #수정할 학생이름으로 기존데이터 조회
        sj = sjdao.selectone_sungjuk(name)

        # 번호/이름/국어/영어/수학/총점/평균/학점/등록일

        # 새로운(기존) 값을 입력받음
        kor = int(input(f'새로운 국어는 ({sj[2]})?'))
        eng = int(input(f'새로운 영어는 ({sj[3]})?'))
        mat = int(input(f'새로운 수학은 ({sj[4]})?'))

        # 다시 성적 처리
        #sj = [name, kor, eng, mat]
        sj = SungJukVO(name, kor, eng, mat)
        #tot, avg, grd = \
        SungJukv8Lib.__computeSungJuk(sj)
        #sj = sj + [tot, avg, grd]

        cnt = sjdao.update_sungjuk(sj)


    @staticmethod
    def remove_sungjuk():
        name = input('삭제할 데이터의 학생 이름은?')

        # 삭제할 학생이름 입력받아 성적테이블에서 해당 데이터 삭제
        cnt = sjdao.delete_sungjuk(name)

        if cnt > 0:
            print('성공적으로 삭제되었어요')

    @staticmethod
    def __compute_sungjuk(sj):
        sj.tot = sj.kor + sj.eng + sj.mat
        sj.avg = sj.tot / 3
        sj.grd = '가'
        if sj.avg >= 90: sj.grd = '수'
        elif sj.avg >= 80: sj.grd = '우'
        elif sj.avg >= 70: sj.grd = '미'
        elif sj.avg >= 60: sj.grd = '양'

