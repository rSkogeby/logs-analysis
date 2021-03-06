# Logs Analysis

App that generates a log of key stats from visits to a news site. 

## About
Logs Analysis is a Python tool for exploring a large database with over a million rows through PostgreSQL queries, allowing to draw business conclusions from the data. The project mimics building an internal reporting tool for a newspaper site to discover what kind of articles the site's readers like. The database contains newspaper articles, information about their authors, as well as visitor logs for the website.

## Requirements

- Python 3
- The psycopg2 Python 3 library
- [Vagrant](https://www.vagrantup.com/downloads.html)
- [VirtualBox version 5.1](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
- [VM Configuration](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)
- [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) 

## Design

The reporting tool was made to analyse a database 'news', with three tables containing information about articles, their authors and visitor logs, in order to answer three questions:

1. What are the three most popular articles of all time?
1. Who are the four most popular authors of all time?
1. On which days did more than 1% of requests lead to errors? 

Each question is answered in a separate appropriately named function through a single select query to the database. The function returns a generator object from which a list containing a formatted string is acquired upon iteration. The list is then joined in main() before being printed to the terminal.

## Usage
Install Vagrant and VirtualBox. Download the VM Configuration. Clone this logs-analysis into the FSND-Virtual-Machine/vagrant directory from the VM Configuration. Download the newsdata.zip file and extract its contents into the logs-analysis diretory. 

In order to have the VM configured with PostgreSQL and the needed Python modules cd into  FSND-Virtual-Machine/vagrant where you have your Vagrantfile and run

``` bash
vagrant up
```
You can then proceed to run

``` bash
vagrant ssh
```

to connect to Vagrant from the terminal. When successfully connected to Vagrant run

``` bash
cd /vagrant/logs-analysis
```

To set up the database run

``` bash
psql -d news -f newsdata.sql
```

Install the PostgreSQL library for Python 3:

``` bash
pip3 install psycopg2-binary
```

Run the program through

``` bash
python3 logs_analysis.py
```

or by 

``` bash
chmod +x logs_analysis.py
./logs_analysis.py
```
## License

[MIT](https://choosealicense.com/licenses/mit/)