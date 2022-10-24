# 회원가입을 처리하는 클래스 생성
# MemberVO :
#     userid, passwd, name, email, milege, grade
# MemberService :
#  registerMember  : 회원 정보 입력
#  processMemberGrade : 마일리지에 따라 회원 등급 결정
#      vip : 마일리지 - 10000이상
#      gold : 마일리지 - 7000이상
#      silver : 마일리지 - 4000이상
#      bronze : 마일리지 - 1000이상
#      member : 그외

class MemberVO:
    def __init__(self, userid, passwd, email, milege):
        self.__userid = userid
        self.__passwd = passwd
        self.__email = email
        self.__milege = milege
        self.__grade = ''

    def __str__(self):
        result = f'{self.__userid}, {self.__passwd}, {self.__email}, {self.__milege}, ' \
                 f' {self.__grade}'

        return result

    @property
    def userid(self):
        return self.__userid

    @property
    def passwd(self):
        return self.__passwd

    @property
    def email(self):
        return self.email

    @property
    def milege(self):
        return self.__milege

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, grade):
        self.__grade = grade

class MemberService:
    @staticmethod
    def register_member():
        uid = input('아이디 입력')
        pwd = input('비밀번호 입력')
        email = input('이메일 입력')
        milege = int(input('마일리지 입력'))

        return MemberVO(uid, pwd, email, milege)

    @staticmethod
    def process_membergrade(mb):
        mvo.grade = 'member'
        if mb.milege >= 10000:
            mb.grade = 'vip'
        elif mb.milege >= 7000:
            mb.grade = 'gold'
        elif mb.milege >= 4000:
            mb.grade = 'silver'
        elif mb.milege >= 1000:
            mb.grade = 'bronze'

mb = MemberService.registerMember()     # 회원정보입력
MemberService.processMemberGrade(mb)    # 회원등급처리
print(mb)           # => 결과 출력