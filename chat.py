from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Chat as ChatModel, Message, ChatType, chat_users

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

class Chat:

    def __init__(self, chat_id: int):
        self.chat_id = chat_id
        self.db: Session = SessionLocal()

    def record_message(self, user_id: int, message: str):
        """
        Record a new message in this chat.
        """
        msg = Message(
            chat_id=self.chat_id,
            sender_id=user_id,
            content=message
        )
        self.db.add(msg)
        self.db.commit()
        return msg.id

    def get_messages(self):
        """
        Retrieve all messages in ascending order"""
        return (
            self.db.query(Message)
            .filter(Message.chat_id == self.chat_id)
            .order_by(Message.created_at)
            .all()
        )

# Helper function to create chats
def create_chat(chat_type: ChatType, user_ids: list[int]) -> int:
    db = SessionLocal()

    if chat_type == ChatType.ONE_TO_ONE and len(user_ids) != 2:
        raise ValueError("One-to-one chat must have exactly 2 users")

    if chat_type == ChatType.GROUP and len(user_ids) < 3:
        raise ValueError("Group chat must have at least 3 users")

    chat = ChatModel(chat_type=chat_type)
    db.add(chat)
    db.commit()
    db.refresh(chat)

    for uid in user_ids:
        db.execute(chat_users.insert().values(chat_id=chat.id, user_id=uid))
    db.commit()

    return chat.id
