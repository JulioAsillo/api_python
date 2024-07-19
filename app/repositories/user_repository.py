from typing import List, Optional
from app.models.user import User

class UserRepository:
    def __init__(self):
        self.users = []

    def add_user(self, user: User) -> User:
        self.users.append(user)
        return user

    def add_users(self, users: List[User]) -> List[User]:
        for user in users:
            self.users.append(user)
        return users

    def get_user(self, user_id: int) -> Optional[User]:
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def get_all_users(self) -> List[User]:
        return self.users