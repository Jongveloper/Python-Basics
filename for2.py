# for문 복습
fr_dict = {"사과":{"온라인" : 5000, "오프라인": 7000},
            "키위":{"온라인" : 7000, "오프라인": 9000},
            "포도":{"온라인": 6000, "오프라인": 8000},
            "수박":{"온라인": 11000, "오프라인": 13000},
            "딸기":{"온라인": 4000, "오프라인": 6000}
            }


# for, if
# 과일들 중 온라인 가격이 5000원 초과인 과일을 고르고
# 그 과일들 중에서 오프라인 가격 순위를 매겨서 순서대로 출력



rank_list = []
for fr_name in fr_dict.keys():
    online = fr_dict[fr_name]["온라인"]
    off = fr_dict[fr_name]["오프라인"]

    if online > 5000:
        ki = (fr_name, off)

        change_idx = None
        for idx, tup in enumerate(rank_list):
            if off > tup[1]:
                change_idx = idx
                break
        if change_idx is not None:
            rank_list.insert(change_idx, ki)
        else:
            rank_list.append(ki)

print(rank_list)


fr_dict = {"사과":{"온라인" : 5000, "오프라인": 7000},
            "키위":{"온라인" : 7000, "오프라인": 9000},
            "포도":{"온라인": 6000, "오프라인": 8000},
            "수박":{"온라인": 11000, "오프라인": 13000},
            "딸기":{"온라인": 4000, "오프라인": 6000}
            }

# ~~~~~ 조금 더 쉬운 문제..
# 리스트로 담는데 온라인 가격 높은 순으로 담자
# 담는 형태 자유

rank_list = [] # rank 리스트를 만들어줬다.
for fr_name in fr_dict.keys():
    on = fr_dict[fr_name]["온라인"]
    sam = (fr_name, on)

    change_idx = None
    for idx, tup in enumerate(rank_list):
        if on > tup[1]:
            change_idx = idx
            break

    if change_idx is not None:
        rank_list.insert(change_idx, sam)
    elif change_idx is None:
        rank_list.append(sam)

price_list = (5000, 2000, 1500, 200, 10000)
rank_list = []
for price in price_list:
    rank_list.append(price)

rank_list.sort()
print(rank_list)



#크기 순서대로 다른 리스트에 넣어라.

