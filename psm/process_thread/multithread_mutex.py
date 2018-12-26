import threading

g_count=0


def thread_main():
    global g_count
    # Lock을 획득
    # 한 스레드가 획득하면
    # 획득을 시도한 나머지 스레드는 대기
    lock.acquire()
    for i in range(100000):
        g_count += 1
    #lock을 반환
    # 획득했던 스레드가 반환하면
    # 대기하던 스레드 중 하나가 획득
    lock.release()


# lock 객체 생성
lock = threading.Lock()
threads = []

for i in range(50):
    th = threading.Thread(target=thread_main)
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()

print('g_count : {:,}'.format(g_count))