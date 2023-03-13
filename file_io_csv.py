import pandas


def read_pandas():
    df = pandas.read_csv('IndianCensus - Sheet1.csv')
    return df


#print(read_pandas())

# without pandas we can use perform csv file

import csv

def read_csv():
    with open('IndianCensus - Sheet1.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

read_csv()


