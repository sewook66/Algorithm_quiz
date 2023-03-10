import matplotlib.pyplot as plt
import networkx as nx
import math
import random

graph = nx.Graph()
mapX = 100
mapY = 100
nodeN = 80


for i in range(nodeN):  # 노드생성
    graph.add_nodes_from(([i]))
pos = []
# x,y 좌표를 랜덤한 값으로 생성
pos = []
for i in range(nodeN):
    while True:
        v = (random.randrange(0, mapX), random.randrange(0, mapY))
        if v not in pos:
            break
    pos.append(v)

# 노드 간선 연결
for i in range(nodeN):
    for k in range(i + 1, nodeN):
        if math.sqrt((pos[i][0] - pos[k][0]) ** 2 + (pos[i][1] - pos[k][1]) ** 2) <= 10 :
            # 두 점 (x1,y1)과 (x2,y2)와 거리는 ((x1-x2)2 + (y1-y2)2)1/2 이며
            # 치료의 최대 반경인 값 20으로 지정( 도시로부터 반경은 반지름 10)
            graph.add_edge(i, k)  # 서로 유효 범위내에 있는 노드끼리 간선 연결)

removed = [False] * nodeN
count = [0] * nodeN
temp = 0
NodeVisitlist = []  # 초기화
NodeVisitCount = 0;

# setCover 알고리즘
while True:  # 무한 반복
    for x in range(nodeN):  # 모든 노드 접근
        count[x] = 0  # 카운터 초기화
        if not removed[x]:  # 자신의 removed값이 False이면
            count[x] += 1  # 자신은 포함이안되어 있기 때문에 카운트 1을 추가
        for cn in graph.neighbors(x):  # 연결되어있는 노드를 찾는다
            if not removed[cn]:  # 노드 x의 연결된 노드값이 removed 값이 False 이면(다른 노드에 간섭이 안되어있으면)
                count[x] += 1  # 카운트 1 추가
    # 위에 알고리즘에서 나온 값을 가지고 가장 많은 간선을 가지고 있는 노드를 찾는다.(카운트가 가장 많은값)
    # 가장 많은 노드의 간선(폭탄)을 구하는 부분
    for i in range(nodeN):
        if count[i] > count[temp]:  # 최대값for문
            temp = i  # temp=최대 연결되어있는 노드
    removed[temp] = True  # 간선이 가장 많은 노드 자신의 removed = True 변경
    for cn in graph.neighbors(temp):  # 최대 연결되어있는 노드의 연결된 노드들
        removed[cn] = True  # temp 노드 각각 간선노드를 Ture 변경(범위안에 포함됨)
    NodeVisitlist.append(temp)  # 가장 많이 커버하는 노드를 찾아 삽입(폭탄노드 생성)
    NodeVisitCount += 1  # 최대 도시 방문량
    if False not in removed:  # removed 에 False 가없으면 종료 (모든 노드가 방문노드 범위에 들어감) U != NULL 부분
        break

print("최소 소요되는 일(날) 수 : ", NodeVisitCount)  # 최소 방문 도시 출력

plt.figure(figsize=(8, 8))  # 캔버스 크기

# 전체 노드 그리기
nx.draw_networkx_nodes(graph, pos=pos, node_color='blue', node_size=30)
# 간선 그리기
nx.draw_networkx_edges(graph, pos=pos)
nx.draw_networkx_nodes(graph, pos = pos, node_color = '#FF0000', nodelist=NodeVisitlist,node_size=6500,alpha= 0.3)
plt.show()
