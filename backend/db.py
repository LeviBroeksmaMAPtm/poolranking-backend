import psycopg2

# connect to DB
con = psycopg2.connect(
    database="poolranking",
    user="postgres",
    password="Funky213.")

# cursor
cur = con.cursor()

# execute query
cur.execute("select id, player, wins, losses, image from scores")

rows = cur.fetchall()

for r in rows:
    print(f" id {r[0]} player {r[1]} wins {r[2]} losses {r[3]} image {r[4]}")

# close the cursor
cur.close()

# close teh connection
con.close()
