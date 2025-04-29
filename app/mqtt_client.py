# mqtt 클라이언트, 브로커 관련 파일

import paho.mqtt.client as mqtt
from fastapi import WebSocket
from sqlalchemy.orm import Session
import asyncio

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

def connect_mqtt():
    client.on_message = on_message
    client.connect(BROKER, PORT)
    client.subscribe(TOPIC)
    client.loop_start()
