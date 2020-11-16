import csv
import os

pyBank_csv = os.path.join('budget_data.csv')

with open(pyBank_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    print(header)
