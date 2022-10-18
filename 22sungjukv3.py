# 성적 처리 프로그램의 메뉴화면 작성 4
#성적 데이터 저장할 변수 선언
sjss = []

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

        sjs = {'names': name, 'kors': kor, 'engs': eng, 'mats': mat, 'tots': tot, 'avgs': avg, 'grds': grd}
        sjss.append(sjs)
        input('성적 데이터 추가 완료')

    elif menu == '2' :    #이름,국어,영어,수학만 출력
        hdr =  '이름 국어 영어 수학\n'
        hdr += '----------------'
        print(hdr)

        for sjs in sjss:
            print(f'{sjs["names"]} {sjs["kors"]} {sjs["engs"]} {sjs["mats"]}')

        input('성적 데이터 조회가 완료되었습니다.')
    elif menu == '3':                  #이름으로 검색 후 해당 학생의 모든 정보를 출력
        name = input('조회할 학생의 이름을 입력하세요')
        sj = None
        for item in sjs:                  #입력한 이름과 일치하는 항목을 sjs에서 찾음
            if item["name"] == name: sj = item


            hdr = '이름 국어 영어 수학 총점 평균 학점\n'
            hdr += '-----------------------------'
            print(hdr)
            for k in sj.keys():
                print(sj.get(k), end=' ')

        input('\n 성적 데이터 상세조회가 완료되었습니다.')
    elif menu == '4':

        input('성적을 수정할 학생의 이름을 입력바랍니다.')

        sj = None
        for i in range(len(sjs)):  # 입력한 이름과 일치하는 항목을 sjs에서 찾음
            if sjs[i]["name"] == name: idx = i
            break

        #새로운 값을 입력받음
        kor = int(input(f'국어점수를 입력바랍니다'({sjs[idx]["kor"]})'))
        kor = int(input(f'영어점수를 입력바랍니다'({sjs[idx]["eng"]})'))
        kor = int(input(f'수학점수를 입력바랍니다'({sjs[idx]["mat"]})'))

        #다시 재평가
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

        #값 다시 저장
        sj = {'names': name, 'kors': kor, 'engs': eng, 'mats': mat, 'tots': tot, 'avgs': avg, 'grds': grd}

        #기존에 저장되었던 list에 수정한 결과값을 다시 저장
        sjs[idx] = sj

    elif menu == '5':
        name = input('삭제할 데이터의 학생 이름을 입력해주세요')

        for i in range(len(sjs)):  # 입력한 이름과 일치하는 항목을 sjs에서 찾음
            item = sjs[i]
            if item["name"] == name: idx = i

        idx = None
        for i in range(len(sjs)):         #삭제할 데이터의 인덱스 조사
            item = sjs[i]
            if item["name"] == name: idx = i

        sjs.pop(idx)
        #for sj in sjs:
        #    if item["name"] == name: del sjss



        input('기존 성적 데이터를 삭제했습니다.')
    else:
        print('잘못된 번호입니다.')