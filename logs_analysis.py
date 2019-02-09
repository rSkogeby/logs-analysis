#!/usr/bin/env python3
"""Logs Analysis for extracting key facts out of a news site's database."""

import psycopg2

DB = 'news'


def most_read_articles(cur):
    """Report the most popular articles of all times."""
    print('\n', 'Most read articles:')
    cur.execute("""
    SELECT articles.title, COUNT(log.path) as num
        FROM log, articles
        WHERE log.path = '/article/' || articles.slug
        GROUP BY articles.title
        ORDER BY num DESC
        LIMIT 3
    """)
    output = cur.fetchall()
    for title, views in output:
        yield '"{}" \u2014 {} views'.format(title, views)


def most_read_authors(cur):
    """Report the most popular author of all times."""
    print('\n', 'Most read authors:')
    cur.execute("""
    SELECT authors.name, COUNT(log.path) as num
        FROM log, articles, authors
        WHERE log.path = '/article/' || articles.slug
        AND articles.author = authors.id
        GROUP BY authors.name
        ORDER BY num DESC
        LIMIT 4
    """)
    output = cur.fetchall()
    for author, views in output:
        yield '{} \u2014 {} views'.format(author, views)


def days_with_most_errors(cur):
    """Report days with more than 1% of requests resulting in errors."""
    print('\n', 'Errors:')
    cur.execute("""
    WITH result AS (
        WITH date_and_status AS (
            SELECT
                log.time::date AS day,
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
        TO_CHAR(day, 'FMMonth dd, yyyy'),
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
    for date, fail_rate in output:
        yield '{} \u2014 {}% errors'.format(date, round(float(fail_rate), 2))


def main():
    """Query a database DB and print the result."""
    conn = psycopg2.connect(database=DB)
    cur = conn.cursor()
    # Get generator for most read articles and print them out
    art_gen = most_read_articles(cur)
    for article in art_gen:
        print(article)
    # And for most read author
    auth_gen = most_read_authors(cur)
    for author in auth_gen:
        print(author)
    # And for days with more than 1% errors
    err_gen = days_with_most_errors(cur)
    for error in err_gen:
        print(error)
    conn.close()


if __name__ == "__main__":
    main()
