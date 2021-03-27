import threading
import time


# def thread_fnc1(종목, 가격):
#     while True:
#         time.sleep(1)
#         print("종목: %s, 가격: %s" % (종목, 가격))
#     print("쓰레드 동작")
#
# print("프로그램 실행")
#
#
# th = threading.threading.Thread(target=thread_fnc1, args=("삼성", 5000))
# # threading.Thread(target=thread_fnc1, args=("삼성", 5000)).start() # thread_fnc1은 괄호가 없어야한다. 함수 메모리만 던져주는 것이다.
# th.daemon = True # <- daemon이 True일 때 메인쓰레드가 종료되면 메인쓰레드에 딸려있던 서브 쓰레드가 강제종료된다.
# th.start()
#
# while True:
#     time.sleep(1)
#     print("while문 이후 실행")

# class Main():
#     def __init__(self):
#         print("메인 동작")
#
#
#         sub = SubMain()
#         th = threading.Thread(target=sub.thread_fnc, args=("삼성", 5000))
#         th.start()
#
#         th2 = threading.Timer(5, sub.thread_fnc_timer)
#         th2.start()
#
# class SubMain():
#     def __init__(self):
#         print("서브메인 동작")
#
#     def thread_fnc(self, 종목명, 가격):
#         while True:
#             time.sleep(1)
#             print("종목명: %s, 가격: %s" % (종목명, 가격))
#
#     def thread_fnc_timer(self):
#         print("쓰레드 타이머 실행")
#
#         th2 = threading.Timer(5, self.thread_fnc_timer)
#         th2.start()
#
# if __name__ == "__main__":
#     Main()

class Main():
    def __init__(self):
        print("메인 동작")

        self.종목 = "삼성"
        self.가격 = 5000
        print(dir(self))

        sub = SubMain()
        th = threading.Thread(target=sub.thread_fnc, args=(self,))
        th.start()

        sub.thread_stop = True

class SubMain():
    def __init__(self):
        print("서브메인 동작")
        self.thread_stop = False

    def thread_fnc(self, main의self:Main):
        while self.thread_stop is False: # 쓰레드를 종료시킬때는 처리중인 것을 그만 처리하게 만들면 된다.
            print("종목명: %s, 가격: %s" % (main의self.종목, main의self.가격))

    def thread_fnc_timer(self):
        print("쓰레드 타이머 실행")


if __name__ == "__main__":
    Main()