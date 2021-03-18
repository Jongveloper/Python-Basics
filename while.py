while True:
    print("while 무한루프")

    break
print("while을 빠져나옴")

while True:
    print("while 무한루프") # while 무한루프

    continue
    print("continue 이후")

print("while을 빠져나옴")
# 컨티뉴는 실행 된다.

earning_rate = 20.2
while earning_rate < 30.5:
    print("계속 주시")
    earning_rate += 1 # earning_rate가 while이 한번씩 돌때마다 1씩 증가한다.
print("수익률이 30.5 이상이여서 매도함")

stock_dict = {}
tick_cnt = 0
while True:
    if tick_cnt > 5:
        print("이 종목을 주시할거다.")
        stock_dict["삼성"] = True

    if "삼성" in stock_dict.keys():
        print("매수? 매도?")
        break

    tick_cnt += 1
print("%s" % stock_dict)

stock_list = ["삼성", "LG", "카카오", "네이버", "대우"]
stock_dict = {}
while True:
    for stock_name in stock_list:
        if stock_name in stock_dict.keys():
            print("매도를 한다.")
            del stock_dict[stock_name]
        elif stock_name not in stock_dict.keys():
            print("매수를 한다.")
            stock_dict[stock_name] = "매수됨"

# 삼성은 매수/매도 싸이클을 3번만
# lg는 매수/매도 싸이클을 2번만
# 카카오는 매수/매도 싸이클을 5번만
# 네이버는 매수/매도를 안한다.
# 대우는 매수/매도 싸이클은 1번만
# 그리고 while문을 종료

stock_list = ["삼성", "LG", "카카오", "네이버", "대우"]
stock_dict = {}
s_cnt = 0
l_cnt = 0
k_cnt = 0
n_cnt = 0
d_cnt = 0
while True:
    for stock_name in stock_list:
        if stock_name == "삼성" and s_cnt != 3:
            print("삼성을 매수하였습니다.")
            print("삼성을 매도하였습니다.")
            s_cnt += 1
        elif stock_name == "LG" and l_cnt != 2:
            print("LG를 매수하였습니다.")
            print("LG를 매도하였습니다.")
            l_cnt += 1
        elif stock_name == "카카오" and k_cnt != 5:
            print("카카오를 매수하였습니다.")
            print("카카오를 매도하였습니다.")
            k_cnt += 1
        elif stock_name == "네이버" and n_cnt != 0:
            print("네이버를 매수하였습니다.")
            print("네이버를 매도하였습니다.")
            n_cnt += 1
        elif stock_name == "대우" and d_cnt != 1:
            print("대우를 매수하였습니다.")
            print("대우를 매도하였습니다.")
            d_cnt += 1
stock_list = ["삼성", "LG", "카카오", "네이버", "대우"]
stock_dict = {"삼성": {"매수여부": False, "매매제한": 3, "매수횟수": 0, "매도횟수": 0},
              "LG": {"매수여부": False, "매매제한": 2, "매수횟수": 0, "매도횟수": 0},
              "카카오": {"매수여부": False, "매매제한": 5, "매수횟수": 0, "매도횟수": 0},
              "네이버": {"매수여부": False, "매매제한": 0, "매수횟수": 0, "매도횟수": 0},
              "대우": {"매수여부": False, "매매제한": 1, "매수횟수": 0, "매도횟수": 0}
              }
while True:
    for stock_name in stock_list:
        unit_dict = stock_dict[stock_name]

        if unit_dict["매수여부"] is False:
            if unit_dict["매매제한"] > unit_dict["매수횟수"]:
                unit_dict["매수횟수"] = unit_dict["매수횟수"] + 1

                if stock_name in stock_list:
                    print("%s 매수 %s" % (stock_name, unit_dict["매수횟수"]), flush=True)
                    unit_dict["매수여부"] = True

        elif unit_dict["매수여부"] is True:
            if unit_dict["매매제한"] > unit_dict["매도횟수"]:
                unit_dict["매도횟수"] = unit_dict["매도횟수"] +1

                if stock_name in stock_list:
                    print("%s 매도 %s" % (stock_name, unit_dict["매도횟수"]), flush=True)
                    unit_dict["매수여부"] = False

stock_name = "삼성"
price = 67500
mesu_price = 0
kospi_unit = 100

while True:
    if mesu_price == 0:
        mesu_price = price
    else:
        price += kospi_unit
        drate = (price - mesu_price) / mesu_price * 100
        if drate >= 30.0:
            print("%s의 30%s부근 가격은 %s이다." % (stock_name,"%",price), flush=True)
            break
