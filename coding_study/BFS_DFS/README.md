## BFS/DFS
-----
### ❓ BFS란?
- 너비 우선 탐색, 가까운 노드부터 탐색하는 알고리즘, 동작 원리 : 큐, 구현 방법 : 큐 자료구조 이용
### ❓ DFS란?
- 깊이 우선 탐색, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘, 동작 원리 : 스택, 구현 방법 : 재귀 함수 이용
### ❓ 그래프란?
- 노드(정점)와 간선으로 표현
- 인접 행렬 : 2차원 배열로 그래프의 연결 관계를 표현하는 방식
  - 모든 관계를 저장하기 때문에 메모리가 불필요하게 낭비
- 인접 리스트 : 리스트로 그래프의 연결 관계를 표현하는 방식
  - 연결된 정보만을 저장하기 때문에 메모리 효율적
  - 인접 행렬 방식에 비해 특정한 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도가 느림
    - 연결된 데이터를 하나씩 확인해야하기 때문
### 🔖 정리
|문제명|업로드|다시 풀기|참고|
|-----|----|----|----|
|[특정 거리의 도시 찾기](https://github.com/soocy0718/python/tree/main/coding_study/BFS_DFS/%EC%9D%B4%EC%BD%94%ED%85%8C_15_%EC%BD%94%EB%93%9C%20%EC%84%A4%EB%AA%85)|⭕||[이것이 취업을 위한 코딩테스트다](https://github.com/ndb796/python-for-coding-test)|
|[연구소](https://github.com/soocy0718/python/blob/main/coding_study/BFS_DFS/%EC%9D%B4%EC%BD%94%ED%85%8C_16_%EC%97%B0%EA%B5%AC%EC%86%8C_0308.py)|⭕||[이것이 취업을 위한 코딩테스트다](https://github.com/ndb796/python-for-coding-test)|
|[경쟁적 전염](https://github.com/soocy0718/python/blob/main/coding_study/BFS_DFS/%EC%9D%B4%EC%BD%94%ED%85%8C_17_%EA%B2%BD%EC%9F%81%EC%A0%81%20%EC%A0%84%EC%97%BC_0308.py)|⭕||[이것이 취업을 위한 코딩테스트다](https://github.com/ndb796/python-for-coding-test)|
|[괄호 변환](https://github.com/soocy0718/python/blob/main/coding_study/BFS_DFS/%EC%9D%B4%EC%BD%94%ED%85%8C_18_%EA%B4%84%ED%98%B8%20%EB%B3%80%ED%99%98_0308.py)|⭕||[이것이 취업을 위한 코딩테스트다](https://github.com/ndb796/python-for-coding-test)|
|[연산자 끼워 넣기](https://github.com/soocy0718/python/blob/main/coding_study/BFS_DFS/%EC%9D%B4%EC%BD%94%ED%85%8C_19_%EC%97%B0%EC%82%B0%EC%9E%90%20%EB%81%BC%EC%9B%8C%20%EB%84%A3%EA%B8%B0_0308.py)|⭕||[이것이 취업을 위한 코딩테스트다](https://github.com/ndb796/python-for-coding-test)|
|[인구 이동](https://github.com/soocy0718/python/blob/main/coding_study/BFS_DFS/%EC%9D%B4%EC%BD%94%ED%85%8C_21_%EC%9D%B8%EA%B5%AC%20%EC%9D%B4%EB%8F%99_0308.py)|⭕||[이것이 취업을 위한 코딩테스트다](https://github.com/ndb796/python-for-coding-test)|
|[바이러스](https://github.com/soocy0718/python/blob/main/coding_study/BFS_DFS/%EB%B0%B1%EC%A4%80_2606_%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4_0308.py)|⭕||[백준](https://www.acmicpc.net/problem/2606) |
|[트리의 부모 찾기](https://github.com/soocy0718/python/blob/main/coding_study/BFS_DFS/%EB%B0%B1%EC%A4%80_11725_%ED%8A%B8%EB%A6%AC%EC%9D%98%20%EB%B6%80%EB%AA%A8%20%EC%B0%BE%EA%B8%B0_0308.py)|⭕||[백준](https://www.acmicpc.net/problem/11725) |
|[미로탐색](https://github.com/soocy0718/python/blob/main/coding_study/BFS_DFS/%EB%B0%B1%EC%A4%80_2178_%ED%9A%A8%EC%9C%A8%EC%A0%81%EC%9D%B8%20%ED%95%B4%ED%82%B9_0308.py)|⭕||[백준](https://www.acmicpc.net/problem/2178) |
|[DFS와 BFS](https://github.com/soocy0718/python/blob/main/coding_study/BFS_DFS/%EB%B0%B1%EC%A4%80__1260_DFS%EC%99%80%20BFS_0308.py)|⭕||[백준](https://www.acmicpc.net/problem/1260) |
|[미로탐색]()|||[백준](https://www.acmicpc.net/problem/2178) |
|[DFS와 BFS](https://github.com/soocy0718/python/blob/main/coding_study/BFS_DFS/%EB%B0%B1%EC%A4%80__1260_DFS%EC%99%80%20BFS_0308.py)|⭕||[백준](https://www.acmicpc.net/problem/1260) |
|[봄버맨](https://github.com/soocy0718/python/tree/main/coding_study/BFS_DFS/%EB%B0%B1%EC%A4%80_16918_%EC%BD%94%EB%93%9C%20%EC%84%A4%EB%AA%85)|⭕||[백준](https://www.acmicpc.net/problem/16918) |