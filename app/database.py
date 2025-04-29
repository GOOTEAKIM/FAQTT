# db 연결하는 파일
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# MySQL 연결 URL (pymysql 사용)

# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://username:password@localhost/db_name"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1157139@127.0.0.1:3305/mqtt_db"

# SQLAlchemy 엔진 생성
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# 세션 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# SQLAlchemy의 Base 클래스 정의
Base = declarative_base()

# 데이터베이스 연결을 위한 종속성 주입 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()