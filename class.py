def cal():
    print("함수다")

class Cal: # 클래스는 앞에 대문자를 써준다.
    print("클래스이다.")
    price = 5000

    def a_fnc(self): #클래스함수는 셀프를 가진다. 셀프는 함수를 사용할때마다 꼭 넣어줘야한다.
        print("a_fnc")
        print(self.price)

        self.name = "삼성"
        print(self.name)

        print(dir(self))

    def b_fnc(self):
        print("b_fnc")

cal = Cal()
cal.a_fnc() # a_fnc를 찾아온다.
cal.b_fnc() # b_fnc를 찾아온다.
#클래스는 여러가지 함수를 가질 수 있다.


class Method():
    def __init__(self, account_num):
        print("초기화")
        print("계좌번호 %s" % account_num)

        self.name = "삼성" # self에 name을 담아준다.
        self.price = 0 # self에  price를 담아준다.
        self.buy_cnt = 0 #self에 buy_cnt 를 담아준다.

    def cal(self):
        self.price = 5000
        self.buy_cnt = 10
        result = self.price * self.buy_cnt
        print("매입금액 %s" % result)

method = Method("123456789")
method.cal()

