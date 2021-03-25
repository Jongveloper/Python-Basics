class OrderClass:
    def __init__(self):
        self.buysell_count = 0

    @staticmethod # self기능을 비활성화한다. 클래스안에있는 내부메모리를 바로 접근하기위해 쓴다.
    def order_fnc(code):
        print("주문을 넣는다: %s" % code)

class Method1():
    def calcul(code):
        print("계산합니다")
        OrderClass.order_fnc(code) # 클래스를 객체화하지 않았기때문에 self를 변수로인식한다.

method1 = Method1()
Method1.calcul("LG")

print("알고리즘 폴더가 커밋이 책정이 안되어 커밋오류 확인용 커밋입니다.")