import csv

with open("C:/Users/verya/Desktop/DS23/BigData/track_playlist1.csv", 'r') as csvin, \
        open("C:/Users/verya/Desktop/DS23/BigData/tsv_track_playlist1.tsv", 'w', newline='') as tsvout:
    csvin = csv.reader(csvin)
    tsvout = csv.writer(tsvout, delimiter='\t')

    for row in csvin:
        tsvout.writerow(row)

with open("C:/Users/verya/Desktop/DS23/BigData/tsv_track_playlist1.tsv", 'r', encoding='utf-8') as tbd:
    print(tbd.read())

# 91335