from datetime import datetime
from pydantic import BaseModel, Field
from uuid import UUID

class ArticleDTO(BaseModel):
    art_seq : int
    title : str =  Field(..., min_length=3, max_length=50)
    content : str =  Field(..., min_length=3, max_length=50)
    create_at : datetime
    updated_at : datetime
    user_id: UUID

    class Config:
        orm_mode = True