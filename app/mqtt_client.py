# mqtt 클라이언트, 브로커 관련 파일

import paho.mqtt.client as mqtt
from fastapi import WebSocket
from sqlalchemy.orm import Session
import asyncio
from database import get_db
import models

BROKER = 'localhost'
PORT = 1883
TOPIC = 'test/topic'

client = mqtt.Client()
websockets = set()

# 비동기적으로 WebSocket 메시지 전송
async def send_to_websocket(ws, message):
    try:
        await ws.send_text(message)
    except Exception as e:
        print(f"WebSocket send error: {e}")

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    print(f"Received MQTT Message : {message}")

    # 데이터베이스에 저장
    db = next(get_db())  # 데이터베이스 세션 가져오기
    db_message = models.Message(content=message)  # Message 객체 생성
    db.add(db_message)  # 세션에 추가
    db.commit()  # 커밋하여 DB에 저장
    db.refresh(db_message)  # DB에서 새로고침하여 최신 데이터 가져오기
    print(f"Saved to DB: {db_message.content}")


def connect_mqtt():
    client.on_message = on_message
    client.connect(BROKER, PORT)
    client.subscribe(TOPIC)
    client.loop_start()
