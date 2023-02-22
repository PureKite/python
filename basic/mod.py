# 모듈이란?
# 미리 만들어 놓은 .py 파일(함수, 변수, 클래스)
import mod1
print(mod1.add(1, 2))

from mod1 import add
print(add(1,2))

## import는 실행 파일과 같은 경로에 있어야 한다.
## 같은 경로가 아니라면?
import sys
sys.path.append('/경로/경로')

import mod1