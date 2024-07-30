from sqlalchemy import create_engine # คือการ import ฟังก์ชัน create_engine จาก sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = os.environ.get('postgresql://default:0HWEDMVF9ILu@ep-sparkling-feather-a101nzh9.ap-southeast-1.aws.neon.tech:5432/verceldb?sslmode=require', 'sqlite:///./sql.db') # คือการกำหนดค่าตัวแปร SQLALCHEMY_DATABASE_URL โดยใช้ฟังก์ชัน os.environ.get โดยถ้าไม่มีการกำหนดค่า DATABASE_URL จะใช้ค่า 'sqlite:///./sql.db' แทน

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} if 'sqlite' in SQLALCHEMY_DATABASE_URL else {} # คือการสร้าง engine โดยใช้ฟังก์ชัน create_engine โดยใช้ตัวแปร SQLALCHEMY_DATABASE_URL และใช้ connect_args ในกรณีที่เป็น sqlite จะใช้ค่า {"check_same_thread": False} แทน
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# commit

Base = declarative_base()
