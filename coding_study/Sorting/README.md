## 정렬
-----
### ❓ 정렬이란?
- 데이터를 특정한 기준에 따라서 순서대로 나열
### ❓ 선택 정렬이란?
- 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복
- 시간 복잡도 : O(N**2)
### ❓ 삽입 정렬이란?
- 데이터를 앞에서부터 하나씩 확인하여 데이터를 적절한 위치에 삽입하는 방법
- 평균 시간 복잡도 : O(N**2), 최선의 경우(현재 리스트의 데이터가 거의 정렬되어 있는 상태) - O(N)
### ❓ 퀵 정렬이란?
- 기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식
- 대부분의 경우 가장 적합하며 충분히 빠르다.
- 평균 시간 복잡도 : 평균적으로 O(NlogN), 최악의 경우(이미 데이터가 정렬되어 있는 경우)
### ❓ 계수 정렬이란?
- 특정한 값을 가지는 데이터의 개수를 카운트하는 방법
- 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘
  - 특정한 조건 : 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만
- 평균 시간 복잡도 : O(N + K)
### 🔖 정리
|문제명|업로드|다시 풀기|참고|
|-----|----|----|----|
|[국영수](https://github.com/soocy0718/python/blob/main/coding_study/Sorting/%EC%9D%B4%EC%BD%94%ED%85%8C_23_%EA%B5%AD%EC%98%81%EC%88%98_0310.py)|⭕||[이것이 취업을 위한 코딩테스트다](https://github.com/ndb796/python-for-coding-test) |
|[안테나](https://github.com/soocy0718/python/blob/main/coding_study/Sorting/%EC%9D%B4%EC%BD%94%ED%85%8C_24_%EC%95%88%ED%85%8C%EB%82%98_0310.py)|⭕||[이것이 취업을 위한 코딩테스트다](https://github.com/ndb796/python-for-coding-test) |
|[실패율](https://github.com/soocy0718/python/blob/main/coding_study/Sorting/%EC%9D%B4%EC%BD%94%ED%85%8C_25_%EC%8B%A4%ED%8C%A8%EC%9C%A8_0310.py)|⭕||[이것이 취업을 위한 코딩테스트다](https://github.com/ndb796/python-for-coding-test) |
|[카드 정렬하기](https://github.com/soocy0718/python/blob/main/coding_study/Sorting/%EC%9D%B4%EC%BD%94%ED%85%8C_26_%EC%B9%B4%EB%93%9C%20%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0_0310.py)|⭕||[이것이 취업을 위한 코딩테스트다](https://github.com/ndb796/python-for-coding-test) |
|[수리공항승](https://github.com/soocy0718/python/blob/main/coding_study/Sorting/%EB%B0%B1%EC%A4%80_1449_%EC%88%98%EB%A6%AC%EA%B3%B5%ED%95%AD%EC%8A%B9_0310.py)|⭕||[백준](https://www.acmicpc.net/problem/1449) |
|[시리얼번호](https://github.com/soocy0718/python/blob/main/coding_study/Sorting/%EB%B0%B1%EC%A4%80_1431_%EC%8B%9C%EB%A6%AC%EC%96%BC%EB%B2%88%ED%98%B8_0310.py)|⭕||[백준](https://www.acmicpc.net/problem/1431) |
|[두수의합](https://github.com/soocy0718/python/blob/main/coding_study/Sorting/%EB%B0%B1%EC%A4%80_3273_%EB%91%90%EC%88%98%EC%9D%98%ED%95%A9_0310.py)|⭕||[백준](https://www.acmicpc.net/problem/3273) |
|[좌표압축](https://github.com/soocy0718/python/blob/main/coding_study/Sorting/%EB%B0%B1%EC%A4%80_18870_%EC%A2%8C%ED%91%9C%EC%95%95%EC%B6%95_0310.py)|⭕||[백준](https://www.acmicpc.net/problem/18870) |
|[신입사원](https://github.com/soocy0718/python/blob/main/coding_study/Sorting/%EB%B0%B1%EC%A4%80_1946_%EC%8B%A0%EC%9E%85%EC%82%AC%EC%9B%90_0310.py)|⭕||[백준](https://www.acmicpc.net/problem/1946) |