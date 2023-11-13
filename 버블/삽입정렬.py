if __name__ == '__main__':
    mylist = [2,1,4,3]
    # 최대값을 저장할 max선언
    max = 0

    for i in range(0,len(mylist)):
        # 가장 처음 인덱스 자리를 넣어둔다
        max = i
        #print("끝")
        # i부터 시작함으로써 찾아야하는 길이를 하나씩 줄인다
        for j in range(i,len(mylist)):
            # 큰수를 찾으면 해당 인덱스 자리로 i를 갱신
            #print("시작")
            if mylist[i] < mylist[j]:
                max = j
                temp = mylist[j]
                mylist[j] = mylist[i]
                mylist[i] = mylist[max]
        print(mylist)