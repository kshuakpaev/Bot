import psycopg2
conn = psycopg2.connect(host="localhost", database="bot", port=5432, user='postgres', password="postgres")
cur = conn.cursor()

class BD1:
    def ss():
        cur.execute("""SELECT * FROM "tblblank" """)
        query_results = cur.fetchall()
        text = '\n\n'.join([', '.join(map(str, x)) for x in query_results])
        return (str(text))

    def ins(binn, nameper, gosnum):
        cur.execute("INSERT INTO tblblank (binn, nameper, gosnum) VALUES(%s, %s, %s)", (binn, nameper, gosnum))
        conn.commit()
        cur.close()
        conn.close()