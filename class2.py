class Stock():
    def __init__(self):
        print("Stock class 실행")

        self.price:int =None # 현재가
        self.drate:float =None # 등락율
        self.high:int = None # 고가
        self.name:str = None # 종목명
        self.start:int = None # 시가
        self.low:int = None # 저가

stock_dict = {}

stock = Stock() #클래스에 변수를 만들어주는 것 = 인스턴스화()
stock.name = "삼성전자"
stock.price = 5000
stock.drate = 3.9
stock.high = 5500
stock.start = 4500
stock.low = 4000

stock_dict[stock.name]= stock
print(stock_dict)

stock = Stock()
stock.name = "LG"
stock.price = 10000
stock.drate = 5.9
stock.high = 11000
stock.start = 7000
stock.low = 6000

stock_dict[stock.name] = stock
print(stock_dict) # 삼성과 서로 다른 클래스이다.

# Stock이라는 클래스를 만들고
# 현재가, 등락율, 고가, 시가, 저가 변수를 만들고
# 딕셔너리에 종목 3개만 생성한다.

# 생성이 됐으면 현재가가 가장 높은 종목만 출력한다.

class Stock():
    def __init__(self):
        print("Stock class 실행")

        self.price:int =None # 현재가
        self.drate:float =None # 등락율
        self.high:int = None # 고가
        self.name:str = None # 종목명
        self.start:int = None # 시가
        self.low:int = None # 저가

stock_dict = {}
name_list = ["삼성전자", "LG", "현대건설"]
for name in name_list:
    if name not in stock_dict.keys():
        stock = Stock()
        stock_dict[name] = stock

    if name == "삼성전자":
        price = 10000
        drate = 3.9
        high = 15000
        start = 9000
        low = 8000
    elif name == "LG":
        price = 70000
        drate = 1.9
        high = 20000
        start = 9000
        low = 8000
    elif name == "현대건설":
        price = 7000
        drate = 5.9
        high = 9000
        start = 6000
        low = 5000

    stock:Stock = stock_dict[name]
    stock.price = price
    stock.drate = drate
    stock.high = high
    stock.start = start
    stock.low = low

top_stock_name = None
top_price = 0
for name in stock_dict.keys():
    stock:Stock = stock_dict[name]
    if stock.price > top_price:
        top_price = stock.price
        top_stock_name = name

print("가장 높은 현재가를 가진 종목: %s" % top_stock_name)




