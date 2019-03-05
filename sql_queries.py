import sqlite3 as sql

def monday(grade):
    try:
        with sql.connect("bot.db") as con:
            cur = con.cursor()
            query = "SELECT lsn1, lsn2, lsn3, lsn4, lsn5, lsn6, lsn7, lsn8, lsn9, lsn10 FROM monday WHERE class = '" + str(grade) + "';"
            cur.execute(query)
            res = cur.fetchall()
            con.commit()
    except Exception as e:   
        print(e)
    print("EXE: ", query)
    return res