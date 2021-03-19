def price_cal():
    return 5000

var_1 = price_cal
print(var_1) # price_pal 함수가 담긴다.
print(var_1() ) # 함수가 담겨 return을 나타낸다.
var_2 = price_cal()
print(var_2) # 함수가 담겨  return의 5000이 변수에 담긴다.


def stock_names():
    return "삼성", "LG"
var_3 = stock_names
print(var_3)
var_4 = var_3()
print(var_4) #('삼성', 'LG') 튜플형태로 나옴

var_5, var_6 = var_3()
print("%s %s" % (var_5, var_6)) #튜플 형태가 풀려서  나온다. # 삼성 LG


#현재 코스피의 등락율을 찾고
# def kospi_fnc()라는 함수를 만들고
# 그 안에서 코스피의 등락율보다 높은 코스피의 종목 1(아무거나)개를 골라서
# 딕셔너리 형태로 만들고 {종목명: {현재가:데이터, 등락율:데이터}}
# 그 중에서 현재가가 5만원 이상인 종목의 종목명과, 현재가, 등락율을
# return 해라.함수 안에서 사용하는 제어문(for과 if) 그리고 print로 출력

def kospi_fnc():
    kospi_number = 5.6
    ks = {"삼성전자": {"현재가": 78000, "등락율": 5.8},
               "LG": {"현재가": 138500, "등락율": 8.5},
               "카카오": {"현재가": 345500, "등락율": 3.5},
               "현대차": {"현재가": 694000, "등락율": 10.5}}

    for name in ks.keys():
        sd = ks[name] #{'현재가' : ...,'등락율'...}
        if 50000 <= sd["현재가"]:
            return name, sd["현재가"], sd["등락율"]

result = kospi_fnc()
print(result) # ('삼성전자', 78000, 5.8)

def price_fnc(current):
    print(current)
price_fnc(5000)

def price_fnc(high, low):
    print("고가: %s, 저가: %s" % (high, low))
price_fnc(5000,3000)

def price_fnc(high:int= 0, low:int=0, current:int=0, drate:float=None):
    print("%s" % high)
price_fnc(drate=0.3, high=2000, low= 1000, current=1500) # 순서대로쓰지않아도 데이터가 찾아간다.


def cal_stock(stock_name = None, limit_price = None):
    ks = {"삼성전자": {"현재가": 78000, "등락율": 5.8},
          "LG": {"현재가": 138500, "등락율": 8.5},
          "카카오": {"현재가": 345500, "등락율": 3.5},
          "현대차": {"현재가": 694000, "등락율": 10.5}
          }
    if ks[stock_name]["현재가"] > limit_price:
        return True
    else:
        return False
result = cal_stock(stock_name="LG", limit_price=50000)
print(result)