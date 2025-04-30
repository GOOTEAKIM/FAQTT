import os
from dotenv import load_dotenv
import paho.mqtt.client as mqtt
from fastapi import WebSocket
from sqlalchemy.orm import Session
import asyncio
from database import get_db
import models

# .env 파일 로드
load_dotenv()

# MQTT 설정
BROKER = os.getenv("BROKER")
PORT = int(os.getenv("PORT"))
TOPIC = os.getenv("TOPIC")
KEEPALIVE = int(os.getenv("KEEPALIVE"))

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

# 연결 성공 처리
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("[MQTT 연결 성공]")
        client.subscribe(TOPIC, qos=1)
    else:
        print(f"[MQTT 연결 실패] 코드 {rc}")

# 연결 끊김 처리
def on_disconnect(client, userdata, rc):
    print(f"[MQTT 연결 종료] 코드: {rc}")
    if rc != 0:
        print("[MQTT 비정상 종료] 재연결 시도 중...")
        try:
            client.reconnect()
        except Exception as e:
            print(f"[재연결 실패] {e}")

# MQTT 연결 함수
def connect_mqtt():
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.connect(BROKER, PORT, KEEPALIVE)
    client.loop_start()
    return client

# MQTT 연결 종료 함수 (FastAPI shutdown 이벤트 등에서 호출 가능)
def disconnect_mqtt():
    client.loop_stop()
    client.disconnect()
