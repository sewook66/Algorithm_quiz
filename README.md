# Algorithm_quiz


### 1. 100개의 임의의 노드들로 구성되는 네트워크(그래프)를 생성하고, 노드 간에 존재하는 간선에는 5~30 사이의 정수를 비용으로 간주하여 배정한다. 이러한 그래프들의 연결된 모습(그림)을 출력하라. 2) 생성된 그래프의 최소비용신장트리를 그래프 상에 굵기를 달리하여 표시하고, 그 때의 비용을 구하시오. 3) 또한 생성된 그래프의 최대비용 신장트리를 그래프상에 나타내고, 그 때의 비용을 구하시오. <br>
- 100개의 노드를 생성하고 생성된 노드들 간의 잇는 랜덤 한 5~30사이의 간선 값을 가지는 간선 99개 생성 <br>
- 기본적으로 생성된 그래프의 연결된 모습을 시각화 된 그래프로 만들고 출력 <br>
- nx.minumum_spanning_tree(graph)로 빈 네트워크에 최소비용신장트리 그래프 생성, nx.get_edge_lables로 lables에 최소비용 간선 값을 저장, layout은 spring 형태 <br>
- 최소비용신장트리 그래프를 간선 넓이3의 시각화 된 그래프로 출력 <br>
- 최소비용신장트리와 같은 방식으로 최대비용신장트리 그래프 생성, 간선 값 저장, 기본 간선 넓이의 시각화 된 그래프 출력 <br>
- 최소비용신장트리에서 사용된 모든 간선 값을 for, if문을 사용해 WSum에 저장 후 최소비용신장트리 비용 출력 <br>
- 같은 방식으로 최대비용신장트리 비용을 출력 <br>
![image](https://user-images.githubusercontent.com/51785417/224268190-ff6cb2c4-6538-4e89-957b-a9a94a4ff1c4.png)
그래프의 연결된 모습 <br>
![image](https://user-images.githubusercontent.com/51785417/224268214-d063d44c-134a-41a3-b70d-7b44d1cbfea4.png)
최소비용신장트리 <br>
![image](https://user-images.githubusercontent.com/51785417/224268227-eea15d26-1ffc-44b4-990e-2f3a626a3418.png)
최대비용신장트리 <br>

최소비용신장트리 비용 : 1084 <br>
최대비용신장트리 비용 : 2197 <br><br><br>

### 2. m x m 크기의 공간에 n(n<m)개의 도시가 무작위로 위치 하고 있다. 코로나 바이러스를 퇴치하기 위해 어떤 의료진이 하루 백신 주사를 놓을 수 있는 범위가 지름 r(=2*m1/2)인 원에 해당한다고 한다. 다음 각 물음에 답하시오. 단, 각 도시의 좌표(x,y)값은 서로 다르다(0<=x,y<=m-1). 1) 모든 도시에 백신 주사를 놓기 위해 며칠이 소요되는 지를 구하는 알고리즘을 설계하라. 2) m=100, n=80, r=20일 경우에 대해 설계한 알고리즘을 구현하여 최소 소요되는 일(날) 수를 구하고, 이들이 백신주사를 놓은 도시를 표시하는 그래픽을 나타내어라. <br>
<img width="471" alt="image" src="https://user-images.githubusercontent.com/51785417/224273350-ad89ff0b-2be6-4a05-bc7c-65b5b2e1e96d.png">
최소 소요되는 일(날) 수 :  32
