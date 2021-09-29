import csv
from datetime import date
from collections import namedtuple

#именованный кортеж
#по названию в скобках будем обращаться в with к списку columns
Column = namedtuple('Column', 'src dest convert')

#from str to date
def parse_date(text):
    return date.fromisoformat(text)

#list with names and types of columns
columns = [
    Column('name', 'Name', str),
    Column('department', 'Department', str),
    Column('birthday', 'Birthday', parse_date
           ),
    Column('salary', 'Salary', int)
    ]

#from csv to dict (one line = new dict), converting data types
with open(r'D:\Epam\Self_study\Python for Data Scientists\Exercise Files\Ch02\02_01\Example.csv', 'rt') as fp:
    reader = csv.DictReader(fp)
    for line in reader:
        record = {}
        for col in columns:
            value = line[col.src]
            record[col.dest] = col.convert(value)
        print(record)
        
