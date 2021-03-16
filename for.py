# for
fr_list = ["딸기", "수박", "사과", "포도"] # index [0,1,2,3]
for name in fr_list:  #in을 기준으로 순서대로 list가 반환된다.
    print(name) # 일자로 딸기,수박,사과,포도

fr_list = ["딸기", "수박", "사과", "포도"]
for name in fr_list:
    if name == "딸기":
        print(name) # 딸기
    elif name != "수박":
        print("수박 제외하고 %s" % name) # 딸기  수박 제외하고 사과  수박제외하고 포도
# 딸기는 if문에 있었기때문에 딸기가 출력되고 elif에 있던 사과와 포도는 출력했을때 앞에 수박 제외하고가 붙는다.

fr_list = ["딸기", "수박", "사과", "포도"]
for name in fr_list:
    if name == "딸기": # if조건에 부합하는 name == "딸기" <- 딸기가 조건에 부합했고 print가 나온다.
        print("%s를 구입하였습니다." % name) # 딸기를 구입하였습니다.
        break # for문을 정지시켜준다.
    print("남은과일들 : %s" % name) #break가 걸려 출력되지 않는다.
print("break 밖으로 나옴")


fr_list = ["딸기", "수박", "사과", "포도"]
for name in fr_list:
    if name != "수박":
        continue # break는 성립이 되면 멈추지만 continue는 성립이 되면 해당부분을 넘어간다.
        #따라서 수박을 제외한 나머지는 출력이되지않고 수박만 출력되는걸 볼 수 있다.
    print("%s" % name)

fr_list = ["딸기", "수박", "사과", "포도"]
for soldout in fr_list:
    if soldout == "수박":
        continue
    elif soldout == "사과":
        continue

    print("남은 과일들 : %s " % soldout)
#     남은과일들 : 딸기
#     남은과일들 : 포도
# 이렇게 출력되는 이유는 위에 설명과 동일하다.
# 딸기 == 수박과 같지않기때문에 elif인 딸기 == 사과로 넘어간다. 하지만 이조건도 맞지않기때문에
# 남은 과일들 : 딸기 그리고 딸기와 같은이유로 남은 과일들 : 포도가 출력된다.

fr_list = ["딸기", "수박", "사과", "포도"]
for name in fr_list:
    print("컨티뉴 실행 전 %s" % name)
    continue
    print("컨티뉴 실행 후 %s" % name)
# 컨티뉴 실행 전 fr_list들이 나온다.

fr_list = ["딸기", "수박", "사과", "포도"]
for name in fr_list:
    print("컨티뉴 실행 전 %s" % name)
    break
    print("컨티뉴 실행 후 %s" % name)
# 컨티뉴 실행 전 딸기만 출력된다.

fr_list = ["딸기", "수박", "사과", "포도"]
for name in fr_list:
    if name == "딸기":
        print("name이 딸기와 같다.")
        continue
    print("name: %s이 딸기와 같지 않다." % name)
#name이 딸기와 같다.
# name: 수박이 딸기와 같지 않다.
# name: 사과이 딸기와 같지 않다.
# name: 포도이 딸기와 같지 않다.

fr_list = ["딸기", "수박", "사과", "포도"]
for name in fr_list:
    if name == "딸기":
        print("name이 딸기와 같다.")
        break
    print("name: %s이 딸기와 같지 않다." % name)
#name이 딸기와 같다.

fr_list = ["딸기", "수박", "사과", "포도"]
for name in enumerate(fr_list):
    print(name) # 튜플형태로 index가 같이나온다.

fr_list = ["딸기", "수박", "사과", "포도"]
for idx, name in enumerate(fr_list):  #enumerate의 단점 : 속도가 느리다.
    print("%s %s" % (idx, name))

fr_list = ["딸기", "수박", "사과", "포도"]
cnt = 0
for name in fr_list:
    print("enumerate 안 쓰고 %s %s" % (cnt, name))
    cnt += 1  # cnt = cnt + 1

fr_list = ["딸기", "수박", "사과", "포도"]
cnt = 0
for name in fr_list:
    cnt += 1
    if cnt == 2:
        print("그만돌림")
        break
fr_list = ["딸기", "수박", "사과", "포도"]
length_fr = len(fr_list)
print(length_fr) # 4
ran_fr = range(length_fr) # range의 여기서 역할 : [0,1,2,3]을 만들어주는 것으로 보면된다.
print(ran_fr) # range(0, 4)
for i in ran_fr:
    print(i) #일렬로 0, 1, 2, 3
fr_list = ["딸기", "수박", "사과", "포도"]
for i in range(len(fr_list)):
    print("한번에 %s" % i) #위의 예제를 한번에..!

# 문제 : 딸기를 처음엔 1개, 2개, 3개, 4개, ... 9개

for i in range(1, 10):
    print("딸기 * %s개 구매하였습니다." % i)

fr_list = ["딸기", "수박", "사과", "포도"]
for name in fr_list:
    if name == "딸기":
        for i in range(1, 10):
            print("%s * %s개 구매하였습니다." % (name, i))

# 구구단 양식 출력
for i in range(1, 10):
    for x in range(1, 10):
        print("구구단 %s * %s" % (i, x))
