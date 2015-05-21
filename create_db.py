import sqlite3

connection = sqlite3.connect('mwo.db')
c = connection.cursor()
c.execute('CREATE TABLE BaseStats(Name TEXT, MC INT, Kills INT, Deaths INT, CBills INT, Exp INT, Win INT, Lose INT, [timestamp] timestamp)')
connection.commit()
