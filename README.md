# Logs Analysis

App that generates a log of key stats from visits to a news site. 

## About
Logs Analysis is a Python tool for exploring a large database with over a million rows through PostgreSQL queries, allowing to draw business conclusions from the data. The project mimics building an internal reporting tool for a newspaper site to discover what kind of articles the site's readers like. The database contains newspaper articles, information about their authors, as well as visitor logs for the website.

## Requirements

- Python 3
- The psycopg2 Python 3 library
- Vagrant
- Virtualbox
- [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) 

## Design

The reporting tool was made to analyse a database 'news', with three tables containing information about articles, their authors and visitor logs, in order to answer three questions:

1. What are the three most popular articles of all time?
1. Who are the four most popular authors of all time?
1. On which days did more than 1% of requests lead to errors? 

Each question is answered in a separate appropriately named function through a single select query to the database. The function returns a generator object from which a list containing a formatted string is acquired upon iteration. The list is then joined in main() before being printed to the terminal.

## Usage

```bash
vagrant up
vagrant ssh
pip3 install psycopg2-binary
python3 logs_analysis.py
```

## License

[MIT](https://choosealicense.com/licenses/mit/)