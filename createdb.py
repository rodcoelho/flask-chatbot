import sqlite3

connection = sqlite3.connect('db/twitter.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE users(
pk INTEGER,
name VARCHAR(32),
PRIMARY KEY(pk))
;""")

cursor.execute("""
CREATE TABLE tweets(
pk INTEGER,
userID INTEGER,
tweet VARCHAR,
FOREIGN KEY(userID) REFERENCES users(pk),
PRIMARY KEY(pk))
;""")

connection.commit()
cursor.close()
