example = 6 > 3
print(example) # True

example = 7 is 7
print(example) # True

example = 7 == 7
print(example) # True

example = 3 == 4
print(example) # False

example = 5 is not 5 #같지 않은 것
print(example) # False

example = 5 != 5  # 같지 않은 것
print(example) # False (같다는 의미)

example = 5 > 3
example = 5 >= 5
print(example) # True

example = 5 < 3
print(example) # False

example = 5 <= 3
print(example) # False

# example = "5000" <= 4000
# print(example) #TypeError: '<=' not supported between instances of 'str' and 'int' (스트링과 인트를 비교할 수 없음)

apple = "사과"
check = "사과"
result = apple == check
print(result) # True

example1 = "딸기"
example2 = "수박"
example3 = "수박"
result = example1 == example2 and example2 == example3
print(result) # False  (and는 두개 다 맞아야하기 때문에 False 가 나왔다.)

result = example1 == example2 or example2 == example3
print(result) # True (or은 둘 중 하나만 맞으면 되기때문에 True가 나왔다.)

example1 = 5000
example2 = 3000
example3 = 2000
example4 = 1000
example5 = 500
price = 3500
result = (price > example1 or price > example2) and price > example3
#괄호 안이 or 이기때문에 둘 중 하나가맞으면되고 and 기준으로 뒤에가 True인지 봐야한다.
print(result) # True  괄호 안에 example2가 3000이기 때문에 price보다 작기때문에
# and 기준으로 뒤에가 맞으면 True인데 example3가 2000이므로 price보다 작기때문에 True이다.

result = (price == example1 or price > example2)\
and price > example3\
and (price < example4 or price > example5)
print("결과 %s" % result) # 결과 True
# (3500 == 5000 or 3500 > 3000 True)
# (and 3500 > 2000 True)
# (and 3500 < 1000 or 3500 > 500 True)이기때문에 True이다


result = 5000 > 3000
if result: #if문은 옆에 있는 변수가 True이냐 False이냐 물어본다
    print("통과") # 통과

result = 5000 < 3000
if result:
    print("통과2")

print("그냥넘김") # 그냥넘김
# 5000 > 3000 이기때문에 Falsue가 나왔고 그래서 라인이같은 print("그냥넘김") 이 출력되었다.

if 5000 > 3000:
    print("통과3") # 통과3

if 5000 > 3000 and 5000 == 3000:
    print("통과4") # 실행되지 않는다 if조건에 맞지 않기때문이다.

elif 3000 == 2000:
    print("통과5") # 통과5
#elif = else if (if가 통과되지 않으면 다른 if문을 보는 것이다.)

else:
    print("통과6") # 통과6
# if와 elif가 모두 조건에 맞지 않을 때 쓰인다.


fr = {"사과": 5000, "수박": 3000, "딸기": 7000, "망고": 12000, "포도": 2500}

if fr["사과"] < 6000:
    print("사과를 구매하였습니다.")

if fr["수박"] > 6000:
    print("수박을 구매하였습니다.")

if fr["딸기"] < 6000:
    print("딸기를 구매하였습니다.")

if fr["망고"] < 6000:
    print("망고를 구매하였습니다.")

if fr["포도"] < 6000:
    print("포도를 구매하였습니다.")