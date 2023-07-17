import csv

with open("C:/Users/verya/Desktop/DS23/BigData/track.csv", 'r') as csvin, \
        open("C:/Users/verya/Desktop/DS23/BigData/tsv_track.tsv", 'w', newline='') as tsvout:
    csvin = csv.reader(csvin)
    tsvout = csv.writer(tsvout, delimiter='\t')

    for row in csvin:
        tsvout.writerow(row)

with open("C:/Users/verya/Desktop/DS23/BigData/tsv_track.tsv", 'r', encoding='utf-8') as tbd:
    print(tbd.read())

# 288