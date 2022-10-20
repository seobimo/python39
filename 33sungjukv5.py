#모듈을 이용한 성적처리 프로그램
#성적 처리 프로그램의 함수들은
#sungjukv5lib.py에 작성함
#모듈명은 sjv5로 줄여서 사용함


#메인 모듈 import


#메인 코드 작성
import sungjukv5lib as sjv5

#프로그램 주 실행부
           #메뉴표시
#메뉴 표시 및 값 입력받음
while True:
    menu = sjv5.displayMenu()

    if menu == '0' :
        print('프로그램을 종료합니다.')
        break
    elif menu == '1': sjv5.addSungJuk()
    elif menu == '2': sjv5.readSungJuk()
    elif menu == '3': sjv5.readOneSungJuk()
    elif menu == '4': sjv5.modifySungJuk()
    elif menu == '5': sjv5.removeSungJuk()
    else:
        print('잘못된 번호입니다.')










#함수 정의부






