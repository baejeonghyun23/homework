from fastapi import FastAPI, HTTPException, Depends, Request
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)  # SQLAlchemy 엔진 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Item(Base):
    __tablename__ = "home_work"
    home_work_id = Column(Integer, primary_key=True, index=True)
    home_work_value = Column(String(255), index=True)

Base.metadata.create_all(bind=engine)   # 테이블 DB 생성

app = FastAPI()

templates = Jinja2Templates(directory="app/templates") # html 파일 사용하게

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ItemCreate(BaseModel):  # BaseModel 상속받아 유효성 검사
    home_work_value: str  # 필드 문자타입으로 선언

@app.post("/add")
def add_item(item: ItemCreate, db: Session = Depends(get_db)): # 함수를 호출하여 데이터베이스 세션을 가져옴
    db_item = Item(home_work_value=item.home_work_value) 
    db.add(db_item) # 추가
    db.commit() # 저장
    db.refresh(db_item) # 새로고침
    return {"message": "성공적으로 추가 되었습니다!"}

@app.get("/get")
def get_item(db: Session = Depends(get_db)): # Depends를 사용하여 자동으로 의존성 해결
    item = db.query(Item).order_by(Item.home_work_id.desc()).first() # 가장 최근값 불러오기
    if item is None:
        raise HTTPException(status_code=404, detail="No items found")
    return {"home_work_value": item.home_work_value}

@app.get("/", response_class=HTMLResponse) # 화면 출력
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
