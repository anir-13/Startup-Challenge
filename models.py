from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from database import Base

class ChatType(enum.Enum):
    ONE_TO_ONE = "one_to_one"
    GROUP = "group"

chat_users = Table(
    "chat_users",
    Base.metadata,
    Column("chat_id", ForeignKey("chats.id"), primary_key=True),
    Column("user_id", ForeignKey("users.id"), primary_key=True)
)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Chat(Base):
    __tablename__ = "chats"
    id = Column(Integer, primary_key=True)
    chat_type = Column(Enum(ChatType), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, ForeignKey("chats.id"))
    sender_id = Column(Integer, ForeignKey("users.id"))
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
