from sqlalchemy import String, Float, Integer

from .base import *


class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(20), nullable=False)
    password: Mapped[str] = mapped_column(String(20), nullable=False)
    email_field: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    weight: Mapped[float] = mapped_column(Float, nullable=True)
    height: Mapped[int] = mapped_column(Integer, nullable=True)

    def __repr__(self):
        return f"User: {self.username}, email: {self.email_field}"
