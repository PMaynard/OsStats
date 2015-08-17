#! /usr/bin/env python
import sqlite3
from dateutil import parser

conn = sqlite3.connect("folding-stats.db")
conn.text_factory = str
c = conn.cursor()

# Create table
# c.execute('''CREATE TABLE user
#              (name text, score text, wu text, team text, position text, import_date text)''')

# c.execute('''CREATE TABLE team
#              (team text, name text, score text, wu text, position text, import_date text)''')

# Read in data.
# data_user = "data/daily_user_summary.txt"
# data_team = "data/daily_team_summary.txt"
data_user = "data/diff_user.txt"
data_team = "data/diff_team.txt"

# Add date.

data = [line.split('\t') for line in open(data_user)]
data_date = parser.parse(str(data[:1][0])[2:-4])

for a in data[1:]:
	c.execute('INSERT INTO user VALUES (?,?,?,?,?,?)', (a[1], a[2], a[3], a[0], data_date))

data = [line.split('\t') for line in open(data_team)]

for a in data[1:]:
	c.execute('INSERT INTO team VALUES (?,?,?,?,?,?)', (a[1], a[2], a[3], a[0], data_date))

conn.commit()
conn.close()