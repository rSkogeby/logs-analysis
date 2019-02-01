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

Answers:
    What are the most popular articles of all time?
    Who are the most popular authors of all time?
    On which days did more than 1% of requests lead to errors?  
"""

import psycopg2

DB = 'news'


def main():
    
    conn = psycopg2.connect(database=DB)
    cur = conn.cursor()
    cur.execute("""SELECT articles.title, COUNT(log.path) as num FROM log, articles 
    WHERE log.path LIKE '%' || articles.slug || '%'
    GROUP BY articles.title
    ORDER BY num DESC
    LIMIT 10
    """)
    output = cur.fetchall()
    for entry in output:
        print('Hits:', entry[1], '-- article:', entry[0])
    conn.close()


if __name__ == "__main__":
    
    main()