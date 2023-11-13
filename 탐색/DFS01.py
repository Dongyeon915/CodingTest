if __name__ == '__main__':

    node = 6
    edge = 5

    nodeList = [[],[2,5],[5,1],[4],[6,3],[1,2],[4]]
    visitList = [False] * (node + 1)

    def DFS(node):
        for i in nodeList[node]:
           # print(f"파라미터로 받은 노드의 안에는{nodeList[i]}")
            if not visitList[i]:
                visitList[i] = True
                DFS(i)

    count = 0

    # 방문 했는지 확인후 방문 하지않았다면 방문체크 후 해당 노드와 연결된 자료들을 체크
    for i in range(1, len(nodeList)):
     # 해당 i자리의 값들을 제대로 찍어 내는지 확인
     #print(f"노드{i}의 자리 값 {nodeList[i]}")
        if not visitList[i]:
            count += 1
            visitList[i] = True
            # 재귀 함수는 스택 구조 // 해당 배열의 자리의 값을 추가적으로 넣어줘야한다
            DFS(i)

    print(f"나눠진 노드 갯수는{count}")