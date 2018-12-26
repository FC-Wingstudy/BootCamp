# threading 모듈은 멀티스레딩을 구현하는데 필요
import threading


# 스레드에서 실행할 함수
# thread_main() 함수는 네개의 스레드에서 실행할 함수
def thread_main(li, i):
    # range() 안의 값이
    # 스레드가 담당할 리스트의 인덱스 범위를 결정
    # for 문으로 인덱스 범위를 설정해 순회하면서 각 인덱스 요소에 2를 곱한다
    # offset 은 데이터 개수를 스레드 개수로 나눈 값
    for i in range(offset * i, offset * (i + 1)):
        # 요소에 2를 곱한다
        li[i] *= 2


# 리스트 요소개수
num_elem = 1000
num_thread = 4

# 오프셋 = 리스트 요수 개수 // 스레드 개수
# 스레드 함수에서 여난을 담당한 인덱스 범위를 구하는데 쓰인다
offset = num_elem // num_thread

li = [i+1 for i in range(num_elem)]

# 스레드를 담을 리스트
threads = []
for i in range(num_thread):
    # 스레드 객체를 생성
    # target은 실행할 스레드 함수
    # args는 전달한 인자 목록
    th = threading.Thread(target=thread_main, args=(li, i))
    threads.append(th)

for th in threads:
    # 스레드 실행 시작
    th.start()

for th in threads:
    # 스레드 실행 완료 대기
    th.join()

print(li)