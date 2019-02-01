"""Logs Analysis"""

import psycopg2

DB = 'news'


def main():
    
    conn = psycopg2.connect(database=DB)
    cur = conn.cursor()
    cur.execute("""SELECT name FROM authors LIMIT 1
    """)
    output = cur.fetchall()
    print(output)
    conn.close()



if __name__ == "__main__":
    
    main()