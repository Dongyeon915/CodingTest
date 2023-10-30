if __name__ == '__main__':
    # 들어온 수를 오름차순으로 정렬하라
    # 수를 담을 배열을 생성
    my_list = [5,2,3,4,1]
    # 자리수를 바꾸게 되면 할당 값이 사라질수 있으므로 빈 변수를 선언
    temp = 0
    # my_list의 첫번째 인덱스의 값이 두번째를 비교해서 값이 큰것을 가장 오른쪽으로 정렬
    # 마지막자리수가 인덱스를 넘어가면 에러가 발생하므로 길이보다 1나작게해서 넘어가는걸 막는다
    for i in range(0, len(my_list)):
        print("끝")
        for j in range(0, len(my_list) - 1):
            print("시작")
            if my_list[i] > my_list[j] :
                temp = my_list[j]
                my_list[j] = my_list[i]
                my_list[i] = temp
    print(my_list)

