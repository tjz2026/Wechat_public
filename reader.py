import csv
from random import randint
def get_quotes():
    with open("quotes.csv") as f:
        reader = csv.reader(f)
        next(reader) # skip header
        data = []
        for row in reader:
            data.append(row)
    num = len(data)
    select = randint(0,num)
    #print num, select
    #print data[select]
    return data[select]

