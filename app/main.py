# FastAPI 실행하는 파일

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from .database import engine
from . import mqtt_client
from . import models

app = FastAPI()

# FastAPI 애플리케이션이 시작될 때 MQTT 클라이언트 연결
@app.on_event("startup")
async def startup_event():
    # mqtt 클라이언트 연결
    mqtt_client.connect_mqtt()
    
    # db 연결
    models.Base.metadata.create_all(bind=engine)

# 루트 경로를 정의하여 404 오류 방지
@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI MQTT WebSocket server!"}

# 웹소켓 엔드포인트
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    mqtt_client.websockets.add(websocket)
    try:
        while True:

            message = await websocket.receive_text()
            
            print(f"[WebSocket에서 받은 메시지] {message}") # 메세지 백엔드 로그로 출력

            # MQTT 브로커에 발행
            mqtt_client.client.publish(mqtt_client.TOPIC, message)
    
    except WebSocketDisconnect:
        mqtt_client.websockets.remove(websocket)
