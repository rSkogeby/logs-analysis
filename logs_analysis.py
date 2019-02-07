"""Logs Analysis
Answers:
What are the most popular articles of all time?
Who are the most popular authors of all time?
On which days did more than 1% of requests lead to errors?
"""

import psycopg2

DB = 'news'


def print_most_read_articles(cur):
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
        print('\"%s\"' % entry[0], '\u2014', entry[1], 'views')
    print()


def print_most_read_authors(cur):
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
        print('\"%s\"' % entry[0], '\u2014', entry[1], 'views')
    print()


def print_days_with_most_errors(cur):
    """Days with more than 1% of requests resulting in errors"""
    print('Errors:')
    cur.execute("""
    WITH result AS (
        WITH date_and_status AS (
            SELECT
                TO_CHAR(log.time::date, 'FMMonth dd, yyyy') AS day,
                log.status as status
            FROM
                log
        )
        SELECT
            day,
            ((COUNT(status) FILTER (WHERE status LIKE '%40%' OR status
            LIKE '%50%'))::float / (COUNT(status))::float) * 100 AS fail_rate
        FROM
            date_and_status
        GROUP BY
            day
    )
    SELECT
        day,
        fail_rate
    FROM
        result
    WHERE
        fail_rate >= 1
    ORDER BY
        fail_rate DESC
    LIMIT
        10
    """)
    output = cur.fetchall()
    for entry in output:
        print('%s' % entry[0], ' \u2014 ', round(float(entry[1]), 2),
              '% errors', sep='')


def main():
    # Connect to database
    conn = psycopg2.connect(database=DB)
    cur = conn.cursor()
    print_most_read_articles(cur)
    print_most_read_authors(cur)
    print_days_with_most_errors(cur)
    conn.close()


if __name__ == "__main__":
    main()
