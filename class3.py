class Stock():
    def __init__(self):
        self.__name = None  #self.__~~~ = 외부접근을 막는데 사용 (ex.읽기 전용)

        # self.__name = "LG"
        # print(self.__name) # 클래스 내부에서는 __언더바가 붙어있어도 바꿀 수 있다.

    def setName(self, nm):
        self.__name = nm

        print(self.__name) # 함수를 통하면 __언더바가 있어도 바꿀 수 있다.

    def getName(self):
        assert self.__name is not None, "name은 None이다." # assert는 에러를 발생시킨다.
        #assert는 잘못된 데이터가 들어가는 것을 방지할 수 있다.
        return self.__name

    def setName(self, name):
        self.__name = name

stock = Stock()
# stock.setName("LG")
print(stock.getName())

class Stock():
    def __init__(self):
        self.__price = None
        self.__high = None

    def setPrice(self, price):
        if self.__high is None or price > self.__high:
            self.__high = price

        if price > 10000:
            self.__price = price
        else:
            self.__price = 5000

    def getPrice(self):
        assert self.__price != None, "가격이 None입니다!"
        return self.__price

    def getHigh(self):
        return self.__high

stock = Stock()
stock.setPrice(15000)
print("주문을 넣습니다, 주문가격 : %s입니다." % stock.getPrice())
print("고가 가격: %s입니다." % stock.getHigh())

class Stock():
    def __init__(self):
        self.__price = None

    @property
    def getPrice(self):
        return self.__price

    @getPrice.setter
    def setPrice(self, price):
        self.__price = price

stock=Stock()
stock.setPrice = 5000
print(stock.getPrice)