# python

## 0. 가상환경 설정

1. 생성

```bash
python -m venv venv (랜덤폴더이름)
```

> 가상환경이란? - 용도에 따라 공간을 나눠주는 것 - jupyter lab을 가상 환경과 실제 환경 나누어 두 번 설치해준다.
>> ! 터미널 껐다 키면 가상 환경이 해지 되니 다시 활성화 필요

2. 활성화
```bash
# windows
source venv/Scripts/activate

#linux /macOS
source venv/bin/activate
```

3. 비활성화
```bash
deactivate
```

4. jupyter lab 설치
```bash
pip install jupyterlab
```

5. jupyter lab 실행
```bash
jupyterlab
```