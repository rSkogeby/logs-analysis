"""Logs Analysis"""

import psycopg2

DB = 'news'


def main():
    
    conn = psycopg2.connect(database=DB)
    conn.close()



if __name__ == "__main__":
    
    main()