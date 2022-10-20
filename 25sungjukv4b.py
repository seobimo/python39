#함수를 이용한 성적처리 프로그램

def computeSungJuk(kor, eng, mat, tot, avg, grd):
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

#성적 데이터 저장할 변수 선언
sjs = []
#함수 정의부
def displayMenu():
    main_menu = f'''
    성적 처리 프로그램 v4
    ----------------
    1. 성적 데이터 추가
    2. 성적 데이터 조회
    3. 성적 데이터 상세조회
    4. 성적 데이터 수정
    5. 성적 데이터 삭제
    0. 프로그램 종료
    ----------------'''
    print(main_menu)


def addSungJuk():
    name = input('이름')
    kor = int(input('국어'))
    eng = int(input('영어'))
    mat = int(input('수학'))

    #성적처리 - tot, avg, grd를 매개변수로 넘겨서
    #총점, 평균, 학점을 계산한 후
    #그 결과를 전달된 tot, avg, grd에 저장함
    #addSungJuk() 함수에서 계산된 결과 확인 - 실패
    tot, avg, grd = 0, 0, '가'
    computeSungJuk(kor, eng, mat, tot, avg, grd)

    sj = {'names': name, 'kors': kor, 'engs': eng, 'mats': mat, 'tots': tot, 'avgs': avg, 'grds': grd}
    sjs.append(sj)
input('성적 데이터 추가 완료')

def readSungJuk():
    hdr = '이름 국어 영어 수학\n'
    hdr += '----------------'
    print(hdr)

    for sj in sjs:
        print(f'{sjs["names"]} {sjs["kors"]} {sjs["engs"]} {sjs["mats"]}')


def readOneSungJuk():
    name = input('조회할 학생의 이름을 입력하세요')
    sj = None
    for item in sjs:  # 입력한 이름과 일치하는 항목을 sjs에서 찾음
        if item['name'] == name: sj = item

        hdr = '이름 국어 영어 수학 총점 평균 학점\n'
        hdr += '-----------------------------'
        print(hdr)
        for k in sj.keys():
            print(sj.get(k), end=' ')


def modifySungJuk():
    name = input('성적을 수정할 학생의 이름을 입력바랍니다.')

    sj = None
    for i in range(len(sjs)):  # 입력한 이름과 일치하는 항목을 sjs에서 찾음
        if sjs[i]["name"] == name: idx = i
        break

    # 새로운 값을 입력받음
    kor = int(input(f'국어점수를 입력바랍니다({sjs[idx]["kor"]})'))
    eng = int(input(f'영어점수를 입력바랍니다({sjs[idx]["eng"]})'))
    mat = int(input(f'수학점수를 입력바랍니다({sjs[idx]["mat"]})'))

    # 다시 재평가
    tot, avg, grd = 0, 0, '가'
    computeSungJuk(kor,eng,mat,tot,avg,grd)
    # 값 다시 저장
    sj = {'names': name, 'kors': kor, 'engs': eng, 'mats': mat, 'tots': tot, 'avgs': avg, 'grds': grd}

    # 기존에 저장되었던 list에 수정한 결과값을 다시 저장
    sjs[idx] = sj


def removeSungJuk():
    name = input('삭제할 데이터의 학생 이름을 입력해주세요')

    for i in range(len(sjs)):  # 입력한 이름과 일치하는 항목을 sjs에서 찾음
        item = sjs[i]
        if item["name"] == name: idx = i

    idx = None
    for i in range(len(sjs)):  # 삭제할 데이터의 인덱스 조사
        item = sjs[i]
        if item["name"] == name: idx = i

    sjs.pop(idx)



#메인 코드 작성


#프로그램 주 실행부

while True:             #메뉴표시
#메뉴 표시 및 값 입력받음
    displayMenu()
    menu = input('=> 메뉴를 선택하세요 : ')


    if menu == '0' :
        print('프로그램을 종료합니다.')
        break
    elif menu == '1': addSungJuk()
    elif menu == '2': readSungJuk()
    elif menu == '3': readOneSungJuk()
    elif menu == '4': modifySungJuk()
    elif menu == '5': removeSungJuk()
    else:
        print('잘못된 번호입니다.')

