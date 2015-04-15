#!/usr/bin/env python
import psycopg2
import sys
ppv = sys.version_info
print ppv

# Connect to an existing database
try:
    conn = psycopg2.connect("dbname=test user=postgres")
except:
    print (">> Sql server connection not available")
# Open a cursor to perform database operations

try:
    cur = conn.cursor()
except:
    print(">> Cursor creation incomplete")

# Execute a command: this creates a new table
# cur.execute("CREATE TABLE last (an_int serial PRIMARY KEY, a_date varchar, a_string varchar);")
#cur.execute("INSERT INTO last (an_int, a_date, a_string) VALUES (11, '2005-11-18', 'O''Reilly');")
rinco = 10+205
rinco = str(rinco)
#execstr =
#print execstr
#cur.execute("INSERT INTO last (an_int, a_date, a_string) VALUES (%s, %s, %s);", (rinco, '2014-1-1', 'tuned'))
#cur.execute("UPDATE last SET an_int=%s, a_date=%s, a_string=%s WHERE an_int == '11' VALUES (%s, %s, %s);", (rinco, '2014-1-1', 'tuned'))






cur.execute("SELECT an_int, a_date, a_string FROM last WHERE an_int=10;")
rows = cur.fetchall()
for row in rows:
    print "   >>", row[1]
    cur.execute("UPDATE last SET a_date=%s, a_string=%s WHERE a_string = %s;", ( '2014-1-12', 'Encrypt Lock', 'Lock'))



#lar = row #cur.fetchone()
#print lar[0]
#cur.execute("UPDATE last SET an_int=%s, a_date=%s, a_string=%s WHERE an_int = %s;", (lar[0], '2014-1-12', 'No Lock', lar[0]))

conn.commit()

# Close communication with the database
cur.close()
conn.close()
