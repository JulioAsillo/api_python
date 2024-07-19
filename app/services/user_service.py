from typing import List, Optional

from app.models.user import User
from app.repositories.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user: User) -> User:
        return self.user_repository.add_user(user)

    def get_user(self, user_id: int) -> Optional[User]:
        return self.user_repository.get_user(user_id)

    def list_users(self) -> List[User]:
        return self.user_repository.get_all_users()

