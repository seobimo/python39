
# 성적 데이터 저장할 변수 선언
sjs = []

# sungjuk.dat 파일을 읽어서 sjs 변수에 초기화
def loadSungJuk():
    global sjs
    with open('data/sungjuk.dat', encoding='UTF-8') as f:
        data = f.readlines()


        outs = []                               # 성적 데이터를 저장하기 위해 리스트 선언
        for d in data:                          # 리스트에 저장된 성적데이터를 한 행씩 읽어와서
            # strip: 쓸데없는 특수기호나 공백, 개행을 없앰
            items = d.strip().split(',')                # 읽어온 데이터를 ,로 분리하고 dict 형식으로 성적데이터를 재작성 함
            item = {'name': items[0], 'kor': items[1], 'eng': items[2], 'mat': items[3], 'tot':items[4], 'avg':items[5], 'grd':items[6]}
            outs.append(item)
            # dict로 작성된 데이터를 리스트에 저장
            sjs = outs
# 성적데이터들을 sungjuk.dat 파일에 저장
# [{'name':name, 'kor':kor, 'eng':eng, 'mat':mat }]
def saveSungJuk(sjs):
    # newline : 성적 데이터 저장시 줄바꿈이 2번 저장되는 것을 방지
    with open('data/sungjuk.dat', 'w', encoding='UTF-8') as f:

        # 방금 입력한 성적데이터와
        # 기존에 입력한 모든 성적 데이터를 파일에 함께 저장

        for sj in sjs:
            dat = f"{sj['name']}, {sj['kor']}, {sj['eng']}, {sj['mat']}, {sj['tot']}, {sj['avg']}, {sj['grd']} \n"
            f.write(dat)

def displayMenu():
    main_menu = f'''
    성적 처리 프로그램 v6
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

def inputSungJuk():
    name = input('이름은?')
    kor = int(input('국어는?'))
    eng = int(input('영어는?'))
    mat = int(input('수학은?'))

    sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat}

    return sj

def addSungJuk():
    # 성적 데이터 입력받기
    sj = inputSungJuk()

    # 입력받은 성적데이터 초기화
    tot, avg, grd = computeSungJuk(sj)

    sj['tot'] = tot
    sj['avg'] = avg
    sj['grd'] = grd

    sjs.append(sj)

    # sjs 에 저장된 성적데이터를 파일에 저장
    saveSungJuk(sjs)

def readSungJuk():
    hdr = '이름 국어 영어 수학\n'
    hdr += '------------------'
    print(hdr)

    for sj in sjs:
        print(f'{sj["name"]} {sj["kor"]} {sj["eng"]} {sj["mat"]}')

def readOneSungJuk():
    name = input('조회할 학생의 이름은?')

    sj = None
    for item in sjs:
        if item['name'] == name: sj = item

    hdr = '이름 국어 영어 수학 총점 평균 학점\n'
    hdr = '------------------------------\n'
    for k in sj.keys():
        print(sj.get(k), end=' ')

def modifySungJuk():
    name = input('수정할 데이터의 학생 이름은?')

    sj = None
    for i in range(len(sjs)):

        if sjs[i]['name'] == name:
            idx = i
            break

    # 새로운(기존) 값을 입력받음
    kor = int(input(f'새로운 국어는 ({sjs[idx]["kor"]})?'))
    eng = int(input(f'새로운 영어는 ({sjs[idx]["eng"]})?'))
    mat = int(input(f'새로운 수학는 ({sjs[idx]["mat"]})?'))

    # 다시 성적 처리
    sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat}
    tot, avg, grd = computeSungJuk(sj)
    sj['tot'] = tot
    sj['avg'] = avg
    sj['grd'] = grd

    # 기존 위치에 다시 저장
    sjs[idx] = sj

    #수정된 성적데이터를 파일에 저장
    saveSungJuk(sjs)

def removeSungJuk():
    name = input('삭제할 데이터의 학생 이름은?')

    idx = None
    for i in range(len(sjs)):  # 삭제할 데이터의 인덱스 조사
        item = sjs[i]
        if item['name'] == name: idx = i

    sjs.pop(idx)

    #삭제된 성적데이터를 파일에 반영
    saveSungJuk(sjs)
def computeSungJuk(sj):
    tot = sj['kor'] + sj['eng'] + sj['mat']
    avg = tot / 3
    grd = '가'
    if avg >= 90: grd = '수'
    elif avg >= 80: grd = '우'
    elif avg >= 70: grd = '미'
    elif avg >= 60: grd = '양'

    return tot, avg, grd