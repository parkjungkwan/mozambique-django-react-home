from pydantic import BaseConfig
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy_utils import UUIDType

class Article(Base):

    __tablename__ = 'articles'

    artseq = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100))
    content = Column(String(1000))
    userid = Column(String(20), ForeignKey('users.userid'), nullable=True)

    user = relationship('User', back_populates='articles')


    class Config:
        BaseConfig.arbitrary_types_allowed = True
        allow_population_by_field_name = True

    def __str__(self):
        return f'글쓴이: {self.userid} ' \
               f'글번호: {self.artseq} ' \
               f'제목: {self.title} ' \
               f'내용: {self.content} ' \
               f'작성일: {self.created} ' \
               f'수정일: {self.modified}'