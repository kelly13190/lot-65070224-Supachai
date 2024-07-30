from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship

from database import Base

class Book(Base): # คือการสร้างคลาส Book โดยสืบทอดคุณสมบัติจาก Base
    __tablename__ = 'books' # คือการกำหนดชื่อตารางในฐานข้อมูล

    id = Column(Integer, primary_key=True, index=True) # คือการกำหนดฟิลด์ id โดยเป็น primary key
    title = Column(String, index=True)
    author = Column(String, index=True)
    year = Column(Integer, index=True)
    is_published = Column(Boolean, index=True)

class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    birth_day = Column(String, index=True)
    age = Column(Integer, index=True)
    sex = Column(String, index=True)
