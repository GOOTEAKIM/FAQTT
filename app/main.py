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
            await websocket.receive_text()
    
    
    except WebSocketDisconnect:
        mqtt_client.websockets.remove(websocket)
