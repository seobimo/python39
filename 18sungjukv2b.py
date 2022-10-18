#성적 처리 프로그램 v2-b
# 2차원 리스트를 이용한 성적처리 프로그램

sjs = []
#성적 데이터 저장할 변수 선언
names = []
kors = []
engs = []
mats = []
tots = []
avgs = []
grds = []

#프로그램 메뉴 출력을 위한 변수 선언
main_menu = f'''
성적 처리 프로그램 v2
----------------
1. 성적 데이터 추가
2. 성적 데이터 조회
3. 성적 데이터 상세조회
4. 성적 데이터 수정
5. 성적 데이터 삭제
0. 프로그램 종료
----------------'''

#프로그램 주 실행부
while True:
    print(main_menu)
    menu = input('=> 메뉴를 선택하세요 : ')

    if menu == '0' :
        print('프로그램을 종료합니다.')
        break



    elif menu == '1' :   #성적 데이터 입력, 성적 처리
        name = input('이름')
        kor = int(input('국어'))
        eng = int(input('영어'))
        mat = int(input('수학'))

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

        sj = []
        sj.append(name)
        sj.append(kor)
        sj.append(eng)
        sj.append(mat)
        sj.append(tot)
        sj.append(avg)
        sj.append(grd)

        sjs.appand(sj)

        input('성적 데이터 추가 완료')

    elif menu == '2' :    #이름,국어,영어,수학만 출력
        hdr =  '이름 국어 영어 수학\n'
        hdr += '----------------'
        print(hdr)

        for sj in sjs:
            for s in  sj:
                print(f'{sj[0]} {sj[1]} {sj[2]} {sj[3]}')

            input('성적 데이터 조회가 완료되었습니다.')


    elif menu == '3':
        print('성적 데이터 상세조회합니다.')
    elif menu == '4':
        print('성적 데이터를 수정합니다.')
    elif menu == '5':
        print('기존 성적 데이터를 삭제합니다.')
    else:
        print('잘못된 번호입니다.')
