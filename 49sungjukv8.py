# OOP를 이용한 성적처리 프로그램
# 성적 처리 프로그램의 모든 함수들은
# sungjukv8lib.py에 작성하고 모듈명은 sjv8로 줄여서 사용함

from SungJukv8Lib import SungJukv8Lib as sjv8

#프로그램 주 실행부
while True:

    # 메뉴 표시 및 값 입력받음
    menu = sjv8.display_Menu()


    if menu == '1': sjv8.add_sungjuk()
    elif menu == '2': sjv8.read_sungjuk()
    elif menu == '3': sjv8.readone_sungjuk()
    elif menu == '4': sjv8.modify_sungjuk()
    elif menu == '5': sjv8.remove_sungjuk()
    elif menu == '0': break
    else:
        print('잘못된 번호입니다.')
