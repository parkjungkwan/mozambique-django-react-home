from fastapi import Depends
from abc import abstractmethod, ABC

from app.admin.security import verify_password
from app.bases.user import UserBase
from app.database import conn
from app.models.user import User
from app.schemas.user import UserDTO
import pymysql
from sqlalchemy.orm import Session
from app.database import get_db
pymysql.install_as_MySQLdb()
'''
Why can't an annotated variable be global?
https://stackoverflow.com/questions/67527942/why-cant-an-annotated-variable-be-global
SQLAlchemy difference between session.execute and session.query
https://www.reddit.com/r/learnpython/comments/r1v776/sqlalchemy_difference_between_sessionexecute_and/
'''


class UserCrud(UserBase, ABC):

    def __init__(self, db: Session):
        self.db: Session = db

    def add_user(self, request_user: UserDTO)->str:
        self.db.add(User(**request_user.dict()))
        self.db.commit()
        return "success"

    def login(self, request_user: UserDTO):
        target = self.find_user_by_id(request_user)
        verified = verify_password(plain_password = request_user.password, hashed_password = target.password)
        if verified:
            return target
        else:
            print(" 비밀번호 오류 ")
            return None

    def update_user(self, user: User):
        return None

    def delete_user(self, request_user: UserDTO):
        return self.db.query(User)

    def find_all_users(self, page:int):
        print(f" page number is {page}")
        return self.db.query(User).all()

    def find_users_by_job(self, search, page):
        return None

    def find_user_by_id(self, request_user: UserDTO):
        user = User(**request_user.dict())
        return self.db.query(User).filter(User.userid == user.userid).first()

    def find_userid_by_email(self, request_user: UserDTO) -> str:
        user = User(**request_user.dict())
        return_user = self.db.query(User).filter(User.email == user.email).first()
        if return_user is not None:
            return return_user.userid
        else:
            return ""

    """
    https://ebs-integrator.com/blog/django-orm-vs-sql-alchemy/
    # SQL Alchemy
    db.query(Student).filter(
        Student.register_id == db.query(Book.id).filter(
          Book.title.contains('english')
       ).subquery()
    )
    db.query(Student).filter(
        Student.id == db.query(StudentCourse.student_id).filter(
            StudentCourse.student_id == Student.id, StudentCourse.final_grade >= 10
        ).limit(1).subquery()
    )
    db.query(Student).options(
        joinedload(Student.student_course).options(
        joinedload(StudentCourse.courses))
    )
    https://www.freecodecamp.org/news/how-to-add-jwt-authentication-in-fastapi/
    https://lowelllll.github.io/til/2019/04/19/TIL-flask-sqlalchemy-orm/
    https://coderpad.io/blog/development/understanding-transactions-in-sqlalchemy/
    """