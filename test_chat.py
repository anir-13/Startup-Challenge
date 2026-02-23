from chat import Chat, create_chat
from models import ChatType
from database import SessionLocal
from models import User

db = SessionLocal()
# Add users if not exist
for uid, name in [(1, "Ani"), (2, "Bob"), (3, "Charlie")]:
    if not db.query(User).filter_by(id=uid).first():
        db.add(User(id=uid, name=name))
db.commit()

# --- Create 1-to-1 chat ---
chat1_id = create_chat(ChatType.ONE_TO_ONE, [1, 2])
chat1 = Chat(chat1_id)
chat1.record_message(1, "Hello Bob!")
chat1.record_message(2, "Hi Ani!")

# --- Create group chat ---
chat2_id = create_chat(ChatType.GROUP, [1, 2, 3])
chat2 = Chat(chat2_id)
chat2.record_message(3, "Hi everyone in group")

# --- Retrieve messages ---
print("Chat 1 Messages:")
for msg in chat1.get_messages():
    print(msg.sender_id, msg.content, msg.created_at)

print("\nChat 2 Messages:")
for msg in chat2.get_messages():
    print(msg.sender_id, msg.content, msg.created_at)
