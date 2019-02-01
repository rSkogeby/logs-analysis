"""Logs Analysis

Reads three tables:

Table name: articles
    Columns: 
        author INTEGER (F ref. authors(id)), title TEXT, 
        slug TEXT (unique constraint), lead TEXT, body TEXT, 
        time TIMESTAMPTZ, id INTEGER (P)

Table name: authors
    Columns:
        name TEXT, bio TEXT, id INTEGER (P)

Table name: log
    Columns:
        path TEXT, ip INET, method TEXT, status TEXT, 
        time TIMESTAMPTZ, id INTEGER (P)

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
    print()
    
    """Reports the most popular articles of all times."""
    print('Most read articles:')    
    cur.execute("""SELECT articles.title, COUNT(log.path) as num 
        FROM log, articles 
        WHERE log.path LIKE '%' || articles.slug || '%'
        GROUP BY articles.title
        ORDER BY num DESC
        LIMIT 3
    """)
    output = cur.fetchall()
    for entry in output:
        print('\"%s\"' % entry[0], '--', entry[1], 'views')
    print()
    
    """Reports the most popular author of all times."""
    print('Most read authors:')
    cur.execute("""SELECT authors.name, COUNT(log.path) as num
        FROM log, articles, authors
        WHERE log.path LIKE '%' || articles.slug || '%'
        AND articles.author = authors.id
        GROUP BY authors.name
        ORDER BY num DESC
        LIMIT 4
    """)

    output = cur.fetchall()
    for entry in output:
        print('\"%s\"' % entry[0], '--', entry[1], 'views')
    print()
    
    """Days with more than 1% of requests resulting in errors"""
    print('Errors:')    
    cur.execute("""SELECT TO_CHAR(log.time::date, 'FMMonth dd, yyyy') AS day, 
        COUNT(log.status) AS num
        FROM log
        WHERE log.status LIKE '%40%'
        OR log.status LIKE '%50%'
        GROUP BY day
        ORDER BY num DESC
        LIMIT 10
    """)

    output = cur.fetchall()
    for entry in output:
        print('\"%s\"' % entry[0], '--', entry[1], 'views')
    
    conn.close()


if __name__ == "__main__":
    
    main()