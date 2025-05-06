# 📖 포팅 메뉴얼

## 목차

1. [사용 도구](#1-사용-도구)
2. [개발 도구](#2-개발-도구)
3. [개발 환경](#3-개발-환경)
4. [포트 정보](#4-포트-정보)
5. [구동 방법](#5-구동-방법)
---
## 1. 사용 도구

- IDE : Visual Studio
- 형상 관리: github
- CI/CD: Docker, Docker-compose

---
## 2. 개발 도구

<!-- ### Frontend -->

### Backend

- 프레임워크 : FastAPI
- 라이브러리 : fastapi, paho-mqtt, uvicorn, pymysql, sqlalchemy

### Database

- MySQL

## 3. 개발 환경

<!-- ### Frontend

| name       | version |
|------------|---------|
| Node.js    | 20.15.0 |
| Vue3       | 18.3.1  | -->

### Backend

| name         | version |
|--------------|---------|
| Python       | 3.9      |
| FastAPI      | 0.115.12   |

### Database

| name   | version |
|--------|---------|
| MySQL  | 9.0.1   |

### Infra

| name     | version                |
|----------|------------------------|
| Docker   | 28.1.1                 |
| Ubuntu   | 24.04.1             |

<!-- ### EM

| name           | version      |
|----------------|--------------|
| Raspberry Pi   | 5            |
| python         | 3.9          |
| Arduino        | D1 R2 mini, UNO | -->

---
## 4. 포트 정보

### MySQL : 3305

### Backend : localhost

<!-- ### FrontEnd : 5173 -->

### MQTT broker

- MQTT : 1883
<!-- - WebSocket : 9001 -->
---
## 5. 구동 방법

<!-- ### FrontEnd

```bash
cd FE

npm install 

npm run dev
``` -->

### BackEnd

1. 가상환경 생성 (초기 한 번만)
    ```bash
    python -m venv venv
    ```
2. 가상환경 실행
    ```bash
    source venv/Scripts/activate
    ```
3. 라이브러리 설치 (초기한 번만) 
    ```bash
    pip install -r requirements.txt
    ```
5. FastAPI 서버 실행 (FastAPI_MQTT/app 에서 실행)
    ```bash
    uvicorn app.main:app --reload
    ```

- requirement.txt

  ```txt
  annotated-types==0.7.0
  anyio==4.9.0
  click==8.1.8
  colorama==0.4.6
  exceptiongroup==1.2.2
  fastapi==0.115.12
  greenlet==3.2.1
  h11==0.16.0
  idna==3.10
  paho-mqtt==2.1.0
  pydantic==2.11.3
  pydantic_core==2.33.1
  PyMySQL==1.1.1
  sniffio==1.3.1
  SQLAlchemy==2.0.40
  starlette==0.46.2
  typing-inspection==0.4.0
  typing_extensions==4.13.2
  uvicorn==0.34.2
  websockets==15.0.1
  ```

### Infra

#### Docker

1. WSL 환경에서 ubuntu 설치

2. Docker 설치

    ```bash

    sudo apt update
    sudo apt upgrade

    curl -fsSL https://get.docker.com -o dockerSetter.sh
    chmod 711 dockerSetter.sh
    ./dockerSetter.sh

    ```

3. Docker 버전 확인

    ```bash
    docker -v
    ```

4. 방화벽, 포트 허용

    ```bash
    sudo ufw status
    sudo ufw enable

    sudo ufw allow 22
    sudo ufw allow 443
    
    sudo shutdown -r now
    
    sudo ufw status
    
    sudo ufw allow 18080
    sudo ufw allow 50000
    sudo ufw allow 8081
    sudo ufw allow 3306
    ```

5. Docker Compose 설치

    ```bash
    sudo apt update
    sudo apt install docker-compose
    ```

6. Docker Compose 버전 확인

    ```bash
    docker-compose --version
    ```

#### eclipse mosquitto

1. eclipse mosquitto 설치

    ```bash
    docker run -it -p 1883:1883 eclipse-mosquitto
    ```

2. mosquitto.conf 생성

    ```bash
    mkdir -p ~/mosquitto/config
    touch ~/mosquitto/config/mosquitto.conf
    ```

3. mosquitto.conf 수정 (외부, 익명 접속 허용)

    ```bash
    listener 1883 0.0.0.0
    allow_anonymous true
    ```

4. 백그라운드에서 실행

    ```bash
    docker run -d -p 1883:1883 eclipse-mosquitto
    ```

5. docker-compose.yml 수정

    ```yml
    version: '3'

    services:
    mosquitto:
        image: eclipse-mosquitto
        container_name: mosquitto
        ports:
        - "1883:1883"    # 외부에서 접속할 수 있도록 1883 포트 열기
        volumes:
        - ~/mosquitto/config/mosquitto.conf:/mosquitto/config/mosquitto.conf   # 수정한 mosquitto.conf 파일을 연결
        restart: always   # 컨테이너가 종료되면 자동으로 다시 시작  

    ```

6. mosquitto-clients 패키지 설치

    ```bash
    sudo apt install mosquitto-clients
    ```

7. Docker Compose 실행

    ```bash
    docker-compose up -d
    ```

8. mqtt 메세지 발행

    ```bash
    mosquitto_pub -h localhost -p 1883 -t test/topic -m "hello world"
    ```

    | 옵션            | 설명                                                         |
    |-----------------|--------------------------------------------------------------|
    | `mosquitto_pub` | Mosquitto의 MQTT 퍼블리셔 명령어                              |
    | `-h localhost`  | 브로커 주소 (`localhost` → 내 PC에 있는 MQTT 브로커)         |
    | `-p 1883`       | 포트 번호 (기본 MQTT 포트)                                   |
    | `-t test/topic` | 토픽 이름 (`test/topic`에 메시지를 보냄)                    |
    | `-m "hello world"`| 보낼 메시지 내용                                             |

#### MySQL

1. MySQL 이미지 다운

    ```bash
    docker pull mysql
    ```

2. MySQL 컨테이너 생성, 실행 (패스워드 필수, 포트 주의)

    ```bash
    docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=<password> -p 3305:3306 -d mysql:latest
    ```

3. local MySQL workbench에서 db 생성

    - 사용자 : root
    - 포트 : 3305
    - password 필수

4. 컨테이너의 MySQL 접속

    ```bash
    docker exec -it mysql_container mysql -uroot -p    
    ```

5. 데이터 베이스 확인
    
    ```sql
    show databases;
    ```

6. 데이터 베이스 선택

    ```sql
    use my_db;
    ```

7. 이후 sql 문으로 데이터 조회 가능 
