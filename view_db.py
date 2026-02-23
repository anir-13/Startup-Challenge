#only for reference. not part of the main code
from sqlalchemy import text
from database import engine

with engine.connect() as conn:
    print("Users:")
    print(conn.execute(text("SELECT * FROM users")).fetchall())

    print("\nChats:")
    print(conn.execute(text("SELECT * FROM chats")).fetchall())

    print("\nChat Members:")
    print(conn.execute(text("SELECT * FROM chat_users")).fetchall())

    print("\nMessages:")
    print(conn.execute(text("SELECT * FROM messages")).fetchall())
