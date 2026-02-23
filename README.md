# Task Description:
Use Python and SQLAlchemy to implement a backend to support a one-to-one chat or a group chat with SQLite as the database.

# Technical Requirements:

1. Create the necessary data tables using SQLAlchemy. DDL scripts are not acceptable.

2. There will be Chat class, once instantiated, it can
a)record messages sent by users.
Assume a function signature such as "record_message(user_id: int, message: str,.....)"
Add other parameters as you see fit.
b)retrieve all messages from a chat in an ascending order (the latest message at the end of the list)
c)retrieve all chats a user has been in
d) retrieve chats by user and by chat type (there are two of them mentioned in the description)

3. Provide a requirements.txt file that will include all necessary packages needed to run your code.
4. Tester can then install the packages, import your code, instantiate the service, and conduct actions as listed in the 2nd point.
# Design Details:
Make minimum assumptions on what attributes/columns the User table should include. This task focus on the chat service.
Make reasonable design decisions on other supporting tables so that the service will function as detailed in the technical requirements.

# Deliverables:
Below is an example of the folder structure that should be submitted:

```

/Deliverable
|-- chat.py (where all functions related to 2nd point of the technical requirement should be defined here)
|-- requirements.txt
|-- support1.py (you may name these support files as appropriate)
|-- support2.py
|-- ...additional support files

```
