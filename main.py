"""
Easy Art ETL
"""
import csv
from csv import DictReader
from argparse import ArgumentParser


def read_file(filename):
    """
    Inputs:
      filename  - name of file
    Output:
      Returns a collection of art.
    """
    data = []
    with open(filename, 'r', encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        csv_dict_reader = DictReader(csv_file)
        for row in csv_dict_reader:
            print(row['name'])
            data.append({'name': row['name'],
                         'genre': row['genre']})
    return data


parser = ArgumentParser()

parser.add_argument('-i', '--input', help='Input file name', required=True, metavar="FILE", dest="filename")
parser.add_argument('-o', '--output', help='Output file name', default="stdout")

args = parser.parse_args()

print(args.filename)

read_file(args.filename)
