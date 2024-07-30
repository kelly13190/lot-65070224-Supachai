from urllib import response
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Depends, Response, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

# Import models
from database import SessionLocal, engine
import models
from . import models
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
router_v1 = APIRouter(prefix='/api/v1')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# https://fastapi.tiangolo.com/tutorial/sql-databases/#crud-utils

@router_v1.get('/books')
async def get_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()

@router_v1.get('/books/{book_id}') # คือการสร้างเส้นทางที่ใช้สำหรับการดึงข้อมูลหนังสือ
async def get_book(book_id: int, db: Session = Depends(get_db)):
    return db.query(models.Book).filter(models.Book.id == book_id).first() # คือการ query ข้อมูลจากฐานข้อมูลโดยใช้ id ของหนังสือ

@router_v1.post('/books') # คือการสร้างเส้นทางที่ใช้สำหรับการสร้างหนังสือ
async def create_book(book: dict, response: Response, db: Session = Depends(get_db)):
    # TODO: Add validation
    newbook = models.Book(title=book['title'], author=book['author'], year=book['year'], is_published=book['is_published'])
    db.add(newbook)
    db.commit()
    db.refresh(newbook)
    response.status_code = 201
    return newbook

# @router_v1.patch('/books/{book_id}')
# async def update_book(book_id: int, book: dict, db: Session = Depends(get_db)):
#     pass

# @router_v1.delete('/books/{book_id}')
# async def delete_book(book_id: int, db: Session = Depends(get_db)):
#     pass
@router_v1.get('/students')
async def get_students(db: Session = Depends(get_db)):
    # print(123)
    return {"kelly": 65070224}
    # return db.query(models.Student).all()

@router_v1.get('/students/{student_id}') # คือการสร้างเส้นทางที่ใช้สำหรับการดึงข้อมูลหนังสือ
async def get_student(student_id: int, db: Session = Depends(get_db)):
    return db.query(models.Student).filter(models.Student.student_id == student_id).first() # คือการ query ข้อมูลจากฐานข้อมูลโดยใช้ id ของหนังสือ

@router_v1.post('/students') # คือการสร้างเส้นทางที่ใช้สำหรับการสร้างหนังสือ
async def create_student(student: dict, response: Response, db: Session = Depends(get_db)):
    # TODO: Add validation
    newstudent = models.Student(student_id=student['student_id'], firstname=student['firstname'], lastname=student['lastname'], birth_day=student['birth_day'], age=student['age'], sex=student['sex'])
    db.add(newstudent)
    db.commit()
    db.refresh(newstudent)
    response.status_code = 201
    return newstudent

@router_v1.put('/students/{student_id}')
async def update_student(student_id: int, student: dict, response: Response, db: Session = Depends(get_db)):
    db_student = db.query(models.Student).filter(models.Student.student_id == student_id).first()
    if db_student:
        db_student.firstname = student['firstname']
        db_student.lastname = student['lastname']
        db_student.birth_day = student['birth_day']
        db_student.age = student['age']
        db_student.sex = student['sex']
        db.commit()
        db.refresh(db_student)
        return {
            'message': f'Student updated {student_id} susscessfully'
        }
    else:
        response.status_code = 404
        return {
            'message': f'Student {student_id} not found'
        }

@router_v1.delete('/students/{student_id}')
async def delete_student(student_id: int, response: Response, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.student_id == student_id).first()
    if student:
        db.delete(student)
        db.commit()
        return {
            'message': f'Student deleted {student_id} susscessfully'
        }
    else:
        response.status_code = 404
        return {
            'message': f'Student {student_id} not found'
        }
        
app.include_router(router_v1)



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
