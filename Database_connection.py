import psycopg2

"""
1. Need to Handle the connection part.
2. Need to handle the query part if query is right.

"""

conn = psycopg2.connect(database='leet_code',user='shresth_rawat',host='localhost',port='5432', password='2714')
cursor = conn.cursor()
cursor.execute("select * from address")
data = cursor.fetchall()
print(f"Connection Established : {data}")
conn.close()


