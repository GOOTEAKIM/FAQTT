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
