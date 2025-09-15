# db 테이블 연동하는 파일
from sqlalchemy import Column, Integer, String
from .database import Base

class Message(Base):
    # 테이블 이름
    __tablename__ = "messages"

    # 테이블 구조
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String(255))  # VARCHAR(255)로 길이 지정

