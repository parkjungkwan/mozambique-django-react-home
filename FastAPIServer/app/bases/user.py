from abc import abstractmethod, ABCMeta
from typing import List
from app.schemas.user import UserDTO
from app.models.user import User
from sqlalchemy.orm import Session

class UserBase(metaclass=ABCMeta):

    @abstractmethod
    def add_user(self, request_user: UserDTO) -> str: pass

    @abstractmethod
    def login(self, request_user: UserDTO) -> str: pass

    @abstractmethod
    def update_user(self, request_user: UserDTO) -> str: pass

    @abstractmethod
    def delete_user(self, request_user: UserDTO) -> str: pass

    @abstractmethod
    def find_all_users(self, page: int) -> List[UserDTO]: pass

    @abstractmethod
    def find_users_by_job(self, request_user: UserDTO, page: int) -> List[UserDTO]: pass

    @abstractmethod
    def find_user_by_id(self, request_user: UserDTO) -> UserDTO: pass

    @abstractmethod
    def find_userid_by_email(self, request_user: UserDTO) -> str: pass