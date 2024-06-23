# 
FROM python:3.12

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 패키지를 캐시하지 않도록 하여 이미지의 크기를 줄이고 최신버전으로 업데이트
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app

# --host 0.0.0.0: 모든 네트워크 인터페이스에서 접속을 허용 , Docker 컨테이너 외부에서 접속할 수 있도록 설정
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]