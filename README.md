# 주소입니다.</br>
# http://localhost:8080/

# 실행 </br>
```
docker-compose up --build
```

# env
```
MYSQL_ROOT_PASSWORD=루트계정 비밀번호 
MYSQL_DATABASE= 생성할 테이블명
MYSQL_USER= 생설할 계정 이름
MYSQL_PASSWORD= 계정 비밀번호
DATABASE_URL=mysql+pymysql://계정이름:비밀번호@db/테이블명
```

# 참고한자료
https://fastapi.tiangolo.com/ko/deployment/docker/
