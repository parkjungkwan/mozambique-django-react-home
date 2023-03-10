from fastapi import APIRouter, Depends
import app.cruds.article as crud
from sqlalchemy.orm import Session
from app.schemas.article import ArticleDTO
from app.database import get_db

router = APIRouter()


@router.post("/")
async def write(article: ArticleDTO, db: Session = Depends(get_db)):
    article_dict = article.dict()
    note_id = await crud.post(article)

    response_object = {
        "id": note_id,
        "title": article.title,
        "description": article.content,
    }
    return response_object

@router.put("/{id}")
async def update(id:int,article: ArticleDTO, db: Session = Depends(get_db)):
    crud.update(art_seq=id,article=article,db=db)
    return {"data":"sucess"}

@router.delete("/{id}")
async def delete(id:int,article: ArticleDTO, db: Session = Depends(get_db)):
    crud.delte(art_seq=id,article=article,db=db)
    return {"data":"sucess"}

## Q
@router.get("/{page}")
async def get_articles(page, db: Session = Depends(get_db)):
    ls = crud.find_articles(page,db)
    return {"data": ls}

@router.get("/email/{id}")
async def get_article(id : int,db: Session = Depends(get_db)):
    crud.find_article(art_seq=id,db=db)
    return {"data": "sucess"}

@router.get("/job/{search}/{no}")
async def get_articles_by_title(search: str, page: int, db: Session = Depends(get_db)):
    crud.find_article_by_title(search,page,db)
    return {"data":"sucess"}