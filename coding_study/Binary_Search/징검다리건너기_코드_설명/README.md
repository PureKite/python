#### 징검다리건너기

- [코드](https://github.com/soocy0718/python/blob/main/coding_study/Binary_Search/%EB%B0%B1%EC%A4%80_22871_%EC%A7%95%EA%B2%80%EB%8B%A4%EB%A6%AC%EA%B1%B4%EB%84%88%EA%B8%B0_0313.py)

- 아래 예제를 넣었을 때 DP 풀이를 하였을 때 돌아가는 과정
  - 틀렸다면 댓글을 남겨주세요
```
5
1 5 2 1 6
```
<html>
<img src="https://github.com/soocy0718/python/blob/main/coding_study/Binary_Search/%EC%A7%95%EA%B2%80%EB%8B%A4%EB%A6%AC%EA%B1%B4%EB%84%88%EA%B8%B0_%EC%BD%94%EB%93%9C_%EC%84%A4%EB%AA%85/%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%93%9C1.PNG", height="300", width="600">
<img src="https://github.com/soocy0718/python/blob/main/coding_study/Binary_Search/%EC%A7%95%EA%B2%80%EB%8B%A4%EB%A6%AC%EA%B1%B4%EB%84%88%EA%B8%B0_%EC%BD%94%EB%93%9C_%EC%84%A4%EB%AA%85/%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%93%9C2.PNG", height="300", width="600">
<img src="https://github.com/soocy0718/python/blob/main/coding_study/Binary_Search/%EC%A7%95%EA%B2%80%EB%8B%A4%EB%A6%AC%EA%B1%B4%EB%84%88%EA%B8%B0_%EC%BD%94%EB%93%9C_%EC%84%A4%EB%AA%85/%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%93%9C3.PNG", height="300", width="600">
<img src="https://github.com/soocy0718/python/blob/main/coding_study/Binary_Search/%EC%A7%95%EA%B2%80%EB%8B%A4%EB%A6%AC%EA%B1%B4%EB%84%88%EA%B8%B0_%EC%BD%94%EB%93%9C_%EC%84%A4%EB%AA%85/%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%93%9C4.PNG", height="300", width="600">
<img src="https://github.com/soocy0718/python/blob/main/coding_study/Binary_Search/%EC%A7%95%EA%B2%80%EB%8B%A4%EB%A6%AC%EA%B1%B4%EB%84%88%EA%B8%B0_%EC%BD%94%EB%93%9C_%EC%84%A4%EB%AA%85/%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%93%9C5.PNG", height="300", width="600">
<img src="https://github.com/soocy0718/python/blob/main/coding_study/Binary_Search/%EC%A7%95%EA%B2%80%EB%8B%A4%EB%A6%AC%EA%B1%B4%EB%84%88%EA%B8%B0_%EC%BD%94%EB%93%9C_%EC%84%A4%EB%AA%85/%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%93%9C6.PNG", height="300", width="600">
<img src="https://github.com/soocy0718/python/blob/main/coding_study/Binary_Search/%EC%A7%95%EA%B2%80%EB%8B%A4%EB%A6%AC%EA%B1%B4%EB%84%88%EA%B8%B0_%EC%BD%94%EB%93%9C_%EC%84%A4%EB%AA%85/%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%93%9C7.PNG", height="300", width="600">
<img src="https://github.com/soocy0718/python/blob/main/coding_study/Binary_Search/%EC%A7%95%EA%B2%80%EB%8B%A4%EB%A6%AC%EA%B1%B4%EB%84%88%EA%B8%B0_%EC%BD%94%EB%93%9C_%EC%84%A4%EB%AA%85/%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%93%9C8.PNG", height="300", width="600">
<img src="https://github.com/soocy0718/python/blob/main/coding_study/Binary_Search/%EC%A7%95%EA%B2%80%EB%8B%A4%EB%A6%AC%EA%B1%B4%EB%84%88%EA%B8%B0_%EC%BD%94%EB%93%9C_%EC%84%A4%EB%AA%85/%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%93%9C9.PNG", height="300", width="600">
<img src="https://github.com/soocy0718/python/blob/main/coding_study/Binary_Search/%EC%A7%95%EA%B2%80%EB%8B%A4%EB%A6%AC%EA%B1%B4%EB%84%88%EA%B8%B0_%EC%BD%94%EB%93%9C_%EC%84%A4%EB%AA%85/%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%93%9C10.PNG", height="300", width="600">
</html>
