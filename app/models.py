# db 테이블 연동하는 파일
from sqlalchemy import Column, Integer, String
from database import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String(255))  # VARCHAR(255)로 길이 지정

