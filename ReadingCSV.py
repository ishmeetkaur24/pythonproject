
import csv

filename = "Details.csv"
mode ='r'
with open(filename,mode) as mycsvfile:
      dataFromFile = csv.reader (mycsvfile)
      for value in dataFromFile:
           print(value)