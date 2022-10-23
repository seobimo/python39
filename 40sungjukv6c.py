# CSV를 이용한 성적처리 프로그램
# 성적 처리 프로그램의 모든 함수들은
# sungjukv6lib.py에 작성하고 모듈명은 sjv6로 줄여서 사용함


#메인 모듈 import


#메인 코드 작성
import sungjukv6clib as sjv6c

#프로그램 주 실행부
sjv6c.loadSungJuk()
#메뉴 표시 및 값 입력받음
while True:

# 파일에 저장된 성적데이터 불러오기



    menu = sjv6c.displayMenu()

    if menu == '0':
        break

    elif menu == '1': sjv6c.addSungJuk()
    elif menu == '2': sjv6c.readSungJuk()
    elif menu == '3': sjv6c.readOneSungJuk()
    elif menu == '4': sjv6c.modifySungJuk()
    elif menu == '5': sjv6c.removeSungJuk()
    else:
        print('잘못된 번호입니다.')
#메모리에 존재하는 성적데이터를 파일에 저장
    #sjv6.saveSungJuk()