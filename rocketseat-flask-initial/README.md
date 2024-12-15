# Flask Auth

This is a project to learn how to use Flask to create a simple authentication system.

## Setup

<!-- Here you show how to setup database, environment and all stuff you need -->
To setup the database you need to run the following commands:
```bash
# uses the flask shell to create the database
flask shell
db.create_all()
db.session.commit()
exit()
```
## Installation

```bash
pip install -r requirements.txt
```
## Usage

```bash
python app.py
```

## Notes

What does ORM mean?

Object relational mapping is a technique that abstracts SQL commands, such as connection, data insertion, table creation, etc. It abstracts these commands to facilitate even the exchange of databases, as it is database-independent.
However, it is dependent on the framework you are using, for example, SQLAlchemy, which is a widely used ORM with Flask and will be used in this specific example.

In this example, we will use Flask-SQLAlchemy with sqlite3, which is a file-based relational database, meaning it is not necessary to install a database on your computer, as sqlite3 creates a .db file that is the database.
