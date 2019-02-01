"""Logs Analysis

Reads three tables:
Table name: articles
    Columns: 
        author INTEGER (F ref. authors(id)), title TEXT, 
        slug TEXT (unique constraint), lead TEXT, body TEXT, 
        time TIMESTAMP, id INTEGER (P)
Table name: authors
    Columns:
        name TEXT, bio TEXT, id INTEGER (P)
Table name: log
    Columns:
        path TEXT, ip INET, method TEXT, status TEXT, 
        time TIMESTAMP, id INTEGER (P)
"""

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