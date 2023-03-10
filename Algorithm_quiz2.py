import random
import matplotlib.pyplot as plt
import networkx as nx

graph = nx.Graph() # 빈 네트워크 생성

tmp = 1
max = 1

# 노드 100개 생성
for i in range(1, 100):
    graph.add_nodes_from([i])

# 간선 생성, 간선값은 5~30사이 랜덤으로 배정
for i in range(1, 100):
    graph.add_edges_from([(i, i + 1, {'weight': random.randrange(5, 30)})])
while max <= 99:
    r = random.randrange(1, 100)
    if (r != tmp):
        graph.add_edges_from([(tmp, r, {'weight': random.randrange(5, 30)})])
        tmp = tmp + 1
        max = max + 1

# 그래프의 연결된 모습 출력
labels = nx.get_edge_attributes(graph, 'weight')
pos = nx.spring_layout(graph)
nx.draw(graph, pos=pos, with_labels=True)
plt.show()

WSum = 0
sum = 0

# 최소스패닝트리
N = nx.minimum_spanning_tree(graph)
labels = nx.get_edge_attributes(N, 'weight') # lable 값은 weight
pos = nx.spring_layout(N) # spring layout

# 최소비용신장트리 출력
nx.draw(N, pos=pos, with_labels=True, width=3)
nx.draw_networkx_edge_labels(N, pos, edge_labels=labels)
plt.show()

# 최대스패닝트리
M = nx.maximum_spanning_tree(graph)
labels = nx.get_edge_attributes(M, 'weight') # lable 값은 weight
pos = nx.spring_layout(M)

# 최대비용신장트리 출력
nx.draw(M, pos=pos, with_labels=True, width=1)
nx.draw_networkx_edge_labels(M, pos, edge_labels=labels)
plt.show()

# 최소비용신장트리 비용 출력
for j, q in N.edges():
    WSum = int(nx.shortest_path_length(N, source=j, target=q, weight='weight'))
    if (5 <= WSum <= 30):
        sum = sum + WSum
print("최소비용신장트리 비용 :", sum)

# 최대비용신장트리 비용 출력
sum = 0
for j, q in M.edges():
    WSum = int(nx.shortest_path_length(M, source=j, target=q, weight='weight'))
    if (5 <= WSum <= 30):
        sum = sum + WSum
print("최대비용신장트리 비용 :", sum)
