def linear_search(data, target):
    for idx in range(len(data)):
        if data[idx] == target:
            return idx
    return None


if __name__ == '__main__':
    data = [i ** 2 for i in range(1, 11)]

    target = 9

    idx = linear_search(data, target)

    if idx == None:
        print(f'{target}이 존재하지 않습니다')
    else:
        print(f'찾는 데이터의 인덱스는 {idx}이고 데이터는 {data[idx]}입니다')