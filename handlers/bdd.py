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
    
    def all_country():
        cur.execute("""SELECT namecountry FROM "tblcountry" GROUP BY namecountry ORDER BY namecountry""")
        query_result = cur.fetchall()
        kk = []
        for i in query_result:
            ss = ""
            ss = i[0]
            kk.append(ss.strip())
        return kk

    def blank_country(namecountry):
        # cur.execute("""SELECT * FROM "tblcountry" WHERE namecountry = '(%s)' """, namecountry)
        cur.execute(f"SELECT * FROM tblcountry WHERE namecountry = '{namecountry}'")
        query_result = cur.fetchall()
        kk = []
        for i in query_result:
            ss = ""
            ss = i[1]
            kk.append(ss.strip())
        return kk

print(BD1.all_country())
nn = BD1.all_country()
for i in nn:
    ss = ""
    ss = i
    print(ss.strip())
print(BD1.blank_country(ss.strip()))
nn = BD1.blank_country(ss.strip())
for i in nn:
    ss = ""
    ss = i
    print(ss.strip())
